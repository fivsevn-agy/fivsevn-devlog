#!/usr/bin/env python3
from __future__ import annotations

import html
import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote

import requests

BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "data"
OUTPUT_JSON = OUTPUT_DIR / "daily_postcard.json"
OUTPUT_HTML = OUTPUT_DIR / "daily_postcard.html"

COMMONS_API = "https://commons.wikimedia.org/w/api.php"
HEADERS = {
    "User-Agent": "fivsevn-devlog-intake/1.0 (https://devlog.fivsevn.com/intake/)"
}


def commons_get(params: dict) -> dict:
    res = requests.get(COMMONS_API, params=params, headers=HEADERS, timeout=30)
    res.raise_for_status()
    return res.json()


def fetch_page_wikitext(title: str) -> str | None:
    data = commons_get(
        {
            "action": "query",
            "format": "json",
            "formatversion": "2",
            "prop": "revisions",
            "rvprop": "content",
            "rvslots": "main",
            "titles": title,
        }
    )
    pages = data.get("query", {}).get("pages", [])
    if not pages or pages[0].get("missing"):
        return None

    revisions = pages[0].get("revisions", [])
    if not revisions:
        return None

    slots = revisions[0].get("slots", {})
    main = slots.get("main", {})
    return main.get("content")


def clean_filename(value: str) -> str:
    value = value.strip()
    value = re.sub(r"^File:", "", value, flags=re.IGNORECASE).strip()
    value = value.replace("_", " ")
    return value


def extract_filename_from_wikitext(wikitext: str) -> str | None:
    if not wikitext:
        return None

    match = re.search(
        r"\{\{\s*Potd filename\s*\|\s*1\s*=\s*([^|}\n]+)",
        wikitext,
        flags=re.IGNORECASE,
    )
    if match:
        return clean_filename(match.group(1))

    match = re.search(
        r"\{\{\s*Potd filename\s*\|\s*([^|}\n]+)",
        wikitext,
        flags=re.IGNORECASE,
    )
    if match:
        first = match.group(1).strip()
        if "=" not in first:
            return clean_filename(first)

    match = re.search(r"(?:File|Image):([^\]|\n]+)", wikitext, flags=re.IGNORECASE)
    if match:
        return clean_filename(match.group(1))

    return None


def fetch_image_info(filename: str) -> dict | None:
    title = f"File:{filename}"
    data = commons_get(
        {
            "action": "query",
            "format": "json",
            "formatversion": "2",
            "prop": "imageinfo",
            "iiprop": "url|extmetadata",
            "titles": title,
        }
    )
    pages = data.get("query", {}).get("pages", [])
    if not pages or pages[0].get("missing"):
        return None

    imageinfo = pages[0].get("imageinfo", [])
    if not imageinfo:
        return None

    info = imageinfo[0]
    return {
        "filename": filename,
        "file_page_url": f"https://commons.wikimedia.org/wiki/File:{quote(filename.replace(' ', '_'), safe=':/_')}",
        "image_url": info.get("url"),
        "metadata": info.get("extmetadata", {}),
    }


def metadata_value(metadata: dict, key: str) -> str:
    value = metadata.get(key, {}).get("value", "")
    return re.sub(r"<[^>]+>", "", value).strip()


def fetch_postcard() -> dict:
    today = datetime.now(timezone.utc).date()
    last_error = None

    for delta in range(0, 10):
        day = today - timedelta(days=delta)
        template_title = f"Template:Potd/{day.isoformat()}"

        try:
            wikitext = fetch_page_wikitext(template_title)
            filename = extract_filename_from_wikitext(wikitext or "")
            if not filename:
                last_error = f"No filename found in {template_title}"
                continue

            image_info = fetch_image_info(filename)
            if not image_info or not image_info.get("image_url"):
                last_error = f"No image info returned for {filename}"
                continue

            metadata = image_info.get("metadata", {})
            title = metadata_value(metadata, "ObjectName") or filename
            description = metadata_value(metadata, "ImageDescription")
            license_short = metadata_value(metadata, "LicenseShortName")
            artist = metadata_value(metadata, "Artist")

            return {
                "date": day.isoformat(),
                "from": "Wikimedia Commons <picture-of-the-day@commons.wikimedia.org>",
                "to_name": "fivsevn",
                "to_email_prefix": "intake@",
                "to_domain": "devlog.fivsevn.com",
                "to_url": "https://devlog.fivsevn.com/",
                "subject": "You have one postcard waiting to be viewed! 你有一张明信片待查收！",
                "title": title,
                "description": description,
                "artist": artist,
                "license": license_short,
                "image_url": image_info["image_url"],
                "original_url": image_info["file_page_url"],
                "source": "Wikimedia Commons Picture of the Day",
                "generated_at": datetime.now(timezone.utc).isoformat(),
            }
        except Exception as exc:
            last_error = str(exc)
            continue

    raise RuntimeError(f"Failed to fetch Wikimedia Commons postcard: {last_error}")


def render_html(payload: dict) -> str:
    from_line = html.escape(payload["from"])
    date_line = html.escape(payload["date"])
    subject_line = html.escape(payload["subject"])
    image_url = html.escape(payload["image_url"], quote=True)
    original_url = html.escape(payload["original_url"], quote=True)
    title = html.escape(payload.get("title") or "Wikimedia Commons Picture of the Day")

    to_name = html.escape(payload["to_name"])
    to_email_prefix = html.escape(payload["to_email_prefix"])
    to_domain = html.escape(payload["to_domain"])
    to_url = html.escape(payload["to_url"], quote=True)

    return f'''<section id="daily-postcard" class="postcard-mail">
  <div class="postcard-header">
    <div><strong>From:</strong> {from_line}</div>
    <div><strong>To:</strong> {to_name} &lt;{to_email_prefix}<a href="{to_url}" target="_blank" rel="noopener noreferrer">{to_domain}</a>&gt;</div>
    <div><strong>Date:</strong> {date_line}</div>
    <div><strong>Subject:</strong> {subject_line}</div>
  </div>

  <p class="postcard-label">View postcard:</p>
  <a class="postcard-image-link" href="{original_url}" target="_blank" rel="noopener noreferrer">
    <img class="postcard-image" src="{image_url}" alt="{title}" loading="lazy">
  </a>
  <p class="postcard-original">Original: <a href="{original_url}" target="_blank" rel="noopener noreferrer">{original_url}</a></p>
</section>
'''


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    payload = fetch_postcard()

    OUTPUT_JSON.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    OUTPUT_HTML.write_text(render_html(payload), encoding="utf-8")
    print(f"Daily postcard: {payload['date']} - {payload['title']}")


if __name__ == "__main__":
    main()
