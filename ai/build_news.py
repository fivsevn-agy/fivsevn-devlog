#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import html
import json
import re
import time
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

NEWS_MAX_ITEMS = 240
OWNED_MAX_ITEMS = 10
OWNED_KINDS = {"owned_site"}

FETCH_TIMEOUT = 20
USER_AGENT = "fivsevn-ai-collaborator/1.0 (+https://devlog.fivsevn.com/)"

FEED_CANDIDATES = (
    "feed.xml",
    "rss.xml",
    "atom.xml",
    "feed",
    "rss",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha16(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:16]


def fetch_url(url: str) -> tuple[str, str]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": (
                "application/rss+xml, application/atom+xml, application/xml, "
                "text/xml, text/html;q=0.8, */*;q=0.5"
            ),
        },
    )
    with urllib.request.urlopen(request, timeout=FETCH_TIMEOUT) as response:
        content_type = response.headers.get("content-type", "")
        raw = response.read()
    return raw.decode("utf-8", errors="replace"), content_type


def strip_html(value: str) -> str:
    value = re.sub(r"(?is)<script[^>]*>.*?</script>", " ", value)
    value = re.sub(r"(?is)<style[^>]*>.*?</style>", " ", value)
    value = re.sub(r"(?s)<[^>]+>", " ", value)
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def norm_url(url: str, base: str | None = None) -> str:
    url = html.unescape(url).strip()

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


def extract_urls_from_markdown(path: Path) -> list[str]:
    if not path.exists():
        print(f"[warn] missing shared sources file: {path}")
        return []

    text = path.read_text(encoding="utf-8", errors="replace")
    urls = re.findall(r"https?://[^\s\]\)\>\"']+", text)

    result: list[str] = []
    seen: set[str] = set()

    for url in urls:
        url = norm_url(url.rstrip(".,;"))
        if not url or url in seen:
            continue
        seen.add(url)
        result.append(url)

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

    for item in sources:
        if not isinstance(item, dict):
            continue

        url = norm_url(str(item.get("url", "")))
        if not url:
            continue

        result.append(
            {
                "name": str(item.get("name") or urllib.parse.urlparse(url).netloc),
                "url": url,
                "kind": str(item.get("kind") or "site"),
            }
        )

    return result


def looks_like_feed(text: str, content_type: str = "") -> bool:
    head = text[:500].lower()
    content_type = content_type.lower()

    if "rss" in content_type or "atom" in content_type or "xml" in content_type:
        return True

    return "<rss" in head or "<feed" in head


def discover_feed_links(page_url: str, html_text: str) -> list[str]:
    feeds: list[str] = []

    link_pattern = re.compile(
        r"""<link[^>]*?(?:type=["'](?:application/rss\+xml|application/atom\+xml|application/xml|text/xml)["'][^>]*?|rel=["'][^"']*alternate[^"']*["'][^>]*?)[^>]*?>""",
        re.I,
    )
    href_pattern = re.compile(r"""href=["']([^"']+)["']""", re.I)

    for match in link_pattern.finditer(html_text):
        href_match = href_pattern.search(match.group(0))
        if not href_match:
            continue

        feed_url = norm_url(href_match.group(1), page_url)
        if feed_url:
            feeds.append(feed_url)

    return feeds


def candidate_feed_urls(url: str) -> list[str]:
    parsed = urllib.parse.urlparse(url)
    base_url = f"{parsed.scheme}://{parsed.netloc}/"

    candidates = [url]
    for suffix in FEED_CANDIDATES:
        candidates.append(urllib.parse.urljoin(base_url, suffix))

    result: list[str] = []
    seen: set[str] = set()

    for item in candidates:
        item = norm_url(item)
        if not item or item in seen:
            continue
        seen.add(item)
        result.append(item)

    return result


def resolve_feed_url(source_url: str) -> tuple[str | None, str | None]:
    for candidate in candidate_feed_urls(source_url):
        try:
            text, content_type = fetch_url(candidate)
        except Exception:
            continue

        if looks_like_feed(text, content_type):
            return candidate, text

        if "text/html" in content_type.lower() or "<html" in text[:500].lower():
            for feed_url in discover_feed_links(candidate, text):
                try:
                    feed_text, feed_content_type = fetch_url(feed_url)
                except Exception:
                    continue

                if looks_like_feed(feed_text, feed_content_type):
                    return feed_url, feed_text

    return None, None


def text_of(node: ET.Element | None) -> str:
    if node is None or not node.text:
        return ""
    return strip_html(node.text)


def find_child(node: ET.Element, names: tuple[str, ...]) -> ET.Element | None:
    for child in list(node):
        local_name = child.tag.split("}")[-1].lower()
        if local_name in names:
            return child
    return None


def find_children(node: ET.Element, names: tuple[str, ...]) -> list[ET.Element]:
    result: list[ET.Element] = []

    for child in list(node):
        local_name = child.tag.split("}")[-1].lower()
        if local_name in names:
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

            if not link:
                link = norm_url(text_of(find_child(raw_item, ("id",))), feed_url)

        else:
            link = norm_url(text_of(find_child(raw_item, ("link",))), feed_url)

        if not link:
            link = norm_url(text_of(find_child(raw_item, ("guid",))), feed_url)

        date_raw = ""
        date_iso = ""

        for date_key in ("published", "updated", "pubdate", "date"):
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


def source_name_from_url(url: str) -> str:
    return urllib.parse.urlparse(url).netloc or url


def dedupe_and_sort(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    deduped: dict[str, dict[str, Any]] = {}

    for item in items:
        deduped[item["id"]] = item

    result = list(deduped.values())
    result.sort(key=lambda item: item.get("published_iso") or "", reverse=True)
    return result


def collect_items() -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    sources: list[dict[str, Any]] = []

    for url in extract_urls_from_markdown(SHARED_SOURCES_MD):
        sources.append(
            {
                "name": source_name_from_url(url),
                "url": url,
                "kind": "shared",
            }
        )

    sources.extend(load_extra_sources(EXTRA_SOURCES_JSON))

    unique_sources: list[dict[str, Any]] = []
    seen: set[str] = set()

    for source in sources:
        url = source["url"]
        if url in seen:
            continue
        seen.add(url)
        unique_sources.append(source)

    news_items: list[dict[str, Any]] = []
    owned_items: list[dict[str, Any]] = []
    source_reports: list[dict[str, Any]] = []

    for source in unique_sources:
        source_url = source["url"]
        source_name = source["name"]
        source_kind = str(source.get("kind", ""))

        print(f"[source] {source_name}: {source_url}")

        feed_url, feed_text = resolve_feed_url(source_url)

        if not feed_url or not feed_text:
            source_reports.append(
                {
                    "name": source_name,
                    "url": source_url,
                    "kind": source_kind,
                    "status": "failed",
                    "feed_url": "",
                    "items": 0,
                }
            )
            continue

        items = parse_feed(feed_url, feed_text, source_name)

        for item in items:
            item["source_kind"] = source_kind
            item["source_url"] = source_url

        source_reports.append(
            {
                "name": source_name,
                "url": source_url,
                "kind": source_kind,
                "status": "ok",
                "feed_url": feed_url,
                "items": len(items),
            }
        )

        if source_kind in OWNED_KINDS:
            owned_items.extend(items)
        else:
            news_items.extend(items)

        time.sleep(0.4)

    news_items = dedupe_and_sort(news_items)[:NEWS_MAX_ITEMS]
    owned_items = dedupe_and_sort(owned_items)[:OWNED_MAX_ITEMS]

    return news_items, owned_items, source_reports


def build_payload() -> dict[str, Any]:
    generated_at = utc_now()
    items, owned_items, source_reports = collect_items()

    content_hash = hashlib.sha256(
        json.dumps(
            {
                "items": items,
                "owned_items": owned_items,
            },
            ensure_ascii=False,
            sort_keys=True,
        ).encode("utf-8")
    ).hexdigest()

    return {
        "schema": "fivsevn.ai.news.v2",
        "generated_at": generated_at,
        "content_hash": f"sha256:{content_hash}",
        "purpose": "AI-readable news bundle for scheduled review and summarization.",
        "source_policy": {
            "shared_sources": "intake/sources.md",
            "extra_sources": "ai/sources_extra.json",
            "note": (
                "Shared sources are used for external news. Extra sources with "
                "kind=owned_site are separated into owned_items and do not compete "
                "with the external news item limit."
            ),
        },
        "limits": {
            "news_max_items": NEWS_MAX_ITEMS,
            "owned_max_items": OWNED_MAX_ITEMS,
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
            "sources_failed": sum(1 for source in source_reports if source.get("status") != "ok"),
            "items": len(items),
            "owned_items": len(owned_items),
        },
        "sources": source_reports,
        "items": items,
        "owned_items": owned_items,
    }


def render_markdown(payload: dict[str, Any]) -> str:
    lines: list[str] = []
    counts = payload.get("counts", {}) or {}
    limits = payload.get("limits", {}) or {}

    lines.append("# AI News")
    lines.append("")
    lines.append(f"- Generated at: `{payload.get('generated_at', '')}`")
    lines.append(f"- Content hash: `{payload.get('content_hash', '')}`")
    lines.append(f"- Sources: {counts.get('sources_ok', 0)} ok / {counts.get('sources_failed', 0)} failed")
    lines.append(f"- External items: {counts.get('items', 0)} / {limits.get('news_max_items', '')}")
    lines.append(f"- Owned items: {counts.get('owned_items', 0)} / {limits.get('owned_max_items', '')}")
    lines.append("")

    lines.append("## Sources")
    lines.append("")

    for source in payload.get("sources", []):
        kind = source.get("kind", "")
        if source.get("feed_url"):
            lines.append(
                f"- `{source.get('status', '')}` `{kind}` {source.get('name', '')} — "
                f"{source.get('items', 0)} items — {source.get('feed_url', '')}"
            )
        else:
            lines.append(
                f"- `{source.get('status', '')}` `{kind}` {source.get('name', '')} — "
                f"{source.get('url', '')}"
            )

    lines.append("")
    lines.append("## External Latest Items")
    lines.append("")

    for item in payload.get("items", []):
        append_item_markdown(lines, item)

    lines.append("")
    lines.append("## Owned Site Items")
    lines.append("")

    owned_items = payload.get("owned_items", [])
    if not owned_items:
        lines.append("_No owned site items found._")
        lines.append("")
    else:
        for item in owned_items:
            append_item_markdown(lines, item)

    return "\n".join(lines).strip() + "\n"


def append_item_markdown(lines: list[str], item: dict[str, Any]) -> None:
    lines.append(f"### {item.get('title', '(untitled)')}")
    lines.append("")
    lines.append(f"- ID: `{item.get('id', '')}`")
    lines.append(f"- Source: {item.get('source', '')}")

    if item.get("source_kind"):
        lines.append(f"- Source kind: `{item.get('source_kind', '')}`")

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
                "schema": "fivsevn.ai.latest_items.v2",
                "generated_at": payload.get("generated_at"),
                "content_hash": payload.get("content_hash"),
                "limits": payload.get("limits", {}),
                "items": payload.get("items", []),
                "owned_items": payload.get("owned_items", []),
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