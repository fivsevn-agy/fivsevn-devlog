---
id: "netcom-readme"
title: "netcom 板块说明"

module: "netcom"
submodule: "guide"
topic: "guide"

type: "note"
status: "active"
canonical: true

summary: "说明netcom 板块说明。"

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
updated: "2026-10-13"
metadata_updated: "2026-10-13"
---
# netcom 板块说明

```text
fivsevn-devlog/netcom/
├── README.md     本说明
├── index.md      文章目录（列表自动生成）
├── _drafts/      长文草稿
├── assets/       现有配图与辅助文件
├── ai/           AI 技术
├── architecture/ 系统架构
├── cs/           计算机基础
├── digital/      数字通信
├── lora/         LoRa / Meshtastic
├── math/         数学基础
├── mcu/          微控制器
├── methods/      方法与工程概念
├── protocol/     协议
├── rf/           射频与天线
└── software/     软件与开发
```

- **[netcom 页面](https://devlog.fivsevn.com/netcom/)**：通信、计算机与工程笔记，包括学习笔记、设备记录和译文。
- **当前只有长文**：直接在 GitHub 编辑和存档，Pages 展示；不经过 WordPress，也没有单图或 trigger 发布步骤。
- 文章按主题目录存放；以上为当前结构，后续可增减。

---

## 1. 新建草稿

- 在 [`netcom/_drafts/`](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/netcom/_drafts)第一层新建 `.md` → 提交并推送到 `main`。
- 自动处理后先拉取，再继续编辑；草稿不进入文章目录。

> [草稿任务](https://github.com/fivsevn-agy/fivsevn-devlog/actions/workflows/apply-draft-frontmatter.yml)启动 → [脚本](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/scripts/apply_draft_frontmatter.py)提取正文标题 → 补 metadata、改名为 `netcom-draft-001.md` 等占位文件 → 自动提交。已有 frontmatter 的文件跳过，不反复改名。

## 2. 发布正式文章

- 放入[对应主题目录](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/netcom)，如 `lora/`、`rf/`、`software/`，不另按年份建目录。
- 按 [metadata 规范](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/spec-content-frontmatter-001.md)填写字段，使用 `module: netcom`、`status: active`、`visibility: public` → 提交并推送。
- **草稿转正式稿**：移出 `_drafts`，整理正式文件名、`id` 和 metadata；只改状态、不移动文件，不会进目录。

> [目录任务](https://github.com/fivsevn-agy/fivsevn-devlog/actions/workflows/publish-pages.yml)扫描文章 → 读取标题、日期、状态等 metadata → 重算 [`netcom/index.md`](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/netcom/index.md)的列表 → 有差异才自动提交。
> 网站构建时，Jekyll 将 Markdown 转成 HTML → GitHub Pages 提供访问。目录更新与页面部署分开检查。

## 3. 新建译文

- 分享原文网址 → 运行 [`translate & post`](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/blogops/docs/auto-translation-shortcut.md) → 把提示词文件交给 AI → 检查译稿、来源与公开发布授权 → 按正式文章流程提交。
- 使用 `module: netcom`、`type: translation`、`source_of_truth: translation`，保留原文链接；详见[翻译规范](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/spec-content-translation-001.md)。

> 快捷指令将网址交给 Jina Reader → 获取网页 Markdown → 拼入翻译要求和规范链接 → 生成日期命名的提示词文件。AI 再生成译稿；提示词不是最终文章，快捷指令不直接发文。

## 4. 修改文章

- **正文小改／大改**：改原文件，保留文件名、`id`、`created`，手动维护 `updated`；不新增目录项。
- **标题**：同时改 `title` 和正文 `# 标题`，不必改文件名；目录替换原标题，文章地址不变。
- **日期**：有有效 `created` 时，只改 `updated` 不置顶；改 `created` 会调整目录日期与排序。同一天内，改标题可能影响排序。
- **重命名／移动**：目录改用新路径；检查旧网址、文章互链和图片路径。
- **复制为另一篇**：两份都符合收录条件时会出现两项；新文章使用新 `id`。
- **隐藏／删除**：`status: hidden` 只移出目录，不等于关闭网址；删除文件后，还要检查部署结果和旧链接。公开仓库不用于保密。

> [索引脚本](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/scripts/update_module_indexes.py)按当前文件**替换原列表，不追加修改记录**，不按 `id` 去重；`README.md`、`_drafts/` 和 `assets/` 不作为文章收录。译文链接本地译稿，`original_url` 保留为来源信息。

## 5. 检查与维护

- 保存 → commit → 推送到 `main`；只在本地保存不会启动远端任务。
- 改文章 metadata，不手改 [`index.md`](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/netcom/index.md) 的 `AUTO-INDEX` 列表。
- 查看 [devlog Actions](https://github.com/fivsevn-agy/fivsevn-devlog/actions) → 检查目录、Pages 部署 → 打开 [netcom 页面](https://devlog.fivsevn.com/netcom/)。

---

核对日期：2026-10-13。按当前目录、脚本与工作流记录，后续可调整。
