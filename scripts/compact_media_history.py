#!/usr/bin/env python3
"""Compact scoped non-WebP image history; prepare locally, then explicitly push.

Requires git-filter-repo. Run after publication, live verification and inbox
cleanup. --prepare never pushes. --push requires the verified external bundle
and an unchanged remote main lease. Remote PR refs are observed, never fetched
or modified; this tool makes no claim about GitHub's server-side garbage collection.
"""
from __future__ import annotations

import argparse
import copy
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.parse import urlsplit


RASTER_EXTENSIONS = frozenset({
    b'jpg', b'jpeg', b'jpe', b'jfif', b'png', b'apng', b'gif', b'heif', b'heic',
    b'tif', b'tiff', b'bmp', b'dib', b'avif', b'ico', b'cur', b'mpo', b'jp2',
    b'jpx', b'jxl', b'pcx', b'pbm', b'pgm', b'ppm', b'pnm', b'pam',
})
REPOSITORIES = {'flux': 'fivsevn/fivsevn-flux', 'savour': 'fivsevn/fivsevn-savour',
                'devlog': 'fivsevn-agy/fivsevn-devlog', 'roll': 'fivsevn/fivsevn-roll'}
STATE_FILES = {
    'flux': ('.publishing/state.json',), 'savour': ('.publishing/state.json',),
    'devlog': ('natsci/fieldlog/.publishing/state.json',),
    'roll': ('.publishing/stills.json', '.publishing/bygone.json', 'stills/.publishing/state.json'),
}
IGNORED_INBOX_NAMES = {b'README.md', b'.keep', b'.gitkeep', b'.DS_Store'}
MAIN = 'refs/heads/main'
OID = re.compile(r'(?:[0-9a-f]{40}|[0-9a-f]{64})\Z')


class CleanupError(RuntimeError):
    pass


class Deferred(CleanupError):
    pass


def run(repo, *args, input=None, check=True):
    result = subprocess.run(['git', '-C', str(repo), *args], input=input, capture_output=True)
    if check and result.returncode:
        raise CleanupError('git ' + args[0] + ' failed: ' + result.stderr.decode('utf-8', 'replace').strip())
    return result


def git(repo, *args):
    return run(repo, *args).stdout


def sha256_file(path):
    value = hashlib.sha256()
    with Path(path).open('rb') as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b''):
            value.update(chunk)
    return value.hexdigest()


def write_json(path, data):
    temporary = Path(str(path) + '.tmp')
    temporary.write_text(json.dumps(data, ensure_ascii=True, indent=2, sort_keys=True) + '\n')
    os.replace(temporary, path)


def scoped_image(path: bytes, scope: str) -> bool:
    extension = path.rsplit(b'/', 1)[-1].rsplit(b'.', 1)
    if len(extension) != 2 or extension[1].lower() not in RASTER_EXTENSIONS:
        return False
    if scope in {'flux', 'savour'}:
        return True
    if scope == 'devlog':
        return path.startswith(b'natsci/fieldlog/')
    return path.startswith((b'stills/bygone/', b'stills/2026/06/bygone/'))


def tree(repo, revision):
    result = {}
    for item in git(repo, 'ls-tree', '-r', '-z', revision).split(b'\0'):
        if item:
            metadata, path = item.split(b'\t', 1)
            mode, kind, oid = metadata.decode('ascii').split()
            result[path] = {'mode': mode, 'type': kind, 'oid': oid}
    return result


def tree_digest(entries):
    return hashlib.sha256(json.dumps([(p.hex(), v) for p, v in sorted(entries.items())],
                                    sort_keys=True).encode()).hexdigest()


def local_refs(repo):
    return dict(line.split(' ', 1) for line in git(repo, 'for-each-ref', '--format=%(refname) %(objectname)').decode().splitlines())


def remote_snapshot(repo, remote_url):
    # Do not fetch PR refs: they must not enter the rewrite or retain local objects.
    refs = {}
    for line in git(repo, 'ls-remote', '--refs', remote_url).decode().splitlines():
        oid, ref = line.split('\t', 1)
        refs[ref] = oid
    writable = {ref: oid for ref, oid in refs.items() if not ref.startswith('refs/pull/')}
    if set(writable) != {MAIN}:
        raise CleanupError('Remote must have exactly main and no tags or other writable refs')
    return {'main': writable[MAIN], 'pr_refs': {k: v for k, v in refs.items() if k.startswith('refs/pull/')},
            'pr_refs_read_only': True}


def object_metrics(repo):
    folder = Path(git(repo, 'rev-parse', '--git-path', 'objects').decode().strip())
    if not folder.is_absolute():
        folder = Path(repo) / folder
    return {'objects_directory_bytes': sum(p.stat().st_size for p in folder.rglob('*') if p.is_file()),
            'count_objects': git(repo, 'count-objects', '-v').decode().strip()}


def ancestor(repo, older, newer):
    return run(repo, 'merge-base', '--is-ancestor', older, newer, check=False).returncode == 0


def publication_sources(repo, scope, states):
    sources = []
    if scope == 'flux':
        state = states.get('.publishing/state.json', {})
        for name, source in state.get('sources', {}).items():
            if source.get('repository') != REPOSITORIES[scope]:
                continue  # External historical sources are stable provenance.
            sources.append((f'sources.{name}.cursor', source['cursor'], source['path']))
    elif scope in {'savour', 'devlog'}:
        path = STATE_FILES[scope][0]
        if path in states:
            sources.append(('cursor', states[path]['cursor'], 'trigger_imgs' if scope == 'savour' else 'natsci/fieldlog/trigger_imgs'))
    return sources


def pending_input_changes(repo, scope, states, head):
    pending = []
    for field, cursor, prefix in publication_sources(repo, scope, states):
        if not isinstance(cursor, str) or not OID.fullmatch(cursor) or not ancestor(repo, cursor, head):
            raise CleanupError('Publication cursor is not a surviving main ancestor: ' + field)
        for commit in git(repo, 'rev-list', head, '^' + cursor).decode().splitlines():
            # --no-renames gives exact source paths; deletions cannot create new posts.
            paths = git(repo, 'diff-tree', '--root', '--no-commit-id', '--name-only', '-r', '-z',
                        '--no-renames', '--diff-filter=AMT', commit).split(b'\0')
            encoded = prefix.encode()
            for path in paths:
                if path and (path == encoded or path.startswith(encoded.rstrip(b'/') + b'/')) and path.rsplit(b'/', 1)[-1] not in IGNORED_INBOX_NAMES:
                    pending.append({'field': field, 'commit': commit, 'path': path.decode('utf-8', 'surrogateescape')})
    if scope == 'roll':
        # An unprocessed WebP upload also needs publication before compaction.
        for path in tree(repo, head):
            if path.startswith(b'stills/bygone/trigger_img/') and path.rsplit(b'/', 1)[-1] not in IGNORED_INBOX_NAMES:
                pending.append({'field': 'Bygone inbox', 'path': path.decode('utf-8', 'surrogateescape')})
    return pending


def map_states(scope, states, mapping):
    changed, changes, cursors = {}, [], []

    def mapped(value, file, field, zero_ok=False):
        if value is None or zero_ok and isinstance(value, str) and value and set(value) == {'0'}:
            return value
        if not isinstance(value, str) or not OID.fullmatch(value) or value not in mapping or set(mapping[value]) == {'0'}:
            raise CleanupError('Unknown or pruned publication commit: ' + file + ':' + field)
        replacement = mapping[value]
        if replacement != value:
            changes.append({'file': file, 'field': field, 'before': value, 'after': replacement})
        return replacement

    for file, original in states.items():
        data = copy.deepcopy(original)
        if 'cursor' in data:
            data['cursor'] = mapped(data['cursor'], file, 'cursor')
            cursors.append((file + ':cursor', data['cursor']))
        if scope == 'flux':
            for name, source in data.get('sources', {}).items():
                if source.get('repository') != REPOSITORIES[scope]:
                    continue
                field = 'sources.' + name
                source['cursor'] = mapped(source['cursor'], file, field + '.cursor')
                cursors.append((file + ':' + field + '.cursor', source['cursor']))
                if 'verification_commits' in source:
                    source['verification_commits'] = [mapped(value, file, field + '.verification_commits') for value in source['verification_commits']]
                # latest_uploads, source_commit and source_key are paired original
                # publication identities. They intentionally keep the old identity.
        if 'events' in data:
            events = {}
            for key, event in data['events'].items():
                if not isinstance(event, dict):
                    raise CleanupError('Invalid publication event in ' + file)
                new_key = key
                if 'commit' in event:
                    old = event['commit']
                    event['commit'] = mapped(old, file, 'events.' + key + '.commit')
                    if key.startswith(old + ':'):
                        new_key = event['commit'] + key[len(old):]
                if scope == 'roll':
                    for field in ('before', 'after'):
                        if field in event:
                            event[field] = mapped(event[field], file, 'events.' + key + '.' + field, zero_ok=field == 'before')
                    parts = key.split(':')
                    if len(parts) >= 2 and parts[0] in {'push', 'manual'} and OID.fullmatch(parts[1]):
                        parts[1] = mapped(parts[1], file, 'events key ' + key)
                        new_key = ':'.join(parts)
                if new_key in events:
                    raise CleanupError('Publication event key collision after rewrite')
                if new_key != key:
                    changes.append({'file': file, 'field': 'event_key', 'before': key, 'after': new_key})
                events[new_key] = event
            data['events'] = events
        if data != original:
            changed[file] = data
    return changed, changes, cursors


def compact(repo, scope, output, defer_if_pending=False, remote='origin'):
    repo, output = Path(repo).resolve(), Path(output).resolve()
    if output.is_relative_to(repo):
        raise CleanupError('Bundle and report directory must be outside the checkout')
    output.mkdir(parents=True, exist_ok=True)
    report_path = output / 'report.json'
    if report_path.exists():
        raise CleanupError('Use a fresh output directory for each preparation')
    report = {'version': 1, 'scope': scope, 'repository_path': str(repo), 'status': 'preparing',
              'created_at': datetime.now(timezone.utc).isoformat(), 'remote_pr_refs_touched': False,
              'state_changes': [], 'changed_state_files': [], 'filtered_path_count': 0,
              'server_gc_completed': False,
              'server_limitations': 'Only main is rewritten. Read-only GitHub PR refs and server object retention are outside this tool.'}
    try:
        if git(repo, 'rev-parse', '--is-bare-repository').strip() != b'false' or git(repo, 'rev-parse', '--is-shallow-repository').strip() != b'false':
            raise CleanupError('A complete non-bare checkout is required')
        if git(repo, 'status', '--porcelain', '--untracked-files=all'):
            raise CleanupError('Checkout must be clean, including untracked files')
        if git(repo, 'worktree', 'list', '--porcelain').count(b'worktree ') != 1:
            raise CleanupError('Linked worktrees are not supported')
        gitdir = Path(git(repo, 'rev-parse', '--absolute-git-dir').decode().strip())
        if Path(git(repo, 'rev-parse', '--show-toplevel').decode().strip()).resolve() != repo or output.is_relative_to(gitdir):
            raise CleanupError('Use the checkout root and an output directory outside its Git directory')
        if (gitdir / 'objects/info/alternates').exists():
            raise CleanupError('Object alternates are not supported')
        allowed = {MAIN, 'refs/remotes/' + remote + '/main', 'refs/remotes/' + remote + '/HEAD'}
        refs = local_refs(repo)
        if set(refs) - allowed:
            raise CleanupError('Local refs must contain only main and its origin tracking refs; no tags/PR refs')
        old_head = git(repo, 'rev-parse', 'HEAD').decode().strip()
        if any(oid != old_head for oid in refs.values()):
            raise CleanupError('Local main and remote tracking refs must agree with HEAD')
        url = git(repo, 'remote', 'get-url', remote).decode().strip()
        parsed = urlsplit(url)
        if parsed.scheme in {'http', 'https'} and (parsed.username or parsed.password or parsed.query or parsed.fragment):
            raise CleanupError('Use a credential-free remote URL and the existing credential helper/header')
        report.update(remote_url=url, remote_name=remote, old_head=old_head, before_refs=refs,
                      before_metrics=object_metrics(repo), remote_before=remote_snapshot(repo, url))
        if report['remote_before']['main'] != old_head:
            raise Deferred('Remote main changed before preparation')
        current = tree(repo, old_head)
        report['before_tree'] = tree_digest(current)
        pending = [path.decode('utf-8', 'surrogateescape') for path in current if scoped_image(path, scope)]
        states = {}
        for file in STATE_FILES[scope]:
            if (repo / file).exists():
                if (repo / file).is_symlink():
                    raise CleanupError('Publishing state must not be a symlink')
                states[file] = json.loads((repo / file).read_text())
        if scope != 'roll' and STATE_FILES[scope][0] not in states:
            raise CleanupError('Required publication state is missing')
        pending_uploads = pending_input_changes(repo, scope, states, old_head)
        report.update(pending_current_non_webp=pending, pending_publication_inputs=pending_uploads)
        if pending or pending_uploads:
            raise Deferred('Unprocessed image/content inputs remain; publish and verify them first')
        commits = git(repo, 'rev-list', old_head).decode().splitlines()
        targets, trees = {}, set()
        for commit in commits:
            tree_id = git(repo, 'rev-parse', commit + '^{tree}').strip()
            if tree_id in trees:
                continue
            trees.add(tree_id)
            for path, entry in tree(repo, commit).items():
                if entry['type'] == 'blob' and scoped_image(path, scope):
                    targets.setdefault(path, set()).add(entry['oid'])
        inventory = [{'path': path.decode('utf-8', 'surrogateescape'), 'path_hex': path.hex(), 'blob_ids': sorted(oids)} for path, oids in sorted(targets.items())]
        write_json(output / 'filtered-paths.json', inventory)
        report.update(filtered_path_count=len(targets), filtered_blob_id_count=len({oid for values in targets.values() for oid in values}),
                      before_commit_count=len(commits), filtered_paths_file='filtered-paths.json')
        if not targets:
            report.update(status='noop', after_head=old_head, protected_files_equal=True, after_metrics=report['before_metrics'])
            write_json(report_path, report)
            return report
        if MAIN not in refs:
            git(repo, 'checkout', '-b', 'main', old_head)
        elif run(repo, 'symbolic-ref', '-q', 'HEAD', check=False).stdout.strip() != MAIN.encode():
            git(repo, 'checkout', 'main')
        bundle = output / 'pre-cleanup.bundle'
        git(repo, 'bundle', 'create', str(bundle), '--all')
        git(repo, 'bundle', 'verify', str(bundle))
        report['backup'] = {'path': str(bundle), 'bytes': bundle.stat().st_size, 'sha256': sha256_file(bundle), 'verified': True}
        write_json(report_path, report)
        if remote_snapshot(repo, url)['main'] != old_head:
            raise Deferred('Remote main changed after backup; no rewrite started')
        if git(repo, 'status', '--porcelain', '--untracked-files=all') or git(repo, 'rev-parse', 'HEAD').decode().strip() != old_head:
            raise CleanupError('Checkout changed during backup; refusing rewrite')
        path_list = output / 'path-hex.json'
        write_json(path_list, [path.hex() for path in sorted(targets)])
        callback = ('import json\n'
                    'paths = globals().get("_webp_cleanup_exact_paths")\n'
                    'if paths is None:\n'
                    f'    with open({str(path_list)!r}, encoding="utf-8") as handle:\n'
                    '        paths = {bytes.fromhex(value) for value in json.load(handle)}\n'
                    '    globals()["_webp_cleanup_exact_paths"] = paths\n'
                    'commit.file_changes = [change for change in commit.file_changes if change.filename not in paths]\n')
        previous = gitdir / 'filter-repo'
        if previous.exists():
            shutil.move(previous, output / 'previous-filter-repo-metadata')
        filtering = subprocess.run([sys.executable, '-m', 'git_filter_repo', '--force', '--refs', MAIN,
                                   '--prune-empty', 'never', '--prune-degenerate', 'never',
                                   '--replace-refs', 'delete-no-add', '--preserve-commit-hashes',
                                   '--preserve-commit-encoding', '--commit-callback', callback],
                                  cwd=repo, capture_output=True)
        (output / 'filter-repo.log').write_bytes(filtering.stdout + filtering.stderr)
        if filtering.returncode:
            raise CleanupError('git-filter-repo failed; inspect external filter-repo.log and restore from bundle if needed')
        raw_map = (gitdir / 'filter-repo/commit-map').read_text()
        mapping = dict(line.split() for line in raw_map.splitlines()[1:] if line.strip())
        filtered_map = {old: mapping[old] for old in commits if old in mapping}
        if len(filtered_map) != len(commits) or any(set(new) == {'0'} for new in filtered_map.values()):
            raise CleanupError('Commit nodes were pruned or missing from commit-map')
        write_json(output / 'commit-map.json', filtered_map)
        (output / 'commit-map.txt').write_text('old new\n' + ''.join(f'{old} {new}\n' for old, new in sorted(filtered_map.items())))
        rewritten = git(repo, 'rev-parse', MAIN).decode().strip()
        if len(git(repo, 'rev-list', rewritten).splitlines()) != len(commits):
            raise CleanupError('Rewrite did not preserve every commit node')
        if tree(repo, rewritten) != current:
            raise CleanupError('Current file modes/blob IDs changed during history filtering')
        checked_trees = set()
        for commit in git(repo, 'rev-list', rewritten).decode().splitlines():
            tree_id = git(repo, 'rev-parse', commit + '^{tree}').strip()
            if tree_id in checked_trees:
                continue
            checked_trees.add(tree_id)
            if any(scoped_image(path, scope) for path in tree(repo, commit)):
                raise CleanupError('Scoped non-WebP image paths remain in rewritten main history')
        changed_states, state_changes, cursors = map_states(scope, states, filtered_map)
        for file, data in changed_states.items():
            write_json(repo / file, data)
        if changed_states:
            git(repo, 'add', '--', *changed_states)
            git(repo, '-c', 'user.name=WebP history maintenance', '-c', 'user.email=webp-history@example.invalid',
                'commit', '--no-gpg-sign', '-m', 'chore: map publication state after image history cleanup')
        final = git(repo, 'rev-parse', MAIN).decode().strip()
        final_tree = tree(repo, final)
        protected = {p: v for p, v in current.items() if p.decode('utf-8', 'surrogateescape') not in changed_states}
        if {p: v for p, v in final_tree.items() if p.decode('utf-8', 'surrogateescape') not in changed_states} != protected:
            raise CleanupError('Protected current files changed while mapping state')
        for field, cursor in cursors:
            if not ancestor(repo, cursor, final):
                raise CleanupError('Mapped cursor is not a surviving main ancestor: ' + field)
        # --refs retains remote credentials/config. Remove only old tracking refs,
        # then expire reflogs and collect unreachable originals for honest metrics.
        removed_refs = []
        for ref in local_refs(repo):
            if ref.startswith('refs/remotes/' + remote + '/'):
                git(repo, 'update-ref', '--no-deref', '-d', ref)
                removed_refs.append(ref)
        git(repo, 'reflog', 'expire', '--expire=now', '--all')
        git(repo, 'gc', '--prune=now')
        git(repo, 'fsck', '--full', '--no-reflogs')
        if set(local_refs(repo)) != {MAIN} or git(repo, 'status', '--porcelain', '--untracked-files=all'):
            raise CleanupError('Prepared checkout must be clean with only local main')
        report.update(status='prepared', rewritten_head=rewritten, after_head=final,
                      after_tree=tree_digest(final_tree), state_changes=state_changes,
                      changed_state_files=sorted(changed_states), state_file_blobs={f: final_tree[f.encode()]['oid'] for f in changed_states},
                      preserved_commit_nodes=len(commits), after_commit_count=len(git(repo, 'rev-list', final).splitlines()),
                      commit_map_file='commit-map.json', protected_files_equal=True, protected_file_count=len(protected),
                      before_git_tree=git(repo, 'rev-parse', rewritten + '^{tree}').decode().strip(),
                      after_git_tree=git(repo, 'rev-parse', final + '^{tree}').decode().strip(), remaining_target_paths=0,
                      cursor_ancestors_verified=True, pending_publication_inputs_after_mapping=0,
                      stable_source_identity_policy='Preserve post source_commit/source_key and Flux latest_uploads; map only explicit cursor/verification/event Git references.',
                      removed_remote_tracking_refs=removed_refs, local_reflogs_expired=True,
                      local_gc_completed=True, after_metrics=object_metrics(repo), credentials_preserved=True)
        write_json(report_path, report)
        return report
    except Deferred as error:
        report.update(status='deferred' if defer_if_pending else 'failed', reason=str(error))
        write_json(report_path, report)
        if defer_if_pending:
            return report
        raise CleanupError(str(error)) from error
    except Exception as error:
        report.update(status='failed', reason=str(error))
        write_json(report_path, report)
        raise


def push(repo, output, defer_if_pending=False):
    repo, output = Path(repo).resolve(), Path(output).resolve()
    path = output / 'report.json'
    report = json.loads(path.read_text())
    if report['status'] in {'noop', 'deferred'}:
        return report
    if report['status'] != 'prepared' or report['repository_path'] != str(repo):
        raise CleanupError('Push requires a prepared report for this checkout')
    backup = report['backup']
    bundle = Path(backup['path'])
    if not bundle.is_file() or sha256_file(bundle) != backup['sha256']:
        raise CleanupError('Verified pre-cleanup bundle is missing or changed')
    git(repo, 'bundle', 'verify', str(bundle))
    if set(local_refs(repo)) != {MAIN} or git(repo, 'status', '--porcelain', '--untracked-files=all') or git(repo, 'rev-parse', MAIN).decode().strip() != report['after_head'] or tree_digest(tree(repo, MAIN)) != report['after_tree']:
        raise CleanupError('Prepared checkout changed before push')
    remote = remote_snapshot(repo, report['remote_url'])
    if remote['main'] != report['old_head']:
        if not defer_if_pending:
            raise CleanupError('Remote lease changed; refusing force push')
        report.update(status='deferred', reason='Remote lease changed; no push attempted', remote_at_defer=remote)
        write_json(path, report)
        return report
    result = run(repo, 'push', '--force-with-lease=' + MAIN + ':' + report['old_head'],
                 report['remote_url'], MAIN + ':' + MAIN, check=False)
    (output / 'push.log').write_bytes(result.stdout + result.stderr)
    if result.returncode:
        current = remote_snapshot(repo, report['remote_url'])
        if defer_if_pending and current['main'] != report['old_head']:
            report.update(status='deferred', reason='Lease rejected during push; remote work preserved', remote_at_defer=current)
            write_json(path, report)
            return report
        raise CleanupError('Force-with-lease push failed; inspect external push.log')
    after = remote_snapshot(repo, report['remote_url'])
    if after['main'] != report['after_head']:
        raise CleanupError('Remote main does not match the pushed prepared head')
    report.update(status='pushed', remote_after=after, pushed_ref=MAIN, force_with_lease_old_head=report['old_head'],
                  pushed_at=datetime.now(timezone.utc).isoformat(), remote_pr_refs_touched=False)
    write_json(path, report)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    stage = parser.add_mutually_exclusive_group(required=True)
    stage.add_argument('--prepare', action='store_true')
    stage.add_argument('--push', action='store_true')
    parser.add_argument('--repo', type=Path, default=Path.cwd())
    parser.add_argument('--scope', choices=tuple(REPOSITORIES))
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--defer-if-pending', action='store_true')
    args = parser.parse_args()
    if args.prepare and args.scope is None:
        parser.error('--prepare requires --scope')
    try:
        report = compact(args.repo, args.scope, args.output_dir, args.defer_if_pending) if args.prepare else push(args.repo, args.output_dir, args.defer_if_pending)
        print(json.dumps(report, ensure_ascii=True, sort_keys=True))
    except (CleanupError, OSError, ValueError) as error:
        print(json.dumps({'status': 'failed', 'error': str(error)}), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
