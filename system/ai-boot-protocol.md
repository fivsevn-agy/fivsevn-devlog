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
  Defines the mandatory initialization sequence for any AI entering the fivsevn system.
  Forces repository topology, interface structure, specification layer, module logic,
  and metadata interpretation rules to be loaded in a fixed order instead of random scanning.

parents: [system-module-map]
related: [system-prompt-routing, workspace-entry]
tags: [boot, initialization, ai, topology, schema]

audience: collaborator
languages: en
maturity: evolving
confidence: 0.97
visibility: public
source_of_truth: devlog

created: 2026-02-15
updated: 2026-03-08
---
# AI Boot Protocol

- fivsevn System Initialization Sequence
> 目的：确保 AI 按固定顺序理解系统，而不是把页面和仓库当成一堆随机文件乱扫。

---

## Step 0 - Identify System Topology

- Goal: Understand the overall system structure before reading any content.
> 目标：先理解整个系统拓扑，再进入正文内容。

- The fivsevn system is **multi-interface** and **partly multi-repository**.
- Do not assume:
  - single-repository architecture
  - single-domain architecture
  - one-surface-per-subsystem design

---

### 0.1 Core Logic

- The system has one primary content line:
  - **the blog system**

- The blog system is expressed through two tightly connected surfaces:
  - **fivsevn.com** → presentation / visual interface
  - **devlog.fivsevn.com** → repository-backed content interface

> 中文注释：这里最重要。  
> `fivsevn.com` 和 `devlog.fivsevn.com` 看起来像两条线，实际是一条博客主线的两个界面。  
> 不要把 devlog 当成第二个独立站点。

- In other words:
  - `fivsevn.com` and `devlog.fivsevn.com` are not separate content systems
  - they are two operational surfaces of the same blog axis

---

### 0.2 Repositories

- [repository: fivsevn-devlog](https://github.com/fivsevn-agy/fivsevn-devlog)
  > Canonical long-form content archive and structural content workspace

- [repository: fivsevn-spec](https://github.com/fivsevn-agy/fivsevn-spec)
  > Writing rules, frontmatter schema, structural conventions

- [repository: fivsevn-57store](https://github.com/fivsevn/fivsevn-57store)
  > 57store subsystem repository for interactive pages, mini-games, experimental UI, and related assets/files

- [repository: fivsevn-assets](https://github.com/fivsevn/fivsevn-assets)
  > Static resource repository

- [repository: fivsevn-internal](https://github.com/fivsevn/fivsevn-internal) (private repository)
  > Internal control layer (AI configs, post-by-mail console, rapid publishing workspace)

---

### 0.3 Public Interfaces

#### Blog System

- [fivsevn.com](https://fivsevn.com)
  > Main public-facing presentation layer of the blog system

- [devlog.fivsevn.com](https://devlog.fivsevn.com)
  > Repository-backed public interface of the devlog archive  
  > This is part of the same blog system, not a separate site

- [fivsevn.com/posts](https://fivsevn.com/posts)
  > General stream / default content stream

- [fivsevn.com/foodie](https://fivsevn.com/foodie)
  > Visual / food-oriented stream

- [fivsevn.com/natsci](https://fivsevn.com/natsci)
  > Natural science-facing presentation stream

> 中文注释：  
> 主站和 devlog 是 blog system。  
> 前者偏展示，后者偏内容与仓库映射。

#### 57store Subsystem

- [fivsevn.com/57store](https://fivsevn.com/57store)
  > Main-site display surface of 57store

- [fivsevn.com/57store/sys](https://fivsevn.com/57store/sys)
  > In-world system-style presentation page

- [fivsevn.com/57store/cctv](https://fivsevn.com/57store/cctv)
  > In-world CCTV-style presentation page

- [57store.fivsevn.com](https://57store.fivsevn.com)
  > Repository-backed public interface for 57store interactive works, experiments, and game-oriented pages

- [57dayshift.wordpress.com](https://57dayshift.wordpress.com)
  > Auxiliary / legacy / parallel narrative node

> 中文注释：  
> 57store 不是一个网址，而是一个子系统。  
> 它可以跨多个 surface 存在，因为有些东西 WordPress 好做，有些东西 GitHub Pages 更适合做。  
> 不要强行要求 57store 绑定单一平台。

---

### 0.4 Structural Principle

- The blog system is the **main line**.
- 57store is a **secondary but meaningful subsystem**.
- 57store is used for:
  - playful or atmospheric interfaces
  - mini-games
  - fictional / narrative surfaces
  - capability display through implementation, aesthetics, and interactive design

> 中文注释：  
> 57store 不是博客主线，不应喧宾夺主。  
> 但它也不是纯装饰物。它承担“有趣、能玩、能展示能力”的作用。

---

## Step 1 - Load Specification Layer

- Goal: Learn structural language before interpreting content.
> 目标：先学习结构规则，再阅读内容。

- Read the spec layer:
  - understand frontmatter schema
  - identify required fields (`id`, `module`, `type`, etc.)
  - treat `id` as stable primary key
  - treat `parents` / `related` as graph edges
  - treat `canonical` as authority indicator
  - treat `source_of_truth` as content ownership / structural authority marker

> Do not interpret markdown files without loading schema first.

---

## Step 2 - Enter the Blog Archive Layer

- Goal: Load the content archive model before reading individual documents.
> 目标：先理解博客档案层，再读单篇内容。

- Enter the devlog archive layer.

- Important:
  - devlog is not a second independent publication line
  - devlog is the repository-backed archive / content workspace of the blog system

> 中文注释：  
> 这里再次防误判。  
> AI 很容易把 `devlog.fivsevn.com` 误判成“另一个站”，这里要明确堵死。

---

## Step 3 - Load Structural Layers

- Goal: Understand system layering before selecting module.
> 目标：在选模块之前，先理解系统分层。

- The fivsevn system is layered, not flat.

---

### Layer 1 — Cognitive Content Axes

- These organize world-facing content in the blog system.
  - `posts` → temporal / reflective axis
  - `natsci` → object-oriented / taxonomic / natural-science axis
  - `netcom` → system-oriented / engineering / protocol axis

> These are content axes, not mere categories.

> 中文注释：  
> `posts` 是默认内容池。  
> `natsci` 和 `netcom` 是已经明显专业化、独立化的主轴。  
> 将来如果 `posts` 某一类内容过多，可以再分化出新专栏。

---

### Layer 2 — Kernel / Protocol Layer

- Defines structural rules of the system.
  - `system` → boot protocol, topology, routing, metadata interpretation, structural rules

> This is not content.  
> This defines how content is organized.

---

### Layer 3 — Meta-Governance Layer

- Documents system evolution.
  - `blogops` → structural adjustments, publishing strategy changes, evolution logs, operating notes

> This is not a world-facing knowledge axis.  
> It operates above content as a meta layer.

---

### Parallel Subsystem — 57store

- `57store` is not part of Layer 1 content axes.
- `57store` is a parallel narrative / interactive subsystem.

- It may include:
  - system-style pages
  - CCTV-style pages
  - mini-games
  - experimental UI
  - fictional interfaces
  - boot capsules
  - other playful or project-like surfaces

> 中文注释：  
> 57store 不归入 `posts / natsci / netcom`。  
> 它属于平行子系统，不是博客知识轴的一部分。

---

> Do not treat all modules, layers, and subsystems as equivalent parallel domains.

---

## Step 4 - Load Module Topology

- Goal: Understand classification logic before content access.
> 目标：先理解分类逻辑，再进入内容。

- Read:
  - [devlog/system/module-map.md](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/system/module-map.md)
  - then module-level `map.md` files where relevant

- Interpret Layer 1 axes as **cognitive organization dimensions**, not just menu buckets:
  - `posts` → temporal / reflective axis
  - `natsci` → natural-object / taxonomic axis
  - `netcom` → systems / engineering axis

- Interpret:
  - `system` as kernel / protocol layer
  - `blogops` as meta-governance layer
  - `57store` as parallel narrative / interactive subsystem

---

## Step 5 - Classify Task Type

- Goal: Determine structural context before selecting documents.
> 目标：在读文档之前，先判断任务属于哪种系统语境。

- Load:
  - [/system/prompt-routing.md](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/system/prompt-routing.md)

- Classify task as one of the following:

### Blog Content Axis
- Temporal / reflection / essay / mixed journal-like writing → `posts`
- Natural science / biology / taxonomy / field observation → `natsci`
- Communications / systems / engineering / protocol → `netcom`

### Structural Layer
- Kernel / topology / metadata / protocol / archive structure → `system`
- Meta / governance / publishing strategy / structural adjustment → `blogops`

### Parallel Subsystem
- Fictional store-world interface
- sys / CCTV presentation
- mini-game
- playable page
- 57store dialogue / script / interface element
- boot capsule and related interactive files
→ `57store`

> 中文注释：  
> 和便利店世界观、sys、cctv、小游戏、店内终端之类有关的，都优先看作 57store，而不是误塞进 posts。

---

## Step 6 - Select Operational Context

- Goal: Choose correct system context before reading documents.
> 目标：先确定当前所在系统，再读内容。

- If task belongs to the blog main line:
  - stay within blog-system context
  - then select `posts`, `natsci`, `netcom`, `system`, or `blogops`

- If task belongs to 57store:
  - switch to 57store subsystem context
  - do not force it into blog content axes unless explicitly cross-referenced

> 中文注释：  
> 这一步是在防止把“结构不同的东西硬塞到同一套分类里”。

---

## Step 7 - Load Local Map Before Reading Documents

- Goal: Understand local structure before opening specific files.
> 目标：先理解局部结构，再读单个文件。

- Read local `map.md` first where available.
- Then read local `index.md`.
- Only after that, open individual documents.

> Never jump directly into isolated files when local topology exists.

---

## Step 8 - Interpret Documents via Frontmatter

- Goal: Use metadata as routing and authority mechanism.
> 目标：通过元数据判断归属、关系和权威性。

- When reading a document:
  - use `id` as primary reference
  - use `module` to confirm domain or layer
  - use `submodule` / `topic` for local placement
  - use `parents` and `related` to build graph context
  - respect `canonical`
  - respect `source_of_truth`
  - distinguish:
    - archive content
    - structural specification
    - subsystem document
    - public-facing presentation artifact

> Never treat content as isolated markdown.

---

## Step 9 - Preserve Main-Line Priority

- Goal: Maintain correct system emphasis during interpretation.
> 目标：保持主线优先级，防止支线喧宾夺主。

- The blog system remains the mainline of the fivsevn project.
- 57store is secondary in system priority, even when it temporarily expands in surface count or development effort.
- Increased activity inside 57store does not change the core structural fact that:
  - the blog system is primary
  - 57store is auxiliary / derivative / side-imprint-like

> 中文注释：  
> 这一条非常重要。  
> 就算某段时间 57store 页面很多、开发时间很多，也不能据此推断“57store 已经变成主站主线”。

---

## Termination Condition

- System is considered initialized only when:
  - system topology is understood
  - blog main-line logic is understood
  - repository / interface distinction is understood
  - specification layer is loaded
  - module structure is mapped
  - subsystem distinction is applied
  - metadata interpretation rules are active

> Only then perform semantic analysis.