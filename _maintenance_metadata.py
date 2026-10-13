"""One-time document migration. No publishing, no display edits, no media writes."""
from __future__ import annotations
import argparse, copy, datetime, json, re, subprocess
from pathlib import Path
import yaml

DAY='2026-10-13'
GROUPS=[['id','title'],['module','submodule','topic'],['type','status','canonical'],['summary'],['parents','related'],['tags'],['audience','languages'],['maturity','confidence'],['visibility','source_of_truth'],['original_title','original_source','original_publisher','original_url','translation_note'],['subtitle','references','rights','archive_url','note','aliases','legacy','filename_policy'],['layout','lang','description','canonical_url','permalink'],['created','updated','metadata_updated']]
ARRAYS={'parents','related','tags','audience','languages','aliases'}
PROTECTED={'README.md','intake/sources.md','intake/llm-context.md','posts/_wordpress/trigger.md','posts/2026/posts-toy-reference.md'}
FIXED={'system-map.md','blogops/docs/publish-memo.md','posts/ai-discourse-analysis/ai-posts-boot-protocol.md'}
RELATIONS={'blogops-map':'blogops-index','netcom-module-map':'netcom-index','system-module-map':'system-map','netcom-mcu-001':'netcom-mcu-overview-001','netcom-math-dynamicalsystem-001':'netcom-math-dynamical-system-prototypes-001','netcom-rf-spectrum-001':'netcom-rf-spectrum-overview-001','netcom-mcu-meshtastic-001':'netcom-mcu-meshtastic-comparison-001','system-source-citation-apa7-001':'spec-source-citation-apa7-001','system-source-citation-mla9-001':'spec-source-citation-mla9-001','system-source-citation-chicago17-001':'spec-source-citation-chicago17-001'}
UNRESOLVED={'netcom-lora-meshtastic-001','system-source-reference-pool-001'}
WP={
'2019-06-18-深夜四時':('posts-20190618-shinya-yoji-001','深夜的一句日文状态记录。'),
'2025-03-13-波洛去埃及':('posts-20250313-poirot-egypt-001','摘录《埃及古墓历险记》，整理波洛赴埃及的行程、地图与参考版本。'),
'2025-03-14-更新计划':('posts-20250314-writing-plan-001','记录当时准备整理的饮食、文学、历史及语言素材。'),
'2025-03-14-泛指、抑或是个人问题':('posts-20250314-framing-001','借《埃及古墓历险记》中的对话讨论框架、提问方式与个人处境。'),
'2025-03-15-麦麦赛博π':('posts-20250315-pi-day-001','从麦当劳派的日常体验延伸到圆周率日、仪式与集体沸腾。'),
'2025-03-17-廷巴克图':('posts-20250317-timbuktu-001','汇集廷巴克图的地名意象、历史、手稿保护与相关外文资料。'),
'2025-03-17-路过':('posts-20250317-passing-by-001','散步途中关于绿地和城隍的图像与随想。'),
'2025-03-18-更新预告：锯锯🪚':('posts-20250318-sawfish-preview-001','暂存锯鳐标本与保护海报，作为后续整理材料。'),
'2025-03-18-绿化带射灯':('posts-20250318-ground-light-001','记录绿化带射灯及其照明场景。'),
'2025-03-20-听壁脚、包打听、讲斤头、牵丝扳藤':('posts-20250320-dialect-expressions-001','整理听壁脚、包打听、讲斤头、牵丝扳藤等表达及相关阅读材料。'),
'2025-03-22-染发香波便便💩':('posts-20250322-shampoo-001','保留染发香波相关的日常图文记录。'),
'2025-03-23-锯锯鱼':('posts-20250323-sawfish-001','整理锯鳐相关材料与观察。'),
'2025-03-23-阈限地带':('posts-20250323-liminal-space-001','记录午夜集市的摊位遗留物、空间痕迹与阈限感。'),
'2025-03-24-摊痕地带':('posts-20250324-market-traces-001','记录集市退去后的地面痕迹与行走感受。'),
'2025-03-26-RayRay的奇妙比喻':('posts-20250326-chandler-metaphors-001','对照中英文摘录，整理钱德勒小说中的明喻、隐喻及文学表达。'),
'2025-03-27-🍚 🦐 🐟':('posts-20250327-shrimp-fish-001','记录饲养鱼虾的图像、动图与喂食片段。'),
'2025-03-28-he1l0.kt7y protocol active surveillance':('posts-20250328-hello-kitty-surveillance-001','以监控协议和系统提示的叙事方式记录日常图像。'),
'2025-03-31-更新预告：如何翻译 “ Profiling ”':('posts-20250331-profiling-preview-001','预告 Profiling 翻译材料的整理，并说明配图的生成与修改方式。'),
'2025-03-31-犯罪小说当中对执法机构的描述（虚构文学研究）':('posts-20250331-crime-fiction-law-enforcement-001','摘录并比较犯罪小说中的虚构执法机构、人物关系和叙述方式。'),
'2025-04-03-开发日志已更新！':('posts-20250403-devlog-update-001','记录当时的开发日志更新与页面入口。'),
'2025-04-09-路灯':('posts-20250409-streetlight-001','记录路灯影像与相关视频。'),
'2025-06-27-【授权转载】Tents in Strong Wind What You Need to Know':('posts-20250627-tents-in-strong-wind-001','存档关于强风与帐篷的第一部分中文译文，并保留当时的限期授权条件。')}

class UniqueLoader(yaml.SafeLoader):pass
def unique_mapping(loader,node,deep=False):
    out={}
    for kn,vn in node.value:
        key=loader.construct_object(kn,deep=deep)
        if key in out:raise ValueError(f'Duplicate YAML key: {key}')
        out[key]=loader.construct_object(vn,deep=deep)
    return out
UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,unique_mapping)
class Literal(str):pass
class Dumper(yaml.SafeDumper):pass
Dumper.add_representer(Literal,lambda d,v:d.represent_scalar('tag:yaml.org,2002:str',v,style='|'))

def plain(v):
    if isinstance(v,(datetime.date,datetime.datetime)):return v.isoformat()
    if isinstance(v,dict):return {str(k):plain(x) for k,x in v.items()}
    if isinstance(v,list):return [plain(x) for x in v]
    return v

def split(text):
    m=re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)',text,re.S)
    if not m:return {},text,''
    fm=yaml.load(m[1],Loader=UniqueLoader) or {}
    if not isinstance(fm,dict):raise ValueError('Expected a mapping')
    return plain(fm),text[m.end():],m[1]

def render(fm,body):
    used=set();groups=[]
    def line(k,v):
        if k in ARRAYS:return k+': '+json.dumps(v,ensure_ascii=False)+'\n'
        if isinstance(v,str) and '\n' not in v:return k+': '+json.dumps(v,ensure_ascii=False)+'\n'
        if isinstance(v,str):v=Literal(v)
        return yaml.dump({k:v},Dumper=Dumper,allow_unicode=True,sort_keys=False,width=120)
    for group in GROUPS:
        text=''.join(line(k,fm[k]) for k in group if k in fm)
        used.update(k for k in group if k in fm)
        if text:groups.append(text.rstrip('\n'))
    rest=''.join(line(k,v) for k,v in fm.items() if k not in used)
    if rest:groups.insert(-1,rest.rstrip('\n'))
    return '---\n'+'\n\n'.join(groups)+'\n---\n'+body

def retain(fm,k,v):fm.setdefault('legacy',{}).setdefault('metadata',{}).setdefault(k,copy.deepcopy(v))
def change(fm,k,v):
    if k in fm and fm[k]!=v:retain(fm,k,fm[k])
    fm[k]=v
def note(fm,text):
    old=fm.get('note','')
    if text not in old:fm['note']=(old+'\n'+text).strip()
def title(body,fallback):
    headings=re.findall(r'^#{1,3}\s+(.+?)\s*$',body,re.M)
    return next((x for x in headings[:2] if re.search(r'[\u4e00-\u9fff]',x)),headings[0] if headings else fallback)
def git_date(root,rel,first):
    lines=subprocess.check_output(['git','log','--follow','--format=%cs','--',rel],cwd=root,text=True).splitlines()
    return (lines[-1] if first else lines[0]) if lines else None

def eligible(repo,rel):
    p=Path(rel)
    return p.suffix=='.md' and p.name.lower() not in {'index.md','index.html'} and not (repo=='devlog' and rel in PROTECTED)

def wp_fields(fm,body,p):
    change(fm,'summary',WP[p.stem][1])
    first=body.strip().splitlines()[0] if body.strip() else ''
    if re.fullmatch(r'[A-Za-z][A-Za-z0-9 /,.!?&():-]{0,119}',first):fm['subtitle']=first
    if fm['type']!='translation':
        fm.setdefault('original_title',fm['title']);fm.setdefault('original_publisher','五月七日')
    refs=[];section='';inside=False
    for line in body.splitlines():
        if '| 【Reference Deck】 |' in line:inside=True;continue
        if not inside or not line.startswith('|'):continue
        cell=line.strip().strip('|').strip()
        if re.fullmatch(r'[- :|]+',cell):continue
        if re.fullmatch(r'\*\*.*\*\*',cell):section=cell.strip('*');continue
        if cell:refs.append({'section':section,'text':cell})
    if refs:fm['references']=refs
    if fm['type']=='translation':
        fm['archive_url']=fm['original_url']
        for k,v in {'original_title':'Tents in Strong Wind: What You Need to Know','original_source':'SlowerHiking','original_publisher':'Helen & Geoff','original_url':'https://slowerhiking.com/shelter/tents-in-strong-wind-what-you-need-to-know','translation_note':'仅存档第一部分中文译文；未使用原文配图，原文段落与授权声明保留。'}.items():change(fm,k,v)
        fm['rights']={'note':'原存档声明经邮件取得 Helen 与 Geoff 的书面授权，仅允许在 8 周试用期内以非营利、无广告形式发布第一部分译文，不包含第二、第三部分且不得使用原文配图。','verification':'仅转录存档已有说明；未核对续期或当前授权有效性。'}
        note(fm,'保持原 hidden 状态；本次不重新公开，不推定限期授权仍有效。')
    else:note(fm,'旧 WordPress 存档；保留原文、图片链接、异名及参考资料的原有表达，未扩写正文。')

SPEC_EXTENSIONS='''## 统一使用与扩展字段

### 适用范围

- **共用核心字段**：原创、译文、旧 WordPress 存档、维护说明、板块 README、规范与历史资料。
- **保留展示入口**：现有 `index.md`、`index.html`、devlog 根 README 和交互展示页不为统一 metadata 而改写。
- **另有格式**：trigger、来源登记、脚本、样式、媒体及自动生成文件不套文章模板。特别设计的叙事文件保持原样。
- **机器校验**：[content-metadata.schema.json](content-metadata.schema.json)。核心字段固定顺序与类型，非核心信息放到有明确用途的扩展字段。

### 身份、路径和历史信息

- 普通文档使用 **`id.md`**；`id` 用小写字母、数字和连字符，确定后尽量不变。
- `README.md` 等固定入口保留名称，标记 `filename_policy: entrypoint`。被展示目录或已发布链接引用、暂不能安全迁移的旧路径使用 `stable-link`，在 `note` 写明原因。
- 旧 ID 规范化后放进 `aliases`；旧路径与原字段值放进 `legacy`。它们只用于追溯和检索，**不会自动建立网页重定向或再次发布文章**。
- `submodule` 对应板块下的一级归属目录；年份写成字符串，例如 `"2026"`。更细主题放在 `topic`、`tags`，原有值必要时保留在 `legacy.metadata`。
- 未知的写作日期或可靠度可写 `null`，并说明缺失原因；不使用虚构日期、默认高分填满字段。
- `created` / `updated` 保留内容日期；纯元数据整理使用 `metadata_updated`。从 Git 补日期时，在 `note` 标明它是首次记录日期，而不是已证实的写作日期。

### 特殊信息放哪里

| 字段 | 格式 | 收纳内容 |
|---|---|---|
| `note` | 字符串，可多行 | 编辑说明、缺失信息、命名例外；不代替摘要 |
| `subtitle` | 字符串 | 旧版副标题或另一语言的标题 |
| `references` | 对象数组，含 `section`、`text` | 旧参考资料的分组与原始引文；正文参考表可继续保留 |
| `rights` | 对象 | 授权条件、范围、期限说明及核对情况；记录声明不等于授予许可 |
| `archive_url` | 完整 URL | 译文等内容曾在本站 WordPress 发布的位置；区别于外文原始来源 `original_url` |
| `aliases` | 字符串数组 | 曾使用的内容 ID，包括历史中文 ID |
| `legacy` | 对象 | 旧字段值、旧路径、无法确认的关系、原 YAML 注释 |
| `extra` | 对象 | 暂无专用字段的特殊资料；子键应说明含义，重复使用再提升为正式扩展 |
| `filename_policy` | `entrypoint` / `stable-link` | 固定入口或旧链接例外；普通 `id.md` 不需要填写 |
| `metadata_updated` | `YYYY-MM-DD` | 本次元数据整理日期 |

`legacy.metadata` 保存变更前的值，`legacy.unresolved_relations` 保存尚不能确认目标的旧关系；不要为了校验通过而编造关系目标。

### 页面字段

按需保留 `layout`、`lang`、`description`、`canonical_url`、`permalink`：它们服务页面构建，不是重复字段。`lang` 不等于语言数组 `languages`，`canonical_url` 不等于布尔值 `canonical`。

改名但要保留原文章网页地址时，可用 `permalink` 固定旧地址；需核对站点构建，不应假定旧 GitHub 文件链接也会重定向。参考 [Jekyll permalink](https://jekyllrb.com/docs/permalinks/)、[Jekyll SEO 字段](https://github.com/jekyll/jekyll-seo-tag/blob/master/docs/usage.md)。

### 特殊情况示例

```yaml
note: >-
  原始写作日期未记录；保留存档中的标题和说明，不补写无法确认的信息。
aliases: [旧文章ID]
legacy:
  path: posts/2025/旧文件名.md
  metadata:
    submodule: 旧主题
rights:
  note: 原存档记载的授权条件原样说明。
  verification: 尚未核对当前授权有效性。
metadata_updated: 2026-10-13
```

**不丢信息，不自动重新公开，不把整理 metadata 当作正文事实或授权复核。**
'''

def body_edits(repo,rel,body):
    if repo=='devlog':
        if rel.startswith('blogops/docs/') and rel!='blogops/docs/auto-translation-shortcut.md':body='\n'.join(x for x in body.split('\n') if not ('修改历史' in x and ('旧版' in x or '历史版本' in x)))
        if rel=='netcom/lora/netcom-lora-meshtastic-device-inventory-001.md':body=body.replace('(lora/netcom-lora-meshtastic-node-observation-001.md)','(netcom-lora-meshtastic-node-observation-001.md)')
        if rel=='posts/2026/posts-20260618-media-studies-wjs3-ai-journalistic-culture-001-revised.md':body=body.replace('(2026/posts-journalism-ai-labeling-001.md)','(posts-journalism-ai-labeling-001.md)')
        if rel=='posts/ai-discourse-analysis/ai-posts-boot-protocol.md':
            body=body.replace('spec-gov-meta-frontmatter-001','spec-content-frontmatter-001').replace('/gov/spec-content-frontmatter-001.md','/content/spec-content-frontmatter-001.md').replace('main/posts/index.md）','main/posts/index.md)')
            body=re.sub(r'\[oai_citation:[^\]]+\]\(sediment://[^)]+\)','[栏目目录](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/posts/ai-discourse-analysis/index.md)',body)
            body=body.replace('- no extra fields','- use the shared core fields; preserve documented optional fields when needed').replace('不加字段','特殊信息使用规范中的扩展字段')
    if repo=='spec' and 'legacy' not in Path(rel).parts:
        body=body.replace('`content-frontmatter-enums.md`','[Content Frontmatter 枚举表](../appendix/spec-content-frontmatter-enums-001.md)').replace('`content-frontmatter-001.md`','[Content Frontmatter 说明](../content/spec-content-frontmatter-001.md)').replace('`commit-message-enums.md`','[Commit Message 枚举表](../appendix/spec-commit-message-enums-001.md)')
        if 'spec-content-frontmatter-enums' in rel:body=body.replace('- 2025','- "2025"').replace('- 2026','- "2026"')
        if rel.endswith('spec-content-frontmatter-enums-quickref-001.md'):
            body=body.replace('普通内容速查模板','普通内容取值目录（不是文章模板）').replace('翻译内容速查模板','翻译内容取值目录（不是文章模板）')
            body=body.replace('本文件按标准 frontmatter 的字段顺序排列。','本文件按标准 frontmatter 的字段顺序排列。\n\n> 前两节列出候选值，不能整块复制为文章 metadata；单值字段每次只选一个值。可复制草稿见第 4、5 节，特殊信息收纳见 [metadata 规范](../content/spec-content-frontmatter-001.md#统一使用与扩展字段)。')
        if rel=='content/spec-content-frontmatter-001.md':
            body=body.replace('`id` 推荐与文件名保持一致，但二者不是同一个概念。文件名可以改变；`id` 一旦确定，应尽量保持稳定。','普通文档文件名统一为 `id.md`；固定入口与不能安全迁移的旧链接保留例外并记录原因。`id` 确定后尽量保持稳定，确需规范化时用 `aliases` 保留旧身份。')
            body+='\n\n---\n\n'+SPEC_EXTENSIONS
        if rel=='appendix/spec-content-frontmatter-enums-001.md':body+='\n\n## 当前目录补充\n\n- `module` 同时支持说明文件所属的 `foodie`、`stills`、`motion`、`now`、`intake`、`assets`。\n- `submodule` 以实际一级归属目录为准，包括 posts 的 `"2019"`、netcom 的 `software`；说明入口可用 `guide`，仓库根说明用 `root`，旧资料用 `legacy`。\n- spec 使用实际目录 `appendix`、`archive`、`content`、`gov`、`legacy`、`source`、`spacetime`、`system`、`ver`；旧 `refs`、`time` 不用于新稿。\n- `source_of_truth: assets` 用于资源仓库维护说明。未知日期、confidence 可为 `null`，应在 note 说明；不得自动填高可信度。\n- 完整字段类型见[机器校验表](../content/content-metadata.schema.json)，特殊信息见[统一与扩展字段](../content/spec-content-frontmatter-001.md#统一使用与扩展字段)。\n'
    return body

def write_schema(root):
    string={'type':'string'};nullable={'type':['string','null']};arr={'type':'array','items':string,'uniqueItems':True}
    props={k:string for k in ['title','module','submodule','type','status','maturity','visibility','source_of_truth']}
    props['id']={'type':'string','pattern':'^[a-z0-9]+(?:-[a-z0-9]+)*$'};props['title']={'type':'string','minLength':1}
    for k in ['topic','summary']:props[k]=nullable
    for k in ARRAYS:props[k]=arr
    props['canonical']={'type':'boolean'};props['confidence']={'type':['number','null'],'minimum':0,'maximum':1}
    for k in ['created','updated','metadata_updated']:props[k]={'type':['string','null'],'format':'date'}
    for k in ['original_title','original_source','original_publisher','original_url','translation_note','subtitle','archive_url','note','layout','lang','description','canonical_url','permalink']:props[k]=nullable
    for k in ['rights','legacy','extra']:props[k]={'type':'object'}
    props['references']={'type':'array','items':{'type':'object','required':['text'],'properties':{'section':string,'text':string},'additionalProperties':False}}
    props['filename_policy']={'enum':['entrypoint','stable-link']}
    for k,values in {'module':['posts','natsci','netcom','blogops','foodie','stills','motion','now','intake','system','spec','assets'],'type':['note','article','translation','index','log','spec','release'],'status':['hidden','private','draft','active','publish','published','archive','archived'],'maturity':['draft','evolving','stable','deprecated'],'visibility':['public','private','internal'],'source_of_truth':['devlog','spec','assets','site','translation','external']}.items():props[k]={'enum':values}
    schema={'$schema':'https://json-schema.org/draft/2020-12/schema','$id':'https://raw.githubusercontent.com/fivsevn-agy/fivsevn-spec/main/content/content-metadata.schema.json','title':'fivsevn shared content metadata','type':'object','required':[k for g in GROUPS[:9] for k in g]+['created','updated'],'properties':props,'additionalProperties':False,'allOf':[{'if':{'properties':{'type':{'const':'translation'}}},'then':{'required':['original_title','original_source','original_publisher','original_url','translation_note']}}]}
    (root/'content/content-metadata.schema.json').write_text(json.dumps(schema,ensure_ascii=False,indent=2)+'\n')

def normalize(root,repo):
    tracked=subprocess.check_output(['git','ls-files','-z'],cwd=root).split(b'\0')
    files=[Path(x.decode()) for x in tracked if x]
    originals={p.as_posix():(root/p).read_bytes() for p in files if p.suffix=='.md'}
    protected={p.as_posix():(root/p).read_bytes() for p in files if p.name.lower() in {'index.md','index.html'} or p.as_posix() in (PROTECTED|{'blogops/.cache'}) and repo=='devlog'}
    manifest=[];renames={}
    for rel,raw in originals.items():
        if not eligible(repo,rel):continue
        p=Path(rel);old,body,rawfm=split(raw.decode('utf-8'));fm=copy.deepcopy(old)
        if repo=='devlog':module=p.parts[0] if len(p.parts)>1 else 'system';sub=p.parts[1] if len(p.parts)>2 else 'guide' if p.name=='README.md' else 'root'
        else:module='spec';sub=p.parts[0] if len(p.parts)>1 else 'root'
        if sub=='_drafts':sub='drafts'
        iswp=repo=='devlog' and p.stem in WP and p.parent.as_posix() in {'posts/2019','posts/2025'}
        ident=WP[p.stem][0] if iswp else old.get('id') or ('-'.join((['spec'] if repo=='spec' else [])+list(p.parent.parts)+['readme']) if p.name=='README.md' else p.stem.lower())
        if old.get('id') and old['id']!=ident:fm.setdefault('aliases',[]).append(old['id']);retain(fm,'id',old['id'])
        fm['id']=ident;fm.setdefault('title',title(body,p.stem));change(fm,'module',module);change(fm,'submodule',str(sub))
        fm.setdefault('topic','guide' if p.name=='README.md' else 'archive' if 'legacy' in p.parts else p.stem.lower())
        fm.setdefault('type','spec' if repo=='spec' and 'legacy' not in p.parts else 'note')
        fm.setdefault('status','archived' if 'legacy' in p.parts else 'hidden' if rel=='natsci/taxonomy/chondrichthyes/鲨鱼数据库.md' else 'active')
        fm.setdefault('canonical','legacy' not in p.parts)
        fm.setdefault('summary',('保留旧版内容：' if 'legacy' in p.parts else '说明')+str(fm['title'])+'。')
        for k in ['parents','related','tags','audience','languages']:
            if k not in fm:fm[k]=['self','internal'] if k=='audience' else ['zh'] if k=='languages' else []
            elif fm[k] is None:change(fm,k,[])
            elif not isinstance(fm[k],list):change(fm,k,[fm[k]])
        for k in ['parents','related']:
            values=[]
            for target in fm[k]:
                if target in UNRESOLVED:fm.setdefault('legacy',{}).setdefault('unresolved_relations',{}).setdefault(k,[]).append(target)
                else:values.append(RELATIONS.get(target,target))
            if values!=fm[k]:change(fm,k,values)
        fm.setdefault('maturity','deprecated' if 'legacy' in p.parts else 'evolving')
        if fm['maturity']=='archive':change(fm,'maturity','stable');note(fm,'旧 maturity: archive 表示存档；原标记保留在 legacy.metadata。')
        fm.setdefault('confidence',None);fm.setdefault('visibility','public');fm.setdefault('source_of_truth',repo)
        if repo=='spec':
            change(fm,'source_of_truth','spec')
            if 'legacy' not in p.parts and fm['type']=='index':change(fm,'type','spec')
        if repo=='devlog' and fm.get('source_of_truth')=='posts':change(fm,'source_of_truth','devlog')
        if fm.get('type') in {'translation','traslation'} and 'legacy' not in p.parts:
            change(fm,'type','translation');change(fm,'source_of_truth','translation')
            for k in ['original_title','original_source','original_publisher','original_url','translation_note']:fm.setdefault(k,None)
        if 'created' not in fm:
            first=git_date(root,rel,True)
            if first and fm.get('updated') and first>fm['updated']:first=None
            fm['created']=first;note(fm,'未记录原始写作日期；created 为本路径首次 Git 记录日期，无法合理确定时留空。')
        fm.setdefault('updated',git_date(root,rel,False));fm['metadata_updated']=DAY
        if iswp:wp_fields(fm,body,p)
        if rel=='netcom/rf/netcom-bluetooth-naming-001.md' and repo=='devlog':
            assert 'https://www.kardach.com/bluetooth/naming-bluetooth' in body;fm['original_url']='https://www.kardach.com/bluetooth/naming-bluetooth'
        if rel=='natsci/taxonomy/chondrichthyes/鲨鱼数据库.md' and repo=='devlog':
            fm['id']='natsci-taxonomy-shark-databases-001';fm['title']='鲨鱼数据库';fm['topic']='shark-databases';fm['summary']='保留现有鲨鱼相关数据库链接与资料说明。';note(fm,'此前无 metadata，未进入目录；补字段后仍保持不收录。')
        if rawfm:
            spans=[(t.start_mark.index,t.end_mark.index) for t in yaml.scan(rawfm) if isinstance(t,yaml.tokens.ScalarToken)]
            comments=[m.group() for m in re.finditer(r'#[^\n]*',rawfm) if not any(a<=m.start()<b for a,b in spans)]
            if comments:fm.setdefault('legacy',{})['comments']=comments
        dest=p
        if p.name=='README.md':fm['filename_policy']='entrypoint'
        elif repo=='devlog' and (rel in FIXED or rel.startswith('blogops/docs/') or rel.startswith('posts/ai-discourse-analysis/content/') or (old.get('status') in {'active','publish','published'} and old.get('original_source')!='WordPress')):
            if p.stem!=fm['id']:fm['filename_policy']='stable-link';note(fm,'保留现有文件名：展示目录或已发布链接使用该路径，本次不修改展示页；metadata id 继续作为内容身份。')
        else:dest=p.with_name(fm['id']+'.md')
        newbody=body_edits(repo,rel,body)
        if dest!=p:
            assert not (root/dest).exists(),str(dest);fm.setdefault('legacy',{})['path']=rel
            if iswp:fm['permalink']='/'+p.with_suffix('.html').as_posix()
            (root/p).unlink();renames[rel]=dest.as_posix()
        (root/dest).write_text(render(fm,newbody),encoding='utf-8')
        for key,value in old.items():
            assert fm.get(key)==value or fm.get('legacy',{}).get('metadata',{}).get(key)==value,(rel,key)
        if iswp:
            assert body==newbody
            for key in ['status','visibility','canonical','created','updated','confidence']:assert old[key]==fm[key],(rel,key)
        manifest.append({'old_path':rel,'path':dest.as_posix(),'id':fm['id'],'added_metadata':not bool(old),'body_changed':body!=newbody})
    for rel,raw in protected.items():assert (root/rel).read_bytes()==raw,rel
    if repo=='spec':write_schema(root)
    result={'repo':repo,'documents':manifest,'renames':renames,'protected_exact':list(protected),'all_original_fields_retained':True}
    Path('/tmp/metadata-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print(f'Normalized {len(manifest)} documents; renamed {len(renames)}; protected {len(protected)} display/configuration files exactly.')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--repo',choices=['devlog','spec'],required=True);ap.add_argument('--root',type=Path,default=Path('.'));a=ap.parse_args();normalize(a.root.resolve(),a.repo)
