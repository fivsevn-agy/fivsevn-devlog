# AI Collaboration Layer

This folder contains AI-facing files for fivsevn.

It is a stable coordination layer for AI collaborators, assistants, scheduled tasks, monitoring jobs, automation agents, and future machine-readable workflows.

The folder is intentionally broader than the current daily news pipeline. It may contain any file that helps an AI understand, monitor, summarize, update, or operate parts of the fivsevn system.

Human-facing page design belongs elsewhere. This folder is for structured context, source data, operational briefs, and AI-readable references.

---

## Purpose

Use this folder as the first place to look for AI-readable system context.

AI collaborators should prefer files in this folder over scraping rendered HTML pages when they need stable information about:

- system structure;
- content categories;
- repository responsibilities;
- source registries;
- generated data bundles;
- scheduled news updates;
- automation inputs;
- future AI collaboration instructions.

Rendered pages such as `fivsevn.com` and `devlog.fivsevn.com` are useful for understanding presentation, but they are not always the best source for machine-readable system context.

---

## Current files

### System context

- `system-map.md` — canonical Chinese system map for fivsevn. Explains public entry points, page sections, content categories, repository responsibilities, and AI collaboration rules.
- `system-map.en.md` — English AI-facing operational brief. This is the recommended file to give to any AI collaborator that needs to understand the whole fivsevn structure quickly.

### Daily news / intake data layer

- `news.json` — primary machine-readable news bundle.
- `news.md` — human-readable and AI-readable news digest.
- `latest-items.json` — simplified item list for diffing and monitoring.
- `sources_extra.json` — extra sources used only by the AI data layer.
- `build_news.py` — script that builds the AI-readable news files.

---

## Recommended AI entry points

For understanding the overall fivsevn system, read:

```text
https://raw.githubusercontent.com/fivsevn-agy/fivsevn-devlog/refs/heads/main/ai/system-map.en.md
```

Canonical Chinese version:

```text
https://raw.githubusercontent.com/fivsevn-agy/fivsevn-devlog/refs/heads/main/ai/system-map.md
```

For scheduled news updates or source monitoring, read:

```text
https://raw.githubusercontent.com/fivsevn-agy/fivsevn-devlog/refs/heads/main/ai/news.json
```

Fallback rendered path:

```text
https://devlog.fivsevn.com/ai/news.json
```

---

## Source policy

The news source registry is shared with the existing intake system:

- Shared sources: `intake/sources.md`
- Extra AI-only sources: `ai/sources_extra.json`

The `intake/` page and its visual design are not part of the AI data contract. `intake/` is the human-facing reading/source area; `ai/` is the AI-facing coordination and data layer.

---

## Generated files

Do not edit generated files manually:

- `ai/news.json`
- `ai/news.md`
- `ai/latest-items.json`

Edit source files instead:

- `intake/sources.md`
- `ai/sources_extra.json`
- `ai/build_news.py`

---

## Future use

This folder may later contain additional AI-facing files, such as:

- task-specific context packs;
- monitoring configuration;
- content routing rules;
- structured metadata exports;
- assistant prompts or operating briefs;
- summaries for external AI collaborators;
- automation state files;
- machine-readable indexes.

Files added here should be stable, explicit, and easy for AI systems to parse. Avoid using this folder for decorative page assets or human-only visual layout files.
