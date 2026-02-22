#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, List, Tuple


YEAR_DIR_RE = re.compile(r"^\d{4}$")  # posts/2025, posts/2026 ...


@dataclass(frozen=True)
class FileItem:
    path: Path
    kind: str  # e.g. README / INDEX / CONTENT / POSTS_YEAR


def read_text(p: Path) -> str:
    # 统一用 UTF-8；遇到奇怪编码直接报错更安全（别悄悄吞）
    return p.read_text(encoding="utf-8")


def is_year_dir(p: Path) -> bool:
    return p.is_dir() and YEAR_DIR_RE.match(p.name) is not None


def collect_files(repo_root: Path) -> List[FileItem]:
    """
    收集你指定的文件集合，并返回一个稳定有序的列表。
    顺序策略：
      1) README
      2) 三个 index（natsci/netcom/posts）
      3) natsci/content 全部 md（按路径排序）
      4) netcom/content 全部 md（按路径排序）
      5) posts/年份 里的全部 md（按 年份->路径 排序）
    """
    repo_root = repo_root.resolve()

    items: List[FileItem] = []

    # 1) README
    readme = repo_root / "README.md"
    if readme.exists():
        items.append(FileItem(readme, "README"))
    else:
        print(f"[WARN] README not found: {readme}")

    # 2) index.md
    for section in ("natsci", "netcom", "posts"):
        idx = repo_root / section / "index.md"
        if idx.exists():
            items.append(FileItem(idx, "INDEX"))
        else:
            print(f"[WARN] index.md not found: {idx}")

    # 3) natsci/content/**/*.md
    natsci_content = repo_root / "natsci" / "content"
    if natsci_content.exists():
        md_files = sorted([p for p in natsci_content.rglob("*.md") if p.is_file()])
        items.extend(FileItem(p, "CONTENT") for p in md_files)
    else:
        print(f"[WARN] natsci/content not found: {natsci_content}")

    # 4) netcom/content/**/*.md
    netcom_content = repo_root / "netcom" / "content"
    if netcom_content.exists():
        md_files = sorted([p for p in netcom_content.rglob("*.md") if p.is_file()])
        items.extend(FileItem(p, "CONTENT") for p in md_files)
    else:
        print(f"[WARN] netcom/content not found: {netcom_content}")

    # 5) posts/{YYYY}/**/*.md
    posts_dir = repo_root / "posts"
    if posts_dir.exists():
        year_dirs = sorted([p for p in posts_dir.iterdir() if is_year_dir(p)], key=lambda p: p.name)
        for yd in year_dirs:
            md_files = sorted([p for p in yd.rglob("*.md") if p.is_file()])
            items.extend(FileItem(p, "POSTS_YEAR") for p in md_files)
    else:
        print(f"[WARN] posts dir not found: {posts_dir}")

    # 去重（理论上不会重复，但保险起见）
    seen = set()
    unique_items = []
    for it in items:
        rp = it.path.resolve()
        if rp in seen:
            continue
        seen.add(rp)
        unique_items.append(it)

    return unique_items


def render_bundle(repo_root: Path, files: List[FileItem]) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rel_paths = [str(f.path.resolve().relative_to(repo_root.resolve())) for f in files]

    lines: List[str] = []
    lines.append("# fivsevn-devlog — merged bundle")
    lines.append("")
    lines.append(f"- Generated: {now}")
    lines.append(f"- Root: `{repo_root.resolve()}`")
    lines.append(f"- Files: {len(files)}")
    lines.append("")
    lines.append("## File index")
    lines.append("")
    for rp in rel_paths:
        lines.append(f"- `{rp}`")
    lines.append("")
    lines.append("---")
    lines.append("")

    for it in files:
        rel = it.path.resolve().relative_to(repo_root.resolve())
        header = f"## FILE: `{rel}`"
        lines.append(header)
        lines.append("")
        try:
            content = read_text(it.path).rstrip()
        except Exception as e:
            # 直接把错误写进总文档，方便你一眼定位问题
            lines.append(f"> [ERROR] Failed to read: `{rel}`")
            lines.append(f"> {type(e).__name__}: {e}")
            lines.append("")
            lines.append("---")
            lines.append("")
            continue

        if not content:
            lines.append("> [EMPTY]")
            lines.append("")
        else:
            lines.append(content)
            lines.append("")

        lines.append("---")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    import argparse

    ap = argparse.ArgumentParser(
        description="Merge selected markdown files from fivsevn-devlog into one bundle md."
    )
    ap.add_argument(
        "repo_root",
        nargs="?",
        default=".",
        help="Path to fivsevn-devlog repo root (default: current directory).",
    )
    ap.add_argument(
        "-o",
        "--out",
        default="",
        help="Output filename. Default: fivsevn-devlog_merged_YYYYMMDD_HHMMSS.md in repo root.",
    )
    args = ap.parse_args()

    repo_root = Path(args.repo_root).resolve()
    if not repo_root.exists():
        raise SystemExit(f"[FATAL] repo_root not found: {repo_root}")

    files = collect_files(repo_root)
    if not files:
        raise SystemExit("[FATAL] No files collected. Check folder structure / paths.")

    bundle = render_bundle(repo_root, files)

    if args.out.strip():
        out_path = Path(args.out).expanduser().resolve()
        if out_path.is_dir():
            raise SystemExit(f"[FATAL] output path is a directory: {out_path}")
    else:
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_path = repo_root / f"fivsevn-devlog_merged_{stamp}.md"

    out_path.write_text(bundle, encoding="utf-8")
    print(f"[OK] Wrote: {out_path}  ({len(files)} files)")


if __name__ == "__main__":
    main()