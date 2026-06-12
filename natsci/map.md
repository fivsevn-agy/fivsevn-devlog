---
id: natsci-module-map
title: natsci — Module Map
module: natsci
submodule: topology
topic: object-axis-definition
type: spec
status: active
canonical: true

summary: >
  Defines natsci as the natural-science object axis of fivsevn-devlog.
  Explains its taxonomy-driven structure, object-first routing logic,
  index behavior, draft policy, and boundary with posts and netcom.

parents:
  - system-map

related:
  - natsci-index
  - system-map
  - posts-module-map
  - netcom-module-map

tags:
  - natsci
  - topology
  - object-axis
  - taxonomy
  - natural-science
  - auto-index

audience:
  - collaborator

languages:
  - en
  - zh

maturity: stable
confidence: 0.98

visibility: public
source_of_truth: devlog

created: 2026-02-28
updated: 2026-06-12
---
# natsci — Module Map

Purpose:

Define the internal structure and routing logic of the `natsci` module.

`natsci` is the natural-science object axis.

It is organized primarily by natural objects, organisms, taxonomy, observation methods, and classification logic.

---

## 1. Structural Principle

Primary ordering logic:

- object-based;
- classification-driven;
- entity-first;
- taxonomy-aware;
- observation-grounded.

Chronology is secondary.

A document belongs to `natsci` when the main organizing force is a natural object, biological group, taxonomic problem, field observation, or natural-science method.

---

## 2. What Belongs Here

Route content to `natsci` when it involves:

- organisms;
- taxonomy;
- biological classification;
- field observation;
- specimen-oriented thinking;
- natural history;
- ecology notes;
- natural-science reading notes;
- observation and retrieval methods for natural-science material.

---

## 3. Current Structure

Current visible structure:

```text
natsci/
├── assets/
├── ethnobiology/
├── methods/
├── reading/
├── taxonomy/
├── index.md
└── map.md
```

Interpretation:

- `taxonomy/` contains classification- and organism-oriented material;
- `methods/` contains observation, retrieval, and research methods;
- `reading/` contains natural-science reading notes;
- `ethnobiology/` contains human-biota relation notes;
- `assets/` stores supporting media and is excluded from article indexing;
- `index.md` is the public-facing natsci landing page;
- `map.md` is this AI-facing routing and topology file.

---

## 4. Index Behavior

`natsci/index.md` is a human-facing landing page.

Its recent-note region is maintained by:

```text
scripts/update_module_indexes.py
```

The script updates the region marked by:

```md
<!-- AUTO-INDEX:NATSCI_RECENT:START -->
...
<!-- AUTO-INDEX:NATSCI_RECENT:END -->
```

Do not manually edit content inside this region.

Manual sections outside the auto-index markers may be edited normally.

---

## 5. Auto-Index Inclusion Rules

A Markdown file in `natsci/` may be listed in `natsci/index.md` if:

- it is a `.md` file;
- it is not `index.md`, `map.md`, or `README.md`;
- it is not inside an excluded directory;
- it has frontmatter;
- it has `title`;
- it has `created`, `date`, or `updated`;
- its `status` is visible.

Visible statuses:

```yaml
status: active
status: publish
status: published
status: draft
```

Hidden statuses:

```yaml
status: hidden
status: private
status: archived
status: archive
```

If `status` is missing, the file is not listed.

---

## 6. Draft Policy

There are two kinds of draft handling.

### `_drafts/`

If a `_drafts/` directory exists under `natsci/`, it is treated as a private buffer.

Files inside `_drafts/` are never indexed.

### `status: draft`

A file outside `_drafts/` with:

```yaml
status: draft
```

appears in `natsci/index.md` as plain text, without a link:

```md
- 2026.06.12 Note title（更新中）
```

Change it to `active`, `publish`, or `published` to make it a clickable entry.

---

## 7. Type Policy

If a note has:

```yaml
type: translation
```

the auto-index appends:

```text
（译文）
```

to the displayed title.

The legacy misspelling is also tolerated:

```yaml
type: traslation
```

Prefer the correct spelling going forward:

```yaml
type: translation
```

---

## 8. Boundary Rules

A document should remain in or route to `natsci` if its main axis is:

- organism;
- classification;
- natural object;
- biological observation;
- natural-science method.

Do not route to `natsci` merely because a post mentions an animal, plant, fossil, ecosystem, or scientific term.

Route to other modules when appropriate:

- `posts`: reflective essay or mixed personal note;
- `netcom`: communications, networks, protocols, or technical systems;
- `blogops`: publishing workflow or repository operation;
- `system`: topology, metadata, routing, or governance;
- `intake`: generated daily input surface.

---

## 9. Interaction With Other Axes

A document may have a temporal publication context and still belong structurally to `natsci`.

Example:

```text
temporal entry → posts-like surface
object structure → natsci
```

The structural axis has priority for canonical placement.

---

## 10. Stability Rule

`natsci` grows through:

- new objects;
- deeper classification;
- method refinement;
- observation records;
- stable natural-science reading clusters.

It should not grow through temporary topical clustering alone.

---

## 11. Minimal AI Rules

1. Treat `natsci` as the object / taxonomy axis.
2. Do not sort or understand it primarily by time.
3. Do not edit generated regions in `natsci/index.md`.
4. Do not index `map.md`.
5. Respect frontmatter as the source of display behavior.
6. Keep taxonomy and observation logic explicit.
