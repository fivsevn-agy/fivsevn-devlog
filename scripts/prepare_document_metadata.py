#!/usr/bin/env python3
"""Complete Jekyll document metadata and build the public discovery files."""
import argparse
from collections import Counter
from html import escape
import json
from pathlib import Path
from urllib.parse import unquote, urlparse

from site_post_metadata import read_frontmatter
from update_module_indexes import status_mode
from web_document import Document, ORIGIN, document_metadata


ROOT = Path(__file__).resolve().parents[1]
SKIP = {'.git', '.github', '.metadata-spec', '.shared-spec', '.venv', '_site', 'scripts', 'schemas', 'tests', 'node_modules', '__pycache__'}


def source_documents(root):
    result = {}
    for source in root.rglob('*'):
        relative = source.relative_to(root)
        if any(part in SKIP or part.startswith('.') for part in relative.parts):
            continue
        if source.suffix.lower() not in {'.md', '.markdown', '.html'} or not source.is_file():
            continue
        metadata, _ = read_frontmatter(source)
        if not metadata:
            continue
        permalink = metadata.get('permalink')
        if isinstance(permalink, str):
            key = unquote(urlparse(permalink).path).lstrip('/')
            if not key or key.endswith('/'):
                key += 'index.html'
        else:
            key = relative.with_suffix('.html').as_posix()
        if key in result:
            raise ValueError('Two source documents claim the same public path: ' + key)
        result[key] = metadata
    return result


def indexable(metadata):
    if not metadata:
        return True  # Generated standalone HTML, such as Intake.
    visibility = str(metadata.get('visibility') or '').strip().lower()
    return status_mode(metadata.get('status')) == 'link' and (not visibility or visibility == 'public')


def public_url(relative):
    path = relative.as_posix()
    if path.endswith('index.html'):
        path = path[:-len('index.html')]
    # Paths from the filesystem are already the Jekyll output paths; retain them.
    from urllib.parse import quote
    return ORIGIN + '/' + quote(path, safe='/%:@-._~')


def prepare(root=ROOT, *, check=False, site=None):
    root = Path(root).resolve()
    site = Path(site or root / '_site').resolve()
    if not site.is_dir() or site.is_symlink():
        raise ValueError('Build the website before preparing its document metadata')
    sources = source_documents(root)
    outputs = {}
    urls = set()
    languages = Counter()
    documents = 0
    for path in sorted(site.rglob('*.html')):
        if path.is_symlink():
            raise ValueError('Unexpected symlink in generated website: ' + str(path))
        relative = path.relative_to(site)
        original = path.read_text(encoding='utf-8')
        parsed = Document(original)
        if parsed.head_end is None or parsed.html_tag is None:
            continue  # Embedded Intake fragments are not standalone documents.
        metadata = sources.get(relative.as_posix(), {})
        allowed = indexable(metadata) and relative.as_posix() != '404.html'
        # Fieldlog is prepared by its own generator before its receipt is hashed.
        if relative.parts[:2] == ('natsci', 'fieldlog'):
            rendered = original
        else:
            rendered = document_metadata(original, url=public_url(relative), metadata=metadata, noindex=not allowed)
        current = Document(rendered)
        documents += 1
        languages[current.html_tag[2].get('lang', '')] += 1
        robots = ','.join([current.existing(name='robots'), current.existing(name='googlebot')]).lower()
        canonical = current.canonical()
        if allowed and 'noindex' not in robots and urlparse(canonical).netloc == urlparse(ORIGIN).netloc:
            urls.add(canonical)
        outputs[path] = rendered.encode('utf-8')
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += ''.join('  <url><loc>' + escape(url, quote=False) + '</loc></url>\n' for url in sorted(urls))
    sitemap += '</urlset>\n'
    outputs[site / 'sitemap.xml'] = sitemap.encode('utf-8')
    robots_path = site / 'robots.txt'
    robots = robots_path.read_text(encoding='utf-8') if robots_path.exists() else 'User-agent: *\nAllow: /\n'
    declaration = 'Sitemap: ' + ORIGIN + '/sitemap.xml'
    if declaration not in robots.splitlines():
        robots = robots.rstrip('\r\n') + '\n' + declaration + '\n'
    outputs[robots_path] = robots.encode('utf-8')
    changed = [path for path, data in outputs.items() if not path.exists() or path.read_bytes() != data]
    if check and changed:
        raise ValueError('Document metadata or discovery files are stale: ' + ', '.join(str(path.relative_to(site)) for path in changed))
    if not check:
        for path in changed:
            path.write_bytes(outputs[path])
    return {'documents': documents, 'changed': len(changed), 'sitemap_urls': len(urls), 'languages': dict(languages)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--site', type=Path, help='Use a separately built artifact directory')
    args = parser.parse_args()
    print(json.dumps(prepare(args.root, check=args.check, site=args.site), ensure_ascii=False))


if __name__ == '__main__':
    main()
