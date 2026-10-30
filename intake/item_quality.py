"""Shared, offline normalization for the HTML shelf and its LLM context."""
from __future__ import annotations

import calendar
import html
import re
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from typing import Any
from urllib.parse import unquote_plus, urlsplit, urlunsplit

UTC_MIN = datetime.min.replace(tzinfo=timezone.utc)
TRACKING_KEYS = {"fbclid", "gclid", "dclid", "msclkid", "mc_cid", "mc_eid"}


class TextExtractor(HTMLParser):
    BLOCKS = {"p", "div", "br", "li", "ul", "ol", "h1", "h2", "h3", "h4", "tr", "td", "blockquote", "hr"}
    HIDDEN = {"script", "style", "template", "iframe", "noscript"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.hidden: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in self.HIDDEN:
            self.hidden.append(tag)
        if not self.hidden and tag in self.BLOCKS:
            self.parts.append(" ")

    def handle_endtag(self, tag):
        if self.hidden:
            if tag == self.hidden[-1]:
                self.hidden.pop()
            return
        if tag in self.BLOCKS:
            self.parts.append(" ")

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


def clean_text(value: Any) -> str:
    """Decode common nested feed entities, remove markup and hidden content."""
    value = str(value or "")
    for _ in range(2):
        decoded = html.unescape(value)
        if decoded == value:
            break
        value = decoded
    parser = TextExtractor()
    parser.feed(value)
    parser.close()
    text = "".join(parser.parts)
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def clean_title(entry: Any) -> str:
    value = entry.get("title", "Untitled")
    if (entry.get("title_detail") or {}).get("type") == "text/plain":
        # A declared plain-text title can contain code such as vector<T>.
        # It is escaped at HTML output, not reinterpreted as markup here.
        for _ in range(2):
            value = html.unescape(str(value or ""))
        value = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", "", value)
        return re.sub(r"\s+", " ", value).strip()
    return clean_text(value)


def http_url(value: Any) -> str:
    value = str(value or "").strip()
    if re.search(r"[\x00-\x20\x7f]", value):
        return ""
    try:
        parts = urlsplit(value)
        if parts.scheme.lower() in {"http", "https"} and parts.hostname and not parts.username:
            _ = parts.port
            return value
    except ValueError:
        pass
    return ""


def article_key(url: str) -> str:
    """Only remove known tracking keys; retain IDs, versions, order and fragments.

    Do not equate hosts, HTTP/HTTPS, trailing slashes, or same-title articles.
    Unknown parameters (including ref/source) may select different content.
    """
    parts = urlsplit(url)
    query = []
    for part in parts.query.split("&") if parts.query else []:
        key = unquote_plus(part.partition("=")[0]).lower()
        if key.startswith("utm_") or key in TRACKING_KEYS:
            continue
        query.append(part)
    host = parts.netloc.lower()
    if (parts.scheme.lower() == "https" and host.endswith(":443")) or (parts.scheme.lower() == "http" and host.endswith(":80")):
        host = host.rsplit(":", 1)[0]
    return urlunsplit((parts.scheme.lower(), host, parts.path or "/", "&".join(query), parts.fragment))


def entry_date(entry: Any, field: str) -> datetime | None:
    value = entry.get(field)
    if isinstance(value, str) and re.match(r"^\d{4}-\d{2}-\d{2}(?:[Tt ]|$)", value.strip()):
        # feedparser normalizes impossible dates (February 31 -> March 2)
        # and assumes UTC for timezone-less ISO input. Reject those before
        # trusting its otherwise preferred parsed tuple.
        try:
            raw_dt = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
            if raw_dt.tzinfo is None:
                return None
        except ValueError:
            return None
    parsed = entry.get(f"{field}_parsed")
    if parsed:
        try:
            return datetime.fromtimestamp(calendar.timegm(parsed), timezone.utc)
        except (ValueError, TypeError, OverflowError, OSError):
            pass
    if not isinstance(value, str) or not value.strip():
        return None
    for parse in (lambda x: datetime.fromisoformat(x.replace("Z", "+00:00")), parsedate_to_datetime):
        try:
            dt = parse(value.strip())
            # A timezone-less timestamp cannot be turned into a precise UTC time.
            if dt.tzinfo is not None:
                return dt.astimezone(timezone.utc)
        except (ValueError, TypeError, OverflowError):
            pass
    return None


def publication_date(entry: Any) -> datetime | None:
    # feedparser aliases missing `published` to `updated` in get(); use a plain
    # dict so an Atom updated-only entry never becomes a publication date.
    values = dict(entry)
    return entry_date(values, "published") or entry_date(values, "created")


def item_sort_key(item: dict[str, Any]) -> tuple[datetime, datetime]:
    if item.get("is_source_link"):
        # Preserve the existing mixed shelf ordering without calling this a
        # publication date. URL cards still occupy their original shelf role.
        observed = item.get("observed_dt") or UTC_MIN
        return observed, observed
    primary = item.get("published_dt") or item.get("updated_dt") or UTC_MIN
    return primary, item.get("updated_dt") or primary


def deduplicate_sections(sections_data: dict[str, list[dict[str, Any]]]) -> None:
    """Collapse identical URLs per placement, preserve every source/category.

    Cross-category placements remain available in each category. Attributions
    are shared across those placements, including original URLs and scores.
    Homepage cards are never merged with articles or other registry entries.
    """
    provenance: dict[str, list[dict[str, Any]]] = {}
    for section, items in sections_data.items():
        for item in items:
            if item.get("is_source_link"):
                continue
            key = article_key(item["link"])
            item["article_key"] = key
            records = provenance.setdefault(key, [])
            origins = item.get("feed_origins") or [{
                "url": item["link"], "published": item.get("published", ""),
                "fetched": item.get("fetched", ""),
            }]
            for origin in origins:
                record = {
                    "source": item["source"], "section": section,
                    "region": item.get("region", ""), "url": origin["url"],
                    "source_meta": item.get("source_meta", {}),
                    "published": origin.get("published", ""),
                    "fetched": origin.get("fetched", ""),
                }
                if record not in records:
                    records.append(record)
    for section, items in sections_data.items():
        seen = set()
        result = []
        for item in sorted(items, key=item_sort_key, reverse=True):
            if not item.get("is_source_link"):
                key = item["article_key"]
                item["attributions"] = provenance[key]
                placement = (key, item.get("region", ""))
                if placement in seen:
                    continue
                seen.add(placement)
            result.append(item)
        sections_data[section] = result
