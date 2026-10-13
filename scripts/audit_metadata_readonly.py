"""Read-only audit of three pinned public repositories; writes reports, never source."""
from __future__ import annotations
import collections
import concurrent.futures
import datetime as dt
import importlib.util
import json
from pathlib import Path, PurePosixPath
import posixpath
import re
import sys
import time
from urllib.parse import quote, unquote, urlparse
from urllib.request import Request, urlopen
import yaml

REFS = {
    'fivsevn-agy/fivsevn-devlog': 'cd86adbf802e279012c259a53d425ee55290b77f',
    'fivsevn-agy/fivsevn-spec': 'e71b4d8a4215f61a0b8d62d57fbea5a82bc0d52e',
    'fivsevn/fivsevn-assets': '7bc35645c4bd6e6a443c34078d9c0a57ede25a3e',
}
OUT = Path('audit-output')
SNAP = OUT / 'sources'
TODAY = dt.date(2026, 10, 13)
CORE = 'id title module submodule topic type status canonical summary parents related tags audience languages maturity confidence visibility source_of_truth created updated'.split()
ARRAYS = 'parents related tags audience languages'.split()
ENUMS = {
    'module': {'posts','natsci','netcom','blogops','spec','system'},
    'type': {'index','note','article','translation','log','spec','release','traslation'},
    'status': {'hidden','private','draft','active','publish','published','archive','archived'},
    'audience': {'self','public','internal'}, 'languages': {'zh','en','ja'},
    'maturity': {'draft','evolving','stable','deprecated'},
    'visibility': {'private','public','internal'},
    'source_of_truth': {'devlog','spec','site','translation','external'},
}
SUBMODULES = {
    'posts': {'index','drafts','2025','2026','ai-discourse-analysis'},
    'natsci': {'index','drafts','ethnobiology','paleontology','reading','taxonomy'},
    'netcom': {'index','drafts','ai','architecture','cs','digital','lora','math','mcu','methods','protocol','rf'},
    'blogops': {'index','content','docs'},
}
ISSUES = []
DOCS = []
TREES = {}
TEXTS = {}
ERRORS = []

class UniqueLoader(yaml.SafeLoader):
    pass

def unique_mapping(loader, node, deep=False):
    loader.flatten_mapping(node)
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f'duplicate YAML key: {key}')
        result[key] = loader.construct_object(value_node, deep=deep)
    return result
UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)

def get(url):
    for attempt in range(3):
        try:
            req = Request(url, headers={'User-Agent':'fivsevn-readonly-metadata-audit'})
            with urlopen(req, timeout=45) as r:
                return r.read().decode('utf-8-sig')
        except Exception:
            if attempt == 2: raise
            time.sleep(attempt + 1)

def issue(repo, path, code, detail, level='review'):
    ISSUES.append({'repo':repo, 'path':path, 'code':code, 'detail':detail, 'level':level})

def read_task(task):
    repo, path = task
    try:
        text = get(f'https://raw.githubusercontent.com/{repo}/{REFS[repo]}/{quote(path, safe="/")}')
        return repo, path, text, None
    except Exception as e:
        return repo, path, None, f'{type(e).__name__}: {e}'

def classify(repo, path):
    p = PurePosixPath(path)
    if 'legacy' in p.parts: return 'legacy'
    if repo.endswith('-spec'): return 'specification'
    if repo.endswith('-assets'): return 'asset_document'
    if p.name.lower() == 'readme.md' or path == 'system-map.md': return 'guide'
    if path.startswith('intake/'): return 'intake_configuration'
    if path == 'posts/_wordpress/trigger.md': return 'publisher_configuration'
    if path == 'now/index.md': return 'handwritten_page'
    if '_drafts' in p.parts:
        return 'template' if p.name.startswith('TEMPLATE-') else 'draft'
    if p.name in {'index.md','map.md'}: return 'index'
    return 'content'

def check_metadata(repo, path, text):
    kind = classify(repo, path)
    doc = {'repo':repo, 'path':path, 'kind':kind, 'frontmatter':False}
    DOCS.append(doc)
    lines = text.splitlines()
    if not lines or lines[0].strip() != '---':
        if kind == 'content': issue(repo,path,'content_without_frontmatter','Ordinary content has no frontmatter')
        return
    doc['frontmatter'] = True
    try:
        end = next(i for i in range(1,len(lines)) if lines[i].strip() == '---')
        fm = yaml.load('\n'.join(lines[1:end]), Loader=UniqueLoader) or {}
        if not isinstance(fm,dict): raise ValueError('frontmatter is not a mapping')
    except Exception as e:
        doc['parse_error'] = type(e).__name__
        issue(repo,path,'invalid_yaml',f'{type(e).__name__}; frontmatter could not be parsed','error')
        return
    doc['metadata'] = fm
    if kind in {'legacy','publisher_configuration','intake_configuration','template','specification','guide','asset_document'}: return
    missing = [k for k in CORE if k not in fm]
    if missing: issue(repo,path,'missing_recommended_fields',', '.join(missing))
    for key in ARRAYS:
        if key in fm and not isinstance(fm[key],list):
            issue(repo,path,'array_as_scalar',key)
        if isinstance(fm.get(key),list) and any(not isinstance(v,str) for v in fm[key]):
            issue(repo,path,'array_non_string_item',key)
    for key,allowed in ENUMS.items():
        if key not in fm: continue
        values = fm[key] if isinstance(fm[key],list) else [fm[key]]
        for value in values:
            if not isinstance(value,str) or value not in allowed:
                issue(repo,path,'value_not_in_current_spec',f'{key}: {value}')
    sub = fm.get('submodule')
    if isinstance(sub,int): issue(repo,path,'numeric_submodule',str(sub),'compatibility')
    mod = fm.get('module')
    if isinstance(mod,str) and mod in SUBMODULES and str(sub) not in SUBMODULES[mod]:
        issue(repo,path,'submodule_not_listed_in_spec',f'{mod}/{sub}','compatibility')
    if isinstance(mod,str) and path.split('/')[0] in {'posts','natsci','netcom','blogops'} and path.split('/')[0] != mod:
        issue(repo,path,'module_path_mismatch',str(mod),'error')
    if 'canonical' in fm and not isinstance(fm['canonical'],bool): issue(repo,path,'canonical_not_boolean','canonical')
    if 'confidence' in fm:
        v=fm['confidence']
        if isinstance(v,bool) or not isinstance(v,(int,float)) or not 0<=v<=1:
            issue(repo,path,'invalid_confidence','Expected a number from 0 to 1')
    ident = fm.get('id')
    if ident and (not isinstance(ident,str) or not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',ident)):
        issue(repo,path,'id_format',str(ident))
    if ident and ident != PurePosixPath(path).stem:
        issue(repo,path,'filename_differs_from_id',str(ident),'compatibility')
    dates={}
    for key in ['created','updated']:
        if key in fm:
            val=str(fm[key])
            try:
                if not re.fullmatch(r'\d{4}-\d{2}-\d{2}',val): raise ValueError()
                dates[key]=dt.date.fromisoformat(val)
            except ValueError: issue(repo,path,'invalid_date',key,'error')
    if dates.get('updated',TODAY)<dates.get('created',dt.date.min): issue(repo,path,'updated_before_created','Date order','error')
    if dates.get('created',dt.date.min)>TODAY: issue(repo,path,'future_created',str(dates['created']))
    if fm.get('status') in {'active','publish','published','draft'} and fm.get('visibility') in {'private','internal'}:
        issue(repo,path,'index_visibility_conflict',f"status={fm.get('status')}; visibility={fm.get('visibility')}",'priority')
    if fm.get('type') in {'translation','traslation'}:
        fields=['original_title','original_source','original_publisher','original_url','translation_note']
        lacking=[k for k in fields if k not in fm]
        if lacking: issue(repo,path,'translation_fields_missing',', '.join(lacking))
        if not fm.get('original_url') and not fm.get('translation_note'):
            issue(repo,path,'translation_source_missing','No source URL or explanatory note')
        if fm.get('source_of_truth')!='translation':
            issue(repo,path,'translation_source_of_truth',str(fm.get('source_of_truth')))
    if fm.get('original_url'):
        u=urlparse(str(fm['original_url']))
        if u.scheme not in {'https','http'} or not u.netloc: issue(repo,path,'invalid_original_url','Expected HTTP(S) URL')
    for k in ('canonical_url','description','lang','date','columns'):
        if k in fm: issue(repo,path,'undocumented_extension',k,'compatibility')
    title=fm.get('title')
    heading=next((l[2:].strip() for l in lines[end+1:] if l.startswith('# ')),None)
    if kind=='content' and fm.get('type') not in {'translation','traslation'} and heading and title and heading!=title:
        issue(repo,path,'title_heading_differs',heading,'compatibility')

def check_links(repo,path,text):
    if classify(repo,path)=='legacy': return
    cleaned=re.sub(r'^```.*?^```[^\n]*', '', text, flags=re.M|re.S)
    cleaned=re.sub(r'<!--[\s\S]*?-->','',cleaned)
    links=re.findall(r'!?\[[^\]\n]*\]\(([^\s\)]+)(?:\s+[^\)]*)?\)',cleaned)
    for dest in sorted(set(links)):
        dest=dest.strip('<>')
        targetrepo=repo
        if dest.startswith('#') or dest.startswith(('mailto:','tel:','data:')): continue
        u=urlparse(dest)
        if u.scheme:
            parts=unquote(u.path).strip('/').split('/')
            if u.netloc=='github.com' and len(parts)>=5 and parts[2] in {'blob','tree'} and parts[3]=='main':
                targetrepo='/'.join(parts[:2]); target='/'.join(parts[4:])
            else: continue
        else:
            if dest.startswith('/') or '{{' in dest: continue
            target=posixpath.normpath(posixpath.join(posixpath.dirname(path),unquote(u.path)))
        if targetrepo not in TREES: continue
        known={x['path'] for x in TREES[targetrepo]}
        if target.endswith('.html') and target[:-5]+'.md' in known: continue
        if target.rstrip('/') not in known:
            issue(repo,path,'unresolved_repo_link',dest)

def load_module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec); sys.modules[name]=module
    spec.loader.exec_module(module)
    return module

def main():
    OUT.mkdir(exist_ok=True)
    for repo,ref in REFS.items():
        data=json.loads(get(f'https://api.github.com/repos/{repo}/git/trees/{ref}?recursive=1'))
        if data.get('truncated'): raise RuntimeError(f'Truncated repository tree: {repo}')
        TREES[repo]=data['tree']
    tasks=[]
    excluded_generated={'intake/llm-context.md','intake/index.html','intake/gpt.md'}
    for repo,tree in TREES.items():
        for f in tree:
            p=f['path']; suffix=PurePosixPath(p).suffix.lower()
            if f['type']=='blob' and p not in excluded_generated and (suffix in {'.md','.py','.yml','.yaml','.scss'} or PurePosixPath(p).name in {'LICENSE','.gitignore','requirements.txt'}):
                tasks.append((repo,p))
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
        for repo,path,text,error in ex.map(read_task,tasks):
            if error:
                ERRORS.append({'repo':repo,'path':path,'error':error}); continue
            TEXTS[(repo,path)]=text
            target=SNAP/repo.split('/')[1]/path
            target.parent.mkdir(parents=True,exist_ok=True); target.write_text(text,encoding='utf-8')
            if path.endswith('.md'):
                check_metadata(repo,path,text)
                check_links(repo,path,text)
    idpaths=collections.defaultdict(list)
    for doc in DOCS:
        ident=doc.get('metadata',{}).get('id')
        if isinstance(ident,str) and doc['kind']!='legacy': idpaths[ident].append(doc)
    for ident,items in idpaths.items():
        if len(items)>1:
            for d in items: issue(d['repo'],d['path'],'duplicate_id',ident,'error')
    knownids=set(idpaths)
    knownids.update(PurePosixPath(p).stem for r,p in TEXTS if r.endswith('-spec') and p.endswith('.md') and not p.startswith('legacy/'))
    for d in DOCS:
        if d['kind'] in {'legacy','template'}: continue
        fm=d.get('metadata',{})
        for key in ['parents','related']:
            vals=fm.get(key,[])
            if not isinstance(vals,list): continue
            for val in vals:
                if isinstance(val,str) and val not in knownids: issue(d['repo'],d['path'],'unresolved_relation',f'{key}: {val}')
    inventory={}
    for repo,tree in TREES.items():
        blobs=[f for f in tree if f['type']=='blob']
        bysha=collections.defaultdict(list)
        for f in blobs: bysha[f['sha']].append(f)
        inventory[repo]={
            'ref':REFS[repo], 'files':len(blobs), 'bytes':sum(f.get('size',0) for f in blobs),
            'markdown':sum(f['path'].endswith('.md') for f in blobs),
            'extensions':dict(collections.Counter(PurePosixPath(f['path']).suffix.lower() or '(no suffix)' for f in blobs)),
            'cache_files':[f for f in blobs if PurePosixPath(f['path']).name in {'.DS_Store','.cache'} or '__pycache__' in f['path']],
            'placeholder_files':[f['path'] for f in blobs if f.get('size',999)<2],
            'duplicate_content':[[{'path':f['path'],'bytes':f.get('size',0)} for f in group] for group in bysha.values() if len(group)>1 and group[0].get('size',0)>1],
            'largest_files':sorted(blobs,key=lambda f:f.get('size',0),reverse=True)[:10],
        }
    diagnostics={}
    dev=SNAP/'fivsevn-devlog'
    try:
        ix=load_module(dev/'scripts/update_module_indexes.py','audit_index')
        diagnostics['index_modules']={}
        for mod,cfg in ix.MODULES.items():
            notes,warnings=ix.collect_notes(mod,cfg)
            text=(dev/cfg['index']).read_text()
            start=f"<!-- AUTO-INDEX:{cfg['marker']}:START -->"; end=f"<!-- AUTO-INDEX:{cfg['marker']}:END -->"
            current=text.split(start)[1].split(end)[0].strip()
            expected=ix.render_notes(notes).strip()
            diagnostics['index_modules'][mod]={'count':len(notes),'matches':current==expected,'warnings':warnings,'paths':[n.source_path for n in notes]}
        diagnostics['invalid_date_result']=ix.normalize_date('2026-02-31')
        sample='<!-- AUTO-INDEX:TEST:START -->\nold\n<!-- AUTO-INDEX:TEST:END -->'
        try:
            ix.replace_between_markers(sample,'TEST','new \\LaTeX')
            diagnostics['backslash_title']='accepted'
        except Exception as e: diagnostics['backslash_title']=type(e).__name__+': '+str(e)
        draft=load_module(dev/'scripts/apply_draft_frontmatter.py','audit_draft')
        for title in ['QA: 游戏测试','游戏 QA # 测试笔记']:
            raw=draft.make_frontmatter('posts','posts-test-001',title,'2026-10-13')
            try: diagnostics[title]=yaml.safe_load(raw.split('---',2)[1])['title']
            except Exception as e: diagnostics[title]=type(e).__name__
    except Exception as e: diagnostics['error']=f'{type(e).__name__}: {e}'
    registry=TEXTS.get(('fivsevn-agy/fivsevn-devlog','intake/sources.md'),'')
    source_blocks=[]
    for match in re.finditer(r'^```source\s*\n(.*?)\n```',registry,re.S|re.M):
        try: source_blocks.append(yaml.load(match.group(1),Loader=UniqueLoader))
        except Exception as e: issue('fivsevn-agy/fivsevn-devlog','intake/sources.md','invalid_source_block',type(e).__name__,'error')
    diagnostics['source_registry_count']=len(source_blocks)
    result={'snapshots':REFS,'inventory':inventory,'fetch_errors':ERRORS,'documents':DOCS,'issues':ISSUES,'diagnostics':diagnostics}
    (OUT/'report.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,default=str),encoding='utf-8')
    summary={
        'inventory':{r:{k:v for k,v in inv.items() if k in {'ref','files','bytes','markdown','extensions','cache_files'}} for r,inv in inventory.items()},
        'doc_kinds':dict(collections.Counter(d['kind'] for d in DOCS)),
        'frontmatter_count':sum(d['frontmatter'] for d in DOCS),
        'parsed_frontmatter_count':sum('metadata' in d for d in DOCS),
        'issue_counts':dict(collections.Counter(i['code'] for i in ISSUES)),
        'fetch_errors':ERRORS, 'diagnostics':diagnostics,
    }
    (OUT/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2,default=str),encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False,indent=2,default=str))
    print('\n=== Issues (file paths and metadata diagnostics only) ===')
    for i in ISSUES: print(json.dumps(i,ensure_ascii=False))
    if ERRORS: raise SystemExit('Audit incomplete: some files could not be read')

if __name__=='__main__': main()
