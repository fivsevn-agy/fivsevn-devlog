#!/usr/bin/env python3
from __future__ import annotations

import concurrent.futures
import hashlib
import html
import json
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any

ROOT_DIR = Path(__file__).resolve().parents[1]

AI_DIR = ROOT_DIR / "ai"
SHARED_SOURCES_MD = ROOT_DIR / "intake" / "sources.md"
EXTRA_SOURCES_JSON = AI_DIR / "sources_extra.json"

NEWS_JSON = AI_DIR / "news.json"
NEWS_MD = AI_DIR / "news.md"
LATEST_ITEMS_JSON = AI_DIR / "latest-items.json"

MAX_ITEMS = 160
DEFAULT_SOURCE_CAP = 6
FETCH_TIMEOUT = 8
MAX_WORKERS = 12

USER_AGENT = "fivsevn-ai-collaborator/1.0 (+https://devlog.fivsevn.com/)"

SOURCE_KEYS = (
    "name",
    "section",
    "feed_url",
    "source_cap",
    "site_url",
    "source_type",
    "authority_level",
    "reliability_score",
    "professional_value",
    "use_role",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha16(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:16]


def clean_value(value: Any) -> str:
    text = str(value or "").strip()
    text = text.strip()
    text = text.strip("'\"`")
    text = text.replace("’‘", "").replace("''", "").replace('""', "")
    text = text.strip("'\"`")
    return text.strip()


def parse_int(value: Any, default: int = 0) -> int:
    try:
        return int(str(value).strip())
    except Exception:
        return default


def norm_url(url: str, base: str | None = None) -> str:
    url = html.unescape(clean_value(url))
    if base:
        url = urllib.parse.urljoin(base, url)

    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return ""

    return urllib.parse.urlunparse(
        (
            parsed.scheme,
            parsed.netloc,
            parsed.path or "/",
            "",
            parsed.query,
            "",
        )
    )


def fetch_url(url: str) -> tuple[str, str]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": (
                "application/rss+xml, application/atom+xml, application/xml, "
                "text/xml, */*;q=0.5"
            ),
        },
    )

    with urllib.request.urlopen(request, timeout=FETCH_TIMEOUT) as response:
        content_type = response.headers.get("content-type", "")
        raw = response.read(5_000_000)

    return raw.decode("utf-8", errors="replace"), content_type


def strip_html(value: str) -> str:
    value = re.sub(r"(?is)<script[^>]*>.*?</script>", " ", value)
    value = re.sub(r"(?is)<style[^>]*>.*?</style>", " ", value)
    value = re.sub(r"(?s)<[^>]+>", " ", value)
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def parse_source_block(block: str) -> dict[str, str]:
    text = " ".join(block.split())

    key_pattern = "|".join(re.escape(key) for key in SOURCE_KEYS)
    pattern = re.compile(
        rf"\b({key_pattern}):\s*(.*?)(?=\s+\b(?:{key_pattern}):\s*|$)",
        re.I,
    )

    result: dict[str, str] = {}
    for match in pattern.finditer(text):
        key = match.group(1).lower()
        value = clean_value(match.group(2))
        result[key] = value

    return result


def load_shared_sources(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        print(f"[warn] missing shared sources file: {path}")
        return []

    text = path.read_text(encoding="utf-8", errors="replace")
    blocks = re.findall(r"```source\s+(.*?)```", text, flags=re.S | re.I)

    result: list[dict[str, Any]] = []
    seen_feeds: set[str] = set()

    for block in blocks:
        data = parse_source_block(block)

        name = clean_value(data.get("name"))
        section = clean_value(data.get("section"))
        feed_url = norm_url(data.get("feed_url", ""))
        site_url = norm_url(data.get("site_url", ""))
        source_cap = parse_int(data.get("source_cap"), DEFAULT_SOURCE_CAP)

        if source_cap <= 0:
            continue

        if not feed_url:
            continue

        if feed_url in seen_feeds:
            continue

        seen_feeds.add(feed_url)

        result.append(
            {
                "name": name or urllib.parse.urlparse(feed_url).netloc,
                "section": section,
                "url": feed_url,
                "feed_url": feed_url,
                "site_url": site_url,
                "kind": "shared",
                "source_cap": source_cap,
            }
        )

    return result


def load_extra_sources(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []

    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception as error:
        print(f"[warn] failed to read {path}: {error}")
        return []

    sources = payload.get("sources", [])
    if not isinstance(sources, list):
        return []

    result: list[dict[str, Any]] = []
    seen_feeds: set[str] = set()

    for item in sources:
        if not isinstance(item, dict):
            continue

        feed_url = norm_url(item.get("feed_url") or item.get("url") or "")
        if not feed_url:
            continue

        source_cap = parse_int(item.get("source_cap"), DEFAULT_SOURCE_CAP)
        if source_cap <= 0:
            continue

        if feed_url in seen_feeds:
            continue

        seen_feeds.add(feed_url)

        result.append(
            {
                "name": clean_value(item.get("name")) or urllib.parse.urlparse(feed_url).netloc,
                "section": clean_value(item.get("section")),
                "url": feed_url,
                "feed_url": feed_url,
                "site_url": norm_url(item.get("site_url") or ""),
                "kind": clean_value(item.get("kind")) or "extra",
                "source_cap": source_cap,
            }
        )

    return result


def text_of(node: ET.Element | None) -> str:
    if node is None:
        return ""
    return strip_html("".join(node.itertext()))


def find_child(node: ET.Element, names: tuple[str, ...]) -> ET.Element | None:
    wanted = {name.lower() for name in names}

    for child in list(node):
        local_name = child.tag.split("}")[-1].lower()
        if local_name in wanted:
            return child

    return None


def find_children(node: ET.Element, names: tuple[str, ...]) -> list[ET.Element]:
    wanted = {name.lower() for name in names}
    result: list[ET.Element] = []

    for child in list(node):
        local_name = child.tag.split("}")[-1].lower()
        if local_name in wanted:
            result.append(child)

    return result


def parse_date(value: str) -> tuple[str, str]:
    value = value.strip()
    if not value:
        return "", ""

    try:
        dt = parsedate_to_datetime(value)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return value, dt.astimezone(timezone.utc).isoformat()
    except Exception:
        pass

    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return value, dt.astimezone(timezone.utc).isoformat()
    except Exception:
        return value, ""


def parse_feed(feed_url: str, feed_text: str, fallback_source_name: str) -> list[dict[str, Any]]:
    try:
        root = ET.fromstring(feed_text.encode("utf-8"))
    except ET.ParseError as error:
        print(f"[warn] failed to parse feed {feed_url}: {error}")
        return []

    root_name = root.tag.split("}")[-1].lower()

    feed_title = fallback_source_name
    raw_items: list[ET.Element] = []

    if root_name == "rss":
        channel = find_child(root, ("channel",))
        if channel is not None:
            feed_title = text_of(find_child(channel, ("title",))) or fallback_source_name
            raw_items = find_children(channel, ("item",))

    elif root_name == "feed":
        feed_title = text_of(find_child(root, ("title",))) or fallback_source_name
        raw_items = find_children(root, ("entry",))

    else:
        channel = find_child(root, ("channel",))
        if channel is not None:
            feed_title = text_of(find_child(channel, ("title",))) or fallback_source_name
            raw_items = find_children(channel, ("item",))
        else:
            raw_items = find_children(root, ("item", "entry"))

    items: list[dict[str, Any]] = []

    for raw_item in raw_items:
        item_name = raw_item.tag.split("}")[-1].lower()

        title = text_of(find_child(raw_item, ("title",)))
        summary = text_of(find_child(raw_item, ("description", "summary", "content", "encoded")))

        link = ""

        if item_name == "entry":
            for link_node in find_children(raw_item, ("link",)):
                rel = (link_node.attrib.get("rel") or "alternate").lower()
                href = link_node.attrib.get("href") or ""
                if rel == "alternate" and href:
                    link = norm_url(href, feed_url)
                    break
        else:
            link = norm_url(text_of(find_child(raw_item, ("link",))), feed_url)

        if not link:
            link = norm_url(text_of(find_child(raw_item, ("guid",))), feed_url)

        date_raw = ""
        date_iso = ""

        for date_key in ("published", "updated", "pubdate", "pubDate", "date"):
            date_node = find_child(raw_item, (date_key,))
            if date_node is not None:
                date_raw, date_iso = parse_date(text_of(date_node))
                if date_raw:
                    break

        if not title and not link:
            continue

        canonical = link or f"{feed_url}::{title}"

        items.append(
            {
                "id": sha16(canonical),
                "source": feed_title,
                "feed_url": feed_url,
                "title": title or "(untitled)",
                "url": link,
                "summary": summary,
                "published": date_raw,
                "published_iso": date_iso,
            }
        )

    return items


def load_sources() -> list[dict[str, Any]]:
    sources = []
    sources.extend(load_shared_sources(SHARED_SOURCES_MD))
    sources.extend(load_extra_sources(EXTRA_SOURCES_JSON))

    unique_sources: list[dict[str, Any]] = []
    seen_feeds: set[str] = set()

    for source in sources:
        feed_url = source.get("feed_url") or source.get("url")
        if not feed_url or feed_url in seen_feeds:
            continue

        seen_feeds.add(feed_url)
        unique_sources.append(source)

    return unique_sources


def fetch_and_parse_source(source: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    source_name = source.get("name") or source.get("feed_url") or source.get("url")
    feed_url = source.get("feed_url") or source.get("url")
    source_cap = parse_int(source.get("source_cap"), DEFAULT_SOURCE_CAP)

    print(f"[source] {source_name}: {feed_url}")

    try:
        feed_text, content_type = fetch_url(feed_url)
    except Exception as error:
        report = {
            "name": source_name,
            "url": source.get("site_url") or feed_url,
            "kind": source.get("kind", ""),
            "section": source.get("section", ""),
            "status": "failed",
            "error": str(error)[:240],
            "feed_url": feed_url,
            "items": 0,
        }
        return [], report

    if not feed_text.strip():
        report = {
            "name": source_name,
            "url": source.get("site_url") or feed_url,
            "kind": source.get("kind", ""),
            "section": source.get("section", ""),
            "status": "failed",
            "error": f"empty response; content-type={content_type}",
            "feed_url": feed_url,
            "items": 0,
        }
        return [], report

    items = parse_feed(feed_url, feed_text, source_name)
    items = items[:source_cap]

    report = {
        "name": source_name,
        "url": source.get("site_url") or feed_url,
        "kind": source.get("kind", ""),
        "section": source.get("section", ""),
        "status": "ok" if items else "empty",
        "feed_url": feed_url,
        "items": len(items),
    }

    return items, report


def collect_items() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    sources = load_sources()

    print(f"[info] explicit feed sources: {len(sources)}")
    print("[info] site_url discovery is disabled")

    all_items: list[dict[str, Any]] = []
    source_reports: list[dict[str, Any]] = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(fetch_and_parse_source, source) for source in sources]

        for future in concurrent.futures.as_completed(futures):
            try:
                items, report = future.result()
            except Exception as error:
                items = []
                report = {
                    "name": "unknown",
                    "url": "",
                    "kind": "",
                    "section": "",
                    "status": "failed",
                    "error": str(error)[:240],
                    "feed_url": "",
                    "items": 0,
                }

            all_items.extend(items)
            source_reports.append(report)

    deduped: dict[str, dict[str, Any]] = {}
    for item in all_items:
        deduped[item["id"]] = item

    items = list(deduped.values())
    items.sort(key=lambda item: item.get("published_iso") or "", reverse=True)

    source_reports.sort(key=lambda item: (item.get("status") != "ok", item.get("name") or ""))

    return items[:MAX_ITEMS], source_reports


def build_payload() -> dict[str, Any]:
    generated_at = utc_now()
    items, source_reports = collect_items()

    content_hash = hashlib.sha256(
        json.dumps(items, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()

    return {
        "schema": "fivsevn.ai.news.v1",
        "generated_at": generated_at,
        "content_hash": f"sha256:{content_hash}",
        "purpose": "AI-readable news bundle for scheduled review and summarization.",
        "source_policy": {
            "shared_sources": "intake/sources.md",
            "extra_sources": "ai/sources_extra.json",
            "note": (
                "Only explicit feed_url entries are used. Empty feed_url, "
                "source_cap: 0, and site_url discovery are skipped."
            ),
        },
        "output_urls": {
            "raw_news_json": "https://raw.githubusercontent.com/fivsevn-agy/fivsevn-devlog/refs/heads/main/ai/news.json",
            "raw_news_md": "https://raw.githubusercontent.com/fivsevn-agy/fivsevn-devlog/refs/heads/main/ai/news.md",
            "raw_latest_items_json": "https://raw.githubusercontent.com/fivsevn-agy/fivsevn-devlog/refs/heads/main/ai/latest-items.json",
            "public_news_json": "https://devlog.fivsevn.com/ai/news.json",
            "public_news_md": "https://devlog.fivsevn.com/ai/news.md",
        },
        "counts": {
            "sources": len(source_reports),
            "sources_ok": sum(1 for source in source_reports if source.get("status") == "ok"),
            "sources_failed": sum(1 for source in source_reports if source.get("status") == "failed"),
            "sources_empty": sum(1 for source in source_reports if source.get("status") == "empty"),
            "items": len(items),
        },
        "sources": source_reports,
        "items": items,
    }


def render_markdown(payload: dict[str, Any]) -> str:
    lines: list[str] = []
    counts = payload.get("counts", {}) or {}

    lines.append("# AI News")
    lines.append("")
    lines.append(f"- Generated at: `{payload.get('generated_at', '')}`")
    lines.append(f"- Content hash: `{payload.get('content_hash', '')}`")
    lines.append(f"- Sources: {counts.get('sources_ok', 0)} ok / {counts.get('sources_failed', 0)} failed / {counts.get('sources_empty', 0)} empty")
    lines.append(f"- Items: {counts.get('items', 0)}")
    lines.append("")

    lines.append("## Sources")
    lines.append("")

    for source in payload.get("sources", []):
        lines.append(
            f"- `{source.get('status', '')}` {source.get('name', '')} — "
            f"{source.get('items', 0)} items — {source.get('feed_url', '')}"
        )
        if source.get("error"):
            lines.append(f"  - Error: {source.get('error')}")

    lines.append("")
    lines.append("## Latest Items")
    lines.append("")

    for item in payload.get("items", []):
        lines.append(f"### {item.get('title', '(untitled)')}")
        lines.append("")
        lines.append(f"- ID: `{item.get('id', '')}`")
        lines.append(f"- Source: {item.get('source', '')}")

        if item.get("published"):
            lines.append(f"- Published: {item.get('published')}")

        if item.get("published_iso"):
            lines.append(f"- Published ISO: `{item.get('published_iso')}`")

        if item.get("url"):
            lines.append(f"- URL: {item.get('url')}")

        summary = item.get("summary", "")
        if summary:
            lines.append("")
            lines.append(summary[:800])

        lines.append("")

    return "\n".join(lines).strip() + "\n"


def main() -> None:
    AI_DIR.mkdir(parents=True, exist_ok=True)

    payload = build_payload()

    NEWS_JSON.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    NEWS_MD.write_text(
        render_markdown(payload),
        encoding="utf-8",
    )

    LATEST_ITEMS_JSON.write_text(
        json.dumps(
            {
                "schema": "fivsevn.ai.latest_items.v1",
                "generated_at": payload.get("generated_at"),
                "content_hash": payload.get("content_hash"),
                "items": payload.get("items", []),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(f"[done] generated {NEWS_JSON}")
    print(f"[done] generated {NEWS_MD}")
    print(f"[done] generated {LATEST_ITEMS_JSON}")


if __name__ == "__main__":
    main()