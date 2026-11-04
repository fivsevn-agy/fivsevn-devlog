---
id: natsci-fieldlog-trigger-imgs-readme
title: Fieldlog 图片入口
module: natsci
submodule: fieldlog
topic: guide
type: note
status: active
canonical: true
summary: 上传自然观察图片、附带配文并自动发布 Fieldlog 的入口说明。
parents: [natsci-fieldlog-readme]
related: []
tags: [fieldlog, publishing]
audience: [self, internal]
languages: [zh]
maturity: evolving
confidence: null
visibility: public
source_of_truth: devlog
filename_policy: entrypoint
created: '2026-10-30'
updated: '2026-11-05'
metadata_updated: '2026-11-05'
---
# Fieldlog 图片入口

把图片放到 **`fivsevn-agy/fivsevn-devlog` 的 `natsci/fieldlog/trigger_imgs/`**，提交并推送到 `main` 即可发布。

1. 先在 Working Copy 同步仓库最新的 `main`；使用 GitHub Desktop 时也先拉取最新提交。
2. 运行现有快捷指令，将 Images 保存到上述完整路径，保留每张照片的原文件名。
3. 快捷指令打开 Working Copy 后，检查图片、提交并推送到 `main`。配文写进提交的 **可选详细说明（extended description）**，支持 Markdown，留空则只发图。
4. 等待[发布任务](https://github.com/fivsevn-agy/fivsevn-devlog/actions)完成，再打开 [Fieldlog](https://devlog.fivsevn.com/natsci/fieldlog/) 检查图片和配文。

支持 JPG/JPEG、PNG、WebP、GIF、HEIC/HEIF。一次多张，每张各发一帖，共用本次配文。系统按提交的北京时间命名、转为 WebP（归档只保留 WebP）、补齐文章资料并发布；核验线上页面和图片后只清理匹配的入口原图。失败会保留原图，同次提交重跑不重复发帖。

修改旧帖请编辑对应文件夹中的 `index.md`；重新上传图片会另建一帖。

日常发布不改写 Git 历史。历史清理默认关闭，只有手动触发 `workflow_dispatch` 并启用 `compact_image_history=true` 时才运行；原件和未推送素材先备份到仓库外，维护后将旧本地副本对齐新 `main` 或重新克隆，不要合并旧历史。

[构建与维护](../README.md#发布图片)
