#!/usr/bin/env python3
"""Stable publication-media names shared by fivsevn boards."""
from __future__ import annotations
import argparse
from datetime import datetime
import hashlib
from pathlib import Path
import re
from zoneinfo import ZoneInfo

SITES = ("flux", "savour", "fieldlog", "stills", "motion", "sys", "cctv")
EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".heic", ".heif", ".avif", ".tif", ".tiff", ".bmp"}
TZ = ZoneInfo("Asia/Shanghai")


def media_prefix(site: str, post_id: str, published_at: str | datetime) -> str:
    if site not in SITES or not isinstance(post_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", post_id):
        raise ValueError("A known board and stable package id are required")
    stamp = published_at if isinstance(published_at, datetime) else datetime.fromisoformat(published_at.replace("Z", "+00:00"))
    if stamp.utcoffset() is None:
        raise ValueError("Publication time requires an explicit timezone")
    token = hashlib.sha256((site + ":" + post_id).encode("utf-8")).hexdigest()[:12]
    return stamp.astimezone(TZ).strftime("%Y%m%d-%H%M%S") + "-" + site + "-" + token


def media_filename(site: str, post_id: str, published_at: str | datetime, number: int, extension: str) -> str:
    if type(number) is not int or number < 1:
        raise ValueError("Media numbers start at 1")
    suffix = extension.lower()
    if not suffix.startswith("."):
        suffix = "." + suffix
    if suffix not in EXTENSIONS:
        raise ValueError("Unsupported image extension")
    if suffix == ".jpeg":
        suffix = ".jpg"
    return f"{media_prefix(site, post_id, published_at)}-{number:03d}{suffix}"


def check(root: Path, site: str) -> int:
    from site_post_metadata import post_paths, read_frontmatter, published_datetime
    seen = set()
    count = 0
    for source in post_paths(root):
        meta, _ = read_frontmatter(source)
        prefix = media_prefix(site, meta["id"], published_datetime(meta))
        numbers = set()
        for path in sorted((source.parent / "assets").rglob("*")):
            if not path.is_file() or path.suffix.lower() not in EXTENSIONS:
                continue
            match = re.fullmatch(re.escape(prefix) + r"-([0-9]{3,})\.(jpg|png|webp|gif|heic|heif|avif|tif|tiff|bmp)", path.name)
            if not match or int(match[1]) < 1 or int(match[1]) in numbers:
                raise ValueError("Invalid or duplicate publication-media name: " + str(path))
            if path.name in seen or path.is_symlink():
                raise ValueError("Publication-media collision or symlink: " + str(path))
            numbers.add(int(match[1])); seen.add(path.name); count += 1
    return count


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["check"])
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--site", required=True, choices=SITES)
    args = parser.parse_args()
    print(f"PASS: {check(args.root.resolve(), args.site)} publication images")
