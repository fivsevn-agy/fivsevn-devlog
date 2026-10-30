#!/usr/bin/env python3
"""Check the combined Jekyll + Fieldlog artifact and its published entrypoints."""
from __future__ import annotations

import argparse
from hashlib import sha256
from pathlib import Path
import time
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
ENTRYPOINTS = ("index.html", "posts/index.html", "natsci/index.html", "netcom/index.html", "intake/index.html", "assets/css/style.css")


def check(root: Path = ROOT, url: str | None = None) -> int:
    site = Path(root) / "_site"
    for relative in ENTRYPOINTS:
        path = site / relative
        if not path.is_file() or not path.stat().st_size:
            raise ValueError(f"Missing combined website entrypoint: {relative}")
        if relative in {"posts/index.html", "natsci/index.html", "netcom/index.html"}:
            if 'class="container-lg px-3 my-5 markdown-body"' not in path.read_text():
                raise ValueError(f"The existing Jekyll theme was not rendered: {relative}")
        if url:
            expected = path.read_bytes()
            fingerprint = sha256(expected).hexdigest()[:12]
            target = url.rstrip("/") + "/" + relative + "?v=" + fingerprint
            for attempt in range(6):
                try:
                    with urlopen(Request(target, headers={"User-Agent": "fivsevn-devlog-publishing"}), timeout=45) as response:
                        actual = response.read()
                    if actual == expected:
                        break
                except OSError:
                    if attempt == 5:
                        raise
                if attempt == 5:
                    raise ValueError(f"Published note entrypoint differs from the artifact: {relative}")
                time.sleep(5)
    if not (site / "natsci/fieldlog/build-receipt.json").is_file():
        raise ValueError("Fieldlog was not overlaid into the combined website")
    if any((site / "natsci/fieldlog").rglob("index.md")):
        raise ValueError("Post source Markdown leaked into the public Fieldlog artifact")
    print(f"Verified {len(ENTRYPOINTS)} existing note entrypoints and the Fieldlog overlay.")
    return len(ENTRYPOINTS)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--url")
    args = parser.parse_args()
    check(args.root.resolve(), args.url)
