---
id: blogops-module-map
title: blogops — Module Map
module: blogops
submodule: topology
topic: meta-governance-axis-definition
type: spec
status: active
canonical: true
summary: >
  Defines blogops as the meta-governance and publishing-operations layer of fivsevn-devlog.
  Clarifies its boundary from public content axes, system topology, generated surfaces,
  and day-to-day repository maintenance.
parents:
  - system-map
related:
  - blogops-index
  - system-map
  - posts-module-map
  - natsci-module-map
  - netcom-module-map
tags:
  - blogops
  - topology
  - meta-governance
  - publishing
  - workflow
  - repository-maintenance
audience:
  - collaborator
languages:
  - en
  - zh
maturity: stable
confidence: 0.96
visibility: public
source_of_truth: devlog
created: 2026-02-28
updated: 2026-06-12
---

# blogops — Module Map

Purpose:

Define the internal structure and routing logic of the `blogops` module.

`blogops` is the meta-governance and publishing-operations layer of `fivsevn-devlog`.

It documents how the blog system is maintained, adjusted, automated, and governed.

---

## 1. Structural Principle

Primary ordering logic:

- workflow;
- publishing process;
- repository operation;
- automation;
- editorial policy;
- structural evolution;
- maintenance decisions.

`blogops` is not a public content axis like `posts`, `natsci`, or `netcom`.

It is a governance and operations layer.

---

## 2. What Belongs Here

Route content to `blogops` when it involves:

- publishing workflow;
- index generation;
- repository maintenance;
- automation scripts;
- editorial process;
- content migration strategy;
- GitHub Actions behavior;
- public/private surface management;
- site structure changes;
- operational logs about the blog system.

---

## 3. Current Structure

Current visible structure:

```text
blogops/
├── content/
├── index.md
└── map.md
```

Interpretation:

- `content/` contains blog-operations notes and documents;
- `index.md` is the public-facing or repository-facing blogops landing page;
- `map.md` is this AI-facing routing and topology file.

---

## 4. Index Behavior

`blogops/index.md` is not currently handled by the automatic module-index script.

The current auto-index script only covers:

```text
posts/
natsci/
netcom/
```

Therefore:

- `blogops/index.md` may be maintained manually;
- `blogops/map.md` should not be treated as article content;
- blogops documents should remain governance / operations material, not mixed into public content axes unless explicitly rewritten as public posts.

---

## 5. Relationship to Auto-Index System

The auto-index system itself belongs conceptually to `blogops`.

Documents explaining:

- how auto-index works;
- how frontmatter controls display;
- how `status: draft` behaves;
- how `index.md` should be maintained;
- how workflow files update indexes;

should be routed to `blogops` or `system` depending on purpose.

Use `blogops` when the document is operational.

Use `system` when the document defines topology, metadata semantics, or global rules.

---

## 6. Boundary With `system`

Route to `system` if the topic is:

- global topology;
- boot protocol;
- module routing;
- metadata interpretation;
- repository authority;
- cross-system boundaries.

Route to `blogops` if the topic is:

- how to publish;
- how to maintain the repository;
- how to operate GitHub Actions;
- how to update index pages;
- how to document editorial practice.

Short distinction:

```text
system = structural authority
blogops = operational governance
```

---

## 7. Boundary With Content Axes

Do not route ordinary articles to `blogops`.

Use:

- `posts` for reflective writing and general notes;
- `natsci` for natural-science object / taxonomy material;
- `netcom` for technical system / network / protocol material.

Use `blogops` only when the subject is the blog system itself.

---

## 8. Draft and Visibility Policy

If `_drafts/` is added under `blogops/`, it should be treated as a private buffer.

`blogops` is not currently auto-indexed, so `status: draft` does not automatically create an index preview unless a separate blogops index workflow is added later.

Recommended status use:

```yaml
status: active
```

for stable operational documentation.

```yaml
status: draft
```

for unfinished operational notes.

```yaml
status: hidden
```

for documents that should remain invisible from public-facing navigation.

---

## 9. Minimal AI Rules

1. Treat `blogops` as the operations and governance layer.
2. Do not confuse `blogops` with `system`.
3. Do not route normal essays, natural-science notes, or technical notes here.
4. Use `blogops` for workflow, publishing, automation, and maintenance documentation.
5. Do not assume `blogops/index.md` is auto-generated unless a workflow explicitly says so.
6. Do not index `map.md` as article content.
