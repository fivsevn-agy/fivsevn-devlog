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
  保留旧发布说明地址，区分 flux 短文发布与长文目录刷新；操作统一指向板块 README。

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
updated: "2026-10-18"
metadata_updated: "2026-10-18"
---

# 发布入口说明

- **发短文**：[posts README｜新建文字](../../posts/README.md#新建文字)。使用 flux 仓库的 [`trigger.md`](https://github.com/fivsevn/fivsevn-flux/blob/main/trigger.md)，发布去向为 [flux](https://flux.fivsevn.com/)。
- **修改、删除旧短帖**：[posts README｜修改旧帖](../../posts/README.md#修改旧帖) · [删除或恢复旧帖](../../posts/README.md#删除或恢复旧帖)。
- **发图片**：快捷指令 → flux 仓库的 [`uploads/`](https://github.com/fivsevn/fivsevn-flux/tree/main/uploads) → 提交并推送直接发布。
- **发布或修改长文**：[posts](../../posts/README.md) · [natsci](../../natsci/README.md) · [netcom](../../netcom/README.md)。
- **目录刷新**：[自动目录入口](auto-index.md)，不负责短文发布。
- **草稿处理**：[自动草稿入口](auto-draft-frontmatter.md)。

2026-10-18 起，WordPress 文字发布已停用。唯一的文字 trigger 迁入 flux 仓库根目录；devlog 的旧 trigger、格式检查工作流和旧 WordPress 发布脚本已移除。

文字和图片提交都直接启动发布，任务成功前会核对线上页面及图片文件；不依赖定时任务或 assets 仓库。实际部署检查 [Publish flux](https://github.com/fivsevn/fivsevn-flux/actions/workflows/build.yml)。日常发布与修改方法统一见 [posts README](../../posts/README.md#1-短内容flux)；[flux README](https://github.com/fivsevn/fivsevn-flux/blob/main/README.md) 提供英文后台维护说明。
