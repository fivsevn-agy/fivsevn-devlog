# natsci 板块说明

```text
fivsevn-devlog/natsci/
├── README.md       本说明
├── index.md        文章目录（列表自动生成）
├── _drafts/        长文草稿
├── assets/         现有配图与辅助文件
├── taxonomy/       生物分类与物种笔记
├── paleontology/   古生物学
└── ethnobiology/   民族生物学

fivsevn-assets/natsci/
├── README.md
└── fieldlog/       WordPress 单图发布入口
```

- **[WordPress natsci](https://fivsevn.com/natsci/)**：自然观察的图像记录，观察窗口式视觉效果在 WordPress 维护。
- **[devlog natsci](https://devlog.fivsevn.com/natsci/)**：自然科学笔记、分类资料与译文；按主题目录保存，不按年份分组。内容类别后续可增减。

---

## 1. 影像记录｜WordPress

### 新建

- 手机分享图片 → 运行[图片快捷指令](https://github.com/fivsevn/fivsevn-assets/blob/main/docs/feat%20Add%20image%20asset.shortcut) → 选择 [`natsci/fieldlog`](https://github.com/fivsevn/fivsevn-assets/tree/main/natsci/fieldlog) → Working Copy 提交并推送到 `main`。
- **每张新图片一条记录**；实际 WordPress 分类是 `fieldlog`，不是 `natsci`；不自动附加标签。
- **配文**：写在提交的 extended description，会公开显示；不要混入技术操作说明。

> [图片发布任务](https://github.com/fivsevn/fivsevn-assets/actions/workflows/publish-image-posts.yml)检查本次推送 → [脚本](https://github.com/fivsevn/fivsevn-assets/blob/main/scripts/publish_image_posts.py)生成 CDN 图片区块和配文段落 → 用 Actions Secrets 中的账号与应用密码调用 WordPress REST API → 新建 `fieldlog` 帖子。  
> 标题取图片提交时间；图片留在 assets 仓库，不上传 WordPress 媒体库。WordPress 页面负责视觉展示。

### 修改与撤下

- **小改、大改、改标题或配文**：在 [WordPress 后台](https://fivsevn.com/wp-admin/)更新原帖，不靠修改提交说明更新旧帖。
- **替换图片**：保存好图片后，更新原帖图片链接；重命名或移动源图时检查旧链接。
- **撤下**：在 WordPress 处理原帖；删除仓库图片不会删除帖子。

> 脚本按图片路径生成 slug → 已有帖子就跳过。上传新路径可能另发一条，不会自动更新原帖。

---

## 2. 长文章｜devlog

### 新建草稿

- 在 [`natsci/_drafts/`](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/natsci/_drafts)第一层新建 `.md` → 提交并推送 → 自动处理后先拉取，再继续编辑。

> [草稿任务](https://github.com/fivsevn-agy/fivsevn-devlog/actions/workflows/apply-draft-frontmatter.yml)运行 → [脚本](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/scripts/apply_draft_frontmatter.py)提取正文标题 → 补 metadata、改名为 `natsci-draft-001.md` 等占位文件 → 自动提交。已有 frontmatter 的文件跳过；草稿不进文章目录。

### 发布正式文章

- 放入 [`taxonomy/`](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/natsci/taxonomy)、[`paleontology/`](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/natsci/paleontology)或 [`ethnobiology/`](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/natsci/ethnobiology)等对应主题目录。
- 按 [metadata 规范](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/spec-content-frontmatter-001.md)填写字段，使用 `module: natsci`、`status: active`、`visibility: public` → 提交并推送。
- **草稿转正式稿**：移出 `_drafts`，整理正式文件名、`id` 和 metadata；只改状态、不移动文件，不会进目录。

> [目录任务](https://github.com/fivsevn-agy/fivsevn-devlog/actions/workflows/update-indexes.yml)扫描文章 → 读取 metadata → 重算 [`natsci/index.md`](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/natsci/index.md)的列表 → 有差异才提交。  
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

- **影像记录**：查看[图片发布任务](https://github.com/fivsevn/fivsevn-assets/actions/workflows/publish-image-posts.yml) → 检查 [WordPress 页面](https://fivsevn.com/natsci/)。
- **长文**：查看 [devlog Actions](https://github.com/fivsevn-agy/fivsevn-devlog/actions) → 检查目录、Pages 部署和[实际页面](https://devlog.fivsevn.com/natsci/)。
- 保存 → commit → 推送到 `main`；不手改 `index.md` 的 `AUTO-INDEX` 列表，不把私密资料放入公开仓库。

---

核对日期：2026-10-13。按当前目录、脚本与工作流记录，后续可调整。
