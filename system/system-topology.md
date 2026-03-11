---
id: system-topology-overview-001

title: System Topology

module: system
submodule: topology
topic: overview

type: note
status: active
canonical: false

summary: >
  提供 fivsevn 系统的极简结构图，
  用于快速理解 blog system、kernel layer 与 57store subsystem 的关系。

parents: [system-module-map-001]
related: [system-ai-boot-protocol, system-prompt-routing]

tags: [system, topology, overview, structure]

audience: [collaborator]
languages: [en]

maturity: stable
confidence: 0.95

visibility: public
source_of_truth: devlog

created: 2026-03-08
updated: 2026-03-08
---
# System Topology

```text
fivsevn system
│
├─ blog system
│   ├─ posts
│   ├─ natsci
│   ├─ netcom
│   │
│   └─ blogops
│
├─ kernel layer
│   ├─ ai-boot-protocol
│   ├─ module-map
│   └─ prompt-routing
│
└─ subsystem
    └─ 57store

interfaces
│
├─ fivsevn.com
├─ devlog.fivsevn.com
└─ 57store.fivsevn.com

repositories
│
├─ fivsevn-devlog
├─ fivsevn-spec
├─ fivsevn-57store
├─ fivsevn-assets
└─ fivsevn-internal
```