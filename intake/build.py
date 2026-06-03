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

    summary_html = ""
    if summary:
        summary_html = f"<p class='summary'>{summary}</p>"

    return f"""
<article class="article">
  <h3><a href="{link}" target="_blank" rel="noopener noreferrer">{title}</a></h3>
  <div class="meta">{source} · {published}</div>
  {summary_html}
</article>
""".strip()



DAILY_FIELD_SAMPLE_PATH = BASE_DIR / "data" / "daily_arthropod.html"


def load_daily_field_sample_html() -> str:
    if not DAILY_FIELD_SAMPLE_PATH.exists():
        return ""
    return DAILY_FIELD_SAMPLE_PATH.read_text(encoding="utf-8").strip()


def render_html(config: dict[str, Any], sections_data: dict[str, list[dict[str, Any]]]) -> str:
    site = config.get("site", {})
    title = escape(site.get("title", "fivsevn / intake"))
    title_zh = escape(site.get("title_zh", "fivsevn / 日常摄入"))
    subtitle = escape(site.get("subtitle", "A daily intake surface."))
    subtitle_zh = escape(site.get("subtitle_zh", "日常信息摄入入口。"))
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    daily_field_sample_html = load_daily_field_sample_html()

    nav_parts = []
    if daily_field_sample_html:
        nav_parts.append('<a href="#daily-field-sample">Daily Field Sample / 今日野外样本</a>')
    section_parts = []

    for section_key, section in config.get("sections", {}).items():
        section_title = escape(section.get("title", section_key))
        section_title_zh = escape(section.get("title_zh", ""))
        section_description = escape(section.get("description", ""))
        section_description_zh = escape(section.get("description_zh", ""))
        items = sections_data.get(section_key, [])

        nav_label = section_title
        if section_title_zh:
            nav_label = f"{section_title} / {section_title_zh}"

        nav_parts.append(f'<a href="#{escape(section_key)}">{nav_label}</a>')

        article_parts = []
        if items:
            for item in items:
                article_parts.append(render_article(item))
        else:
            article_parts.append("<p class='empty'>No items fetched.</p>")

        title_zh_html = ""
        if section_title_zh:
            title_zh_html = f"<p class='section-title-zh'>{section_title_zh}</p>"

        description_html = ""
        if section_description:
            description_html = f"<p class='section-description'>{section_description}</p>"

        description_zh_html = ""
        if section_description_zh:
            description_zh_html = f"<p class='section-description-zh'>{section_description_zh}</p>"

        section_parts.append(
            f"""
<section id="{escape(section_key)}">
  <h2>{section_title}</h2>
  {title_zh_html}
  {description_html}
  {description_zh_html}
  {''.join(article_parts)}
</section>
""".strip()
        )

    nav_html = "\n".join(nav_parts)
    sections_html = "\n".join(section_parts)

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>
    :root {{
      --bg: #0f1115;
      --panel: #171a21;
      --text: #e8e8e8;
      --muted: #9ca3af;
      --border: #2a2f3a;
      --link: #8ab4ff;
    }}

    * {{
      box-sizing: border-box;
    }}

    body {{
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", Arial, sans-serif;
      line-height: 1.6;
    }}

    main {{
      width: min(980px, calc(100% - 32px));
      margin: 0 auto;
      padding: 36px 0 80px;
    }}

    header {{
      padding-bottom: 24px;
      margin-bottom: 32px;
      border-bottom: 1px solid var(--border);
    }}

    h1 {{
      margin: 0 0 8px;
      font-size: clamp(2rem, 5vw, 3rem);
      letter-spacing: -0.04em;
      line-height: 1.1;
    }}

    .title-zh {{
      margin: 0 0 12px;
      color: var(--text);
      font-size: 1.15rem;
      font-weight: 500;
    }}

    .subtitle,
    .subtitle-zh {{
      margin: 0;
      color: var(--muted);
      max-width: 760px;
    }}

    .subtitle-zh {{
      margin-top: 4px;
    }}

    .generated {{
      margin-top: 10px;
      color: var(--muted);
      font-size: 0.9rem;
    }}

    nav {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 22px;
    }}

    nav a {{
      color: var(--link);
      text-decoration: none;
      border: 1px solid var(--border);
      border-radius: 999px;
      padding: 5px 12px;
      font-size: 0.9rem;
    }}

    section {{
      margin: 42px 0;
    }}

    h2 {{
      margin: 0 0 2px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--border);
      font-size: 1.4rem;
    }}

    .section-title-zh {{
      margin: -2px 0 6px;
      color: var(--text);
      font-size: 1rem;
      font-weight: 500;
    }}

    .section-description,
    .section-description-zh {{
      color: var(--muted);
      margin: 0;
    }}

    .section-description-zh {{
      margin-top: 4px;
      margin-bottom: 18px;
    }}

    .daily-field-sample,
    .daily-arthropod {{
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 18px;
      margin: 34px 0 42px;
    }}

    .daily-field-sample h2,
    .daily-arthropod h2 {{
      margin-bottom: 14px;
    }}

    .daily-field-sample p,
    .daily-arthropod p {{
      margin: 12px 0;
    }}

    .daily-field-sample a,
    .daily-arthropod a {{
      color: var(--link);
      text-decoration: none;
    }}

    .daily-field-sample a:hover,
    .daily-arthropod a:hover {{
      text-decoration: underline;
    }}

    .article {{
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 16px;
      margin: 14px 0;
    }}

    .article h3 {{
      margin: 0 0 8px;
      font-size: 1.05rem;
      line-height: 1.4;
    }}

    .article h3 a {{
      color: var(--text);
      text-decoration: none;
    }}

    .article h3 a:hover {{
      color: var(--link);
    }}

    .meta {{
      color: var(--muted);
      font-size: 0.86rem;
      margin-bottom: 8px;
    }}

    .summary {{
      color: #c9ced6;
      font-size: 0.95rem;
      margin: 0;
    }}

    .empty {{
      color: var(--muted);
    }}

    footer {{
      margin-top: 48px;
      padding-top: 20px;
      border-top: 1px solid var(--border);
      color: var(--muted);
      font-size: 0.9rem;
    }}

    code {{
      color: var(--text);
    }}
  </style>
</head>
<body>
  <main>
    <header>
      <h1>{title}</h1>
      <p class="title-zh">{title_zh}</p>
      <p class="subtitle">{subtitle}</p>
      <p class="subtitle-zh">{subtitle_zh}</p>
      <p class="generated">Generated at {generated_at}</p>
      <nav>
        {nav_html}
      </nav>
    </header>

    {daily_field_sample_html}

    {sections_html}

    <footer>
      Generated from <code>intake/feeds.yml</code>. This page is a daily intake surface, not a permanent note archive.
    </footer>
  </main>
</body>
</html>
"""


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
