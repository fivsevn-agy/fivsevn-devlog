---
id: "blogops-docs-auto-draft-frontmatter-001"
title: "自动草稿说明入口"

module: "blogops"
submodule: "docs"
topic: "auto-draft-frontmatter"

type: "note"
status: "active"
canonical: false

summary: |
  保留旧草稿手册地址；日常操作指向板块 README，字段规则与脚本各自维护，不复制源码。

parents: []
related: ["system-docs-auto-index-manual-001"]

tags: ["blogops", "docs", "automation", "draft", "frontmatter"]

audience: ["self", "internal"]
languages: ["zh"]

maturity: "stable"
confidence: 0.9

visibility: "public"
source_of_truth: "devlog"

note: "保留现有文件名：展示目录或已发布链接使用该路径，本次不修改展示页；metadata id 继续作为内容身份。"
filename_policy: "stable-link"

created: "2026-06-12"
updated: "2026-10-13"
metadata_updated: "2026-10-13"
---

# 自动草稿说明入口

> 本页保留旧链接，不再另行维护一整份模板、脚本和工作流副本。

- **新建／编辑／发布草稿**：[posts](../../posts/README.md) · [natsci](../../natsci/README.md) · [netcom](../../netcom/README.md)。
- **字段规范**：[metadata 说明](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/spec-content-frontmatter-001.md)。
- **当前实现**：[草稿脚本](../../scripts/apply_draft_frontmatter.py) · [工作流文件](../../.github/workflows/apply-draft-frontmatter.yml) · [运行记录](https://github.com/fivsevn-agy/fivsevn-devlog/actions/workflows/apply-draft-frontmatter.yml)。

> `_drafts/` 第一层的无 frontmatter Markdown → 提取标题、补字段、生成占位文件名 → 自动提交。已有 frontmatter 的文件跳过；正式发布仍按板块 README 操作。

**不进入目录不等于私密。**`_drafts/` 和 `visibility: private` 不是访问控制；私密材料不要提交到公开仓库。
