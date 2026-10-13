# posts 板块说明

- **[WordPress posts](https://fivsevn.com/posts/)**：随手发文字、图片。
- **[flux](https://flux.fivsevn.com/)**：同步 WordPress，作为静态备份与迁移试验。
- **[devlog posts](https://devlog.fivsevn.com/posts/)**：保存需要长期整理、修改和查阅的文章。

## 1. 短内容｜WordPress

### 新建

- **文字**：替换 [`trigger.md`](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/posts/_wordpress/trigger.md) 正文，保留发布配置 → 提交并推送 → 新发一条。查看[文字发布任务](https://github.com/fivsevn-agy/fivsevn-devlog/actions/workflows/publish-wp-trigger.yml)。
- **图片**：快捷指令选择 [`post/stream`](https://github.com/fivsevn/fivsevn-assets/tree/main/post/stream) → Working Copy 提交并推送 → 每张新图片新发一条。查看[图片发布任务](https://github.com/fivsevn/fivsevn-assets/actions/workflows/publish-image-posts.yml)。
- **图片配文**：提交的 extended description 会作为公开配文，不放技术操作说明。详见[图片发布说明](https://github.com/fivsevn/fivsevn-assets/blob/main/README.md#image-post-automation)。

### 修改

- **小改、大改、改标题**：直接在 [WordPress 后台](https://fivsevn.com/wp-admin/)更新原帖，**不回头改 trigger**。
- **原始发布时间**：尽量不改，避免 flux 生成新包并留下旧包。
- **另发一条**：重新使用 trigger 或图片快捷指令，旧帖保留。

### flux 同步

- **近期内容**：[自动同步任务](https://github.com/fivsevn/fivsevn-flux/actions/workflows/sync-live.yml)每天定时检查 5 次，范围为按发表日期排序的最新 **77 条**公开 posts；自动管理的包使用 `sync: auto`。不是实时同步。
- **旧帖修改**：手动运行 [Full rescan WordPress posts](https://github.com/fivsevn/fivsevn-flux/actions/workflows/full-rescan.yml)，当前上限 **9999 条**。
- **只运行 [Build flux](https://github.com/fivsevn/fivsevn-flux/actions/workflows/build.yml)**：只构建仓库已有内容，不读取 WordPress。
- **撤下、转私密、删除**：WordPress 处理后，还要另行撤下 [flux 对应副本](https://github.com/fivsevn/fivsevn-flux/tree/main/flux)；当前**不会自动同步删除**。

## 2. 长文章｜devlog

### 新建

- **草稿**：放进 [`posts/_drafts/`](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/posts/_drafts) 第一层并提交。无 frontmatter 时自动补 metadata、生成占位文件名，不进入文章目录。查看[草稿处理任务](https://github.com/fivsevn-agy/fivsevn-devlog/actions/workflows/apply-draft-frontmatter.yml)。
- **正式文章**：放进[对应年份目录](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/posts)，按 [metadata 规范](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/spec-content-frontmatter-001.md)补齐字段，设置 `status: active`、`visibility: public`，提交后自动更新目录。
- **草稿转正式稿**：移出 `_drafts`，整理正式文件名、`id` 和 metadata；只改状态、不移动文件，不会进入目录。

### 修改

- **正文小改／大改**：直接改原文件，保留文件名、`id`、`created`，手动维护 `updated`。**不新增目录项。**
- **标题**：同时改 metadata 的 `title` 和正文 `# 标题`，不必改文件名。**目录替换原标题，不重复收录；只改标题，原网址不变。**
- **日期**：有有效 `created` 时，仅改 `updated` 不会置顶；改 `created` 会影响目录日期与排序。同一天内，改标题可能调整排序。
- **重命名／移动文件**：目录更新路径；检查原网址、文章互链和图片路径。
- **复制为另一篇**：两份都符合收录条件时，目录出现两项；新文章使用新 `id`。
- **隐藏**：设置 `status: hidden`，移出目录；不代表文件私密或网址失效。

## 3. 共用备忘

- **提交**：推送到 `main`；手机本地保存、commit 不等于已上线。
- **目录**：修改文章 metadata，不手改 [`index.md`](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/posts/index.md) 的 `AUTO-INDEX` 区域。[目录任务](https://github.com/fivsevn-agy/fivsevn-devlog/actions/workflows/update-indexes.yml)重新运行时替换原列表，不重复追加；具体规则见[索引脚本](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/scripts/update_module_indexes.py)。
- **README**：直接修改，不作为普通文章进入目录。
- **ChatGPT 文章**：沿用“ChatGPT 写给五月七日的……”命名，保留具体主题，不另设系列名。
- **上线检查**：查看 [devlog Actions](https://github.com/fivsevn-agy/fivsevn-devlog/actions) 或 [flux Actions](https://github.com/fivsevn/fivsevn-flux/actions)，任务完成后检查部署和实际页面。

---

核对日期：2026-10-13。本文只覆盖 posts，按当前脚本与工作流记录。
