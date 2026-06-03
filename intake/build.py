#!/usr/bin/env python3
from __future__ import annotations

import html
import re
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any

import feedparser
import yaml


BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "feeds.yml"
OUTPUT_PATH = BASE_DIR / "index.html"
DATA_DIR = BASE_DIR / "data"
REPO_URL = "https://github.com/fivsevn-agy/fivsevn-devlog/tree/233c5bab2dba086446db83ee8e7b232b46c53a1a/intake"


def load_config() -> dict[str, Any]:
    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def escape(value: Any) -> str:
    if value is None:
        return ""
    return html.escape(str(value), quote=True).strip()


def strip_html(value: str) -> str:
    if not value:
        return ""
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def parse_entry_date(entry: Any) -> datetime:
    for key in ("published", "updated", "created"):
        value = entry.get(key)
        if not value:
            continue
        try:
            parsed = parsedate_to_datetime(value)
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=timezone.utc)
            return parsed
        except Exception:
            continue
    return datetime.now(timezone.utc)


def format_datetime(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def fetch_feed(feed_name: str, feed_url: str) -> list[dict[str, Any]]:
    parsed = feedparser.parse(feed_url)
    if getattr(parsed, "bozo", False):
        print(f"[warn] feed parse warning: {feed_name} — {feed_url}")

    items: list[dict[str, Any]] = []
    for entry in parsed.entries:
        link = entry.get("link", "").strip()
        title = entry.get("title", "Untitled").strip()
        if not link or not title:
            continue

        raw_summary = entry.get("summary", "") or entry.get("description", "")
        summary = strip_html(raw_summary)
        published_dt = parse_entry_date(entry)
        items.append(
            {
                "title": title,
                "link": link,
                "summary": summary,
                "source": feed_name,
                "published_dt": published_dt,
                "published": format_datetime(published_dt),
            }
        )
    return items


def build_section(section: dict[str, Any], max_items: int) -> list[dict[str, Any]]:
    all_items: list[dict[str, Any]] = []
    seen_links: set[str] = set()

    for feed in section.get("feeds", []):
        feed_name = feed.get("name", "Unknown Source")
        feed_url = feed.get("url")
        if not feed_url:
            continue

        print(f"[fetch] {feed_name}: {feed_url}")
        try:
            items = fetch_feed(feed_name, feed_url)
        except Exception as error:
            print(f"[error] failed to fetch {feed_name}: {error}")
            continue

        for item in items:
            normalized_link = item["link"].split("?")[0].rstrip("/")
            if normalized_link in seen_links:
                continue
            seen_links.add(normalized_link)
            all_items.append(item)

    all_items.sort(key=lambda item: item["published_dt"], reverse=True)
    return all_items[:max_items]


def render_article(item: dict[str, Any]) -> str:
    title = escape(item["title"])
    link = escape(item["link"])
    source = escape(item["source"])
    published = escape(item["published"])
    summary = escape(item.get("summary", ""))
    summary_html = f"\n\n{summary}" if summary else ""

    return f"""
### [{title}]({link})

{source} · {published}{summary_html}
""".strip()


def load_fragment(filename: str) -> str:
    fragment_path = DATA_DIR / filename
    if not fragment_path.exists():
        return ""
    return fragment_path.read_text(encoding="utf-8").strip()


def render_html(config: dict[str, Any], sections_data: dict[str, list[dict[str, Any]]]) -> str:
    site = config.get("site", {})
    title = escape(site.get("title", "Today’s Arrival"))
    title_zh = escape(site.get("title_zh", "本日入荷"))
    opened_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    daily_postcard_html = load_fragment("daily_postcard.html")
    daily_field_sample_html = load_fragment("daily_field_sample.html")

    nav_parts: list[str] = []
    if daily_postcard_html:
        nav_parts.append("[postcard / 明信片](#postcard--明信片)")
    if daily_field_sample_html:
        nav_parts.append("[Daily Field Sample / 今日野采样本](#daily-field-sample--今日野采样本)")

    section_parts: list[str] = []
    for section_key, section in config.get("sections", {}).items():
        section_title = escape(section.get("title", section_key))
        section_title_zh = escape(section.get("title_zh", ""))
        section_description = escape(section.get("description", ""))
        section_description_zh = escape(section.get("description_zh", ""))
        items = sections_data.get(section_key, [])

        nav_label = section_title
        if section_title_zh:
            nav_label = f"{section_title} / {section_title_zh}"
        nav_parts.append(f"[{nav_label}](#{section_key})")

        article_parts = [render_article(item) for item in items]
        if not article_parts:
            article_parts = ["No items fetched."]

        title_zh_html = f"\n\n{section_title_zh}" if section_title_zh else ""
        description_html = f"\n\n{section_description}" if section_description else ""
        description_zh_html = f"\n\n{section_description_zh}" if section_description_zh else ""

        section_parts.append(
            f"""
## {section_title}
{title_zh_html}{description_html}{description_zh_html}

{chr(10).join(article_parts)}
""".strip()
        )

    nav_html = " · ".join(nav_parts)
    modules_html = "\n\n".join(
        part for part in [daily_postcard_html, daily_field_sample_html] if part
    )
    sections_html = "\n\n".join(section_parts)

    return f"""
# {title}

{title_zh}

Courier on duty / 投递员：

GitHub Actions

Shift opened / 到店时间：

{opened_at}

On the shelf / 本日上架：

{nav_html}

{modules_html}

{sections_html}

GitHub Actions 每日生成，数据来自 RSS 与采样脚本。[查看仓库]({REPO_URL})
""".strip() + "\n"


def main() -> None:
    config = load_config()
    max_items = int(config.get("site", {}).get("max_items_per_section", 20))

    sections_data: dict[str, list[dict[str, Any]]] = {}
    for section_key, section in config.get("sections", {}).items():
        print(f"[section] {section_key}")
        sections_data[section_key] = build_section(section, max_items)

    OUTPUT_PATH.write_text(render_html(config, sections_data), encoding="utf-8")
    print(f"[done] generated {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
