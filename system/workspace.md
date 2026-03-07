---
id: workspace-entry
title: fivsevn Workspace (AI Entry)

module: system
submodule: workspace
topic: orientation-layer

type: index
status: active
canonical: false

summary: >
  AI orientation entry for the fivsevn system.
  Provides repository topology and public interface overview.
  This file is a navigation layer, not a boot protocol.

parents: [system-ai-boot-protocol]
related: [system-module-map]
tags: [workspace, ai-entry, navigation]

audience: collaborator
languages: en
maturity: evolving
confidence: 0.94
visibility: public
source_of_truth: devlog

created: 2026-02-20
updated: 2026-03-08
---

# fivsevn Workspace (AI Entry)

Purpose:

High-level orientation entry for AI.

This file provides a **system overview and navigation map**.

It is **not** responsible for initialization.

Initialization logic is defined in:

- /system/ai-boot-protocol.md

---

# 0. System Overview

The fivsevn system is:

- multi-repository
- multi-interface
- structurally layered

It consists of:

- a **primary blog system**
- optional **parallel subsystems**

---

# 1. Core Repositories

### Canonical Archive

Repository:

https://github.com/fivsevn-agy/fivsevn-devlog

Purpose:

Primary long-form structured content archive.

Contains:

- posts
- natsci
- netcom
- system
- blogops

---

### Structural Specification

Repository:

https://github.com/fivsevn-agy/fivsevn-spec

Defines:

- frontmatter schema
- id rules
- structural conventions

---

### 57store Subsystem Repository

Repository:

https://github.com/fivsevn/fivsevn-57store

Contains:

- interactive HTML pages
- mini-games
- experimental interfaces
- UI experiments
- narrative subsystem assets

---

### Static Assets

Repository:

https://github.com/fivsevn/fivsevn-assets

CDN:

https://cdn.jsdelivr.net/gh/fivsevn/fivsevn-assets/

Purpose:

Images and static resources.

No textual authority.

---

### Internal Control Layer (Private)

Repository:

https://github.com/fivsevn/fivsevn-internal

Contains:

- AI configuration
- post-by-mail console
- rapid publishing workspace
- operational scripts

Not public.

---

# 2. Public Interfaces

The system exposes multiple public interfaces.

---

## Blog System

Main presentation surface:

https://fivsevn.com

Repository-backed archive interface:

https://devlog.fivsevn.com

Presentation streams:

- https://fivsevn.com/posts
- https://fivsevn.com/foodie
- https://fivsevn.com/natsci

Important principle:
```
fivsevn.com  
+  
devlog.fivsevn.com  
```
represent **two surfaces of the same blog system**.

---

## 57store Subsystem

Interactive narrative / experimental subsystem.

Possible interfaces include:

Main-site interface:

https://fivsevn.com/57store

Interface pages:

- https://fivsevn.com/57store/sys
- https://fivsevn.com/57store/cctv

Repository-backed interface:

https://57store.fivsevn.com

Auxiliary narrative node:

https://57dayshift.wordpress.com

Important:

57store is **not part of the blog content axes**.

It operates as a **parallel subsystem**.

---

# 3. Structural Layers

Defined in:

/system/module-map.md

Layer summary:

Layer 1 — Cognitive Content

- posts
- natsci
- netcom

Layer 2 — Kernel

- system

Layer 3 — Meta Governance

- blogops

Parallel subsystem:

- 57store

---

# 4. Kernel Documents

System structure is defined by three kernel documents:

Boot protocol:

/system/ai-boot-protocol.md

Topology definition:

/system/module-map.md

Task routing:

/system/prompt-routing.md

These files define system structure and interpretation rules.

---

# 5. Assets

Static assets repository:

https://github.com/fivsevn/fivsevn-assets

CDN:

https://cdn.jsdelivr.net/gh/fivsevn/fivsevn-assets/

Images and icons only.

No content authority.

---

# 6. Contact

mail:

fivsevn0507@outlook.com