---
id: 
title: 

module: system / natsci / netcom / posts / blogops / narrative
submodule: 
topic: 

type: note / article / index / log / spec / release
status: draft / active / archived
canonical: true / false

summary: >

parents: []
related: []
tags: []

audience: self / public / tutorial / collaborator
languages: zh / en / jp
maturity: draft / evolving / stable / deprecated
confidence: 0.0
visibility: public / private
source_of_truth: devlog / site / spec / internal

created: 
updated: 
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

- Do not assume single-repo architecture.

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

- Do not interpret markdown files without loading schema first.

---
## Step 2 - Enter Devlog (Canonical Archive)

- Goal: Load structural model of content repository.
> 目标：理解内容仓库的整体结构

- Navigate to devlog.

- Do not read individual articles yet.

---
## Step 3 - Load Module Topology

- Goal: Understand classification axes.
> 目标：理解模块的分类逻辑

- Read:
  - [/system/module-map.md](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/system/module-map.md)
  - Then module-level map.md files

- Core axes:
- Core axes define cognitive organization dimensions, not categories.
  - posts → temporal axis
  - natsci → taxonomic / object axis
  - netcom → system / engineering axis
  - system → kernel & protocol layer

---
## Step 4 - Classify Task Type

- Goal: Determine cognitive axis before selecting module.
> 目标：在进入模块前，先判断任务类型

- Load:
  - [/system/prompt-routing.md](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/system/prompt-routing.md)

- Classify task as:
  - Temporal
  - Object
  - Structural

- Route accordingly:
  - Temporal → posts
  - Object → natsci
  - Structural → netcom

- Only after classification, proceed to Step 5.

---
## Step 5 - Select Module

- Goal: Choose domain context before reading documents.
> 目标：先确定语境，再读正文

- Based on task type:
  - Reflection / essays → posts
  - Natural science → natsci
  - Communications / engineering → netcom

- Enter module directory.

---
## Step 6 - Load Module Map

- Goal: Understand internal structure before reading content.
> 目标：先理解子系统结构

- Read module map.md first.
- Then read module index.md.

- Only after that, open individual documents.

---
## Step 7 — Interpret Articles via Frontmatter

- Goal: Use metadata as routing mechanism.
> 目标：用元数据进行结构化理解

- When reading an article:
  - Use id as primary reference
  - Use module to confirm domain
  - Use parents and related to build graph context
  - Respect canonical flag

- Never treat content as isolated markdown.

---
## Termination Condition

- System considered initialized when:
  - Repository topology is understood
  - Schema is loaded
  - Module structure is mapped
  - Metadata interpretation rules are applied

- Only then perform semantic analysis.


