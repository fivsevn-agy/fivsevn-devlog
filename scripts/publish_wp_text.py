from __future__ import annotations

import calendar
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import markdown
import requests
import yaml


ROOT = Path(__file__).resolve().parents[1]

SOURCE_FILE = ROOT / os.getenv("WP_SOURCE_FILE", "posts/_wordpress/trigger.md")

WP_SITE_URL = os.environ["WP_SITE_URL"].rstrip("/")
WP_USERNAME = os.environ["WP_USERNAME"]
WP_APP_PASSWORD = os.environ["WP_APP_PASSWORD"]

# WordPress article endpoint: /wp/v2/posts
WP_POST_TYPE = os.getenv("WP_POST_TYPE", "posts").strip("/")

# Taipei time: UTC+8
WP_TIMEZONE = os.getenv("WP_TIMEZONE", "Asia/Taipei")

# Default WordPress category slug
WP_CATEGORY_SLUG = os.getenv("WP_CATEGORY_SLUG", "posts")

GITHUB_SHA = os.getenv("GITHUB_SHA", "local")[:7]


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """
    Only the body after the second --- is published.

    Example:

    ---
    wp_status: publish
    category: posts
    ---

    This part is published.
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


def normalize_category_slugs(meta: dict[str, Any]) -> list[str]:
    """
    Supported YAML keys:

    category: posts

    or:

    categories:
      - posts
      - something-else

    Also supports the common typo:
    catagory: posts
    """
    value = (
        meta.get("categories")
        or meta.get("category")
        or meta.get("catagory")
        or WP_CATEGORY_SLUG
    )

    if isinstance(value, str):
        return [value.strip()]

    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]

    return [WP_CATEGORY_SLUG]


def get_category_id_by_slug(slug: str) -> int:
    endpoint = f"{WP_SITE_URL}/wp-json/wp/v2/categories"

    response = requests.get(
        endpoint,
        auth=(WP_USERNAME, WP_APP_PASSWORD),
        params={
            "slug": slug,
            "per_page": 100,
        },
        timeout=30,
    )

    if not response.ok:
        print(f"Failed to look up WordPress category: {slug}")
        print(response.status_code)
        print(response.text)
        raise RuntimeError("WordPress category lookup failed.")

    data = response.json()

    if not data:
        raise RuntimeError(
            f"WordPress category not found: {slug}\n"
            f"Create it in WordPress first: Posts / Categories / Name: {slug}, Slug: {slug}"
        )

    return int(data[0]["id"])


def get_category_ids(slugs: list[str]) -> list[int]:
    ids: list[int] = []

    for slug in slugs:
        category_id = get_category_id_by_slug(slug)

        if category_id not in ids:
            ids.append(category_id)

    return ids


def find_existing_post_by_slug(endpoint: str, slug: str) -> dict[str, Any] | None:
    """
    Prevent duplicate posts when the same GitHub Action run is retried.

    Search several statuses separately instead of relying on status=any.
    """
    statuses = ["publish", "future", "draft", "pending", "private"]

    for status in statuses:
        response = requests.get(
            endpoint,
            auth=(WP_USERNAME, WP_APP_PASSWORD),
            params={
                "slug": slug,
                "status": status,
                "context": "edit",
                "per_page": 100,
            },
            timeout=30,
        )

        if not response.ok:
            print(f"Failed checking existing post for status={status}")
            print(response.status_code)
            print(response.text)
            raise RuntimeError("Existing post check failed.")

        data = response.json()

        if data:
            return data[0]

    return None


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

    category_slugs = normalize_category_slugs(meta)
    category_ids = get_category_ids(category_slugs)

    html = markdown.markdown(
        body,
        extensions=["extra", "sane_lists", "nl2br"],
    )

    endpoint = f"{WP_SITE_URL}/wp-json/wp/v2/{WP_POST_TYPE}"

    existing = find_existing_post_by_slug(endpoint, slug)

    if existing:
        print(f"Post already exists for slug={slug}. Skip.")
        print(existing.get("link", ""))
        return 0

    payload: dict[str, Any] = {
        "title": title,
        "content": html,
        "status": status,
        "slug": slug,
    }

    # Categories only apply to WordPress posts.
    if WP_POST_TYPE == "posts":
        payload["categories"] = category_ids

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