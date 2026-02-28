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
Define task-type recognition logic.

---

## 1. Task Classification

Tasks are categorized into:

- Temporal
- Object
- Structural

---

## 2. Routing Rules

If task involves:
- reflection
- updates
- evolution
→ route to posts

If task involves:
- biological entity
- classification
- natural objects
→ route to natsci

If task involves:
- protocol
- system
- architecture
- hardware/software
→ route to netcom