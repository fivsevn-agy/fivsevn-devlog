# Daily News Radar
This directory contains the daily news reading surface for:
```text
devlog.fivsevn.com/news/
```

## Role

news/ is a lightweight daily intake surface.

It is used for reading current updates from selected RSS feeds. It does not serve as a note archive, research database, or canonical knowledge category.

Notes, reflections, and long-form writing derived from the news should be routed separately into the relevant devlog sections.

## Files

```
news/
├── README.md
├── feeds.yml
├── requirements.txt
├── build.py
└── index.html
```

## File roles

* feeds.yml defines the RSS sources and section structure.
* requirements.txt defines Python dependencies for the builder.
* build.py fetches RSS feeds and generates index.html.
* index.html is the public page served at /news/.

## Update model

The page is designed to be regenerated automatically.

Manual build:

pip install -r news/requirements.txt
python news/build.py

## Boundary

This page is for daily reading only.

It should not become a permanent content archive. The source list may evolve, but the page itself should remain simple, current-facing, and operational.
