---
id: "blogops-docs-auto-translation-shortcut-001"
title: "自动翻译快捷流程说明"

module: "blogops"
submodule: "docs"
topic: "auto-translation-shortcut"

type: "note"
status: "active"
canonical: true

summary: |
  说明 自动翻译快捷流程说明 的使用场景、操作流程与维护规则。

parents: []
related: ["spec-content-translation-001", "spec-content-frontmatter-001"]

tags: ["blogops", "docs", "translation", "shortcuts", "automation"]

audience: ["self", "internal"]
languages: ["zh"]

maturity: "stable"
confidence: 0.9

visibility: "public"
source_of_truth: "devlog"

note: "保留现有文件名：展示目录或已发布链接使用该路径，本次不修改展示页；metadata id 继续作为内容身份。"
filename_policy: "stable-link"

created: "2026-06-15"
updated: '2026-11-01'
metadata_updated: '2026-11-01'
---

# 翻译快捷指令

[translate & post.shortcut](translate%20%26%20post.shortcut) 从分享菜单接收网页网址，经 Jina Reader 取得文本，生成发给 AI 的 Markdown 提示词文件。

1. 在手机上分享原文网址，运行 `translate & post`。
2. 将生成的提示词文件交给 AI，取得中文译稿。
3. 核对正文、来源链接、图片及发布授权，再按 [posts](../../posts/README.md)、[natsci](../../natsci/README.md)或 [netcom](../../netcom/README.md) 的方式保存文章。

抓取失败时，改用原文、PDF 或截图。提示词文件是临时输入；快捷指令不直接发布文章。

字段和译文要求见[翻译规范](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/spec-content-translation-001.md)。
