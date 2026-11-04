---
id: devlog-readme
title: fivsevn-devlog

module: system
submodule: devlog
topic: null

type: index
status: active
canonical: true

summary: null

parents: []
related: []

tags: []

audience:
- self
- internal
languages:
- en

maturity: evolving
confidence: null

visibility: public
source_of_truth: devlog

filename_policy: entrypoint

created: null
updated: '2026-11-05'
metadata_updated: '2026-11-05'
---

# fivsevn-devlog

[System map](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/system-map.md)

Content and build source for [devlog.fivsevn.com](https://devlog.fivsevn.com/). Jekyll renders the note modules; a Python build overlays Fieldlog's static pages into the same GitHub Pages artifact.

## Content and publishing

| Path | Responsibility |
|---|---|
| `index.md` | Homepage artwork and links |
| `posts/` | Year/month publication packages, each with `index.md` and its own media or attachments |
| `natsci/`, `netcom/` | Topic-organized Markdown notes, translations and generated module directories |
| `natsci/fieldlog/` | Dated Fieldlog packages, image upload entry, publishing state and [guide](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/natsci/fieldlog/README.md) |
| `intake/` | News intake sources, generated intake page and its validation |
| `blogops/` | Manually maintained blog operations records |
| `now/`, `system-map.md` | Current state and repository map |
| `stills/`, `motion/`, `savour/` | Entry guides to the repositories that own those boards |
| `scripts/`, `schemas/`, `tests/` | Build tools, shared metadata copies and checks |

Edit notes in their module and push to `main`. First-level `_drafts/` notes are handled by the existing metadata completion workflow and do not independently trigger a deployment. The module-index updater preserves its declared manual sections. Do not use it to rewrite the operations log.

Before each Fieldlog upload, sync the latest `main` in Working Copy or GitHub Desktop. Save the shortcut's Images into this repository's full `natsci/fieldlog/trigger_imgs/` path, then commit and push to `main`. Each input becomes one editable package with optional commit-description text. The importer saves a WebP, publishes and verifies it, then clears only matching inbox originals. Saved Fieldlog titles, captions and publication controls can be edited in `index.md`.

Daily publishing adds normal commits and does not rewrite Git history. History cleanup is off by default and runs only through manual `workflow_dispatch` with `compact_image_history=true`. Keep original images and unpushed work backed up outside the repository. After that maintenance, realign or re-clone old local checkouts; do not merge the old history.

## Build and Actions

`Build and deploy devlog` checks out current main and the authoritative spec, normalizes and validates Fieldlog, imports pending uploads, refreshes module directories, runs Jekyll, overlays Fieldlog, and verifies source and generated links. It saves generated content and state together, deploys through GitHub Pages, verifies public entry points and image bytes, then clears only verified inbox originals.

The intake workflow compiles `intake/sources.md` with `intake/config.yml`, writes `index.html` and `llm-context.md` directly, and triggers a Pages rebuild after a successful run. The draft, intake and metadata workflows have separate responsibilities and remain active. Pages uses `_config.yml`, the existing layouts, and the custom domain in `CNAME`; Fieldlog must not disable Jekyll for the note modules.

```sh
python -m pip install -r scripts/requirements-fieldlog.txt -r intake/requirements.txt
python -m unittest discover -s tests -v
python -m unittest discover -s scripts -p 'test_fieldlog*.py' -v
python scripts/site_post_metadata.py check --site fieldlog --root natsci/fieldlog --schema-dir schemas
python scripts/media_naming.py check --site fieldlog --root natsci/fieldlog
python scripts/build_fieldlog.py
python scripts/build_fieldlog.py --check
```

The full Jekyll artifact is built and checked by Actions. `scripts/check_devlog_site.py` checks the combined website; `scripts/verify_fieldlog_live.py` compares Fieldlog's deployment receipt with the public pages and media.

The [spec repository](https://github.com/fivsevn-agy/fivsevn-spec) defines common frontmatter, the site-post profile and publication media names. Local helper/schema copies keep content checks offline. Both workflows read the pinned revision from [`.github/spec-ref`](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/.github/spec-ref); upgrade this pin and the local helper/schema copies together. Keep IDs and publication instants stable when editing saved packages; hidden and draft packages are omitted from public output.
