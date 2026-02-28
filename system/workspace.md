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

- Purpose: Entry point for AI-level structural navigation.

- This file is not a boot protocol.
- It is a high-level orientation layer.

- Boot sequence is defined in:
  - [/system/ai-boot-protocol.md](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/system/ai-boot-protocol.md)

---
## 0. System Overview

- The fivsevn system is multi-layered and multi-repository.

- It contains:
  - Canonical archive (devlog)
  - Structural specification (spec)
  - Static assets (assets)
  - Internal control layer (internal)
  - Public presentation streams (website)
  - Experimental narrative layer (kiosk)

Do not assume single-repo architecture.

---
## 1. Canonical Archive (Authoritative Content)

- Repository: https://github.com/fivsevn-agy/fivsevn-devlog

> This is the long-form structured content base.

- Raw index: https://raw.githubusercontent.com/fivsevn-agy/fivsevn-devlog/main/README.md

- All structural interpretation must begin here after boot.

---
## 2. Structural Definition Layer

- Spec: https://github.com/fivsevn-agy/fivsevn-spec

- Defines:
  - frontmatter schema
  - id rules
  - graph structure

- Module topology:
  - /system/module-map.md

- Axes are defined in module-map.md.

---
## 3. Public Presentation Streams

- Main site: https://fivsevn.com

- Streams:
  - https://fivsevn.com/posts
  > Short-form temporal stream.

  - https://fivsevn.com/foodie
  > Visual stream.

- Streams are presentation interfaces.
- They are not canonical archives.

---
## 4. Narrative Layer (Side System)

- https://fivsevn.com/kiosk
- https://fivsevn.com/kiosk/sys
- https://fivsevn.com/kiosk/cctv
- https://57dayshift.wordpress.com

- Experimental narrative module.
- Not part of knowledge axes.

---
## 5. Assets

- https://github.com/fivsevn/fivsevn-assets
- https://cdn.jsdelivr.net/gh/fivsevn/fivsevn-assets/

- Static-only.
- No textual authority.

---
## 6. Internal Control Layer (Private)

- https://github.com/fivsevn/fivsevn-internal

- Contains:
  - AI configs
  - post-by-mail console
  - rapid publishing workspace
  - operational scripts

- Not publicly accessible.
- Not part of semantic knowledge structure.

---
## 7. Contact

mail: fivsevn0507@outlook.com


