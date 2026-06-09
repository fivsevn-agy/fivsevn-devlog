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

DEFAULT_SOURCE_CAP = 4
DEFAULT_SECTION_CAP = 12

REGION_LABELS: dict[str, tuple[str, str]] = {
    "global": ("global", "国际"),
    "north_america": ("north america", "北美"),
    "europe": ("europe", "欧洲"),
    "east_asia": ("east asia", "东亚"),
    "southeast_asia": ("southeast asia", "东南亚"),
    "china": ("china", "中国"),
    "south_asia": ("south asia", "南亚"),
    "middle_east": ("middle east", "中东"),
    "latin_america": ("latin america", "拉美"),
    "africa": ("africa", "非洲"),
}


def get_region_label(region_key: str) -> tuple[str, str]:
    return REGION_LABELS.get(region_key, (region_key.replace("_", " "), ""))


def make_region_section_key(section_key: str, region_key: str) -> str:
    return f"{section_key}__{region_key}"


def get_section_regions(config: dict[str, Any], section_key: str, section: dict[str, Any]) -> dict[str, Any]:
    """Return regional feeds for a section.

    The preferred shape is `sections.<section_key>.regions`. For the world news
    section, also accept the existing top-level `regions` block so older/current
    configs keep working without changing the page UI.
    """
    regions = section.get("regions")
    if isinstance(regions, dict):
        return regions

    if section_key == "world_society":
        top_level_regions = config.get("regions")
        if isinstance(top_level_regions, dict):
            return {
                str(region_key): feeds
                for region_key, feeds in top_level_regions.items()
                if str(region_key) in REGION_LABELS and isinstance(feeds, list)
            }

    return {}


def is_explicit_link_source(feed: dict[str, Any]) -> bool:
    feed_type = str(feed.get("type", "")).strip().lower()
    return feed_type in {"link", "url", "homepage", "page"}


def looks_like_feed_url(feed_url: str) -> bool:
    value = feed_url.lower()
    feed_markers = ("rss", "atom", "rdf", "feed", "xml")
    return any(marker in value for marker in feed_markers)


def make_link_source_item(feed_name: str, feed_url: str) -> dict[str, Any]:
    return {
        "title": feed_name,
        "link": feed_url,
        "summary": "Source homepage / 来源主页",
        "source": "URL-only source / 仅网址源",
        "published_dt": datetime.now(timezone.utc),
        "published": "",
        "is_source_link": True,
    }


def load_config() -> dict[str, Any]:
    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def escape(value: Any) -> str:
    if value is None:
        return ""
    return html.escape(str(value), quote=True).strip()


SUMMARY_CHAR_CAP = 1100


def strip_html(value: str) -> str:
    if not value:
        return ""
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def clamp_summary(value: str) -> str:
    value = re.sub(r"\s+", " ", value or "").strip()
    if not value:
        return ""
    if len(value) <= SUMMARY_CHAR_CAP:
        return value

    cut = value[:SUMMARY_CHAR_CAP].rstrip()
    sentence_end = max(cut.rfind("."), cut.rfind("。"), cut.rfind("!"), cut.rfind("?"))
    if sentence_end >= int(SUMMARY_CHAR_CAP * 0.55):
        return cut[:sentence_end + 1]
    return cut.rstrip(" ,;:，；：") + "…"


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


def get_int(value: Any, default: int) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def get_disabled_feed_names(config: dict[str, Any]) -> set[str]:
    disabled_names: set[str] = set()
    for feed in config.get("disabled_feeds", []):
        if isinstance(feed, dict):
            name = feed.get("name")
        else:
            name = feed
        if name:
            disabled_names.add(str(name))
    return disabled_names


def fetch_feed(feed_name: str, feed_url: str, limit: int = DEFAULT_SOURCE_CAP) -> list[dict[str, Any]]:
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
        summary = clamp_summary(strip_html(raw_summary))
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


def iter_section_feeds(section_key: str, section: dict[str, Any], config: dict[str, Any]) -> list[dict[str, Any]]:
    """Return feeds from either the legacy `feeds:` shape or the regional `regions:` shape."""
    feeds = section.get("feeds")
    if isinstance(feeds, list):
        return [feed for feed in feeds if isinstance(feed, dict)]

    regional_feeds: list[dict[str, Any]] = []
    regions = get_section_regions(config, section_key, section)
    if isinstance(regions, dict):
        for region_key, feeds_in_region in regions.items():
            if not isinstance(feeds_in_region, list):
                continue
            for feed in feeds_in_region:
                if not isinstance(feed, dict):
                    continue
                feed_copy = dict(feed)
                feed_copy.setdefault("region", str(region_key))
                regional_feeds.append(feed_copy)

    return regional_feeds


def build_section(section_key: str, section: dict[str, Any], config: dict[str, Any]) -> list[dict[str, Any]]:
    display = config.get("display", {})
    default_source_cap = get_int(display.get("default_source_cap"), DEFAULT_SOURCE_CAP)
    default_section_cap = get_int(display.get("max_items_per_section"), DEFAULT_SECTION_CAP)
    source_caps = display.get("source_caps", {}) or {}
    section_caps = display.get("section_caps", {}) or {}
    section_cap = get_int(section_caps.get(section_key), default_section_cap)
    disabled_feed_names = get_disabled_feed_names(config)

    section_items: list[dict[str, Any]] = []

    for feed in iter_section_feeds(section_key, section, config):
        feed_name = feed.get("name", "Unknown Source")
        feed_url = feed.get("url")
        if not feed_url:
            continue

        if feed_name in disabled_feed_names:
            print(f"[skip] disabled feed: {feed_name}")
            continue

        source_cap = get_int(source_caps.get(feed_name), default_source_cap)
        if source_cap <= 0:
            print(f"[skip] source cap <= 0: {feed_name}")
            continue

        region = feed.get("region")
        region_suffix = f" [{region}]" if region else ""

        if is_explicit_link_source(feed):
            print(f"[link] {feed_name}{region_suffix}: {feed_url}")
            items = [make_link_source_item(feed_name, feed_url)]
        else:
            print(f"[fetch] {feed_name}{region_suffix}: {feed_url}")
            try:
                items = fetch_feed(feed_name, feed_url, source_cap)
            except Exception as error:
                print(f"[error] failed to fetch {feed_name}: {error}")
                print(f"[link] fetch failed; rendering source link: {feed_name}")
                items = [make_link_source_item(feed_name, str(feed_url))]

            if not items:
                print(f"[link] no RSS entries returned; rendering source link: {feed_name}")
                items = [make_link_source_item(feed_name, str(feed_url))]

        print(f"[items] {feed_name}: {len(items)}")
        if region:
            for item in items:
                item["region"] = str(region)
        section_items.extend(items)

    section_items.sort(key=lambda item: item["published_dt"], reverse=True)

    # Regional sections are rendered as virtual subsections, e.g.
    # world_society__global, world_society__europe, etc.  The old behavior
    # applied `section_cap` once to the whole parent section before rendering;
    # that lets active regions consume the entire quota and leaves other
    # subscribed regions displaying "No items fetched."  Cap each virtual region
    # independently instead.
    regions = get_section_regions(config, section_key, section)
    if isinstance(regions, dict) and regions:
        capped_items: list[dict[str, Any]] = []
        for region_key in regions.keys():
            region_key = str(region_key)
            virtual_section_key = make_region_section_key(section_key, region_key)
            raw_region_cap = section_caps.get(virtual_section_key, section_caps.get(section_key, default_section_cap))
            region_cap = get_int(raw_region_cap, default_section_cap)
            region_items = [item for item in section_items if str(item.get("region", "")) == region_key]
            if region_cap > 0:
                region_items = region_items[:region_cap]
            capped_items.extend(region_items)
        capped_items.sort(key=lambda item: item["published_dt"], reverse=True)
        return capped_items

    if section_cap <= 0:
        return section_items
    return section_items[:section_cap]


def render_article(item: dict[str, Any]) -> str:
    title = escape(item["title"])
    link = escape(item["link"])
    source = escape(item["source"])
    published = escape(item["published"])
    summary = escape(item.get("summary", ""))
    summary_html = f"<p class='summary'>{summary}</p>" if summary else ""
    if item.get("is_source_link") or not published:
        meta_html = f"<div class=\"meta\">{source}</div>"
    else:
        meta_html = f"<div class=\"meta\">{source} · {published}</div>"

    return f"""
<article class="article">
  <h3><a href="{link}" target="_blank" rel="noopener noreferrer">{title}</a></h3>
  {meta_html}
  {summary_html}
</article>
""".strip()


def render_label(title: Any, title_zh: Any = "") -> str:
    title_text = escape(title)
    title_zh_text = escape(title_zh)
    if title_text and title_zh_text:
        return f"{title_text} / {title_zh_text}"
    return title_text or title_zh_text


def get_first_category_key(config: dict[str, Any]) -> str:
    categories = config.get("categories", {}) or {}
    for category_key in categories.keys():
        return str(category_key)
    return ""


def get_first_section_for_category(category: dict[str, Any], sections: dict[str, Any]) -> str:
    for section_key in category.get("sections", []) or []:
        if section_key in sections:
            return str(section_key)
    return ""


def render_drawer_nav(config: dict[str, Any], daily_postcard_html: str, daily_field_sample_html: str) -> str:
    widgets = config.get("widgets", {}) or {}
    parts: list[str] = []

    if daily_postcard_html:
        widget = widgets.get("postcard", {}) or {}
        label = render_label(widget.get("title", "postcard"), widget.get("title_zh", "明信片"))
        parts.append(f'<a href="#daily-postcard" data-drawer-item="daily-postcard">{label}</a>')

    if daily_field_sample_html:
        widget = widgets.get("daily_field_sample", {}) or {}
        label = render_label(widget.get("title", "Daily Field Sample"), widget.get("title_zh", "今日野采样本"))
        parts.append(f'<a href="#daily-field-sample" data-drawer-item="daily-field-sample">{label}</a>')

    return "\n".join(parts)


def render_category_nav(config: dict[str, Any]) -> str:
    categories = config.get("categories", {}) or {}
    sections = config.get("sections", {}) or {}
    parts: list[str] = []

    for category_key, category in categories.items():
        first_section_key = get_first_section_for_category(category, sections)
        if not first_section_key:
            continue
        href = f"#{escape(first_section_key)}"
        label = render_label(category.get("title", category_key), category.get("title_zh", ""))
        parts.append(
            f'<a href="{href}" data-category="{escape(category_key)}" data-first-section="{escape(first_section_key)}">{label}</a>'
        )

    return "\n".join(parts)


def render_section_nav(config: dict[str, Any]) -> str:
    categories = config.get("categories", {}) or {}
    sections = config.get("sections", {}) or {}
    first_category_key = get_first_category_key(config)
    parts: list[str] = []

    for category_key, category in categories.items():
        for section_key in category.get("sections", []) or []:
            section = sections.get(section_key)
            if not section:
                continue

            regions = get_section_regions(config, str(section_key), section)
            if isinstance(regions, dict) and regions:
                for region_key in regions.keys():
                    region_key = str(region_key)
                    title, title_zh = get_region_label(region_key)
                    label = render_label(title, title_zh)
                    hidden = "" if str(category_key) == first_category_key else " hidden"
                    virtual_section_key = make_region_section_key(str(section_key), region_key)
                    parts.append(
                        f'<a href="#{escape(virtual_section_key)}" data-parent-category="{escape(category_key)}" data-section-key="{escape(virtual_section_key)}"{hidden}>{label}</a>'
                    )
                continue

            label = render_label(section.get("title", section_key), section.get("title_zh", ""))
            hidden = "" if str(category_key) == first_category_key else " hidden"
            parts.append(
                f'<a href="#{escape(section_key)}" data-parent-category="{escape(category_key)}" data-section-key="{escape(section_key)}"{hidden}>{label}</a>'
            )

    return "\n".join(parts)

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

    drawer_nav_html = render_drawer_nav(config, daily_postcard_html, daily_field_sample_html)
    category_nav_html = render_category_nav(config)
    section_nav_html = render_section_nav(config)

    section_to_category: dict[str, str] = {}
    sections_config_for_map = config.get("sections", {}) or {}
    for category_key, category in (config.get("categories", {}) or {}).items():
        for mapped_section_key in category.get("sections", []) or []:
            mapped_section_key = str(mapped_section_key)
            section_to_category[mapped_section_key] = str(category_key)
            section_config = sections_config_for_map.get(mapped_section_key, {}) or {}
            regions = get_section_regions(config, mapped_section_key, section_config)
            if isinstance(regions, dict):
                for region_key in regions.keys():
                    section_to_category[make_region_section_key(mapped_section_key, str(region_key))] = str(category_key)

    def ordered_section_keys() -> list[str]:
        sections = config.get("sections", {}) or {}
        categories = config.get("categories", {}) or {}
        ordered: list[str] = []
        seen: set[str] = set()

        for category in categories.values():
            for section_key in category.get("sections", []) or []:
                section_key = str(section_key)
                if section_key in sections and section_key not in seen:
                    ordered.append(section_key)
                    seen.add(section_key)

        # Fallback: preserve any legacy/uncategorized sections instead of dropping them.
        for section_key in sections.keys():
            if section_key not in seen:
                ordered.append(section_key)
                seen.add(section_key)

        return ordered

    section_parts: list[str] = []
    sections_config = config.get("sections", {}) or {}
    for section_key in ordered_section_keys():
        section = sections_config[section_key]
        section_title = escape(section.get("title", section_key))
        section_title_zh = escape(section.get("title_zh", ""))
        section_description = escape(section.get("description", ""))
        section_description_zh = escape(section.get("description_zh", ""))
        items = sections_data.get(section_key, [])

        regions = get_section_regions(config, section_key, section)
        if isinstance(regions, dict) and regions:
            items_by_region: dict[str, list[dict[str, Any]]] = {str(region_key): [] for region_key in regions.keys()}
            for item in items:
                region_key = str(item.get("region", ""))
                if region_key in items_by_region:
                    items_by_region[region_key].append(item)

            for region_key in regions.keys():
                region_key = str(region_key)
                region_title, region_title_zh = get_region_label(region_key)
                virtual_section_key = make_region_section_key(section_key, region_key)
                region_article_parts = [render_article(item) for item in items_by_region.get(region_key, [])]
                if not region_article_parts:
                    region_article_parts = ['<p class="empty">No items fetched.</p>']

                region_title_escaped = escape(region_title)
                region_title_zh_escaped = escape(region_title_zh)
                title_zh_html = f"<p class='section-title-zh'>{region_title_zh_escaped}</p>" if region_title_zh_escaped else ""
                description_html = f"<p class='section-description'>{section_description}</p>" if section_description else ""
                description_zh_html = f"<p class='section-description-zh'>{section_description_zh}</p>" if section_description_zh else ""
                section_category = escape(section_to_category.get(virtual_section_key, ""))
                section_parts.append(
                    f"""
<section id="{escape(virtual_section_key)}" data-section-category="{section_category}">
  <h2>{region_title_escaped}</h2>
  {title_zh_html}
  {description_html}
  {description_zh_html}
  {''.join(region_article_parts)}
</section>
""".strip()
                )
            continue

        article_parts = [render_article(item) for item in items]
        if not article_parts:
            article_parts = ['<p class="empty">No items fetched.</p>']

        title_zh_html = f"<p class='section-title-zh'>{section_title_zh}</p>" if section_title_zh else ""
        description_html = f"<p class='section-description'>{section_description}</p>" if section_description else ""
        description_zh_html = f"<p class='section-description-zh'>{section_description_zh}</p>" if section_description_zh else ""

        section_category = escape(section_to_category.get(section_key, ""))
        section_parts.append(
            f"""
<section id="{escape(section_key)}" data-section-category="{section_category}">
  <h2>{section_title}</h2>
  {title_zh_html}
  {description_html}
  {description_zh_html}
  {''.join(article_parts)}
</section>
""".strip()
        )

    modules_html = "\n".join(part for part in [daily_postcard_html, daily_field_sample_html] if part)
    sections_html = "\n".join(section_parts)
    drawer_block_html = ""
    if drawer_nav_html or modules_html:
        drawer_block_html = f"""
<section class="intake-block drawer-block">
  <div class="shelf-nav drawer-nav">
    <p class="kicker">Junk drawer / 杂物箱：</p>
    <nav>
      {drawer_nav_html}
    </nav>
  </div>

  {modules_html}
</section>
""".strip()

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

    html {{
      font-size: 75%;
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
      padding-bottom: 0;
      margin-bottom: 0;
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

    .intake-block {{
      position: relative;
    }}

    .shelf-nav {{
      position: sticky;
      top: 0;
      z-index: 20;
      background: var(--bg);
      padding-bottom: 24px;
      margin-bottom: 32px;
      border-bottom: 1px solid var(--border);
    }}

    nav {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 12px;
    }}

    .shelf-nav nav {{
      flex-wrap: nowrap;
      overflow-x: auto;
      overflow-y: hidden;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
    }}

    .shelf-nav nav::-webkit-scrollbar {{
      display: none;
    }}

    nav a {{
      color: var(--site-green);
      text-decoration: none;
      border: 1px solid var(--border);
      border-radius: 999px;
      padding: 5px 12px;
      font-size: 0.9rem;
    }}

    .shelf-nav nav a {{
      flex: 0 0 auto;
      white-space: nowrap;
    }}

    .section-nav {{
      margin-top: 8px;
    }}

    .section-nav a {{
      color: var(--muted);
      font-size: 0.86rem;
    }}

    .section-nav a[hidden] {{
      display: none;
    }}

    nav a:hover,
    nav a[aria-current="true"] {{
      border-color: var(--site-green);
    }}

    .section-nav a:hover,
    .section-nav a[aria-current="true"] {{
      border-color: var(--muted);
    }}

    section {{
      margin: 42px 0;
      scroll-margin-top: 122px;
    }}

    h2 {{
      margin: 0 0 2px;
      padding-bottom: 8px;
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

    </header>

    {drawer_block_html}

    <section class="intake-block shelf-block">
      <div class="shelf-nav feed-nav">
        <p class="kicker">On the shelf / 本日上架：</p>
        <nav class="category-nav">
          {category_nav_html}
        </nav>
        <nav class="section-nav">
          {section_nav_html}
        </nav>
      </div>

      {sections_html}
    </section>

    <footer>
      <p>本页面由 GitHub Actions 每日生成，数据来自 RSS 与采样脚本。<a href="https://github.com/fivsevn-agy/fivsevn-devlog/tree/233c5bab2dba086446db83ee8e7b232b46c53a1a/intake">查看仓库</a></p>
    </footer>
  </main>

  <script>
    (() => {{
      const hasInitialHash = Boolean(window.location.hash);
      if ("scrollRestoration" in history && !hasInitialHash) {{
        history.scrollRestoration = "manual";
      }}

      const forceTopOnPlainEntry = () => {{
        if (!hasInitialHash) {{
          window.scrollTo(0, 0);
        }}
      }};

      forceTopOnPlainEntry();
      window.addEventListener("pageshow", forceTopOnPlainEntry);
      window.addEventListener("load", forceTopOnPlainEntry);

      const allNavs = Array.from(document.querySelectorAll(".shelf-nav nav"));
      const categoryLinks = Array.from(document.querySelectorAll(".category-nav a[data-category]"));
      const sectionLinks = Array.from(document.querySelectorAll(".section-nav a[data-parent-category]"));
      const drawerLinks = Array.from(document.querySelectorAll(".drawer-nav a[href^='#']"));
      const trackedLinks = [...drawerLinks, ...sectionLinks];

      const keepLinkVisible = (link) => {{
        const nav = link.closest("nav");
        if (!nav) return;

        const navRect = nav.getBoundingClientRect();
        const linkRect = link.getBoundingClientRect();
        const margin = 16;

        if (linkRect.left < navRect.left + margin || linkRect.right > navRect.right - margin) {{
          link.scrollIntoView({{ behavior: "smooth", block: "nearest", inline: "center" }});
        }}
      }};

      const showCategorySections = (categoryKey) => {{
        sectionLinks.forEach((link) => {{
          link.hidden = link.dataset.parentCategory !== categoryKey;
        }});

        categoryLinks.forEach((link) => {{
          if (link.dataset.category === categoryKey) {{
            link.setAttribute("aria-current", "true");
            keepLinkVisible(link);
          }} else {{
            link.removeAttribute("aria-current");
          }}
        }});
      }};

      const getCategoryForSection = (sectionId) => {{
        const sectionLink = sectionLinks.find((link) => link.dataset.sectionKey === sectionId);
        return sectionLink ? sectionLink.dataset.parentCategory : "";
      }};

      const setCurrentTrackedLink = (activeId) => {{
        trackedLinks.forEach((link) => {{
          const href = link.getAttribute("href") || "";
          const id = decodeURIComponent(href.slice(1));
          if (id === activeId) {{
            link.setAttribute("aria-current", "true");
            keepLinkVisible(link);
          }} else {{
            link.removeAttribute("aria-current");
          }}
        }});
      }};

      const targets = trackedLinks
        .map((link) => {{
          const href = link.getAttribute("href") || "";
          const id = decodeURIComponent(href.slice(1));
          const target = document.getElementById(id);
          return target ? {{ id, link, target }} : null;
        }})
        .filter(Boolean);

      if (!categoryLinks.length && !targets.length) return;

      const initialHashId = decodeURIComponent((window.location.hash || "").slice(1));
      const initialCategory = getCategoryForSection(initialHashId) || categoryLinks[0]?.dataset.category;
      if (initialCategory) showCategorySections(initialCategory);

      const scrollToTargetId = (targetId) => {{
        const target = document.getElementById(targetId);
        if (!target) return;
        target.scrollIntoView({{ behavior: "smooth", block: "start" }});
        if (history.pushState) {{
          history.pushState(null, "", `#${{encodeURIComponent(targetId)}}`);
        }} else {{
          window.location.hash = targetId;
        }}
      }};

      categoryLinks.forEach((link) => {{
        link.addEventListener("click", (event) => {{
          const categoryKey = link.dataset.category;
          const firstSection = link.dataset.firstSection;
          if (!categoryKey) return;

          event.preventDefault();
          showCategorySections(categoryKey);

          const firstVisibleSectionLink = sectionLinks.find((sectionLink) => {{
            return sectionLink.dataset.parentCategory === categoryKey && !sectionLink.hidden;
          }});
          const targetId = firstVisibleSectionLink?.dataset.sectionKey || firstSection;
          if (targetId) {{
            setCurrentTrackedLink(targetId);
            scrollToTargetId(targetId);
          }}
        }});
      }});

      sectionLinks.forEach((link) => {{
        link.addEventListener("click", (event) => {{
          const targetId = link.dataset.sectionKey;
          if (!targetId) return;
          event.preventDefault();
          const categoryKey = link.dataset.parentCategory;
          if (categoryKey) showCategorySections(categoryKey);
          setCurrentTrackedLink(targetId);
          scrollToTargetId(targetId);
        }});
      }});

      let currentId = "";
      let ticking = false;

      const getOffset = () => {{
        const visibleStickyHeights = allNavs
          .map((nav) => nav.closest(".shelf-nav"))
          .filter(Boolean)
          .map((nav) => nav.getBoundingClientRect())
          .filter((rect) => rect.top <= 1 && rect.bottom > 0)
          .map((rect) => rect.height);
        const stickyHeight = visibleStickyHeights.length ? Math.max(...visibleStickyHeights) : 0;
        return stickyHeight + Math.min(180, window.innerHeight * 0.22);
      }};

      const updateCurrent = () => {{
        ticking = false;
        if (!targets.length) return;

        const offset = getOffset();
        let active = targets[0];

        for (const item of targets) {{
          if (item.target.getBoundingClientRect().top <= offset) {{
            active = item;
          }} else {{
            break;
          }}
        }}

        if (!active || active.id === currentId) return;
        currentId = active.id;
        setCurrentTrackedLink(active.id);

        const categoryKey = getCategoryForSection(active.id);
        if (categoryKey) showCategorySections(categoryKey);
      }};

      const requestUpdate = () => {{
        if (ticking) return;
        ticking = true;
        window.requestAnimationFrame(updateCurrent);
      }};

      window.addEventListener("scroll", requestUpdate, {{ passive: true }});
      window.addEventListener("resize", requestUpdate);
      window.addEventListener("hashchange", requestUpdate);
      requestUpdate();
    }})();
  </script>
</body>
</html>
"""


def main() -> None:
    config = load_config()

    sections_data: dict[str, list[dict[str, Any]]] = {}
    for section_key, section in config.get("sections", {}).items():
        print(f"[section] {section_key}")
        sections_data[section_key] = build_section(section_key, section, config)

    OUTPUT_PATH.write_text(render_html(config, sections_data), encoding="utf-8")
    print(f"[done] generated {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
