---
id: "blogops-readme"
title: "blogops 板块说明"

module: "blogops"
submodule: "guide"
topic: "guide"

type: "note"
status: "active"
canonical: true

summary: "说明后台日志的手动更新方式、维护文档的存放位置，以及各板块操作入口。"

parents: []
related: []

tags: ["blogops", "maintenance"]

audience: ["self", "internal"]
languages: ["zh"]

maturity: "evolving"
confidence: null

visibility: "public"
source_of_truth: "devlog"

note: |
  created 为本路径首次 Git 记录日期。
  blogops/.cache 是特别设计的叙事文件，不是程序缓存；保持原样，不清理、移动或套用文章 metadata。
filename_policy: "entrypoint"

created: "2026-10-13"
updated: '2026-11-01'
metadata_updated: '2026-11-01'
---

# blogops

[后台日志](index.md)手动记录博客更新；在 `Directory` 顶部添加日期、说明和链接，更新 `updated` 后推送到 `main`。

- `content/`：博客说明与创作资料。
- `docs/`：[翻译快捷指令](docs/auto-translation-shortcut.md)。
- `legacy/`：历史记录。
- `.cache`：57store 叙事文本。

当前发布方式见各板块 README；网站与仓库分工见[系统总览](../system-map.md)。
