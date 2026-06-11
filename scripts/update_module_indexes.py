from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

MODULES = {
    "posts": {
        "root": "posts",
        "index": "posts/index.md",
        "heading": "## Recent Posts",
        "marker": "POSTS_RECENT",
        "exclude_dirs": {"assets", "_drafts", "ai-discourse-analysis"},
    },
    "natsci": {
        "root": "natsci",
        "index": "natsci/index.md",
        "heading": "## Recent Notes 更新记录",
        "marker": "NATSCI_RECENT",
        "exclude_dirs": {"assets", "_drafts"},
    },
    "netcom": {
        "root": "netcom",
        "index": "netcom/index.md",
        "heading": "## Recent Notes 更新记录",
        "marker": "NETCOM_RECENT",
        "exclude_dirs": {"assets", "_drafts"},
    },
}

COMMON_EXCLUDE_DIRS = {
    ".git",
    ".github",
    ".obsidian",
    "assets",
    "_drafts",
    "node_modules",
    "__pycache__",
}

EXCLUDE_NAMES = {
    "index.md",
    "map.md",
    "README.md",
    ".DS_Store",
    ".cache",
    ".gitkeep",
}

LINK_STATUSES = {"active", "publish", "published"}
TEXT_STATUSES = {"draft"}
HIDE_STATUSES = {"hidden", "private", "archived", "archive"}

DATE_RE = re.compile(r"(\d{4})[-.](\d{1,2})[-.](\d{1,2})")


@dataclass(frozen=True)
class Note:
    title: str
    date: str
    status: str
    link: str | None
    source_path: str


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1].strip()
    return value


def parse_frontmatter(text: str) -> dict[str, str] | None:
    """Parse simple YAML front matter using only the standard library.

    It intentionally extracts only scalar `key: value` fields. That is enough for
    title/module/status/created/date/updated/original_url.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None

    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break

    if end is None:
        return None

    fm: dict[str, str] = {}
    for raw_line in lines[1:end]:
        if not raw_line.strip() or raw_line.startswith((" ", "\t", "-")):
            continue
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        key = key.strip()
        value = strip_quotes(value)
        if key:
            fm[key] = value
    return fm


def normalize_date(value: str | None) -> str | None:
    if not value:
        return None
    match = DATE_RE.search(str(value))
    if not match:
        return None
    year, month, day = match.groups()
    return f"{int(year):04d}-{int(month):02d}-{int(day):02d}"


def get_note_date(fm: dict[str, str]) -> str | None:
    for key in ("created", "date", "updated"):
        date = normalize_date(fm.get(key))
        if date:
            return date
    return None


def status_mode(status: str | None) -> str:
    normalized = (status or "").strip().lower()
    if normalized in LINK_STATUSES:
        return "link"
    if normalized in TEXT_STATUSES:
        return "text"
    if normalized in HIDE_STATUSES:
        return "hide"
    # 没写 status 时不进目录，避免半成品被误公开。
    return "hide"


def should_skip_path(path: Path, root_dir: Path, extra_exclude_dirs: set[str]) -> bool:
    if path.suffix.lower() != ".md":
        return True
    if path.name in EXCLUDE_NAMES:
        return True
    if path.name.startswith("."):
        return True

    rel_parts = path.relative_to(root_dir).parts
    excluded = COMMON_EXCLUDE_DIRS | extra_exclude_dirs
    return any(part in excluded or part.startswith(".") for part in rel_parts)


def collect_notes(module_name: str, config: dict) -> tuple[list[Note], list[str]]:
    root_dir = ROOT / config["root"]
    warnings: list[str] = []
    notes: list[Note] = []

    if not root_dir.exists():
        warnings.append(f"[{module_name}] root not found: {root_dir}")
        return notes, warnings

    for path in sorted(root_dir.rglob("*.md")):
        if should_skip_path(path, root_dir, config["exclude_dirs"]):
            continue

        rel_to_root = path.relative_to(root_dir).as_posix()
        text = path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm is None:
            warnings.append(f"[{module_name}] skipped, no front matter: {rel_to_root}")
            continue

        fm_module = (fm.get("module") or "").strip()
        if fm_module and fm_module != module_name:
            warnings.append(
                f"[{module_name}] skipped, module mismatch: {rel_to_root} "
                f"(module: {fm_module})"
            )
            continue

        title = (fm.get("title") or "").strip()
        if not title:
            warnings.append(f"[{module_name}] skipped, missing title: {rel_to_root}")
            continue

        note_date = get_note_date(fm)
        if not note_date:
            warnings.append(f"[{module_name}] skipped, missing created/date/updated: {rel_to_root}")
            continue

        status = (fm.get("status") or "").strip().lower()
        mode = status_mode(status)
        if mode == "hide":
            continue

        if mode == "link":
            link = (fm.get("original_url") or "").strip() or rel_to_root
        else:
            link = None

        notes.append(
            Note(
                title=title,
                date=note_date,
                status=status,
                link=link,
                source_path=rel_to_root,
            )
        )

    notes.sort(key=lambda note: (note.date, note.title, note.source_path), reverse=True)
    return notes, warnings


def render_notes(notes: list[Note]) -> str:
    if not notes:
        return "<!-- no notes found -->"

    lines: list[str] = []
    for note in notes:
        display_date = note.date.replace("-", ".")
        if note.link:
            lines.append(f"- {display_date} [{note.title}]({note.link})")
        else:
            lines.append(f"- {display_date} {note.title}（更新中）")
    return "\n".join(lines)


def replace_between_markers(text: str, marker: str, body: str) -> tuple[str, bool]:
    start = f"<!-- AUTO-INDEX:{marker}:START -->"
    end = f"<!-- AUTO-INDEX:{marker}:END -->"
    pattern = re.compile(re.escape(start) + r"\n.*?\n" + re.escape(end), re.S)
    replacement = f"{start}\n{body}\n{end}"

    if pattern.search(text):
        return pattern.sub(replacement, text), True
    return text, False


def replace_after_heading(text: str, heading: str, marker: str, body: str) -> str:
    start = f"<!-- AUTO-INDEX:{marker}:START -->"
    end = f"<!-- AUTO-INDEX:{marker}:END -->"
    block = f"{start}\n{body}\n{end}\n"

    lines = text.splitlines(keepends=True)
    heading_index = None
    for i, line in enumerate(lines):
        if line.strip() == heading:
            heading_index = i
            break

    if heading_index is None:
        raise RuntimeError(f"heading not found: {heading}")

    # 保留标题下方的说明行，例如 `> 更新中......`。
    content_start = heading_index + 1
    while content_start < len(lines):
        stripped = lines[content_start].strip()
        if stripped == "" or stripped.startswith(">"):
            content_start += 1
            continue
        break

    content_end = content_start
    while content_end < len(lines):
        stripped = lines[content_end].strip()
        if stripped == "---":
            break
        if stripped.startswith("## ") and content_end != content_start:
            break
        content_end += 1

    replacement_lines = [line if line.endswith("\n") else f"{line}\n" for line in block.splitlines()]
    new_lines = lines[:content_start] + replacement_lines + lines[content_end:]
    return "".join(new_lines)


def update_index(config: dict, rendered: str) -> bool:
    index_path = ROOT / config["index"]
    if not index_path.exists():
        raise RuntimeError(f"index not found: {index_path}")

    old_text = index_path.read_text(encoding="utf-8")
    new_text, found = replace_between_markers(old_text, config["marker"], rendered)
    if not found:
        new_text = replace_after_heading(old_text, config["heading"], config["marker"], rendered)

    if new_text != old_text:
        index_path.write_text(new_text, encoding="utf-8")
        return True
    return False


def main() -> int:
    changed_any = False
    all_warnings: list[str] = []

    for module_name, config in MODULES.items():
        notes, warnings = collect_notes(module_name, config)
        all_warnings.extend(warnings)
        rendered = render_notes(notes)
        changed = update_index(config, rendered)
        changed_any = changed_any or changed
        print(f"{module_name}: {len(notes)} item(s), changed={changed}")

    if all_warnings:
        print("\nWarnings:")
        for warning in all_warnings:
            print(f"- {warning}")

    if changed_any:
        print("\nIndex files updated.")
    else:
        print("\nIndex files already up to date.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
