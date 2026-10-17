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

- **发短文**：[posts README｜新建文字](../../posts/README.md#新建文字)。使用 devlog 仓库的 `posts/_flux/trigger.md`，发布去向为 [flux](https://flux.fivsevn.com/)。
- **修改、删除旧短帖**：[posts README｜修改旧帖](../../posts/README.md#修改旧帖) · [删除或恢复旧帖](../../posts/README.md#删除或恢复旧帖)。
- **发图片**：原快捷指令 → assets 的 `post/flux` → flux 自动接收。
- **发布或修改长文**：[posts](../../posts/README.md) · [natsci](../../natsci/README.md) · [netcom](../../netcom/README.md)。
- **目录刷新**：[自动目录入口](auto-index.md)，不负责短文发布。
- **草稿处理**：[自动草稿入口](auto-draft-frontmatter.md)。

2026-10-18 起，WordPress 文字发布已停用。trigger 已移到 `_flux` 文件夹；`scripts/publish_wp_text.py` 只校验 Markdown，任何参数都不会请求 WordPress。

flux 约每 5 分钟检查新提交，GitHub 调度可能延后；实际部署检查 [Publish flux](https://github.com/fivsevn/fivsevn-flux/actions/workflows/build.yml)。日常发布与修改方法统一见 [posts README](../../posts/README.md#1-短内容flux)；[flux README](https://github.com/fivsevn/fivsevn-flux/blob/main/README.md) 提供英文后台维护说明。
