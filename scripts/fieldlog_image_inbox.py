#!/usr/bin/env python3
"""Clear only exact inbox copies whose saved package was verified publicly."""
import argparse
import hashlib
import json
from pathlib import Path
from site_post_metadata import is_published, read_frontmatter

ROOT = Path(__file__).resolve().parents[1]
CONTENT = 'natsci/fieldlog'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def clear_verified(root=ROOT, output=None):
    root = Path(root).resolve()
    folder = root / CONTENT
    site = Path(output or root / '_site' / CONTENT)
    receipt_path = site / 'build-receipt.json'
    fingerprint = digest(receipt_path)
    receipt = json.loads(receipt_path.read_text())
    deployed = json.loads((folder / '.publishing/deployed.json').read_text())
    verified = json.loads((site / '.verified.json').read_text())
    if (deployed.get('receipt_sha256') != fingerprint or verified.get('receipt_sha256') != fingerprint
            or deployed.get('files') != receipt['files']):
        raise ValueError('Refusing inbox cleanup without matching public verification.')
    state = json.loads((folder / '.publishing/state.json').read_text())
    inbox = folder / 'trigger_imgs'
    pending = set()
    # A reused path belongs to its newest upload, even if its bytes are identical.
    latest = {event['upload_path']: event for event in state['events'].values()}
    for event in latest.values():
        source = root / event['upload_path']
        saved = root / event['image_path']
        if ('..' in Path(event['upload_path']).parts or '..' in Path(event['image_path']).parts
                or source.is_symlink() or saved.is_symlink()
                or not source.resolve().is_relative_to(inbox.resolve())
                or not saved.resolve().is_relative_to(folder.resolve())):
            raise ValueError('Unsafe inbox cleanup path.')
        if not source.is_file() or not saved.is_file():
            continue
        saved_sha = event.get('file_sha256', event['sha256'])
        if digest(source) != event['sha256'] or digest(saved) != saved_sha:
            continue  # A newer upload or manually edited saved image is never removed.
        package = saved.parent.parent
        meta, _ = read_frontmatter(package / 'index.md')
        if not is_published(meta):
            continue
        route = event['route']
        if not route.startswith(CONTENT + '/') or '..' in Path(route).parts:
            raise ValueError('Unsafe publication route')
        route = route[len(CONTENT) + 1:]
        page = route + 'index.html'
        media = route + 'assets/' + saved.name
        for path in [page, media]:
            expected = receipt['files'].get(path)
            if not expected or not (site / path).is_file() or digest(site / path) != expected:
                raise ValueError('Saved package was not verified live: ' + path)
        if digest(saved) != receipt['files'][media]:
            raise ValueError('Saved image changed after verification.')
        pending.add(source)
    # Validate every candidate before removing any file.
    total = sum(path.stat().st_size for path in pending)
    for path in sorted(pending):
        path.unlink()
    print(f'Cleared {len(pending)} verified inbox files ({total:,} bytes).')
    return len(pending), total


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    clear_verified(args.root, args.output)
