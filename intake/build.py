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

ITEMS_PER_FEED = 5


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


def fetch_feed(feed_name: str, feed_url: str, limit: int = ITEMS_PER_FEED) -> list[dict[str, Any]]:
    parsed = feedparser.parse(feed_url)
    if getattr(parsed, "bozo", False):
        print(f"[warn] feed parse warning: {feed_name} — {feed_url}")

    items: list[dict[str, Any]] = []
    seen_links: set[str] = set()

    for entry in parsed.entries:
        link = entry.get("link", "").strip()
        title = entry.get("title", "Untitled").strip()
        if not link or not title:
            continue

        normalized_link = link.split("?")[0].rstrip("/")
        if normalized_link in seen_links:
            continue
        seen_links.add(normalized_link)

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

    items.sort(key=lambda item: item["published_dt"], reverse=True)
    return items[:limit]


def build_section(section: dict[str, Any]) -> list[dict[str, Any]]:
    section_items: list[dict[str, Any]] = []

    for feed in section.get("feeds", []):
        feed_name = feed.get("name", "Unknown Source")
        feed_url = feed.get("url")
        if not feed_url:
            continue

        print(f"[fetch] {feed_name}: {feed_url}")
        try:
            items = fetch_feed(feed_name, feed_url, ITEMS_PER_FEED)
        except Exception as error:
            print(f"[error] failed to fetch {feed_name}: {error}")
            continue

        print(f"[items] {feed_name}: {len(items)}")
        section_items.extend(items)

    section_items.sort(key=lambda item: item["published_dt"], reverse=True)
    return section_items


def render_article(item: dict[str, Any]) -> str:
    title = escape(item["title"])
    link = escape(item["link"])
    source = escape(item["source"])
    published = escape(item["published"])
    summary = escape(item.get("summary", ""))
    summary_html = f"<p class='summary'>{summary}</p>" if summary else ""

    return f"""
<article class="article">
  <h3><a href="{link}" target="_blank" rel="noopener noreferrer">{title}</a></h3>
  <div class="meta">{source} · {published}</div>
  {summary_html}
</article>
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
        nav_parts.append('<a href="#daily-postcard">postcard / 明信片</a>')
    if daily_field_sample_html:
        nav_parts.append('<a href="#daily-field-sample">Daily Field Sample / 今日野采样本</a>')

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
        nav_parts.append(f'<a href="#{escape(section_key)}">{nav_label}</a>')

        article_parts = [render_article(item) for item in items]
        if not article_parts:
            article_parts = ['<p class="empty">No items fetched.</p>']

        title_zh_html = f"<p class='section-title-zh'>{section_title_zh}</p>" if section_title_zh else ""
        description_html = f"<p class='section-description'>{section_description}</p>" if section_description else ""
        description_zh_html = f"<p class='section-description-zh'>{section_description_zh}</p>" if section_description_zh else ""

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
    modules_html = "\n".join(part for part in [daily_postcard_html, daily_field_sample_html] if part)
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
      --site-green: #6becae;
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
      margin: 0 0 28px;
      color: var(--text);
      font-size: 1.15rem;
      font-weight: 500;
    }}

    .kicker {{
      margin: 18px 0 2px;
      color: var(--muted);
      font-size: 0.95rem;
    }}

    .kicker-value {{
      margin: 0 0 8px;
      color: var(--text);
      font-size: 1.05rem;
      font-weight: 650;
    }}

    nav {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 12px;
    }}

    nav a {{
      color: var(--site-green);
      text-decoration: none;
      border: 1px solid var(--border);
      border-radius: 999px;
      padding: 5px 12px;
      font-size: 0.9rem;
    }}

    nav a:hover {{
      border-color: var(--site-green);
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

    .article,
    .daily-field-sample,
    .postcard-mail {{
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 16px;
      margin: 14px 0;
    }}

    .postcard-mail {{
      padding: 18px;
    }}

    .postcard-header {{
      margin: 0 0 20px;
      color: var(--muted);
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
      font-size: 0.95rem;
      line-height: 1.55;
      white-space: normal;
    }}

    .postcard-header div {{
      margin: 0;
    }}

    .postcard-header strong {{
      color: var(--muted);
      font-weight: 800;
    }}

    .postcard-header a {{
      color: var(--muted);
      text-decoration: underline;
      text-underline-offset: 2px;
    }}

    .postcard-label {{
      margin: 0 0 10px;
      color: var(--muted);
      font-weight: 650;
    }}

    .postcard-image-link {{
      display: block;
      width: fit-content;
      max-width: 100%;
      margin: 0 auto;
    }}

    .postcard-image {{
      display: block;
      max-width: 100%;
      max-height: 620px;
      border: 1px solid var(--border);
      border-radius: 10px;
      object-fit: contain;
    }}

    .postcard-original {{
      margin: 8px 0 0;
      color: var(--muted);
      font-size: 0.78rem;
      word-break: break-all;
    }}

    .postcard-original a {{
      color: var(--muted);
      text-decoration: underline;
      text-underline-offset: 2px;
    }}

    .daily-field-sample h2 {{
      margin-bottom: 18px;
    }}

    .daily-field-sample p {{
      margin: 0 0 18px;
    }}

    .daily-field-sample a {{
      color: var(--site-green);
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

    footer a {{
      color: var(--site-green);
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

      <p class="kicker">Courier on duty / 投递员：</p>
      <p class="kicker-value">GitHub Actions</p>

      <p class="kicker">Shift opened / 到店时间：</p>
      <p class="kicker-value">{opened_at}</p>

      <p class="kicker">On the shelf / 本日上架：</p>
      <nav>
        {nav_html}
      </nav>
    </header>

    {modules_html}
    {sections_html}

    <footer>
      <p>本页面由 GitHub Actions 每日生成，数据来自 RSS 与采样脚本。<a href="https://github.com/fivsevn-agy/fivsevn-devlog/tree/233c5bab2dba086446db83ee8e7b232b46c53a1a/intake">查看仓库</a></p>
    </footer>
  </main>
</body>
</html>
"""


def main() -> None:
    config = load_config()

    sections_data: dict[str, list[dict[str, Any]]] = {}
    for section_key, section in config.get("sections", {}).items():
        print(f"[section] {section_key}")
        sections_data[section_key] = build_section(section)

    OUTPUT_PATH.write_text(render_html(config, sections_data), encoding="utf-8")
    print(f"[done] generated {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
