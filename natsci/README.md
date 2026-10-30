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
updated: "2026-10-30"
metadata_updated: "2026-10-30"
---
# natsci 板块说明

```text
fivsevn-devlog/natsci/
├── README.md       本说明
├── index.md        文章目录（列表自动生成）
├── _drafts/        长文草稿
├── assets/         现有配图与辅助文件
├── fieldlog/       自然观察影像、配文与独立展示页面
├── taxonomy/       生物分类与物种笔记
├── paleontology/   古生物学
└── ethnobiology/   民族生物学
```

- **[devlog fieldlog](https://devlog.fivsevn.com/natsci/fieldlog/)**：自然观察影像记录，保留观察窗口式视觉效果，每则图片和配文在同一文件夹维护。
- **[devlog natsci](https://devlog.fivsevn.com/natsci/)**：自然科学笔记、分类资料与译文；按主题目录保存，不按年份分组。内容类别后续可增减。

---

## 1. 影像记录｜fieldlog

### 新建

- 图片放入本仓库 [`natsci/fieldlog/trigger_imgs/`](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/natsci/fieldlog/trigger_imgs) → Working Copy 或 GitHub 提交并推送到 `main`。
- **每张新图片一条记录**，自动保存为 `fieldlog/YYYY/MM/唯一id/index.md` 与同目录 `assets/` WebP 图片。
- **配文**：写在提交的 extended description，只在详情页显示；列表点击绿色时间码进入详情页。

> [fieldlog 发布任务](https://github.com/fivsevn-agy/fivsevn-devlog/actions/workflows/publish-pages.yml)读取提交历史 → 保存图片和配文 → 生成统一 `_site/` 网站产物 → 部署 GitHub Pages。日期取提交时间并转换为北京时间；不调用 WordPress。完整字段、手动发布和注意事项见 [fieldlog 说明](fieldlog/README.md)。

### 修改与撤下

- **改标题、日期、配文**：编辑原帖文件夹内的 `index.md`，保留 `id` 和目录名。
- **替换图片**：修改原帖 `assets/` 图片，或更新 `extra.image` 字段；发布任务统一保存为 WebP。
- **从页面撤下**：把 `status` 改为 `hidden` 后提交；下一次构建会移除详情 HTML。公开仓库仍保留历史与原图。

> 重传入口图片会生成新帖，不会更新原帖。使用共享规范的 frontmatter；发布时间、图片等展示字段放在 `extra`，发布状态由 `status` 和 `visibility` 控制。

---

## 2. 长文章｜devlog

### 新建草稿

- 在 [`natsci/_drafts/`](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/natsci/_drafts)第一层新建 `.md` → 提交并推送 → 自动处理后先拉取，再继续编辑。

> [草稿任务](https://github.com/fivsevn-agy/fivsevn-devlog/actions/workflows/apply-draft-frontmatter.yml)运行 → [脚本](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/scripts/apply_draft_frontmatter.py)提取正文标题 → 补 metadata、改名为 `natsci-draft-001.md` 等占位文件 → 自动提交。已有 frontmatter 的文件跳过；草稿不进文章目录。

### 发布正式文章

- 放入 [`taxonomy/`](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/natsci/taxonomy)、[`paleontology/`](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/natsci/paleontology)或 [`ethnobiology/`](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/natsci/ethnobiology)等对应主题目录。
- 按 [metadata 规范](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/spec-content-frontmatter-001.md)填写字段，使用 `module: natsci`、`status: active`、`visibility: public` → 提交并推送。
- **草稿转正式稿**：移出 `_drafts`，整理正式文件名、`id` 和 metadata；只改状态、不移动文件，不会进目录。

> [目录任务](https://github.com/fivsevn-agy/fivsevn-devlog/actions/workflows/publish-pages.yml)扫描文章 → 读取 metadata → 重算 [`natsci/index.md`](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/natsci/index.md)的列表 → 有差异才提交。
> 网站构建时，Jekyll 将 Markdown 转为 HTML → GitHub Pages 提供访问；不经过 WordPress，也不会自动生成一条影像记录。

### 新建译文

- 分享原文网址 → 运行 [`translate & post`](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/blogops/docs/auto-translation-shortcut.md) → 把提示词文件交给 AI → 检查译稿、来源与公开发布授权 → 按正式文章流程提交。
- 使用 `module: natsci`、`type: translation`、`source_of_truth: translation`，保留原文链接；详见[翻译规范](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/spec-content-translation-001.md)。

> 快捷指令将网址交给 Jina Reader → 获取网页 Markdown → 拼入翻译要求和规范链接 → 生成日期命名的提示词文件。AI 再生成译稿；快捷指令不直接发文。

### 修改文章

- **正文小改／大改**：改原文件，保留文件名、`id`、`created`，手动维护 `updated`；不新增目录项。
- **标题**：同时改 `title` 和正文 `# 标题`；不必改文件名，目录替换原标题，文章地址不变。
- **日期**：有有效 `created` 时，只改 `updated` 不置顶；同一天内改标题可能影响排序。
- **重命名／移动／复制**：移动后检查旧网址、互链和图片路径；保留两份可收录文件就会出现两项。
- **隐藏**：设为 `status: hidden`，只移出目录，不等于私密存储或关闭网址。

> [索引脚本](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/scripts/update_module_indexes.py)重新扫描文件并**替换原列表，不追加修改记录**；不按 `id` 去重。`README.md`、`_drafts/` 和 `assets/` 不作为文章收录。

## 3. 检查与维护

- **影像记录**：查看 [fieldlog 发布任务](https://github.com/fivsevn-agy/fivsevn-devlog/actions/workflows/publish-pages.yml) → 检查 [fieldlog 页面](https://devlog.fivsevn.com/natsci/fieldlog/)。
- **长文**：查看 [devlog Actions](https://github.com/fivsevn-agy/fivsevn-devlog/actions) → 检查目录、Pages 部署和[实际页面](https://devlog.fivsevn.com/natsci/)。
- 保存 → commit → 推送到 `main`；不手改 `index.md` 的 `AUTO-INDEX` 列表，不把私密资料放入公开仓库。

---

核对日期：2026-10-30。按当前目录、脚本与工作流记录，后续可调整。
