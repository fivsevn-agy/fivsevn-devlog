"""Publish the trigger snapshot; maintenance changes never create a post."""
from __future__ import annotations

import argparse
import calendar
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import requests
import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCE_FILE = ROOT / os.getenv("WP_SOURCE_FILE", "posts/_wordpress/trigger.md")
WP_SITE_URL = os.getenv("WP_SITE_URL", "").rstrip("/")
WP_USERNAME = os.getenv("WP_USERNAME", "")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD", "")
WP_POST_TYPE = os.getenv("WP_POST_TYPE", "posts").strip("/")
WP_TIMEZONE = os.getenv("WP_TIMEZONE", "Asia/Taipei")
WP_CATEGORY_SLUG = os.getenv("WP_CATEGORY_SLUG", "posts")
POST_STATUSES = ("publish", "future", "draft", "pending", "private")
SHA_RE = re.compile(r"[0-9a-f]{40}")


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    ).stdout.strip()


def source_commit() -> str:
    """Use the last trigger change, not an unrelated newer repository commit."""
    if git("rev-parse", "--is-shallow-repository") == "true":
        raise ValueError("Full Git history is required; checkout must use fetch-depth: 0.")
    path = SOURCE_FILE.resolve().relative_to(ROOT.resolve()).as_posix()
    sha = git("log", "-1", "--first-parent", "--format=%H", "HEAD", "--", path)
    if not SHA_RE.fullmatch(sha):
        raise ValueError("Cannot identify the trigger's source commit; refusing to publish.")
    return sha


def publishing_allowed() -> bool:
    """Fail closed on unknown events or a push without a trigger change."""
    if os.getenv("GITHUB_ACTIONS") != "true":
        return True  # Explicit local invocation; --dry-run is available.
    if os.getenv("GITHUB_REF") != "refs/heads/main":
        return False
    event_name = os.getenv("GITHUB_EVENT_NAME", "")
    if event_name not in {"push", "workflow_dispatch"}:
        return False
    head = git("rev-parse", "HEAD")
    if head != os.getenv("GITHUB_SHA"):
        raise ValueError("Checkout does not match the event commit; refusing to publish.")
    if event_name == "workflow_dispatch":
        return True
    event = json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text(encoding="utf-8"))
    before = str(event.get("before", ""))
    if not SHA_RE.fullmatch(before) or before == "0" * 40:
        raise ValueError("No valid push base; use a manual run after reviewing the trigger.")
    if event.get("after") != head:
        raise ValueError("Push payload does not match checkout; refusing to publish.")
    path = SOURCE_FILE.resolve().relative_to(ROOT.resolve()).as_posix()
    return bool(git("diff", "--name-only", before, head, "--", path))


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    text = text.replace("\r\n", "\n").lstrip("\ufeff")
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return {}, text
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        raise ValueError("Frontmatter is missing its closing ---; nothing was published.")
    raw_yaml = "".join(lines[1:end])
    meta = yaml.safe_load(raw_yaml)
    if meta is None:
        meta = {}
    if not isinstance(meta, dict):
        raise ValueError("YAML frontmatter must be a key-value object.")
    return meta, "".join(lines[end + 1:]).lstrip("\n")


def make_time_title() -> str:
    now = datetime.now(ZoneInfo(WP_TIMEZONE))
    month = calendar.month_abbr[now.month]
    return f"{now.day} {month}, {now.year} {now.hour:02d}:{now.minute:02d}"


def normalize_category_slugs(meta: dict[str, Any]) -> list[str]:
    # Keep the existing category / categories / catagory inputs compatible.
    value = meta.get("categories") or meta.get("category") or meta.get("catagory") or WP_CATEGORY_SLUG
    if isinstance(value, str):
        values = [value.strip()]
    elif isinstance(value, list):
        values = [str(item).strip() for item in value if str(item).strip()]
    else:
        values = [WP_CATEGORY_SLUG]
    if not values or any(not item for item in values):
        raise ValueError("At least one non-empty WordPress category is required.")
    return list(dict.fromkeys(values))


def wp_get(endpoint: str, params: dict[str, Any]) -> list[dict[str, Any]]:
    response = requests.get(endpoint, auth=(WP_USERNAME, WP_APP_PASSWORD), params=params, timeout=30)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, list) or any(not isinstance(item, dict) for item in data):
        raise ValueError("Unexpected WordPress response; refusing to create a post.")
    return data


def get_category_id_by_slug(slug: str) -> int:
    data = wp_get(f"{WP_SITE_URL}/wp-json/wp/v2/categories", {"slug": slug, "per_page": 100})
    if not data:
        raise ValueError(f"WordPress category not found: {slug}. Create it in WordPress first.")
    return int(data[0]["id"])


def get_category_ids(slugs: list[str]) -> list[int]:
    return list(dict.fromkeys(get_category_id_by_slug(slug) for slug in slugs))


def find_existing_post_by_slug(endpoint: str, slug: str) -> dict[str, Any] | None:
    # Preserve the existing status checks, including WordPress-side drafts/private posts.
    for status in POST_STATUSES:
        data = wp_get(endpoint, {"slug": slug, "status": status, "context": "edit", "per_page": 100})
        if data:
            return data[0]
    return None


def render_body(body: str) -> str:
    import markdown
    # Keep the previous rendering and line-break behavior unchanged.
    return markdown.markdown(body, extensions=["extra", "sane_lists", "nl2br"])


def report(message: str) -> None:
    print(message)
    summary = os.getenv("GITHUB_STEP_SUMMARY")
    if summary:
        with Path(summary).open("a", encoding="utf-8") as handle:
            handle.write(message + "\n\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="Validate/render locally; never contact WordPress.")
    mode.add_argument("--check-event", action="store_true", help="Output whether this event may publish; no credentials needed.")
    args = parser.parse_args(argv)

    if args.check_event:
        allowed = publishing_allowed()
        if allowed:
            source_commit()  # Verify history before enabling the credential-bearing step.
        output = os.getenv("GITHUB_OUTPUT")
        if output:
            with Path(output).open("a", encoding="utf-8") as handle:
                handle.write(f"publish={'true' if allowed else 'false'}\n")
        report("Publishing event accepted." if allowed else "Maintenance or review only: publishing skipped.")
        return 0

    if not args.dry_run and not publishing_allowed():
        report("Maintenance or review only: publishing skipped.")
        return 0

    raw = SOURCE_FILE.read_text(encoding="utf-8-sig").strip()
    meta, body = split_frontmatter(raw)
    body = body.strip()
    if not body:
        report("Body is empty. Nothing to publish.")
        return 0

    status = str(meta.get("wp_status") or "publish").strip()
    if status not in POST_STATUSES:
        raise ValueError(f"Unsupported wp_status: {status}")
    title = make_time_title()
    # Existing explicit slugs are respected; automatic slugs keep their original format.
    slug = str(meta.get("slug") or f"github-text-{source_commit()[:7]}").strip()
    if not slug:
        raise ValueError("WordPress slug cannot be empty.")
    category_slugs = normalize_category_slugs(meta)
    html = render_body(body)

    if args.dry_run:
        report(f"Preview only: slug={slug}, status={status}, categories={category_slugs}, HTML length={len(html)}. No WordPress requests.")
        return 0

    if not all((WP_SITE_URL, WP_USERNAME, WP_APP_PASSWORD)):
        raise ValueError("Set WP_SITE_URL, WP_USERNAME and WP_APP_PASSWORD in Actions Secrets.")
    endpoint = f"{WP_SITE_URL}/wp-json/wp/v2/{WP_POST_TYPE}"
    existing = find_existing_post_by_slug(endpoint, slug)
    if existing:
        report(f"Already exists: {slug}. Skipped without modifying WordPress. {existing.get('link', '')}")
        return 0

    payload: dict[str, Any] = {"title": title, "content": html, "status": status, "slug": slug}
    if WP_POST_TYPE == "posts":
        payload["categories"] = get_category_ids(category_slugs)

    # Never retry a POST blindly: a timeout may occur after WordPress saved the post.
    response = requests.post(endpoint, auth=(WP_USERNAME, WP_APP_PASSWORD), json=payload, timeout=30)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict) or not data.get("id"):
        raise ValueError("Unclear publish response. Check WordPress before retrying the same source.")
    report(f"Published: {data.get('link', '')} (slug={slug})")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, OSError, KeyError, yaml.YAMLError, subprocess.CalledProcessError, requests.RequestException) as exc:
        # Do not dump request bodies, credentials or the entire WordPress error page.
        print(f"Stopped: {type(exc).__name__}. Check configuration and WordPress before retrying; no automatic POST retry.", file=sys.stderr)
        if isinstance(exc, ValueError) and not isinstance(exc, requests.RequestException):
            print(str(exc), file=sys.stderr)
        sys.exit(1)
