---
id: system-docs-auto-index-manual-001
title: 自动目录说明入口

module: blogops
submodule: docs
topic: auto-index

type: note
status: active
canonical: false

summary: >
  保留旧自动目录手册地址；日常操作指向板块 README，规则实现指向当前索引脚本与工作流。

parents: []
related: [spec-content-frontmatter-001]

tags: [blogops, docs, automation, index, frontmatter]
audience: [self, internal]
languages: [zh]
maturity: stable
confidence: 0.9
visibility: public
source_of_truth: devlog
created: 2026-06-12
updated: 2026-10-13
---

# 自动目录说明入口

> 本页保留旧链接，不再复制完整操作步骤、脚本和工作流。修改标题、日期、路径或状态时，直接查看对应板块说明。

- **日常操作**：[posts](../../posts/README.md) · [natsci](../../natsci/README.md) · [netcom](../../netcom/README.md)。
- **字段含义**：[metadata 规范](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/spec-content-frontmatter-001.md)。
- **当前实现**：[索引脚本](../../scripts/update_module_indexes.py) · [工作流文件](../../.github/workflows/update-indexes.yml) · [运行记录](https://github.com/fivsevn-agy/fivsevn-devlog/actions/workflows/update-indexes.yml)。

> 提交文章 → 脚本扫描 metadata → 替换 index 的 `AUTO-INDEX` 列表 → 有变化才提交。它不向 WordPress 发文；Pages 部署另行检查。

旧版手册保留在[修改历史](https://github.com/fivsevn-agy/fivsevn-devlog/commits/main/blogops/docs/auto-index.md)，不作为当前操作依据。
