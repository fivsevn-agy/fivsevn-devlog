---
id: "foodie-readme"
title: "Savour 板块说明"

module: "foodie"
submodule: "guide"
topic: "guide"

type: "note"
status: "active"
canonical: true

summary: "Savour 吃喝记录的网站、上传与维护入口。"

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
updated: "2026-10-29"
metadata_updated: "2026-10-13"
---
# Savour 板块说明

Savour 是 [fivsevn.com](https://fivsevn.com/) 的吃喝分享板块。

- **网站**：[savour.fivsevn.com](https://savour.fivsevn.com/)，每张照片一帖，以手机聊天界面展示。
- **内容与图片**：[fivsevn-savour](https://github.com/fivsevn/fivsevn-savour) 独立保存、构建并通过 GitHub Pages 发布。
- **上传图片**：看 [中文图片入口说明](https://github.com/fivsevn/fivsevn-savour/tree/main/trigger_imgs)；保留原文件名，配文写在提交的 extended description 中，推送到 `main`。仓库自动转 WebP、命名、建帖与发布，线上核验后清理入口原图。
- **修改旧帖**：编辑 `savour/YYYY/MM/{id}/index.md`；正文放在 frontmatter 后。设为 `hidden`／`draft` 可隐藏，删除整个帖子文件夹可移除。
- **详细维护**：看 [英文 README](https://github.com/fivsevn/fivsevn-savour/blob/main/README.md)，页面样式与发布流程在该仓库修改。

本目录提供操作说明，照片与发布内容统一保存在 savour 仓库。
