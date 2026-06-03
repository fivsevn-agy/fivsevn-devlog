#!/usr/bin/env python3
from __future__ import annotations

import html
import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import requests

BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "data"
OUTPUT_JSON = OUTPUT_DIR / "daily_postcard.json"
OUTPUT_HTML = OUTPUT_DIR / "daily_postcard.html"
COMMONS_API = "https://commons.wikimedia.org/w/api.php"
USER_AGENT = "fivsevn-devlog-intake/1.0 (https://devlog.fivsevn.com/intake/)"


def commons_get(params: dict[str, Any]) -> dict[str, Any]:
    response = requests.get(
        COMMONS_API,
        params={"format": "json", "formatversion": 2, **params},
        headers={"User-Agent": USER_AGENT},
        timeout=30,
    )
    response.raise_for_status()
    data = response.json()
    if "error" in data:
        raise RuntimeError(data["error"].get("info", "Commons API error"))
    return data


def get_potd_file_name(date_value: datetime) -> str:
    page = f"Template:Potd/{date_value:%Y-%m-%d}"
    data = commons_get(
        {
            "action": "parse",
            "page": page,
            "prop": "wikitext",
        }
    )
    wikitext = data["parse"]["wikitext"]
    file_name = re.sub(r"<!--.*?-->", "", wikitext, flags=re.S).strip()
    file_name = file_name.strip("[] ")
    file_name = re.sub(r"^:?\s*(File|Image):", "", file_name, flags=re.I).strip()
    if not file_name:
        raise RuntimeError(f"No Picture of the Day file found for {date_value:%Y-%m-%d}")
    return file_name


def get_image_info(file_name: str) -> dict[str, Any]:
    data = commons_get(
        {
            "action": "query",
            "titles": f"File:{file_name}",
            "prop": "imageinfo",
            "iiprop": "url|canonicaltitle|extmetadata",
            "iiurlwidth": 1200,
        }
    )
    pages = data["query"]["pages"]
    if not pages:
        raise RuntimeError(f"No Commons file page returned for {file_name}")

    page = pages[0]
    imageinfo = page.get("imageinfo") or []
    if not imageinfo:
        raise RuntimeError(f"No image info returned for {file_name}")

    info = imageinfo[0]
    extmetadata = info.get("extmetadata") or {}
    title = page.get("title", f"File:{file_name}")

    return {
        "title": title,
        "image_url": info.get("thumburl") or info.get("url"),
        "original_url": info.get("descriptionurl") or f"https://commons.wikimedia.org/wiki/{title.replace(' ', '_')}",
        "artist": clean_metadata(extmetadata.get("Artist", {}).get("value", "")),
        "license": clean_metadata(extmetadata.get("LicenseShortName", {}).get("value", "")),
    }


def clean_metadata(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value or "")
    value = re.sub(r"\s+", " ", value)
    return html.unescape(value).strip()


def fetch_postcard() -> dict[str, Any]:
    # Commons POTD templates are sometimes prepared in UTC with slight timing gaps.
    # Try today first, then walk backward for a recent available postcard.
    now = datetime.now(timezone.utc)
    last_error: Exception | None = None
    for days_back in range(0, 7):
        date_value = now - timedelta(days=days_back)
        try:
            file_name = get_potd_file_name(date_value)
            image_info = get_image_info(file_name)
            image_url = image_info.get("image_url")
            original_url = image_info.get("original_url")
            if not image_url or not original_url:
                raise RuntimeError("Commons image info did not include usable URLs.")
            return {
                "date": date_value.strftime("%Y-%m-%d"),
                "subject": "You have one postcard waiting to be viewed! 你有一张明信片待查收！",
                "from": "Wikimedia Commons <picture-of-the-day@commons.wikimedia.org>",
                "to": "fivsevn <intake@devlog.fivsevn.com>",
                "file_name": file_name,
                "title": image_info["title"],
                "image_url": image_url,
                "original_url": original_url,
                "artist": image_info.get("artist", ""),
                "license": image_info.get("license", ""),
                "generated_at": now.isoformat(),
            }
        except Exception as error:
            last_error = error
            continue
    raise RuntimeError(f"Failed to fetch Wikimedia Commons postcard: {last_error}")


def render_html(payload: dict[str, Any]) -> str:
    mail_from = html.escape(payload["from"])
    mail_to = html.escape(payload["to"])
    date = html.escape(payload["date"])
    subject = html.escape(payload["subject"])
    image_url = html.escape(payload["image_url"], quote=True)
    original_url = html.escape(payload["original_url"], quote=True)
    image_alt = html.escape(payload.get("title") or "Wikimedia Commons Picture of the Day", quote=True)

    return f'''<section id="daily-postcard" class="postcard-mail">
  <pre class="mail-header">From: {mail_from}
To: {mail_to}
Date: {date}
Subject: {subject}</pre>

  <p class="mail-label">View postcard:</p>

  <a class="postcard-image-link" href="{original_url}" target="_blank" rel="noopener noreferrer">
    <img class="postcard-image" src="{image_url}" alt="{image_alt}" loading="lazy">
  </a>

  <p class="postcard-original">Original: <a href="{original_url}" target="_blank" rel="noopener noreferrer">{original_url}</a></p>
</section>
'''


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    payload = fetch_postcard()
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    OUTPUT_HTML.write_text(render_html(payload), encoding="utf-8")
    print(f"[daily postcard] {payload['date']} — {payload['title']}")


if __name__ == "__main__":
    main()
