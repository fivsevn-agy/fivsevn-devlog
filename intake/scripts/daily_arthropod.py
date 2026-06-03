import json
import random
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

import requests


# GBIF Backbone 里 Arthropoda 的 taxonKey。
# 如果以后不放心，也可以改成先用 /species/match?name=Arthropoda 查。
ARTHROPODA_KEY = 54

OUTPUT_DIR = Path("data")
OUTPUT_JSON = OUTPUT_DIR / "daily_arthropod.json"
OUTPUT_HTML = OUTPUT_DIR / "daily_arthropod.html"


def get_count() -> int:
    url = "https://api.gbif.org/v1/species/search"
    params = {
        "rank": "SPECIES",
        "higherTaxonKey": ARTHROPODA_KEY,
        "status": "ACCEPTED",
        "limit": 0,
    }

    res = requests.get(url, params=params, timeout=30)
    res.raise_for_status()
    data = res.json()

    return int(data["count"])


def fetch_random_species(count: int) -> dict:
    # GBIF search API 常见 limit 最大 100。
    # 这里一次取 20 条，再从里面随机一个，避免 offset 抽到空结果时太脆。
    limit = 20
    offset = random.randint(0, max(0, count - limit))

    url = "https://api.gbif.org/v1/species/search"
    params = {
        "rank": "SPECIES",
        "higherTaxonKey": ARTHROPODA_KEY,
        "status": "ACCEPTED",
        "limit": limit,
        "offset": offset,
    }

    res = requests.get(url, params=params, timeout=30)
    res.raise_for_status()
    data = res.json()

    results = data.get("results", [])
    if not results:
        raise RuntimeError("GBIF returned no species results.")

    # 过滤掉学名缺失、分类不完整的结果
    candidates = []
    for item in results:
        if not item.get("scientificName"):
            continue

        taxonomy_parts = [
            item.get("kingdom"),
            item.get("phylum"),
            item.get("class"),
            item.get("order"),
            item.get("family"),
        ]

        if all(taxonomy_parts):
            candidates.append(item)

    if not candidates:
        raise RuntimeError("No usable species found in this GBIF batch.")

    return random.choice(candidates)


def build_payload(item: dict) -> dict:
    usage_key = item.get("key") or item.get("usageKey")
    scientific_name = item["scientificName"]

    taxonomy = [
        item.get("kingdom"),
        item.get("phylum"),
        item.get("class"),
        item.get("order"),
        item.get("family"),
    ]

    taxonomy_text = " / ".join([x for x in taxonomy if x])

    google_query = urllib.parse.quote_plus(scientific_name)

    return {
        "title": "Daily Arthropod / 今日节肢动物",
        "scientific_name_label": "Scientific name / 学名",
        "scientific_name": scientific_name,
        "taxonomy_label": "Taxonomy / 分类",
        "taxonomy": taxonomy_text,
        "source_label": "Source / 来源",
        "source_name": "GBIF",
        "source_url": f"https://www.gbif.org/species/{usage_key}",
        "search_label": "Search / 搜索",
        "search_name": "Google",
        "search_url": f"https://www.google.com/search?q={google_query}",
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }


def render_html(payload: dict) -> str:
    return f"""<section class="daily-arthropod">
  <h2>{payload["title"]}</h2>

  <p>
    <strong>{payload["scientific_name_label"]}:</strong><br>
    <em>{payload["scientific_name"]}</em>
  </p>

  <p>
    <strong>{payload["taxonomy_label"]}:</strong><br>
    {payload["taxonomy"]}
  </p>

  <p>
    <strong>{payload["source_label"]}:</strong><br>
    <a href="{payload["source_url"]}" target="_blank" rel="noopener noreferrer">{payload["source_name"]}</a>
  </p>

  <p>
    <strong>{payload["search_label"]}:</strong><br>
    <a href="{payload["search_url"]}" target="_blank" rel="noopener noreferrer">{payload["search_name"]}</a>
  </p>
</section>
"""


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    count = get_count()

    # 多试几次，避免抽到分类不完整的条目
    last_error = None
    for _ in range(10):
        try:
            item = fetch_random_species(count)
            payload = build_payload(item)

            OUTPUT_JSON.write_text(
                json.dumps(payload, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            OUTPUT_HTML.write_text(render_html(payload), encoding="utf-8")
            print(f"Daily arthropod: {payload['scientific_name']}")
            return
        except Exception as exc:
            last_error = exc

    raise RuntimeError(f"Failed to generate daily arthropod: {last_error}")


if __name__ == "__main__":
    main()
