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
  Defines task classification and routing rules for the layered fivsevn system.
  Requests are first classified by structural layer,
  then routed to the appropriate module or subsystem.

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
updated: 2026-03-08
---
# Prompt Routing Policy

Purpose:

Define how incoming tasks are classified and routed within the fivsevn system.

Routing follows the **layered model** defined in the Module Map.

---

# 1. Task Classification (Layer-first)

First determine which **structural layer** the request belongs to.

### Layer 1 — Cognitive Content
World-facing knowledge content of the blog system.

Typical orientations:

- Temporal reflection
- Natural objects / biological observation
- Engineering systems / communications

---

### Layer 2 — Kernel / Protocol
System architecture and structural rules.

Examples:

- boot protocol
- topology
- module map
- metadata schema
- routing logic

---

### Layer 3 — Meta-Governance
Documentation about how the system evolves.

Examples:

- publishing workflow
- structural adjustments
- methodology notes
- system evolution logs

---

### Parallel Subsystems
Components that operate outside the blog content axes.

Example:

- 57store interactive subsystem

> 中文注释  
> 这一类任务不属于 posts / natsci / netcom。  
> 它们属于独立子系统。

---

# 2. Routing Rules

After classification, route the task to the correct module.

---

## 2.1 Layer 1 — Blog Content Axes

If task involves:

- reflection  
- updates  
- personal thinking  
- essay-like writing  
- mixed observation

→ route to **posts**

---

If task involves:

- biological entities  
- taxonomy  
- natural science observation  
- specimen description

→ route to **natsci**

---

If task involves:

- communications  
- networking  
- protocols  
- hardware / software systems  
- infrastructure architecture

→ route to **netcom**

---

## 2.2 Layer 2 — Kernel / Protocol

If task involves:

- boot sequence
- topology definition
- module map
- routing policy
- frontmatter schema
- metadata interpretation

→ route to **system**

---

## 2.3 Layer 3 — Meta-Governance

If task involves:

- system evolution
- publishing workflow
- structural adjustments
- explanation of methodology

→ route to **blogops**

---

## 2.4 Parallel Subsystem Routing

If task involves elements of the **57store world/interface**, such as:

- fictional store-world UI
- sys interface
- CCTV-style page
- mini-game
- interactive HTML page
- dialogue or in-world script
- boot capsule
- experimental interface elements

→ route to **57store subsystem**

> 中文注释  
> 只要明显是便利店世界观 / UI / 游戏 / 实验页面  
> 都不要塞进 posts。

---

# 3. Priority Rule

Routing priority:
```
Layer detection  
→ Module routing  
→ Subsystem override (if applicable)  
```

Meaning:

1. Identify the structural layer
2. Route to the correct module
3. If the request clearly belongs to a subsystem (e.g. 57store),
   use subsystem routing instead of forcing it into blog axes.

---

# Structural Reminder

The **blog system** remains the main line of the fivsevn project.

Subsystems (such as 57store):

- extend experimentation
- enable interactive or narrative interfaces

But they do not replace the blog archive as the structural core.