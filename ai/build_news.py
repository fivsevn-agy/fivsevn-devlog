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

NEWS_MAX_ITEMS = 240
OWNED_MAX_ITEMS = 20
OWNED_KINDS = {"owned_site"}
FETCH_TIMEOUT = 20
REQUEST_DELAY_SECONDS = 0.4
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
    value = re.sub(r"(?is)<script\b[^>]*>.*?</script>", " ", value)
    value = re.sub(r"(?is)<style\b[^>]*>.*?</style>", " ", value)
    value = re.sub(r"(?s)<[^>]+>", " ", value)
    value = html.unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def norm_url(url: str, base: str | None = None) -> str:
    url = html.unescape(str(url or "")).strip()
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


def source_name_from_url(url: str) -> str:
    return urllib.parse.urlparse(url).netloc or url


def extract_urls_from_markdown(path: Path) -> list[str]:
    if not path.exists():
        print(f"[warn] missing shared sources file: {path}")
        return []

    text = path.read_text(encoding="utf-8", errors="replace")
    urls = re.findall(r"https?://[^\s\]\)>\"']+", text)

    result: list[str] = []
    seen: set[str] = set()
    for raw_url in urls:
        url = norm_url(raw_url.rstrip(".,;"))
        if not url or url in seen:
            continue
        seen.add(url)
        result.append(url)
    return result


def load_extra_sources(path: Path) -> list[dict[str, str]]:
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

    result: list[dict[str, str]] = []
    for item in sources:
        if not isinstance(item, dict):
            continue
        url = norm_url(str(item.get("url", "")))
        if not url:
            continue
        result.append(
            {
                "name": str(item.get("name") or source_name_from_url(url)),
                "url": url,
                "kind": str(item.get("kind") or "site"),
            }
        )
    return result


def looks_like_feed(text: str, content_type: str = "") -> bool:
    head = text[:1000].lower()
    content_type = content_type.lower()
    if "rss" in content_type or "atom" in content_type or "xml" in content_type:
        return True
    return "<rss" in head or "<feed" in head or "<rdf:rdf" in head


def html_attr(tag: str, attr_name: str) -> str:
    pattern = rf"\b{re.escape(attr_name)}=[\"']([^\"']+)[\"']"
    match = re.search(pattern, tag, re.I)
    return html.unescape(match.group(1)) if match else ""


def extract_feed_links(html_text: str, page_url: str) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()

    for match in re.finditer(r"<link\b[^>]*>", html_text, re.I):
        tag = match.group(0)
        rel = html_attr(tag, "rel").lower()
        link_type = html_attr(tag, "type").lower()
        href = html_attr(tag, "href")

        if "alternate" not in rel:
            continue
        if not any(token in link_type for token in ("rss", "atom", "xml")):
            continue

        feed_url = norm_url(href, page_url)
        if feed_url and feed_url not in seen:
            seen.add(feed_url)
            result.append(feed_url)

    return result


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
        if item and item not in seen:
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

        if "text/html" in content_type.lower() or "<html" in text[:1000].lower():
            for feed_url in extract_feed_links(text, candidate):
                try:
                    feed_text, feed_content_type = fetch_url(feed_url)
                except Exception:
                    continue
                if looks_like_feed(feed_text, feed_content_type):
                    return feed_url, feed_text

    return None, None


def local_name(node: ET.Element) -> str:
    return node.tag.split("}")[-1].lower()


def text_of(node: ET.Element | None) -> str:
    if node is None:
        return ""
    return strip_html("".join(node.itertext()))


def find_child(node: ET.Element, names: tuple[str, ...]) -> ET.Element | None:
    wanted = {name.lower() for name in names}
    for child in list(node):
        if local_name(child) in wanted:
            return child
    return None


def find_children(node: ET.Element, names: tuple[str, ...]) -> list[ET.Element]:
    wanted = {name.lower() for name in names}
    return [child for child in list(node) if local_name(child) in wanted]


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


def atom_entry_link(entry: ET.Element, feed_url: str) -> str:
    for link_node in find_children(entry, ("link",)):
        rel = (link_node.attrib.get("rel") or "alternate").lower()
        href = link_node.attrib.get("href") or ""
        if rel == "alternate" and href:
            return norm_url(href, feed_url)
    return norm_url(text_of(find_child(entry, ("id",))), feed_url)


def rss_item_link(item: ET.Element, feed_url: str) -> str:
    link = norm_url(text_of(find_child(item, ("link",))), feed_url)
    if link:
        return link
    return norm_url(text_of(find_child(item, ("guid",))), feed_url)


def parse_feed(feed_url: str, feed_text: str, fallback_source_name: str) -> list[dict[str, str]]:
    try:
        root = ET.fromstring(feed_text.encode("utf-8"))
    except ET.ParseError as error:
        print(f"[warn] failed to parse feed {feed_url}: {error}")
        return []

    root_name = local_name(root)
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

    items: list[dict[str, str]] = []
    for raw_item in raw_items:
        item_type = local_name(raw_item)
        title = text_of(find_child(raw_item, ("title",)))
        summary = text_of(
            find_child(raw_item, ("description", "summary", "content", "encoded"))
        )
        link = atom_entry_link(raw_item, feed_url) if item_type == "entry" else rss_item_link(raw_item, feed_url)

        date_raw = ""
        date_iso = ""
        for date_key in ("published", "updated", "pubdate", "date"):
            date_node = find_child(raw_item, (date_key,))
            if date_node is None:
                continue
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
                "title": title or "(untitled)",
                "url": link,
                "summary": summary,
                "published": date_raw,
                "published_iso": date_iso,
            }
        )

    return items


def dedupe_and_sort(items: list[dict[str, str]], limit: int) -> list[dict[str, str]]:
    deduped: dict[str, dict[str, str]] = {}
    for item in items:
        deduped[item["id"]] = item

    result = list(deduped.values())
    result.sort(key=lambda item: item.get("published_iso") or "", reverse=True)
    return result[:limit]


def collect_sources() -> list[dict[str, str]]:
    sources: list[dict[str, str]] = []

    for url in extract_urls_from_markdown(SHARED_SOURCES_MD):
        sources.append(
            {
                "name": source_name_from_url(url),
                "url": url,
                "kind": "shared",
            }
        )

    sources.extend(load_extra_sources(EXTRA_SOURCES_JSON))

    unique_sources: list[dict[str, str]] = []
    seen: set[str] = set()
    for source in sources:
        url = source["url"]
        if url in seen:
            continue
        seen.add(url)
        unique_sources.append(source)

    return unique_sources


def collect_items() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    news_items: list[dict[str, str]] = []
    owned_items: list[dict[str, str]] = []

    for source in collect_sources():
        source_url = source["url"]
        source_name = source["name"]
        source_kind = source.get("kind", "")

        print(f"[source] {source_name}: {source_url}")
        feed_url, feed_text = resolve_feed_url(source_url)
        if not feed_url or not feed_text:
            print(f"[warn] no feed found: {source_name}")
            continue

        items = parse_feed(feed_url, feed_text, source_name)
        for item in items:
            item["source_kind"] = source_kind
            item["source_url"] = source_url
            item["feed_url"] = feed_url

        if source_kind in OWNED_KINDS:
            owned_items.extend(items)
        else:
            news_items.extend(items)

        time.sleep(REQUEST_DELAY_SECONDS)

    return (
        dedupe_and_sort(news_items, NEWS_MAX_ITEMS),
        dedupe_and_sort(owned_items, OWNED_MAX_ITEMS),
    )


def build_payload() -> dict[str, Any]:
    items, owned_items = collect_items()
    return {
        "schema": "fivsevn.ai.news.v3",
        "generated_at": utc_now(),
        "purpose": "Daily news data for AI summarization. Use items and owned_items as the content source.",
        "source_policy": {
            "shared_sources": "intake/sources.md",
            "extra_sources": "ai/sources_extra.json",
        },
        "items": items,
        "owned_items": owned_items,
    }


def main() -> None:
    AI_DIR.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    NEWS_JSON.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"[done] generated {NEWS_JSON}")


if __name__ == "__main__":
    main()