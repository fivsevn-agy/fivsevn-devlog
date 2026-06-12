from __future__ import annotations

import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MODULES = {
    "posts": {
        "draft_id_pattern": "posts-{yyyymmdd}-draft-{seq:03d}",
    },
    "natsci": {
        "draft_id_pattern": "natsci-draft-{seq:03d}",
    },
    "netcom": {
        "draft_id_pattern": "netcom-draft-{seq:03d}",
    },
}


def has_frontmatter(text: str) -> bool:
    return text.startswith("---\n") or text.startswith("---\r\n")


def extract_title(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            if title:
                return title
    return "TODO"


def next_draft_id(module: str, draft_dir: Path, today: str) -> str:
    yyyymmdd = today.replace("-", "")
    pattern = MODULES[module]["draft_id_pattern"]

    existing_stems = {p.stem for p in draft_dir.glob("*.md")}
    seq = 1

    while True:
        candidate = pattern.format(yyyymmdd=yyyymmdd, seq=seq)
        if candidate not in existing_stems:
            return candidate
        seq += 1


def make_frontmatter(module: str, doc_id: str, title: str, today: str) -> str:
    return f"""---
id: {doc_id}
title: {title}

module: {module}
submodule: drafts
topic: draft

type: note
status: hidden
canonical: true

summary: TODO

parents: []
related: []

tags: [{module}]
audience: [self]
languages: [zh]

maturity: draft
confidence: 0.0

visibility: private
source_of_truth: devlog

created: {today}
updated: {today}
---

"""


def should_skip(path: Path, text: str) -> bool:
    if path.name.startswith("TEMPLATE-"):
        return True

    if has_frontmatter(text):
        return True

    return False


def process_file(module: str, path: Path) -> bool:
    text = path.read_text(encoding="utf-8")

    if should_skip(path, text):
        print(f"SKIP: {path}")
        return False

    today = date.today().isoformat()
    draft_dir = path.parent
    doc_id = next_draft_id(module, draft_dir, today)
    new_path = draft_dir / f"{doc_id}.md"

    if new_path.exists():
        raise FileExistsError(f"Target already exists: {new_path}")

    title = extract_title(text)
    frontmatter = make_frontmatter(module, doc_id, title, today)
    new_text = frontmatter + text

    new_path.write_text(new_text, encoding="utf-8")

    if new_path != path:
        path.unlink()

    print(f"UPDATED: {path} -> {new_path}")
    return True


def main() -> int:
    changed = False

    for module in MODULES:
        draft_dir = ROOT / module / "_drafts"

        if not draft_dir.exists():
            continue

        for path in sorted(draft_dir.glob("*.md")):
            if process_file(module, path):
                changed = True

    if not changed:
        print("No draft files needed frontmatter.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
