---
id: netcom-module-map
title: netcom — Module Map
module: netcom
submodule: topology
topic: system-axis-definition
type: spec
status: active
canonical: true
summary: >
  Defines netcom as the communications, networks, protocols, and technical systems axis
  of fivsevn-devlog. Documents its subsystem-oriented structure, index behavior,
  draft policy, and routing boundaries.
parents:
  - system-map
related:
  - netcom-index
  - system-map
  - posts-module-map
  - natsci-module-map
tags:
  - netcom
  - topology
  - system-axis
  - communications
  - networks
  - protocols
  - auto-index
audience:
  - collaborator
languages:
  - en
  - zh
maturity: stable
confidence: 0.97
visibility: public
source_of_truth: devlog
created: 2026-02-28
updated: 2026-06-12
---

# netcom — Module Map

Purpose:

Define the internal structure and routing logic of the `netcom` module.

`netcom` is the technical system axis.

It is organized around communications, networks, protocols, computing systems, RF, embedded systems, and infrastructure-oriented technical thinking.

---

## 1. Structural Principle

Primary ordering logic:

- system-based;
- protocol-aware;
- infrastructure-oriented;
- engineering-facing;
- layered by technical domain.

Chronology is secondary.

A document belongs to `netcom` when its main organizing force is a technical system, network, protocol, signal chain, hardware/software architecture, or engineering method.

---

## 2. What Belongs Here

Route content to `netcom` when it involves:

- communications;
- networks;
- protocols;
- RF systems;
- LoRa;
- microcontrollers;
- embedded systems;
- computer science notes;
- AI model evaluation notes;
- digital systems;
- technical architecture;
- engineering methods;
- infrastructure analysis.

---

## 3. Current Structure

Current visible structure:

```text
netcom/
├── _drafts/
├── ai/
├── architecture/
├── assets/
├── cs/
├── digital/
├── lora/
├── math/
├── mcu/
├── methods/
├── protocol/
├── rf/
├── index.md
└── map.md
```

Interpretation:

- `ai/` contains AI-related technical notes;
- `architecture/` contains system architecture material;
- `cs/` contains computer-science-oriented notes;
- `digital/` contains digital-system material;
- `lora/` contains LoRa-related material;
- `math/` contains mathematical support notes;
- `mcu/` contains microcontroller material;
- `methods/` contains technical methods and workflows;
- `protocol/` contains protocol-oriented material;
- `rf/` contains radio-frequency material;
- `assets/` stores supporting media and is excluded from article indexing;
- `_drafts/` is a private buffer and is excluded from article indexing;
- `index.md` is the public-facing netcom landing page;
- `map.md` is this AI-facing routing and topology file.

---

## 4. Index Behavior

`netcom/index.md` is a human-facing landing page.

Its recent-note region is maintained by:

```text
scripts/update_module_indexes.py
```

The script updates the region marked by:

```md
<!-- AUTO-INDEX:NETCOM_RECENT:START -->
...
<!-- AUTO-INDEX:NETCOM_RECENT:END -->
```

Do not manually edit content inside this region.

Manual sections outside the auto-index markers may be edited normally.

---

## 5. Auto-Index Inclusion Rules

A Markdown file in `netcom/` may be listed in `netcom/index.md` if:

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

`netcom/_drafts/` is a private buffer.

Files inside `_drafts/` are never indexed, even if their frontmatter says:

```yaml
status: publish
```

Use `_drafts/` for unstable technical notes, scratch files, temporary experiments, and incomplete naming.

### `status: draft`

A file outside `_drafts/` with:

```yaml
status: draft
```

appears in `netcom/index.md` as plain text, without a link:

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

A document should remain in or route to `netcom` if its main axis is:

- communication system;
- protocol;
- RF / signal chain;
- embedded system;
- computing system;
- engineering architecture;
- technical method.

Do not route to `netcom` merely because a post mentions software, AI, devices, or technical terms.

Route to other modules when appropriate:

- `posts`: reflective essay or mixed personal note;
- `natsci`: organism, taxonomy, natural object, or natural-science observation;
- `blogops`: publishing workflow or repository operation;
- `system`: topology, metadata, routing, or governance;
- `intake`: generated daily input surface.

---

## 9. Stability Rule

`netcom` grows through:

- new technical subsystems;
- clearer protocol categories;
- engineering method refinement;
- infrastructure notes;
- accumulated system analysis.

It should not grow through temporary news clustering alone.

---

## 10. Minimal AI Rules

1. Treat `netcom` as the technical system axis.
2. Do not sort or understand it primarily by time.
3. Do not edit generated regions in `netcom/index.md`.
4. Do not index `map.md`.
5. Respect frontmatter as the source of display behavior.
6. Keep system, protocol, and infrastructure boundaries explicit.
