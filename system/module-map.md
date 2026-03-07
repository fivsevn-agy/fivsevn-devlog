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
  Defines the structural axes of the fivsevn system.
  Includes the layered model, interaction rules between axes,
  and conditions under which new axes or subsystems may emerge.

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
updated: 2026-03-08
---
# Module Map — Global Topology

Purpose:  
Define the global structural topology of the fivsevn system.

This file defines **axes, layers, and subsystem boundaries**.

---

# 1. Structural Model (Layered)

The fivsevn system is **layered**, not flat.

Layers define **structural roles**, not visual menu layout.

---

## Layer 1 — Cognitive Content Axes
*(world-facing knowledge layer)*

This layer contains the primary knowledge content of the blog system.

These axes represent **ways of organizing knowledge**, not just categories.

### posts
Temporal / reflective axis.

Typical content:
- essays
- reflections
- journal-like entries
- mixed observations
- project notes

> 中文注释：  
> posts 是默认内容池。  
> 当某一类内容规模足够大时，可以从 posts 中分化出新的轴。

---

### natsci
Object-oriented domain.

Focus:
- natural science
- taxonomy
- biological observation
- field notes
- specimen-oriented thinking

---

### netcom
System-oriented domain.

Focus:
- communications
- networks
- protocols
- engineering systems
- technical infrastructure

---

> Important principle:

These axes are **cognitive orientations**, not menu labels.

---

## Layer 2 — Kernel / Protocol Layer

This layer defines the **rules of the system itself**.

Module:

### system

Responsibilities include:

- boot protocol
- topology definition
- prompt routing
- metadata interpretation
- structural conventions

> This layer does not contain world-facing content.  
> It defines how the system works.

---

## Layer 3 — Meta-Governance Layer

This layer documents **how the system evolves**.

Module:

### blogops

Responsibilities:

- structural adjustments
- publishing strategy changes
- architecture notes
- operational logs
- system evolution records

> blogops is **meta-level documentation**, not a knowledge axis.

---

# 2. Parallel Subsystems

Some components of the fivsevn project exist **outside the cognitive content axes**.

These are treated as **parallel subsystems**.

---

## 57store Subsystem

57store is a **parallel narrative / interactive subsystem**.

It is not part of Layer 1 knowledge axes.

Typical characteristics:

- fictional store-world interfaces
- system-style UI pages
- CCTV-style pages
- mini-games
- experimental interactive pages
- playful or atmospheric presentation layers
- project-like UI experiments

Possible surfaces include:

- `fivsevn.com/57store`
- `fivsevn.com/57store/sys`
- `fivsevn.com/57store/cctv`
- `57store.fivsevn.com`
- auxiliary narrative nodes such as `57dayshift.wordpress.com`

> 中文注释：  
> 57store 是一个“互动 / 叙事 / 实验子系统”。  
> 它不属于 posts / natsci / netcom 的知识轴。

Important:

- 57store may temporarily grow in surface count.
- This **does not change the fact** that the blog system remains the main line.

---

# 3. Interaction Rules

Define how modules and axes interact.

---

## 3.1 Cross-layer references

- blogops may reference any layer (meta level)
- system may define rules affecting all layers
- posts may link to natsci / netcom as narrative context
- natsci / netcom may reference posts for temporal history

---

## 3.2 Metadata resolves placement

Placement of documents is determined by metadata:

- `module` defines primary structural location
- `parents` / `related` define graph relationships
- `canonical` indicates authoritative version
- `source_of_truth` indicates structural ownership

---

# 4. Expansion Rules

Define when new structural units may be created.

---

## 4.1 New Content Axis

A new Layer 1 axis may emerge only if:

- it develops stable methodology
- it has independent structural logic
- it is sustainable long-term
- it is not a temporary topic cluster

Example:
```
posts → large domain → new axis
```

---

## 4.2 New Meta Layer

A new meta layer may be created only if:

- it governs or describes the system itself
- it does not become a dumping ground for content

---

## 4.3 New Parallel Subsystem

A subsystem may emerge if:

- it operates with a different structural logic than the blog archive
- it contains interactive, narrative, or experimental interfaces
- it may require different repositories or platforms
- it should not be forced into existing content axes

Example:
```
57store
```

---

# Structural Principle

The fivsevn project contains:

- a **primary blog system**
- optional **parallel subsystems**

The blog system remains the structural core.

Subsystems may extend expression and experimentation,  
but they do not replace the core knowledge archive.