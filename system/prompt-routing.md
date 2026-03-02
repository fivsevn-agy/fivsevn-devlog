---
id: system-prompt-routing
title: Prompt Routing Policy

module: system
submodule: routing
topic: task-classification

type: spec
status: active
canonical: true

summary: >
  定义任务类型识别逻辑。
  将用户请求分类为 Temporal / Object / Structural，
  并据此路由至 posts、natsci 或 netcom 模块。

parents: [system-module-map]
related: [system-ai-boot-protocol]
tags: [routing, classification, cognitive-axis]

audience: collaborator
languages: en
maturity: evolving
confidence: 0.95
visibility: public
source_of_truth: devlog

created: 2026-02-15
updated: 2026-03-01
---
# Prompt Routing Policy

Purpose:
Define task classification and routing rules for the layered fivsevn system.

---
## 1. Task Classification (Layer-first)

Classify the request into one of the following:

### Layer 1 — Cognitive Content
- Temporal (reflection, updates, personal evolution)
- Object (natural objects, taxonomy, observation)
- Engineering (protocols, hardware, systems, infrastructure)

### Layer 2 — Kernel / Protocol
- Kernel (boot protocol, topology, routing rules, metadata schema)

### Layer 3 — Meta-Governance
- Meta (system evolution log, structural adjustments, publishing strategy)

---
## 2. Routing Rules

### 2.1 Layer 1 routing
If task involves:
- reflection / updates / evolving thought
→ route to **posts**

If task involves:
- biological entity / classification / natural objects / observation
→ route to **natsci**

If task involves:
- protocol / system / architecture / topology / hardware/software infrastructure
→ route to **netcom**

### 2.2 Layer 2 routing
If task involves:
- boot / topology / module map / frontmatter interpretation / routing policy
→ route to **system**

### 2.3 Layer 3 routing
If task involves:
- “how the system changed”
- publishing workflow evolution
- methodology explanation for humans
→ route to **blogops**
