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
updated: '2026-10-30'
---
# Fieldlog 图片入口

把图片上传到 **`fivsevn-agy/fivsevn-devlog` 的 `natsci/fieldlog/trigger_imgs/`**，提交并推送到 `main` 即可发布。目录名是 `trigger_imgs`（带 s）。

1. Working Copy / 快捷指令先拉取最新的 `main`；网页上传可直接[点这里选图](https://github.com/fivsevn-agy/fivsevn-devlog/upload/main/natsci/fieldlog/trigger_imgs)。
2. 保存图片到本目录，保留手机原文件名。快捷指令的目标仓库和路径也设为上面的地址。
3. 配文写在提交的 **可选详细说明（extended description）** 中，支持 Markdown；留空则只发图。提交并推送到 `main`。
4. 等待 [Publish fieldlog](https://github.com/fivsevn-agy/fivsevn-devlog/actions/workflows/publish-fieldlog.yml) 和 GitHub Pages 部署完成，打开 [Fieldlog](https://devlog.fivsevn.com/natsci/fieldlog/) 核对图片；点击绿色时间码进入详情核对配文。

> **格式与批量**：支持 JPG/JPEG、PNG、WebP、GIF、HEIC/HEIF。一次上传多张，每张各发一帖，共用这次配文。
>
> **自动处理**：按上传提交的北京时间生成时间码和默认标题、转为 WebP、保存为 `YYYY/MM/唯一id/index.md` 与同目录 `assets/` 图片，再生成列表和详情页。同次提交重跑不会重复发帖或覆盖已保存的修改。
>
> **标题与配文**：提交摘要用于说明这次提交，不作为帖子标题。发布后可修改帖子 `index.md` 的 `title`；留空时显示时间。配文写在正文，只在详情页显示。
>
> **入口原图**：目前保留，不自动删除；这是与 flux、savour 的区别。删除入口图片不会撤回已提交的发布事件或帖子。
>
> **修改旧帖**：编辑已保存帖子文件夹中的 `index.md`，替换图片也在该帖的 `assets/` 中处理。重新上传图片会生成新帖；同名同内容没有 Git 变化时不会触发，重发可用新文件名。

本 README 不会被当作图片或帖子发布。

[完整发布与维护说明](../README.md) · [flux 图片入口](https://github.com/fivsevn/fivsevn-flux/blob/main/trigger_imgs/README.md) · [savour 图片入口](https://github.com/fivsevn/fivsevn-savour/blob/main/trigger_imgs/README.md)
