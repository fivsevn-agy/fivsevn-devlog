---
id: posts-module-map
title: posts — Module Map
module: posts
submodule: topology
topic: temporal-reflective-axis-definition
type: spec
status: active
canonical: true
summary: >
  Defines posts as the temporal and reflective content axis of fivsevn-devlog.
  Clarifies its role as the default essay, note, update, and mixed-observation pool,
  and documents index, draft, and routing behavior.
parents:
  - system-map
related:
  - posts-index
  - system-map
  - blogops-module-map
tags:
  - posts
  - topology
  - temporal-axis
  - reflective-axis
  - auto-index
  - routing
audience:
  - collaborator
languages:
  - en
  - zh
maturity: stable
confidence: 0.96
visibility: public
source_of_truth: devlog
created: 2026-02-28
updated: 2026-06-12
---

# posts — Module Map

Purpose:

Define the internal structure and routing logic of the `posts` module.

`posts` is the temporal / reflective axis of the repository.

It is the default long-form content pool for writing that is not structurally governed by a more specific object axis (`natsci`) or system axis (`netcom`).

---

## 1. Structural Principle

Primary ordering logic:

- time;
- reflection;
- essay sequence;
- personal observation;
- mixed-topic notes;
- project-facing updates.

`posts` is not organized by taxonomy or technical system hierarchy.

It is the general cognitive stream.

---

## 2. What Belongs Here

Route content to `posts` when it involves:

- essays;
- reflections;
- short-to-medium personal notes;
- reading reflections;
- public updates;
- project notes;
- mixed observations;
- writing that crosses multiple domains;
- material that has not yet developed into a stable independent axis.

If a topic later becomes structurally stable, it may be split out into another module or subsystem.

---

## 3. Current Structure

Current visible structure:

```text
posts/
├── 2019/
├── 2025/
├── 2026/
├── ai-discourse-analysis/
├── index.md
└── map.md
```

Interpretation:

- year directories contain time-based posts;
- `ai-discourse-analysis/` is currently excluded from the auto-index workflow;
- `index.md` is the public-facing posts landing page;
- `map.md` is this AI-facing routing and topology file.

---

## 4. Index Behavior

`posts/index.md` is a human-facing landing page.

Its recent-post region is maintained by:

```text
scripts/update_module_indexes.py
```

The script updates the region marked by:

```md
<!-- AUTO-INDEX:POSTS_RECENT:START -->
...
<!-- AUTO-INDEX:POSTS_RECENT:END -->
```

Do not manually edit content inside this region.

Manual sections outside the auto-index markers may be edited normally.

---

## 5. Auto-Index Inclusion Rules

A Markdown file in `posts/` may be listed in `posts/index.md` if:

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

If a `_drafts/` directory exists under `posts/`, it is treated as a private buffer.

Files inside `_drafts/` are never indexed.

### `status: draft`

A file outside `_drafts/` with:

```yaml
status: draft
```

appears in `posts/index.md` as plain text, without a link:

```md
- 2026.06.12 Post title（更新中）
```

Change it to `active`, `publish`, or `published` to make it a clickable entry.

---

## 7. WordPress / External Link Policy

Some older `posts` entries may use:

```yaml
original_url: https://...
```

If an article has `original_url` and a linkable status, the auto-index uses `original_url` as the target instead of the repository-local Markdown path.

This preserves older WordPress / Home Blog formatting where appropriate.

---

## 8. Type Policy

If a post has:

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

## 9. Boundary Rules

Do not route to `posts` if the content clearly belongs to:

- `natsci`: taxonomy, organisms, field observation, natural science objects;
- `netcom`: communications, networks, protocols, technical systems;
- `blogops`: publishing workflow, repository maintenance, editorial operations;
- `system`: topology, routing policy, metadata rules, boot protocol;
- `intake`: generated daily RSS / input surface;
- `now`: current status page;
- `57store`: interactive narrative / experimental subsystem.

When uncertain, `posts` is the default content axis, but only after checking whether another module has a stronger structural claim.

---

## 10. Minimal AI Rules

1. Treat `posts` as the temporal / reflective axis.
2. Do not treat `posts` as a catch-all for system governance or technical architecture.
3. Do not edit generated regions in `posts/index.md`.
4. Do not index `map.md`.
5. Respect frontmatter as the source of display behavior.
6. Use `original_url` when present for published external posts.
