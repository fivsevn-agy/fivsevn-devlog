---
id: "blogops-docs-post-publish-trigger-001"
title: "发布入口说明"

module: "blogops"
submodule: "docs"
topic: "post-publish-trigger"

type: "note"
status: "active"
canonical: false

summary: |
  Flux、Savour、Fieldlog 的发布入口，以及长文目录与草稿处理说明。

parents: []
related: ["system-docs-auto-index-manual-001", "blogops-docs-auto-draft-frontmatter-001"]

tags: ["blogops", "docs", "automation", "publish", "trigger"]

audience: ["self", "internal"]
languages: ["zh"]

maturity: "stable"
confidence: 0.9

visibility: "public"
source_of_truth: "devlog"

note: "保留现有文件名：展示目录或已发布链接使用该路径，本次不修改展示页；metadata id 继续作为内容身份。"
filename_policy: "stable-link"

created: "2026-06-13"
updated: "2026-10-30"
metadata_updated: "2026-10-30"
---

# 发布入口说明

- **发短文**：[posts README｜新建文字](../../posts/README.md#新建文字)。使用 flux 仓库的 [`trigger_text.md`](https://github.com/fivsevn/fivsevn-flux/blob/main/trigger_text.md)，发布去向为 [flux](https://flux.fivsevn.com/)。
- **修改、删除旧短帖**：[posts README｜修改旧帖](../../posts/README.md#修改旧帖) · [删除或恢复旧帖](../../posts/README.md#删除或恢复旧帖)。
- **Flux 图片**：[`trigger_imgs/`](https://github.com/fivsevn/fivsevn-flux/tree/main/trigger_imgs)。
- **Savour 图片**：[`trigger_imgs/`](https://github.com/fivsevn/fivsevn-savour/tree/main/trigger_imgs)。
- **Fieldlog 图片**：[`natsci/fieldlog/trigger_imgs/`](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/natsci/fieldlog/trigger_imgs)。
- **发布或修改长文**：[posts](../../posts/README.md) · [natsci](../../natsci/README.md) · [netcom](../../netcom/README.md)。
- **目录刷新**：[自动目录入口](auto-index.md)，不负责短文发布。
- **草稿处理**：[自动草稿入口](auto-draft-frontmatter.md)。

图片保留原文件名，配文写在提交的 extended description 中，然后提交并推送到对应仓库的 `main`。三站统一自动保存 WebP、补齐共享 frontmatter、按每页 11 则正式帖子构建；线上核验通过后清理入口原图。文字入口和图片入口只负责新建，修改旧帖要编辑对应发布包。

三站的内容与图片由各自仓库管理。日常操作见 [Flux](../../posts/README.md#1-短内容flux)、[Savour](../../savour/README.md)、[Fieldlog](../../natsci/README.md#1-影像记录fieldlog)；英文维护说明见各内容仓库 README。
