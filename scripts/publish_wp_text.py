from __future__ import annotations

import calendar
import os
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import markdown
import requests
import yaml


ROOT = Path(__file__).resolve().parents[1]

SOURCE_FILE = ROOT / os.getenv("WP_SOURCE_FILE", "posts/_wordpress/trigger.md")
WP_SITE_URL = os.environ["WP_SITE_URL"].rstrip("/")
WP_USERNAME = os.environ["WP_USERNAME"]
WP_APP_PASSWORD = os.environ["WP_APP_PASSWORD"]

WP_POST_TYPE = os.getenv("WP_POST_TYPE", "posts").strip("/")
WP_TIMEZONE = os.getenv("WP_TIMEZONE", "Asia/Taipei")

GITHUB_SHA = os.getenv("GITHUB_SHA", "local")[:7]


def split_frontmatter(text: str) -> tuple[dict, str]:
    """
    YAML frontmatter:
    ---
    key: value
    ---

    Only the body after the second --- is published.
    """
    text = text.replace("\r\n", "\n")

    if not text.startswith("---\n"):
        return {}, text

    end = text.find("\n---", 4)
    if end == -1:
        return {}, text

    raw_yaml = text[4:end].strip()
    body = text[end + 4 :].lstrip("\n")

    if not raw_yaml:
        return {}, body

    meta = yaml.safe_load(raw_yaml) or {}

    if not isinstance(meta, dict):
        raise ValueError("YAML frontmatter must be a key-value object.")

    return meta, body


def make_time_title() -> str:
    now = datetime.now(ZoneInfo(WP_TIMEZONE))
    month = calendar.month_abbr[now.month]
    return f"{now.day} {month}, {now.year} {now.hour:02d}:{now.minute:02d}"


def main() -> int:
    if not SOURCE_FILE.exists():
        raise FileNotFoundError(f"Source file not found: {SOURCE_FILE}")

    raw = SOURCE_FILE.read_text(encoding="utf-8").strip()

    if not raw:
        print("Source file is empty. Nothing to publish.")
        return 0

    meta, body = split_frontmatter(raw)

    body = body.strip()

    if not body:
        print("Body is empty. Nothing to publish.")
        return 0

    title = make_time_title()
    status = str(meta.get("wp_status") or "publish").strip()

    # One commit = one WordPress post.
    # If the same GitHub Action run is retried, the same slug prevents duplicates.
    slug = str(meta.get("slug") or f"github-text-{GITHUB_SHA}").strip()

    html = markdown.markdown(
        body,
        extensions=["extra", "sane_lists", "nl2br"],
    )

    endpoint = f"{WP_SITE_URL}/wp-json/wp/v2/{WP_POST_TYPE}"

    check = requests.get(
        endpoint,
        auth=(WP_USERNAME, WP_APP_PASSWORD),
        params={
            "slug": slug,
            "context": "edit",
            "status": "any",
        },
        timeout=30,
    )

    if check.ok:
        existing = check.json()
        if existing:
            print(f"Post already exists for slug={slug}. Skip.")
            print(existing[0].get("link", ""))
            return 0

    payload = {
        "title": title,
        "content": html,
        "status": status,
        "slug": slug,
    }

    response = requests.post(
        endpoint,
        auth=(WP_USERNAME, WP_APP_PASSWORD),
        json=payload,
        timeout=30,
    )

    if not response.ok:
        print("WordPress publish failed.")
        print(response.status_code)
        print(response.text)
        return 1

    data = response.json()

    print("Published:")
    print(data.get("link"))

    return 0


if __name__ == "__main__":
    sys.exit(main())
