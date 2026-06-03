#!/usr/bin/env python3

from __future__ import annotations

import html
import json
import random
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests


BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "data"
OUTPUT_JSON = OUTPUT_DIR / "daily_arthropod.json"
OUTPUT_HTML = OUTPUT_DIR / "daily_arthropod.html"

# GBIF Backbone taxon key for Arthropoda.
ARTHROPODA_KEY = 54


def gbif_get(path: str, params: dict[str, Any]) -> dict[str, Any]:
    response = requests.get(
        f"https://api.gbif.org/v1{path}",
        params=params,
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


def get_species_count() -> int:
    data = gbif_get(
        "/species/search",
        {
            "highertaxon_key": ARTHROPODA_KEY,
            "rank": "SPECIES",
            "status": "ACCEPTED",
            "limit": 0,
        },
    )
    return int(data.get("count", 0))


def fetch_random_species(count: int) -> dict[str, Any]:
    limit = 20
    offset = random.randint(0, max(0, count - limit))

    data = gbif_get(
        "/species/search",
        {
            "highertaxon_key": ARTHROPODA_KEY,
            "rank": "SPECIES",
            "status": "ACCEPTED",
            "limit": limit,
            "offset": offset,
        },
    )

    candidates: list[dict[str, Any]] = []

    for item in data.get("results", []):
        taxonomy_parts = [
            item.get("kingdom"),
            item.get("phylum"),
            item.get("class"),
            item.get("order"),
            item.get("family"),
        ]

        if item.get("scientificName") and all(taxonomy_parts):
            candidates.append(item)

    if not candidates:
        raise RuntimeError("No usable arthropod species returned by GBIF.")

    return random.choice(candidates)


def build_payload(item: dict[str, Any]) -> dict[str, Any]:
    usage_key = item.get("key") or item.get("usageKey")
    scientific_name = item["scientificName"]

    taxonomy = " / ".join(
        [
            item["kingdom"],
            item["phylum"],
            item["class"],
            item["order"],
            item["family"],
        ]
    )

    google_query = urllib.parse.quote_plus(scientific_name)

    return {
        "title": "Daily Arthropod / 今日节肢动物",
        "scientific_name": scientific_name,
        "taxonomy": taxonomy,
        "source_name": "GBIF",
        "source_url": f"https://www.gbif.org/species/{usage_key}",
        "search_name": "Google",
        "search_url": f"https://www.google.com/search?q={google_query}",
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }


def render_html(payload: dict[str, Any]) -> str:
    title = html.escape(payload["title"])
    scientific_name = html.escape(payload["scientific_name"])
    taxonomy = html.escape(payload["taxonomy"])
    source_name = html.escape(payload["source_name"])
    source_url = html.escape(payload["source_url"], quote=True)
    search_name = html.escape(payload["search_name"])
    search_url = html.escape(payload["search_url"], quote=True)

    return f'''<section id="daily-arthropod" class="daily-arthropod">
  <h2>{title}</h2>

  <p>
    <strong>Scientific name / 学名:</strong><br>
    <em>{scientific_name}</em>
  </p>

  <p>
    <strong>Taxonomy / 分类:</strong><br>
    {taxonomy}
  </p>

  <p>
    <strong>Source / 来源:</strong><br>
    <a href="{source_url}" target="_blank" rel="noopener noreferrer">{source_name}</a>
  </p>

  <p>
    <strong>Search / 搜索:</strong><br>
    <a href="{search_url}" target="_blank" rel="noopener noreferrer">{search_name}</a>
  </p>
</section>
'''


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    count = get_species_count()
    if count <= 0:
        raise RuntimeError("GBIF returned zero accepted Arthropoda species.")

    last_error: Exception | None = None

    for _ in range(10):
        try:
            item = fetch_random_species(count)
            payload = build_payload(item)

            OUTPUT_JSON.write_text(
                json.dumps(payload, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            OUTPUT_HTML.write_text(render_html(payload), encoding="utf-8")

            print(f"[daily arthropod] {payload['scientific_name']}")
            return
        except Exception as error:
            last_error = error

    raise RuntimeError(f"Failed to generate daily arthropod: {last_error}")


if __name__ == "__main__":
    main()
