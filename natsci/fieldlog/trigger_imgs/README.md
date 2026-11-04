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

1. 推荐网页或直接调用 GitHub 的快捷指令上传；网页可直接[点这里选图](https://github.com/fivsevn-agy/fivsevn-devlog/upload/main/natsci/fieldlog/trigger_imgs)。
2. 保留手机原文件名；配文写进提交的 **可选详细说明（extended description）**，支持 Markdown，留空则只发图。
3. 等待[发布任务](https://github.com/fivsevn-agy/fivsevn-devlog/actions)完成，再打开 [Fieldlog](https://devlog.fivsevn.com/natsci/fieldlog/) 检查图片和配文。

支持 JPG/JPEG、PNG、WebP、GIF、HEIC/HEIF。一次多张，每张各发一帖，共用本次配文。系统按提交的北京时间命名、转为 WebP（归档只保留 WebP）、补齐文章资料；核验线上页面和图片后清理入口原图及已转换旧图的 `main` 历史。失败会保留原图，同次提交重跑不重复发帖。

修改旧帖请编辑对应文件夹中的 `index.md`；重新上传图片会另建一帖。

历史清理会更新版本编号；旧 Working Copy 副本请重新克隆，不要合并旧历史。

[构建与维护](../README.md#发布图片)
