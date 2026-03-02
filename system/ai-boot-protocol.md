---
id: system-ai-boot-protocol
title: AI Boot Protocol

module: system
submodule: boot
topic: initialization-sequence

type: spec
status: active
canonical: true

summary: >
  定义 AI 进入 fivsevn 系统时必须遵循的初始化顺序。
  强制加载仓库拓扑、规范层、模块结构与元数据解释规则，
  防止随机扫描式理解。

parents: [system-module-map]
related: [system-prompt-routing, workspace-entry]
tags: [boot, initialization, ai, topology, schema]

audience: collaborator
languages: en
maturity: evolving
confidence: 0.95
visibility: public
source_of_truth: devlog

created: 2026-02-15
updated: 2026-03-01
---
# AI Boot Protocol

- fivsevn System Initialization Sequence
> 目的：确保任何 AI 按固定顺序理解系统结构，而非随机扫描。

---
## Step 0 - Identify Repository Topology

- Goal: Understand multi-repo and website structure before reading content.
> 目标：先理解仓库结构，再进入内容

- The fivsevn-system consists of multiple repositories and web interfaces.

- Repositories:
  - [repository: fivsevn-devlog](https://github.com/fivsevn-agy/fivsevn-devlog)
    > Canonical long-form content archive
  - [repository: fivsevn-spec](https://github.com/fivsevn-agy/fivsevn-spec)
    > Writing rules & frontmatter schema
  - [repository: fivsevn-assets](https://github.com/fivsevn/fivsevn-assets)
    > Static resource repository
  - [repository: fivsevn-internal](https://github.com/fivsevn/fivsevn-internal)(private repository)
    > Internal control layer (AI configs, post-by-mail console, rapid publishing workspace)

- Web Interfaces:
  - [fivsevn.com](https://fivsevn.com)
    > Presentation layer (public-facing stream interface)
  - [fivsevn.com/posts](https://fivsevn.com/posts)
      > Short-form stream (fast publish layer)
  - [fivsevn.com/foodie](https://fivsevn.com/foodie)
      > Visual stream (image-dominant feed)
  - fivsevn-kiosk layer
    > Narrative Interfaces:
    - [fivsevn-kiosk](http://fivsevn.com/kiosk)
    - [fivsevn-kiosk-sys](http://fivsevn.com/kiosk/sys)
    - [fivsevn-kiosk-cctv](http://fivsevn.com/kiosk/cctv)
    - [fivsevn-kiosk-57 Day Shift](http://57dayshift.wordpress.com)
    > Experimental narrative layer

> Do not assume single-repo architecture.

---
## Step 1 - Load Specification Layer

- Goal: Learn schema before interpreting content.
> 目标：先学习结构语言，再阅读文章

- Read spec repository:
  - Understand frontmatter schema
  - Identify required fields (id, module, type, etc.)
  - Treat id as stable primary key
  - Treat parents / related as graph edges
  - Treat canonical as authoritative indicator

> Do not interpret markdown files without loading schema first.

---
## Step 2 - Enter Devlog (Canonical Archive)

- Goal: Load structural model of content repository.
> 目标：理解内容仓库的整体结构

- Navigate to devlog.

> Do not read individual articles yet.

---
## Step 3 - Load Structural Layers

- Goal: Understand system layering before selecting module.
> 目标：在进入模块前，先理解系统层级

- The fivsevn system is layered, not flat.

---
### Layer 1 — Cognitive Content Axes

- These organize world-facing content.
  - posts → temporal axis (time-oriented reflection)
  - natsci → object-oriented cognition (taxonomic / biological focus)
  - netcom → system-oriented cognition (engineering / protocol focus)

> These are content domains.

---
### Layer 2 — Kernel / Protocol Layer

- Defines structural rules of the system.
  - system → boot protocol, topology, routing, metadata schema

> This is not content.    
> This defines how content is structured.

---
### Layer 3 — Meta-Governance Layer

- Documents evolution of the system itself.
  - blogops → structural adjustments, publishing strategy changes, system evolution log

> This is not a knowledge axis.    
> It operates above content.

---
> Do not treat all modules as parallel domains.

---
## Step 4 - Load Module Topology

- Goal: Understand classification axes.
> 目标：理解模块的分类逻辑

- Read:
  - [devlog/system/module-map.md](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/system/module-map.md)
  - Then module-level map.md files

- Layer 1 axes (content layer):  
- Layer 1 axes define cognitive organization dimensions, not categories.
  - posts → temporal axis
  - natsci → taxonomic / object axis
  - netcom → system / engineering axis

> system / blogops are layers, not axes.

---
## Step 5 - Classify Task Type

- Goal: Determine cognitive axis before selecting module.
> 目标：在进入模块前，先判断任务类型

- Load:
  - [/system/prompt-routing.md](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/system/prompt-routing.md)

- Classify task as:
  - Temporal → posts
  - Object → natsci
  - System / Engineering → netcom
  - Kernel / Protocol → system
  - Meta / Governance → blogops

> Only after classification, proceed to module selection.

---
## Step 6 - Select Module

- Goal: Choose domain context before reading documents.
> 目标：先确定语境，再读正文

- Based on task type:
  - Reflection / essays → posts
  - Natural science → natsci
  - Communications / engineering → netcom

> Enter module directory.

---
## Step 7 - Load Module Map

- Goal: Understand internal structure before reading content.
> 目标：先理解子系统结构

- Read module map.md first.
- Then read module index.md.

> Only after that, open individual documents.

---
## Step 8 — Interpret Articles via Frontmatter

- Goal: Use metadata as routing mechanism.
> 目标：用元数据进行结构化理解

- When reading an article:
  - Use id as primary reference
  - Use module to confirm domain
  - Use parents and related to build graph context
  - Respect canonical flag

> Never treat content as isolated markdown.

---
## Termination Condition

- System considered initialized when:
  - Repository topology is understood
  - Schema is loaded
  - Module structure is mapped
  - Metadata interpretation rules are applied

> Only then perform semantic analysis.
