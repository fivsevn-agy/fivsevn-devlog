---
id: netcom-module-map
title: netcom — Module Map

module: netcom
submodule: topology
topic: system-axis-definition

type: spec
status: active
canonical: true

summary: >
  定义 netcom 作为系统轴（System Axis）的结构逻辑。
  说明其以工程分层、协议结构与硬件软件关系为核心，
  时间顺序不参与组织。

parents: [system-module-map]
related: [netcom-index]
tags: [netcom, topology, system-axis, engineering]

audience: collaborator
languages: en
maturity: stable
confidence: 0.98
visibility: public
source_of_truth: devlog

created: 2025-11-16
updated: 2026-03-01
---
# netcom — Module Map

Purpose:
Define internal structure of the Communications & Engineering axis.

This module is organized by systems and structural logic.

---

## 1. Structural Principle

Primary ordering logic:
- Architecture
- Protocol layers
- Hardware-software relationship
- Mathematical foundation

Chronology is irrelevant.

---

## 2. Sub-Structures

Possible structural divisions:

- architecture/
  System models and layered thinking

- protocol/
  Communication rules and abstractions

- rf/
  Radio frequency theory

- lora/
  LoRa and mesh systems

- mcu/
  Hardware components

- math/
  Mathematical foundations

- methods/
  Conceptual tools

---

## 3. Organizational Pattern

Documents follow:

system → subsystem → component → principle

Example:

lora/
  meshtastic/
    document.md

---

## 4. Axis Interaction

netcom documents may:

- Be announced in posts (temporal axis)
- Be referenced in system (meta layer)

Structure remains engineering-driven.

---

## 5. Stability Rule

netcom expands through:

- Structural depth
- Layer refinement
- Model clarification

Not through trend-driven topics.