---
id: system-map
title: System Map — fivsevn AI Orientation and Topology

module: system
submodule: topology
topic: ai-orientation

type: spec
status: active
canonical: true

summary: >
  Single-file orientation map for AI collaborators entering the fivsevn system.
  Defines repository authority, public interfaces, structural topology,
  routing rules, map/index conventions, and publication boundaries.

parents: [system-ai-boot-protocol]
related: [system-module-map, system-prompt-routing, system-topology-overview-001, posts-module-map, natsci-module-map, netcom-module-map, blogops-module-map]

tags: [system, topology, ai-entry, routing, repository-boundary, index-map, automation]

audience: [collaborator]
languages: [en, zh]

maturity: stable
confidence: 0.97

visibility: public
source_of_truth: devlog

created: 2026-05-23
updated: 2026-06-15
---

# System Map — fivsevn AI Orientation and Topology

Purpose:

This file is the global orientation map for AI collaborators entering the fivsevn system.

Use it to quickly understand:

- which repositories exist;
- which repository has authority for what;
- how public interfaces relate to repositories;
- how the blog system is structurally organized;
- how to route tasks;
- how `index.md` and `map.md` differ;
- which files and generated surfaces should not be treated as canonical writing.

This file is a topology layer, not an article index.

Initialization behavior, if needed, is defined separately in:

- `/system/ai-boot-protocol.md`

---

## 0. Core Principle

The fivsevn system is:

- multi-repository;
- multi-interface;
- structurally layered;
- partially WordPress-presented;
- partially repository-backed;
- metadata-governed.

Primary rule:

```text
Do not infer structural authority from public appearance alone.
```

A public page, visual surface, asset repository, generated page, and canonical text archive may cooperate, but they do not have the same authority level.

---

## 1. Repository Authority

### 1.1 Canonical Text Archive

Repository:

```text
fivsevn-devlog
```

Role:

Primary long-form structured content archive.

Contains:

- `posts`
- `natsci`
- `netcom`
- `system`
- `blogops`
- `intake`
- `now`

Authority:

Canonical source for structured textual content, system-facing written records, and devlog-backed archive material.

Important:

- Do not assume every public page on `fivsevn.com` has a dedicated content axis here.
- Visual presentation pages may exist outside the canonical text archive structure.
- Generated operational surfaces are not automatically canonical articles.

---

### 1.2 Structural Specification

Repository:

```text
fivsevn-spec
```

Role:

Structural specification for the fivsevn system.

Defines:

- frontmatter schema;
- id rules;
- document conventions;
- controlled vocabulary;
- structural consistency rules.

Authority:

Canonical source for schema and structural-rule interpretation.

---

### 1.3 Static Assets

Repository:

```text
fivsevn-assets
```

Role:

Static asset repository.

Contains:

- images;
- photography assets;
- icons;
- static resources.

Authority:

No textual authority.

Important:

Assets may support public pages, but they do not define canonical textual meaning, metadata, or structural classification.

---

### 1.4 57store Subsystem

Repository:

```text
fivsevn-57store
```

Role:

Interactive narrative / experimental subsystem repository.

Contains:

- interactive HTML pages;
- mini-games;
- experimental interfaces;
- UI experiments;
- narrative subsystem assets.

Authority:

Canonical source for 57store-specific interface files and subsystem assets.

Boundary:

57store is a parallel subsystem, not a normal blog content axis.

---

### 1.5 Internal Control Layer

Repository:

```text
fivsevn-internal
```

Role:

Private operational and control layer.

Contains:

- AI configuration;
- operational scripts;
- rapid publishing workspace;
- internal workflow material.

Visibility:

Private.

Authority:

Operational authority only.

Important:

Do not cite or assume public availability unless explicitly provided in context.

---

## 2. Public Interfaces

### 2.1 Primary Blog Interface

Main presentation surface:

```text
fivsevn.com
```

Repository-backed archive interface:

```text
devlog.fivsevn.com
```

Interpretation:

```text
fivsevn.com + devlog.fivsevn.com
= two public surfaces of the primary blog system
```

They are related, but not identical:

- `fivsevn.com` is the main public presentation surface.
- `devlog.fivsevn.com` is the repository-backed archive interface.

---

### 2.2 Cognitive Content Axes

The current repository-backed cognitive axes are:

- `posts`
- `natsci`
- `netcom`

These axes contain canonical Markdown articles and notes.

They are maintained by frontmatter and partially surfaced through auto-generated `index.md` files.

---

### 2.3 Presentation Surfaces

Presentation surfaces expose content or assets but do not automatically become canonical text axes.

Current examples:

- `stills`
- `motion`

Rules:

- Stills is a still-image presentation surface.
- Motion is a moving-image / video presentation surface.
- Neither should be forced into `posts`, `natsci`, or `netcom` unless there is a separate canonical text article.

---

### 2.4 Intake

Repository path:

```text
intake/
```

Public interface:

```text
devlog.fivsevn.com/intake/
```

Role:

- daily external signal intake;
- RSS-backed information shelf;
- lightweight reading surface;
- current-facing feed.

Boundary:

```text
intake = daily input surface
not = permanent knowledge archive
not = cognitive content axis
not = source registry
```

Do not classify Intake items as canonical notes unless they are later rewritten or routed into `posts`, `natsci`, or `netcom`.

---

### 2.5 Now

Repository path:

```text
now/
```

Role:

Current status / now-page surface.

Boundary:

- `now/` is a public status page.
- It is not a long-form content axis.
- It should not be indexed as a normal article module.

---

### 2.6 57store Interfaces

57store is an interactive narrative / experimental subsystem.

Boundary:

- 57store is not part of the blog content axes.
- Do not classify 57store pages as `posts`, `natsci`, `netcom`, `blogops`, `stills`, or `motion`.

---

## 3. Repository Topology

```text
fivsevn system
│
├─ primary blog system
│  │
│  ├─ cognitive content axes
│  │  ├─ posts
│  │  ├─ natsci
│  │  └─ netcom
│  │
│  ├─ presentation surfaces
│  │  ├─ stills
│  │  └─ motion
│  │
│  ├─ operational surfaces
│  │  ├─ intake
│  │  └─ now
│  │
│  └─ meta-governance
│     └─ blogops
│
├─ kernel / protocol layer
│  └─ system
│     └─ system-map
│
├─ structural specification
│  └─ fivsevn-spec
│
├─ static asset layer
│  └─ fivsevn-assets
│
├─ parallel subsystem
│  └─ 57store
│
└─ private operational layer
   └─ fivsevn-internal
```

---

## 4. `index.md` and `map.md` Convention

### `index.md`

`index.md` is a human-facing landing page.

In the main content axes, it may contain:

- module introduction;
- public-facing notes;
- images;
- contact or section links;
- an auto-generated recent list.

For `posts`, `natsci`, and `netcom`, the recent list is generated by:

```text
scripts/update_module_indexes.py
```

The script updates only marked regions:

```text
<!-- AUTO-INDEX:...:START -->
...
<!-- AUTO-INDEX:...:END -->
```

Do not hand-edit generated regions.

---

### `map.md`

`map.md` is an AI-facing topology and routing file.

It explains:

- module purpose;
- structural principle;
- directory meaning;
- boundary rules;
- index-generation behavior;
- draft policy;
- routing rules.

`map.md` is not an article and must not be included in auto-generated article indexes.

---

### `system-map.md`

`system/system-map.md` is the global map.

It explains the whole system, not only one module.

Module-level `map.md` files should stay smaller and should not duplicate this file.

---

## 5. Auto-Index Policy

The auto-index script currently covers:

```text
posts/
natsci/
netcom/
```

It updates:

```text
posts/index.md
natsci/index.md
netcom/index.md
```

It does not automatically index:

- `system`
- `blogops`
- `intake`
- `now`
- assets
- generated operational files.

Core rules:

```text
status: active / publish / published
→ show as link

status: draft
→ show as text with （更新中）

status: hidden / private / archived
→ do not show

type: translation
→ append （译文） to title

original_url
→ prefer external URL as link target
```

Path-level exclusions include:

```text
assets/
_drafts/
posts/ai-discourse-analysis/
```

File-level exclusions include:

```text
index.md
map.md
README.md
```

---

## 6. Module Routing Rules

### Route to `posts`

Use `posts` for:

- personal notes;
- essays;
- reflections;
- updates;
- journal-like entries;
- mixed observations;
- material that has not grown into a stable independent domain.

---

### Route to `natsci`

Use `natsci` for:

- natural science;
- taxonomy;
- organisms;
- biological observation;
- specimen-oriented notes;
- field-note-derived structured writing.

---

### Route to `netcom`

Use `netcom` for:

- communications;
- networks;
- protocols;
- RF systems;
- computing systems;
- embedded systems;
- technical infrastructure;
- engineering notes.

---

### Route to `blogops`

Use `blogops` for:

- repository workflow;
- publishing rules;
- site operation;
- automation notes;
- editorial process;
- system evolution records.

---

### Route to `system`

Use `system` for:

- boot protocol;
- topology;
- routing rules;
- metadata interpretation;
- repository authority;
- structural governance.

---

### Route to `intake`

Use `intake` for:

- RSS source configuration;
- daily generated reading shelf;
- generated operational feed behavior.

Do not route canonical essays or notes to `intake`.

---

### Route to `now`

Use `now` for:

- current status;
- short present-state updates;
- now-page maintenance.

Do not route long-form notes to `now`.

---

## 7. Boundary Rules

### Public page vs content axis

A public page is not automatically a cognitive content axis.

```text
stills → presentation surface
motion → presentation surface
now → status surface
intake → input surface
```

---

### Asset source vs textual authority

An asset repository may supply images, icons, or static files.

It does not define canonical textual interpretation.

---

### Generated surface vs archive

Generated operational pages may be public, but they are not automatically archival writing.

```text
intake/index.html → generated output
not → canonical note
```

---

### Draft path vs draft status

`_drafts/` and `status: draft` are different.

```text
_drafts/
→ private buffer; excluded from index

status: draft
→ public preview; appears as text only if outside _drafts/
```

---

## 8. Minimal AI Working Rules

1. Read this file before classifying fivsevn work.
2. Treat `fivsevn-devlog` as the canonical structured text archive.
3. Treat `fivsevn-spec` as the structural schema source.
4. Treat `fivsevn-assets` as asset storage, not textual authority.
5. Treat `posts`, `natsci`, and `netcom` as the current cognitive content axes.
6. Treat `blogops` as meta-governance, not a public content axis.
7. Treat `system` as kernel/protocol/topology.
8. Treat `intake` as a generated daily input surface.
9. Treat `now` as a current-status surface.
10. Treat `map.md` as AI-facing topology, not article content.
11. Treat `index.md` as human-facing landing page.
12. Do not hand-edit auto-generated index regions.
13. Do not infer structural authority from public appearance alone.

---

## 9. Contact

Mail:

```text
fivsevn57@outlook.com
```
