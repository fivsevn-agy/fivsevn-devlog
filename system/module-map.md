---
id: system-module-map-001
title: Module Map — Global Topology

module: system
submodule: topology
topic: axis-definition

type: spec
status: active
canonical: true

summary: >
  定义 fivsevn 知识系统的结构轴向。
  包括分层结构模型，以及轴之间的交互规则与扩展条件。

parents: []
related: [system-ai-boot-protocol, system-prompt-routing]
tags: [topology, axis, structure, cognition]

audience: collaborator
languages: en
maturity: stable
confidence: 0.98
visibility: public
source_of_truth: devlog

created: 2026-02-15
updated: 2026-03-01
---
# Module Map - Global Topology

- Purpose: Define the global structure of the fivsevn system.

---
## 1. Structural Model (Layered)

- The fivsevn system is **layered**, not flat.

### Layer 1 — Cognitive Content Layer (world-facing content)
> This layer contains the primary knowledge content.

- posts → temporal reflection axis
- natsci → object-oriented domain (taxonomy / observation)
- netcom → system-oriented domain (engineering / protocols)

> These are **content axes**.

---
### Layer 2 — Kernel / Protocol Layer (rules)
- system → boot protocol, topology, routing, metadata interpretation

> This is **not content**.  
> This layer defines how Layer 1 is organized.

---
### Layer 3 — Meta-Governance Layer (system evolution)
- blogops → structural adjustments, publishing strategy changes, evolution log

> This is **not a knowledge axis**.  
> It documents how the system changes over time.

---
## 2. Interaction Rules

### 2.1 Cross-layer references
- blogops may reference any layer (it is meta-level)
- system may define rules that affect any layer
- posts may link to natsci/netcom as “temporal context”
- natsci/netcom may link back to posts as “history / reflections”

### 2.2 Metadata resolves placement
- `module` defines the primary location
- `parents` / `related` define graph positioning across modules
- `canonical` indicates authoritative version

---
## 3. Expansion Rule

- A new **content axis** may be created only if:
  - it develops stable methodology
  - it has independent structural logic
  - it is sustainable long-term
  - it is not a temporary interest cluster

- A new **meta layer** may be created only if:
  - it governs or describes the system itself
  - it does not become a dumping ground for content
