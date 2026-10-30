#!/usr/bin/env python3
"""Copy migration media once, verifying each original before installation."""
from __future__ import annotations
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import tempfile
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_HOSTS = {"raw.githubusercontent.com", "fonts.wp.com"}


def safe_url(url: str) -> bool:
    parts = urlsplit(url)
    return (parts.scheme == "https" and parts.hostname in ALLOWED_HOSTS
            and not (parts.username or parts.password or parts.port or parts.fragment))


def atomic_write(destination: Path, data: bytes) -> None:
    """Install only complete files, including the one-time completion marker."""
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=destination.parent, prefix=".fieldlog-media-", delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(data)
        os.replace(temporary, destination)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def restore(root: Path = ROOT) -> int:
    root = Path(root).resolve()
    folder = root / "natsci/fieldlog"
    flag = folder / ".publishing/media-restored.json"
    if any(p.is_symlink() for p in [flag, *flag.parents] if p.is_relative_to(root)):
        raise ValueError("Unsafe migration media completion path")
    if flag.exists():
        print("Migration media already installed; preserving subsequent image edits.")
        return 0
    manifest = json.loads((folder / "migration/manifest.json").read_text())
    ui = json.loads((folder / "migration/ui-resources.json").read_text())
    entries = [dict(path=e["image_path"], url=e["download_url"], sha256=e["sha256"], bytes=e["bytes"]) for e in manifest["entries"]] + ui
    targets = set()
    for e in entries:
        path = Path(e["path"])
        target = folder / path
        if (path.is_absolute() or ".." in path.parts or not target.resolve().is_relative_to(folder)
                or any(p.is_symlink() for p in [target, *target.parents] if p.is_relative_to(folder))
                or not safe_url(e["url"])):
            raise ValueError("Unsafe migration media path or URL")
        if target in targets:
            raise ValueError("Duplicate migration media destination")
        targets.add(target)
    with tempfile.TemporaryDirectory(prefix="fieldlog-media-") as temporary:
        staging = Path(temporary)
        def prepare(item):
            index, entry = item
            destination = folder / entry["path"]
            if destination.is_file():
                data = destination.read_bytes()
            else:
                request = Request(entry["url"], headers={"User-Agent": "fivsevn-fieldlog-migration"})
                with urlopen(request, timeout=90) as response:
                    if not safe_url(response.url):
                        raise ValueError("Unexpected media redirect")
                    data = response.read(entry["bytes"] + 1)
            if len(data) != entry["bytes"] or hashlib.sha256(data).hexdigest() != entry["sha256"]:
                raise ValueError(f"Migration image checksum mismatch: {entry['path']}")
            if destination.exists():
                return None
            pending = staging / str(index)
            pending.write_bytes(data)
            return pending, destination
        with ThreadPoolExecutor(max_workers=6) as pool:
            prepared = list(pool.map(prepare, enumerate(entries)))
        installed = []
        try:
            for pair in prepared:
                if pair is None:
                    continue
                pending, destination = pair
                destination.parent.mkdir(parents=True, exist_ok=True)
                atomic_write(destination, pending.read_bytes())
                installed.append(destination)
            flag.parent.mkdir(parents=True, exist_ok=True)
            atomic_write(flag, (json.dumps({"version": 1, "files": len(entries), "source": "migration manifests; all bytes and SHA-256 verified"}, indent=2) + "\n").encode("utf-8"))
        except BaseException:
            for destination in installed:
                destination.unlink(missing_ok=True)
            raise
    print(f"Verified {len(entries)} migration media files; installed {len(installed)}.")
    return len(installed)


if __name__ == "__main__":
    restore()
