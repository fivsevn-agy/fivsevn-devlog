"""Compatibility entry point: validate the flux trigger; never contact WordPress."""
from pathlib import Path
import argparse
import yaml
import markdown

ROOT = Path(__file__).resolve().parents[1]
SOURCE_FILE = ROOT / 'posts/_flux/trigger.md'


def split_frontmatter(text):
    lines = text.replace('\r\n','\n').lstrip('\ufeff').splitlines(keepends=True)
    if not lines or lines[0].strip() != '---':
        return {}, ''.join(lines)
    end = next((i for i in range(1,len(lines)) if lines[i].strip()=='---'),None)
    if end is None:
        raise ValueError('Frontmatter is missing its closing ---')
    meta = yaml.safe_load(''.join(lines[1:end])) or {}
    if not isinstance(meta,dict): raise ValueError('Frontmatter must be a mapping')
    return meta,''.join(lines[end+1:]).strip()


def validate(text):
    meta,body=split_frontmatter(text)
    if str(meta.get('status') or meta.get('wp_status') or 'published') not in {'published','publish','draft','pending','private'}:
        raise ValueError('Use status: published or draft; future scheduling is not supported')
    if meta.get('title') is not None and not isinstance(meta['title'],str):
        raise ValueError('title must be text; use title: "" for the default time title')
    return markdown.markdown(body,extensions=['extra','sane_lists','nl2br'])


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dry-run',action='store_true')
    parser.add_argument('--check-event',action='store_true')
    parser.parse_args(argv)
    html=validate(SOURCE_FILE.read_text(encoding='utf-8-sig'))
    print(f'Trigger validated ({len(html)} HTML characters). No publication or WordPress request was made.')
    print('flux checks committed trigger changes approximately every 5 minutes; GitHub scheduling may delay a run.')
    print('Publication status: https://github.com/fivsevn/fivsevn-flux/actions/workflows/build.yml')
    return 0


if __name__=='__main__':
    raise SystemExit(main())
