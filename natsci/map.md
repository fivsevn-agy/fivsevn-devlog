---
id: natsci-module-map
title: natsci — Module Map

module: natsci
submodule: topology
topic: object-axis-definition

type: spec
status: active
canonical: true

summary: >
  定义 natsci 作为对象轴（Object Axis）的结构逻辑。
  说明其以自然对象与分类体系为核心，
  时间顺序为次级维度。

parents: [system-module-map]
related: [natsci-index]
tags: [natsci, topology, object-axis, taxonomy]

audience: collaborator
languages: en
maturity: stable
confidence: 0.98
visibility: public
source_of_truth: devlog

created: 2026-02-28
updated: 2026-03-01
---
# natsci — Module Map

Purpose:
Define internal structure of the Natural Science axis.

This module is organized by object and taxonomy,
not by time.

---

## 1. Structural Principle

Primary ordering logic:
- Object-based
- Classification-driven
- Entity-first

Chronology is secondary.

---

## 2. Sub-Structures

The module may contain:

- taxonomy/
  Biological classification layers

- methods/
  Observation and retrieval techniques

- field-notes/
  Raw observation logs

- memo/
  Draft-level reflections

---

## 3. Organizational Pattern

Hierarchy example:

taxonomy/
  insecta/
    coleoptera/
      genus/
        document.md

This structure reflects taxonomic depth.

---

## 4. Interaction With Other Axes

A document may:

- Appear in posts (temporal entry)
- Belong structurally to natsci

Temporal and object axes are orthogonal.

---

## 5. Stability Rule

natsci grows through:
- New objects
- Deeper classification
- Method refinement

Not through topical clustering.