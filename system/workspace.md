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
  AI 结构级入口文件。
  提供系统多仓库拓扑概览，
  指向 boot protocol 与 spec 层，
  用于高层导航而非初始化流程。

parents: [system-ai-boot-protocol]
related: [system-module-map]
tags: [workspace, ai-entry, navigation]

audience: collaborator
languages: en
maturity: evolving
confidence: 0.92
visibility: public
source_of_truth: devlog

created: 2026-02-20
updated: 2026-03-01
---
# fivsevn Workspace (AI Entry)

Purpose:
High-level orientation entry for AI. This is **not** a boot protocol.

Boot sequence is defined in:
- [/system/ai-boot-protocol.md](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/system/ai-boot-protocol.md)

---
## 0. System Overview

The fivsevn system is multi-repository and **layered**.

### Core repositories / layers
- Canonical archive (devlog): long-form structured content base
- Structural specification (spec): schema & writing rules
- Kernel layer (system): boot / topology / routing / structural rules
- Meta-governance layer (blogops): evolution log & methodology notes
- Static assets (assets): images/icons, no textual authority
- Internal control layer (internal): operational scripts (private)

### Public interfaces
- Main site: https://fivsevn.com
- Streams: https://fivsevn.com/posts, https://fivsevn.com/foodie, https://fivsevn.com/natsci
- Narrative interfaces (57store side-system): https://fivsevn.com/57store and related pages

Do not assume single-repo architecture.

---
## 1. Canonical Archive (Authoritative Content)

Repository:
- https://github.com/fivsevn-agy/fivsevn-devlog

This is the long-form structured content base.

---
## 2. Structural Definition Layer (Spec)

Spec repository:
- https://github.com/fivsevn-agy/fivsevn-spec

Defines:
- frontmatter schema
- id rules
- graph structure

---
## 3. Kernel Layer (System)

In devlog:
- /system/ai-boot-protocol.md
- /system/module-map.md
- /system/prompt-routing.md

This layer defines structure and routing rules.
It is not domain content.

---
## 4. Meta-Governance Layer (Blogops)

Blogops module:
- (public-facing) blogops pages / index
- (content) blogops documents in devlog

This layer documents:
- structural adjustments
- publishing strategy changes
- system evolution log

---
## 5. Public Presentation Streams

Streams are presentation interfaces, not canonical archives.

- https://fivsevn.com/posts
- https://fivsevn.com/foodie
- https://fivsevn.com/natsci

---
## 6. Narrative Layer (Side System)

- https://fivsevn.com/57store
- https://fivsevn.com/57store/sys
- https://fivsevn.com/57store/cctv
- https://57dayshift.wordpress.com

Experimental narrative module.
Not part of Layer 1 content axes.

---
## 7. Assets

- https://github.com/fivsevn/fivsevn-assets
- https://cdn.jsdelivr.net/gh/fivsevn/fivsevn-assets/

Static-only. No textual authority.

---
## 8. Internal Control Layer (Private)

- https://github.com/fivsevn/fivsevn-internal

Contains:
- AI configs
- post-by-mail console
- rapid publishing workspace
- operational scripts

Not publicly accessible.

---
## 9. Contact

mail: fivsevn0507@outlook.com
