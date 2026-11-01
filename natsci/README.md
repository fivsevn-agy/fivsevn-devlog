---
id: "natsci-readme"
title: "natsci 板块说明"

module: "natsci"
submodule: "guide"
topic: "guide"

type: "note"
status: "active"
canonical: true

summary: "说明natsci 板块说明。"

parents: []
related: []

tags: []

audience: ["self", "internal"]
languages: ["zh"]

maturity: "evolving"
confidence: null

visibility: "public"
source_of_truth: "devlog"

note: "未记录原始写作日期；created 为本路径首次 Git 记录日期，无法合理确定时留空。"
filename_policy: "entrypoint"

created: "2026-10-13"
updated: '2026-11-01'
metadata_updated: '2026-11-01'
---

# natsci

[自然科学笔记](https://devlog.fivsevn.com/natsci/)按 `taxonomy/`、`paleontology/`、`ethnobiology/` 等主题目录保存。

- **发布文章**：放入对应主题目录，使用 `module: natsci`、`status: active`、`visibility: public`，推送到 `main`。
- **草稿**：放在 `_drafts/` 第一层；正式发布时移出草稿区。新草稿会自动补资料，继续编辑前先拉取。
- **修改文章**：编辑原文件，保留 `id`、文件名和 `created`，更新 `updated`。目录自动生成。
- **译文**：保留来源链接，使用 `type: translation`；见[翻译快捷指令](../blogops/docs/auto-translation-shortcut.md)。

## Fieldlog

[自然观察图片](https://devlog.fivsevn.com/natsci/fieldlog/)由本仓库发布，每张照片一帖。上传到 [`fieldlog/trigger_imgs/`](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/natsci/fieldlog/trigger_imgs/README.md)，配文写在提交详细说明中。旧帖编辑原发布包。

[Fieldlog 维护](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/natsci/fieldlog/README.md) · [共享规范](https://github.com/fivsevn-agy/fivsevn-spec) · [Actions](https://github.com/fivsevn-agy/fivsevn-devlog/actions)
