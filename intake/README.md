# Daily Intake

This directory contains the daily intake surface for:

```text
devlog.fivsevn.com/intake/
```

## Role

`intake/` is a lightweight daily reading surface.

It collects selected RSS feeds, a postcard-style daily image from Wikimedia Commons, and a small daily field sample into one current-facing page. It is not a permanent note archive, research database, or canonical knowledge category.

Notes, reflections, and long-form writing derived from this page should be routed separately into the relevant devlog sections.

## Files

```text
intake/
├── README.md
├── feeds.yml
├── requirements.txt
├── build.py
├── index.html
├── scripts/
│   ├── daily_postcard.py
│   └── daily_field_sample.py
└── data/
    ├── daily_postcard.html
    ├── daily_postcard.json
    ├── daily_field_sample.html
    └── daily_field_sample.json
```

## File roles

- `feeds.yml` defines the RSS sources and section structure.
- `requirements.txt` defines Python dependencies for the intake builder.
- `scripts/daily_postcard.py` generates the postcard-style Wikimedia Commons Picture of the Day fragment.
- `scripts/daily_field_sample.py` generates the daily field sample from GBIF and search links.
- `data/daily_postcard.html` is the generated postcard HTML fragment inserted into the page.
- `data/daily_postcard.json` is the generated structured postcard data.
- `data/daily_field_sample.html` is the generated field sample HTML fragment inserted into the page.
- `data/daily_field_sample.json` is the generated structured field sample data.
- `build.py` fetches RSS feeds, loads the daily fragments, and generates `index.html`.
- `index.html` is the public page served at `/intake/`.

## Header model

The generated page uses a lightweight convenience-store/newspaper-stand frame:

```text
Courier on duty / 今日投递员：
GitHub Actions

Shift opened / 到店时间：
YYYY-MM-DD HH:MM UTC

On the shelf / 今日上架：
[section tags]
```

Operational notes stay in the footer so the top of the page reads like a daily arrival shelf rather than a project description.

## Update model

The page is designed to be regenerated automatically by GitHub Actions.

Manual build:

```bash
pip install -r intake/requirements.txt
python intake/scripts/daily_postcard.py
python intake/scripts/daily_field_sample.py
python intake/build.py
```

## Boundary

This page is for daily reading only.

It should remain simple, current-facing, and operational. The source list and daily modules may evolve, but the page should not become a permanent archive.
