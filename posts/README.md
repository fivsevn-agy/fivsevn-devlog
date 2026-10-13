# posts 板块说明

```text
fivsevn-devlog/posts/
├── README.md               本说明
├── index.md                文章目录（列表自动生成）
├── 2019/                   2019 年存档
├── 2025/                   2025 年存档
├── 2026/                   2026 年文章
├── _drafts/                长文草稿
├── _wordpress/
│   └── trigger.md          WordPress 文字发布入口
└── ai-discourse-analysis/  AI 话语分析独立栏目
```

- **[WordPress posts](https://fivsevn.com/posts/)**：随手发文字、图片。
- **[flux](https://flux.fivsevn.com/)**：同步 WordPress，作为静态备份与迁移试验。
- **[devlog posts](https://devlog.fivsevn.com/posts/)**：保存需要长期整理、修改和查阅的文章。

---

## 1. 短内容｜WordPress

### 新建文字

- 替换 [`trigger.md`](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/posts/_wordpress/trigger.md) 正文，保留发布配置 → 提交并推送 → 新发一条。

> [文字发布任务](https://github.com/fivsevn-agy/fivsevn-devlog/actions/workflows/publish-wp-trigger.yml)启动 → [脚本](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/scripts/publish_wp_text.py)读取本次提交的 `trigger.md` → 正文转成 HTML → 调用 [WordPress REST API](https://developer.wordpress.org/rest-api/reference/posts/) 新建帖子。  
> 脚本用 Actions Secrets 中的 WordPress 账号与应用密码验证身份；配置区不进入正文，标题按运行时间生成。

### 新建图片

- 快捷指令选择 [`post/stream`](https://github.com/fivsevn/fivsevn-assets/tree/main/post/stream) → Working Copy 提交并推送 → 每张新图片新发一条。
- **配文**：写在提交的 extended description，不放技术操作说明。

> [图片发布任务](https://github.com/fivsevn/fivsevn-assets/actions/workflows/publish-image-posts.yml)检查本次推送的图片 → [脚本](https://github.com/fivsevn/fivsevn-assets/blob/main/scripts/publish_image_posts.py)把 CDN 图片链接和配文组装成 WordPress 区块 → 调用 REST API 发文。  
> 图片留在 assets 仓库，不上传 WordPress 媒体库；脚本按图片路径生成 slug，查到已有帖子就跳过。详见[图片发布说明](https://github.com/fivsevn/fivsevn-assets/blob/main/README.md#image-post-automation)。

### 修改原帖

- **小改、大改、改标题**：在 [WordPress 后台](https://fivsevn.com/wp-admin/)更新原帖，**不回头改 trigger**。
- **原始发布时间**：尽量不改；flux 按这个时间定位文章包，改动可能另建新包并留下旧包。
- **另发一条**：重新使用 trigger 或图片快捷指令，旧帖保留。

> WordPress 保存原帖新版 → flux 下次扫描到它时，用标题、正文等信息计算 `source_hash` → 与副本记录对比 → 有变化就更新原包。  
> 正常同步以 WordPress 为准，不回写 trigger；`sync: manual` 的包跳过正文同步。改 trigger 再提交，默认是新帖，不是修改旧帖。

### flux 同步与撤下

- **近期内容**：[自动同步任务](https://github.com/fivsevn/fivsevn-flux/actions/workflows/sync-live.yml)每天定时检查 **5 次**，范围为按发表日期排序的最新 **77 条**公开 posts；自动管理的包使用 `sync: auto`。不是实时同步。
- **旧帖修改**：手动运行 [Full rescan WordPress posts](https://github.com/fivsevn/fivsevn-flux/actions/workflows/full-rescan.yml)，当前上限 **9999 条**。
- **只运行 [Build flux](https://github.com/fivsevn/fivsevn-flux/actions/workflows/build.yml)**：只构建仓库已有内容，不读取 WordPress。
- **撤下、转私密、删除**：WordPress 处理后，还要另行撤下 [flux 对应副本](https://github.com/fivsevn/fivsevn-flux/tree/main/flux)；当前**不会自动同步删除**。

> [同步脚本](https://github.com/fivsevn/fivsevn-flux/blob/main/scripts/sync-from-live.py)读取 WordPress REST API → 正文转 Markdown、尽量下载图片 → 保存文章包到 `flux/YYYY/MM/{id}/` → 自动提交 → 启动 Build flux。  
> [构建脚本](https://github.com/fivsevn/fivsevn-flux/blob/main/scripts/build.py)读取文章包 → 生成 HTML 时间线与文章页 → 提交回仓库；随后检查 Pages 部署和实际网页。当前同步任务未启用删除检查。

---

## 2. 长文章｜devlog

### 目前的内容

以下是现有内容概览，后续可增减，不必另建分类目录。

- **旧 WordPress 存档**：早期内容按年份保留，见 [2019](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/posts/2019)、[2025](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/posts/2025)；保留原文来源与链接。
- **自己写的文章**：随笔、观察、资料整理与研究笔记，按年份存放。
- **译文存档**：外文材料的中文译稿，使用 `type: translation`，保留原文链接与翻译说明。
- **AI 写给五月七日**：知识讲解、方法手册与指导笔记；沿用“ChatGPT 写给五月七日的……”命名，例如[游戏开发流程手册](https://devlog.fivsevn.com/posts/2026/posts-2026-umwelt-game-development-handbook-001.html)。
- **[AI 话语分析](https://devlog.fivsevn.com/posts/ai-discourse-analysis/)**：AI 辅助拆解公共讨论的论证结构；在首页底部 `Section` 单独列出，[栏目目录](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/posts/ai-discourse-analysis/index.md)独立维护。

### 新建草稿

- 放进 [`posts/_drafts/`](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/posts/_drafts) 第一层 → 提交并推送。
- 自动处理后先拉取，再继续编辑；草稿不进入文章目录。

> [草稿处理任务](https://github.com/fivsevn-agy/fivsevn-devlog/actions/workflows/apply-draft-frontmatter.yml)启动 → [脚本](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/scripts/apply_draft_frontmatter.py)提取正文标题 → 补 metadata、生成占位文件名 → 自动提交回仓库。已有 frontmatter 的文件跳过，不反复改名。

### 新建译文｜translate & post

- 分享原文网址 → 运行 [`translate & post`](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/blogops/docs/auto-translation-shortcut.md) → 将生成的提示词文件分享给 ChatGPT。无分享输入时读取剪贴板。
- 按[翻译规范](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/spec-content-translation-001.md)检查译稿、metadata、原文链接与公开发布授权 → 按下方正式文章流程保存、提交；抓取不完整时先补齐原文。

> 快捷指令给原文网址加上 `https://r.jina.ai/` 前缀 → [Jina Reader](https://jina.ai/reader/)抓取网页、返回 Markdown → 拼入原文网址、翻译要求和规范链接 → 生成日期命名的 `.md` **提示词文件**。  
> 分享给 AI → AI 生成带 metadata 的**中文译稿**；日期文件不是最终译文，快捷指令本身不直接发文。提交译稿后，再由目录任务和 Pages 处理发布。

### 发布正式文章

- **直接新建**：放进[对应年份目录](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/posts) → 按 [metadata 规范](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/spec-content-frontmatter-001.md)补齐字段 → 设置 `status: active`、`visibility: public` → 提交并推送。
- **草稿转正式稿**：移出 `_drafts`，整理正式文件名、`id` 和 metadata。只改状态、不移动文件，不会进入目录。

> [目录任务](https://github.com/fivsevn-agy/fivsevn-devlog/actions/workflows/update-indexes.yml)扫描文章 → 读取标题、日期、状态等 metadata → 重算 [`index.md`](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/posts/index.md) 的文章列表 → 有差异才自动提交。  
> 网站构建时，[Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll)把 Markdown 转成 HTML，GitHub Pages 提供访问；不经过 WordPress。目录更新与网站部署分开检查。

### 修改文章

- **正文小改／大改**：改原文件，保留文件名、`id`、`created`，手动维护 `updated`。**不新增目录项。**
- **标题**：同时改 metadata 的 `title` 和正文 `# 标题`，不必改文件名。**目录替换原标题，不重复收录；只改标题，原网址不变。**
- **日期**：有有效 `created` 时，仅改 `updated` 不会置顶；改 `created` 会调整目录日期与排序。同一天内，改标题可能调整排序。
- **重命名／移动文件**：目录更新路径；检查原网址、文章互链和图片路径。
- **复制为另一篇**：两份都符合收录条件时，目录出现两项；新文章使用新 `id`。
- **隐藏**：设为 `status: hidden`，移出目录；不代表文件私密或网址失效。

> [索引脚本](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/scripts/update_module_indexes.py)按当前文件重新生成列表，**替换、不追加**；不按标题或 `id` 去重。`title` 提供目录文字，路径提供本地链接，日期决定排序。

---

## 3. 共用备忘

- **提交**：保存 → 本地 commit → 推送到 `main`；只在手机本地保存、commit，不会启动远端任务。
- **目录**：改文章 metadata，不手改 [`index.md`](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/posts/index.md) 的 `AUTO-INDEX` 区域；脚本会替换这部分。
- **README**：直接改；索引脚本按文件名排除它，不作为普通文章收录。
- **上线检查**：打开 [devlog Actions](https://github.com/fivsevn-agy/fivsevn-devlog/actions) 或 [flux Actions](https://github.com/fivsevn/fivsevn-flux/actions) → 查看处理结果 → 检查部署 → 打开实际页面。

---

核对日期：2026-10-13。本文只覆盖 posts，按当前脚本与工作流记录。
