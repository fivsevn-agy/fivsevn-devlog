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
  routing rules, boundary rules, and expansion principles.

parents: [system-ai-boot-protocol]
related: [system-module-map, system-prompt-routing, system-topology-overview-001, workspace-entry, intake]
tags: [system, topology, ai-entry, routing, workspace, interface-boundary, intake]

audience: collaborator
languages: en
maturity: stable
confidence: 0.97
visibility: public
source_of_truth: devlog

created: 2026-05-23
updated: 2026-06-03
---

# System Map — fivsevn AI Orientation and Topology

Purpose:

This file is the single orientation map for AI collaborators entering the fivsevn system.

Use it to quickly understand:

- which repositories exist
- which repository has authority for what
- how public interfaces relate to repositories
- how the blog system is structurally organized
- how to route tasks
- which surfaces, assets, and subsystems must not be conflated

This file is a navigation and topology layer.

Initialization behavior, if needed, is defined separately in:

- `/system/ai-boot-protocol.md`

---

# 0. Core Principle

The fivsevn system is:

- multi-repository
- multi-interface
- structurally layered
- partially WordPress-presented
- partially repository-backed

Primary rule:

```text
Do not infer structural authority from public appearance alone.
```

A public page, visual surface, asset repository, and canonical text archive may cooperate, but they do not have the same authority level.

---

# 1. Repository Map and Authority

## 1.1 Canonical Text Archive

Repository:

- `https://github.com/fivsevn-agy/fivsevn-devlog`

Role:

Primary long-form structured content archive.

Contains:

- `posts`
- `natsci`
- `netcom`
- `system`
- `blogops`

Authority:

Canonical source for structured textual content, system-facing written records, and devlog-backed archive material.

Important:

- Do not assume every public page on `fivsevn.com` has a dedicated content axis here.
- Visual presentation pages may exist outside the canonical text archive structure.

---

## 1.2 Structural Specification

Repository:

- `https://github.com/fivsevn-agy/fivsevn-spec`

Role:

Structural specification for the fivsevn system.

Defines:

- frontmatter schema
- id rules
- document conventions
- structural consistency rules

Authority:

Canonical source for schema and structural-rule interpretation.

---

## 1.3 Static Assets

Repository:

- `https://github.com/fivsevn/fivsevn-assets`

CDN:

- `https://cdn.jsdelivr.net/gh/fivsevn/fivsevn-assets/`

Role:

Static asset repository.

Contains:

- images
- photography assets
- icons
- static resources

Used by:

- blog visual presentation
- still-image pages
- interface assets
- public static resource delivery

Authority:

No textual authority.

Important:

Assets may support public pages, but they do not define canonical textual meaning, metadata, or structural classification.

---

## 1.4 57store Subsystem Repository

Repository:

- `https://github.com/fivsevn/fivsevn-57store`

Role:

Interactive narrative / experimental subsystem repository.

Contains:

- interactive HTML pages
- mini-games
- experimental interfaces
- UI experiments
- narrative subsystem assets

Authority:

Canonical source for 57store-specific interface files and subsystem assets.

Important:

57store is a parallel subsystem, not a normal blog content axis.

---

## 1.5 Internal Control Layer

Repository:

- `https://github.com/fivsevn/fivsevn-internal`

Role:

Private operational and control layer.

Contains:

- AI configuration
- post-by-mail console
- rapid publishing workspace
- operational scripts

Visibility:

Private.

Authority:

Operational authority only.

Important:

Do not cite or assume public availability unless explicitly provided in context.

---

# 2. Public Interfaces

The system exposes several public surfaces.

## 2.1 Primary Blog Interface

Main presentation surface:

- `https://fivsevn.com`

Repository-backed archive interface:

- `https://devlog.fivsevn.com`

Presentation streams:

- `https://fivsevn.com/posts`
- `https://fivsevn.com/foodie`
- `https://fivsevn.com/natsci`
- `https://fivsevn.com/stills`
- `https://fivsevn.com/motion`

Interpretation:

```text
fivsevn.com + devlog.fivsevn.com
= two public surfaces of the primary blog system
```

They are related, but not identical:

- `fivsevn.com` is the main public presentation surface.
- `devlog.fivsevn.com` is the repository-backed archive interface.

---

## 2.2 Stills

Stills is a main-site photography presentation surface.

Interface:

- `https://fivsevn.com/stills`

Role:

- curated photography presentation
- still-image archive surface
- visual entry for photo rolls and image sets

Operational model:

```text
fivsevn-assets → image source
WordPress page → visual presentation
fivsevn.com/stills → public interface
```

Boundary:

- Stills belongs to the primary blog public interface.
- Stills is not a canonical text axis in `fivsevn-devlog`.
- Stills is not part of the 57store subsystem.
- Stills is not a generic media library.

---

## 2.3 Motion

Motion is a main-site moving-image / video presentation surface.

Interface:

- `https://fivsevn.com/motion`

Role:

- curated motion-image presentation
- video / moving-frame archive surface
- visual entry for clips, sequences, and motion studies

Operational model:

```text
fivsevn-assets or external media source → motion asset source
WordPress page → visual presentation
fivsevn.com/motion → public interface
```

Boundary:

- Motion belongs to the primary blog public interface.
- Motion is not a canonical text axis in `fivsevn-devlog`.
- Motion is not part of the 57store subsystem.
- Motion is not a generic media library.
- Motion should not be conflated with Stills; Stills is still-image presentation, Motion is moving-image presentation.

---

## 2.4 57store Interfaces

57store is an interactive narrative / experimental subsystem.

Possible interfaces:

- `https://fivsevn.com/57store`
- `https://fivsevn.com/57store/sys`
- `https://fivsevn.com/57store/cctv`
- `https://57store.fivsevn.com`
- `https://57dayshift.wordpress.com`

Boundary:

57store is not part of the blog content axes.

It operates as a parallel subsystem.

Do not classify 57store pages as `posts`, `natsci`, `netcom`, `blogops`, or `stills`.



## 2.5 Intake

Intake is a repository-backed daily input surface.

Interface:

- `https://devlog.fivsevn.com/intake/`

Repository path:

- `fivsevn-devlog/intake/`

Role:

- daily external signal intake
- RSS-backed information shelf
- lightweight reading surface
- current-facing news / science / ideas / arts feed
- non-archival awareness interface

Operational model:

```text
RSS sources → GitHub Actions → generated static HTML → devlog.fivsevn.com/intake/
```

Boundary:

- Intake belongs to the repository-backed archive interface.
- Intake is not a cognitive content axis.
- Intake is not a canonical note archive.
- Intake does not replace `posts`, `natsci`, or `netcom`.
- Items seen through Intake may later be routed into canonical axes only after they become notes, reflections, observations, or structured writing.
- Intake should be treated as an operational reading surface, not as a source of structural authority.

Interpretation:

```text
intake = daily input surface
not → permanent knowledge archive
not → content axis
not → source registry
```

---

# 3. Structural Topology

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
│  ├─ operational intake surface
│  │  └─ intake
│  │
│  └─ meta-governance
│     └─ blogops
│
├─ kernel / protocol layer
│  └─ system
│     ├─ ai-boot-protocol
│     └─ system-map
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

# 4. Structural Layers

## 4.1 Layer 1 — Cognitive Content Axes

World-facing knowledge layer of the blog system.

These axes are cognitive orientations, not menu labels.

### posts

Temporal / reflective axis.

Typical content:

- essays
- reflections
- journal-like entries
- mixed observations
- project notes

中文注释：

`posts` 是默认内容池。只有当某类内容规模足够大，并形成稳定方法论时，才可以从 `posts` 中分化出新的轴。

### natsci

Object-oriented domain.

Focus:

- natural science
- taxonomy
- biological observation
- field notes
- specimen-oriented thinking

### netcom

System-oriented domain.

Focus:

- communications
- networks
- protocols
- engineering systems
- technical infrastructure

---

## 4.2 Layer 2 — Kernel / Protocol

Rules of the system itself.

Module:

- `system`

Responsibilities:

- boot protocol
- topology definition
- routing policy
- metadata interpretation
- structural conventions
- interface boundary clarification

This layer does not contain world-facing content.

---

## 4.3 Layer 3 — Meta-Governance

Documentation about how the system evolves.

Module:

- `blogops`

Responsibilities:

- structural adjustments
- publishing strategy changes
- architecture notes
- operational logs
- system evolution records

`blogops` is meta-level documentation, not a knowledge axis.

---

## 4.4 Presentation Surfaces

Public-facing pages that present content or assets without becoming canonical text axes.

Current presentation surfaces:

- `stills`
- `motion`

Rule:

A visual page is not automatically a cognitive axis.

---

## 4.5 Parallel Subsystems

Components outside the blog content axes and outside ordinary presentation surfaces.

Current subsystem:

- `57store`

Typical characteristics:

- fictional store-world interfaces
- system-style UI pages
- CCTV-style pages
- mini-games
- experimental interactive pages
- playful or atmospheric presentation layers
- project-like UI experiments

中文注释：

`57store` 是互动 / 叙事 / 实验子系统，不属于 `posts / natsci / netcom`。

---

# 5. Prompt Routing Rules

Routing priority:

```text
Layer detection
→ module routing
→ presentation-surface routing
→ subsystem override
```

Meaning:

1. Identify the structural layer or interface class.
2. Route to the correct module if it belongs to a canonical layer.
3. If the request concerns a public presentation surface, route to that surface.
4. If the request clearly belongs to a subsystem, route to the subsystem instead of forcing it into blog axes.

---

## 5.1 Route to posts

If the task involves:

- reflection
- updates
- personal thinking
- essay-like writing
- mixed observation
- journal-style material

Route to:

- `posts`

---

## 5.2 Route to natsci

If the task involves:

- biological entities
- taxonomy
- natural science observation
- specimen description
- field-note style natural observation

Route to:

- `natsci`

---

## 5.3 Route to netcom

If the task involves:

- communications
- networking
- protocols
- hardware / software systems
- infrastructure architecture

Route to:

- `netcom`

---

## 5.4 Route to system

If the task involves:

- boot sequence
- topology definition
- module map
- routing policy
- frontmatter schema
- metadata interpretation
- repository boundary clarification

Route to:

- `system`

---

## 5.5 Route to blogops

If the task involves:

- system evolution
- publishing workflow
- structural adjustments
- methodology notes
- operational documentation

Route to:

- `blogops`

---

## 5.6 Route to stills

If the task involves:

- `fivsevn.com/stills`
- photography feature layout
- photo-roll presentation
- visual archive presentation
- WordPress-edited photography page
- image display sourced from `fivsevn-assets`

Route to:

- `main blog presentation surface: stills`

Rules:

- Use `fivsevn-assets` for image/static asset source questions.
- Treat WordPress as the page presentation layer.
- Route to `posts` only if the task explicitly asks for a canonical textual post.
- Never route Stills to 57store.

---

## 5.7 Route to motion

If the task involves:

- `fivsevn.com/motion`
- motion-image feature layout
- video / moving-frame presentation
- clip archive presentation
- WordPress-edited motion page
- moving-image assets or embedded media

Route to:

- `main blog presentation surface: motion`

Rules:

- Use the relevant asset/media source for motion/static resource questions.
- Treat WordPress as the page presentation layer.
- Route to `posts` only if the task explicitly asks for a canonical textual post.
- Never route Motion to 57store.
- Never conflate Motion with Stills.

---

## 5.8 Route to 57store

If the task involves:

- fictional store-world UI
- 57store sys interface
- CCTV-style page
- mini-game
- interactive HTML page
- in-world dialogue or script
- boot capsule
- experimental interface elements

Route to:

- `57store subsystem`

Rule:

Do not force 57store material into `posts`.

---

# 6. Boundary Rules

Use these rules when classification is ambiguous.

## 6.1 Public page vs content axis

A public page is not automatically a Layer 1 cognitive axis.

Example:

```text
stills → presentation surface
motion → presentation surface
not → cognitive content axis
```

---

## 6.2 Asset source vs textual authority

An asset repository may supply images, icons, or static files.

It does not define canonical textual interpretation.

Example:

```text
fivsevn-assets → image/static asset source
not → textual source of truth
```

---

## 6.3 Public interface vs subsystem

A public page belongs to a subsystem only if it follows that subsystem's independent logic.

Example:

```text
57store/sys → 57store subsystem
stills → main blog presentation surface
motion → main blog presentation surface
```

---

## 6.4 Repository-backed archive vs WordPress presentation

Repository-backed archive and WordPress presentation may expose related material, but their authority differs.

Example:

```text
fivsevn-devlog → canonical structured text
fivsevn.com → public presentation
```

---

# 7. Expansion Rules

## 7.1 New Cognitive Content Axis

A new Layer 1 axis may emerge only if it:

- develops stable methodology
- has independent structural logic
- is sustainable long-term
- is not merely a temporary topic cluster
- is not merely a visual interface or presentation page

Pattern:

```text
posts → large domain → stable methodology → new axis
```

---

## 7.2 New Presentation Surface

A new presentation surface may be created if it:

- exposes existing content or assets through a specific public interface
- has visual or navigational identity
- does not require a new cognitive methodology
- does not claim canonical textual authority

Pattern:

```text
asset/content source + public presentation layer → presentation surface
```

Current examples:

```text
fivsevn-assets + WordPress page → stills
motion asset source + WordPress page → motion
```

---

## 7.3 New Parallel Subsystem

A subsystem may emerge if it:

- operates with a different structural logic than the blog archive
- contains interactive, narrative, or experimental interfaces
- may require different repositories or platforms
- should not be forced into existing content axes or presentation surfaces

Current example:

```text
57store
```

---

# 8. Minimal AI Working Rules

For blank AI collaborators:

1. Use this file to orient yourself before classifying fivsevn work.
2. Treat `fivsevn-devlog` as the canonical structured text archive.
3. Treat `fivsevn-spec` as the structural schema/specification source.
4. Treat `fivsevn-assets` as static and visual asset storage, not textual authority.
5. Treat `/stills/` as a WordPress-presented photography feature using assets from `fivsevn-assets`.
6. Treat `/motion/` as a WordPress-presented moving-image feature using its relevant asset or media source.
7. Treat 57store as a parallel subsystem, not part of the primary blog content axes.
8. Do not infer repository structure from public page appearance alone.
9. Do not classify visual or motion feature pages as canonical modules unless explicit structure says so.
10. Treat `/intake/` as a repository-backed daily input surface generated from RSS feeds by GitHub Actions; do not classify it as a cognitive content axis or permanent note archive.

---

# 9. Contact

Mail:

- `fivsevn57@outlook.com`
