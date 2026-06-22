AI Collaboration Layer

This folder contains AI-facing files for fivsevn.

It is a stable coordination layer for AI collaborators, assistants, scheduled tasks, monitoring jobs, automation agents, and future machine-readable workflows.

The folder is broader than the daily news pipeline. It may contain any file that helps an AI understand, monitor, summarize, update, or operate parts of the fivsevn system.

Human-facing page design belongs elsewhere. This folder is for structured context, source data, operational briefs, and AI-readable references.

⸻

Purpose

Use this folder as the first place to look for AI-readable system context.

AI collaborators should prefer files in this folder over scraping rendered HTML pages when they need stable information about:

* system structure;
* content categories;
* repository responsibilities;
* source registries;
* generated news data;
* scheduled news updates;
* automation inputs;
* future AI collaboration instructions.

Rendered pages such as fivsevn.com and devlog.fivsevn.com are useful for understanding presentation, but they are not always the best source for machine-readable system context.

⸻

Current files

System context

* system-map.en.md — AI-facing operational brief for understanding the fivsevn system.
* system-map.md — canonical Chinese system map, if present.

These files are not part of the daily news generation pipeline. They exist so AI collaborators can understand the broader blog system.

Daily news data layer

* news.json — the only generated daily news data file.
* sources_extra.json — extra sources used only by the AI data layer.
* build_news.py — script that builds news.json.

The daily news pipeline intentionally produces only one data file. This keeps the system simple and prevents AI tasks from reading duplicate summaries or backend status reports.

⸻

Recommended AI entry points

For understanding the overall fivsevn system, read:

ai/system-map.en.md

For scheduled news summaries, read only:

ai/news.json

A daily briefing task should use only items and owned_items from news.json.

It should not summarize schema, generated_at, purpose, source_policy, build logs, missing feeds, or other operational details.

⸻

Source policy

The news source registry is shared with the existing intake system:

* Shared sources: intake/sources.md
* Extra AI-only sources: ai/sources_extra.json

The intake/ page and its visual design are not part of the AI data contract.

intake/ is the human-facing reading/source area; ai/ is the AI-facing coordination and data layer.

⸻

Generated files

Do not edit generated files manually:

* ai/news.json

Edit source files instead:

* intake/sources.md
* ai/sources_extra.json
* ai/build_news.py

⸻

Daily briefing behavior

The generated news file is a data source, not a finished article.

AI tasks that read news.json should produce a natural-language briefing in clear Chinese. They should not report backend fields, build status, source counts, hashes, or feed failures.

If owned_items is empty, the briefing should simply skip the self-site section. It should not say that no self-site content was captured.

⸻

Future use

This folder may later contain additional AI-facing files, such as:

* task-specific context packs;
* monitoring configuration;
* content routing rules;
* structured metadata exports;
* assistant prompts or operating briefs;
* summaries for external AI collaborators;
* automation state files;
* machine-readable indexes.

Files added here should be stable, explicit, and easy for AI systems to parse. Avoid using this folder for decorative page assets or human-only visual layout files.