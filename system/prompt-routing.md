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