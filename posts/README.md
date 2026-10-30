---
id: "posts-readme"
title: "posts 板块说明"

module: "posts"
submodule: "guide"
topic: "guide"

type: "note"
status: "active"
canonical: true

summary: "说明posts 板块说明。"

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
# posts 板块说明

```text
fivsevn-devlog/posts/
├── README.md               本说明
├── index.md                文章目录（列表自动生成）
├── 2019/                   2019 年存档
├── 2025/                   2025 年存档
├── 2026/                   2026 年文章
├── _drafts/                长文草稿
└── ai-discourse-analysis/  AI 话语分析独立栏目
```

- **[flux](https://flux.fivsevn.com/)**：随手发文字、图片，直接从 GitHub 发布。
- **[devlog posts](https://devlog.fivsevn.com/posts/)**：保存需要长期整理、修改和查阅的文章。

---

## 1. 短内容｜flux

### 新建文字

1. 打开 flux 仓库的 [`trigger_text.md`](https://github.com/fivsevn/fivsevn-flux/blob/main/trigger_text.md)。
2. 保留文件顶部的配置区，设置发布状态和标题：

   ```yaml
   status: published
   title: ""
   ```

3. 在配置区结束线 `---` 后替换正文。正文用 Markdown，链接写成 `[文字](网址)`。
4. 提交并推送到 flux 仓库的 `main`，等待 [Publish flux](https://github.com/fivsevn/fivsevn-flux/actions/workflows/build.yml) 完成，再打开网页确认。

> **标题**：`title` 留空时，系统用提交时的北京时间生成标题；填写 `title: "你的标题"` 则显示自定义标题。下一条要恢复时间标题，把 `title` 清空。
>
> **发布时间**：下方实际发布时间独立保存，发布后保持不变。修改标题不会改变它。
>
> **草稿**：`status: draft` 只保存草稿，不上网页；GitHub 仓库中的文件仍然公开。

### 新建图片

**首次设置快捷指令**

1. 将 flux 分支的“存储文件”目标设为 **fivsevn-flux** 仓库，目录选为 [`trigger_imgs/`](https://github.com/fivsevn/fivsevn-flux/tree/main/trigger_imgs)。
2. 在保存图片前，通过 Working Copy 自动拉取该仓库最新的 `main`。
3. 在保存图片后，提交并推送到同一仓库的 `main`；快捷指令中已有的提交、推送动作也要指向 fivsevn-flux。

**日常发布**

1. 选择图片，运行快捷指令。保留手机原文件名即可。
2. 需要配文时，写在提交的 extended description 中，支持 Markdown；不需要配文就留空。
3. 等待 [Publish flux](https://github.com/fivsevn/fivsevn-flux/actions/workflows/build.yml) 完成，打开 flux 核对图片和配文。

> **文件格式**：支持 JPG/JPEG、PNG、WebP、GIF、HEIC/HEIF。手机不用提前转换格式或创建发布包。
>
> **自动命名**：仓库按上传提交的北京时间命名，例如 `20261018-103012-01.webp`；同批多张自动加序号。原稿清理后，下次可以继续上传同名文件。
>
> **批量与配文**：同次提交多张图片时，每张各生成一帖，使用同一段配文；不写配文则只显示图片。
>
> **图片处理**：仓库自动转 WebP、保存发布包、制作网页并发布。核验公开页面和图片后，清除入口原图；失败时保留原图，重跑不重复发帖。
>
> 完整设置见 [图片目录说明](https://github.com/fivsevn/fivsevn-flux/blob/main/trigger_imgs/README.md)。

### 修改旧帖

1. 在 flux 点击该帖标题，进入独立页面。
2. 按网址找到 [flux 仓库](https://github.com/fivsevn/fivsevn-flux/tree/main/flux)中的文件：`/page/年/月/帖子编号/` 对应 `flux/年/月/帖子编号/index.md`。
3. 修改 `index.md` 的正文、配文或顶部 `title`。需要换图时，在该发布包的 `assets/` 中保存图片，并更新正文里的图片链接。
4. 提交并推送，等待部署完成，再核对首页和独立页面。

> 保留 `extra.published_at`、`id`、目录和来源字段。修改标题不会改变原网址、下方发布时间或时间排序。存档使用共享 frontmatter，展示与发布资料放在 `extra`；入口文件仍可只填写简短配置。
>
> **trigger 只负责新发一条。修改旧帖要改对应的发布包；再次提交 trigger 会生成新帖。**

### 删除或恢复旧帖

**从网页撤下，保留仓库文件**

1. 打开该帖的 `index.md`，将顶部状态改为 `status: hidden`。
2. 提交并推送，等待部署完成。
3. 确认首页和原独立页面都不再显示该帖。

**恢复已撤下的帖子**

1. 将该帖状态改回 `status: published`。
2. 提交并推送，确认原网址恢复显示。

**连发布包一起删除**

1. 确认包内附件没有被其他帖子引用。
2. 删除整个 `flux/年/月/帖子编号/` 文件夹及其附件，再提交并推送。
3. 部署完成后，确认首页不再显示该帖，原独立页面无法访问。

> 恢复已撤下的帖子会保留原网址和发布时间。
>
> 删除后 GitHub 历史仍保留原文件；误删时可从历史恢复整个发布包。不要通过删除 trigger 来删除旧帖。

### 何时生效

1. 将文字、图片或发布包的改动推送到 flux 仓库的 `main`。
2. 打开 [Publish flux](https://github.com/fivsevn/fivsevn-flux/actions/workflows/build.yml)，检查导入、构建、部署和线上核验是否全部成功。
3. 打开 flux 首页和该帖独立页面；图片帖同时核对实际图片是否显示。

> **触发方式**：提交后直接启动，无需等待定时检查。修改或删除发布包也会启动同一任务；`status: draft` 只存档，不上网页。
>
> **失败处理**：查看失败步骤，修复原因后重跑。同一次提交不会被重复导入；线上核验通过后，任务才显示成功。
>
> 日常发布方法看本节；文件维护和构建细节见 [flux 后台说明](https://github.com/fivsevn/fivsevn-flux/blob/main/README.md#edit-an-existing-entry)。短帖流程已不经过 WordPress，也不读取 assets 的 flux 图片目录。

---

## 2. 长文章｜devlog

### 目前的内容

- **旧 WordPress 存档**：早期内容按年份保留，见 [2019](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/posts/2019)、[2025](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/posts/2025)；保留原文来源与链接。
- **自己写的文章**：随笔、观察、资料整理与研究笔记，按年份存放。
- **译文存档**：外文材料的中文译稿，使用 `type: translation`，保留原文链接与翻译说明。
- **AI 写给五月七日**：知识讲解、方法手册与指导笔记；沿用“ChatGPT 写给五月七日的……”命名，例如[游戏开发术语与流程手册](https://devlog.fivsevn.com/posts/2026/posts-2026-umwelt-game-development-handbook-001.html)。
- **[AI 话语分析](https://devlog.fivsevn.com/posts/ai-discourse-analysis/)**：AI 辅助拆解公共讨论的论证结构；在首页底部 `Section` 单独列出，[栏目目录](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/posts/ai-discourse-analysis/index.md)独立维护。

### 新建草稿

1. 将文件放进 [`posts/_drafts/`](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/posts/_drafts) 第一层。
2. 提交并推送，等待 [草稿处理任务](https://github.com/fivsevn-agy/fivsevn-devlog/actions/workflows/apply-draft-frontmatter.yml) 完成。
3. 拉取自动处理后的文件，再继续编辑。

> 草稿不进入文章目录。[处理脚本](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/scripts/apply_draft_frontmatter.py)会提取正文标题、补 metadata、生成占位文件名，再自动提交回仓库；已有 frontmatter 的文件会跳过，不反复改名。

### 新建译文｜translate & post

1. 分享原文网址，运行 [`translate & post`](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/blogops/docs/auto-translation-shortcut.md)。
2. 将生成的提示词文件分享给 ChatGPT，取得带 metadata 的中文译稿。
3. 按[翻译规范](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/spec-content-translation-001.md)检查译稿、metadata、原文链接和公开发布授权。
4. 按下方[发布正式文章](#发布正式文章)的步骤保存、提交并推送。

> **原文输入**：无分享输入时，快捷指令读取剪贴板；抓取不完整时，先补齐原文再生成译稿。
>
> **文件用途**：快捷指令通过 [Jina Reader](https://jina.ai/reader/) 抓取原文，拼入网址、翻译要求和规范链接，生成日期命名的 `.md` 提示词文件。这个文件供 AI 生成译稿，快捷指令本身不直接发文。

### 发布正式文章

**直接新建**

1. 将文章放进[对应年份目录](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/posts)。
2. 按 [metadata 规范](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/spec-content-frontmatter-001.md)补齐字段。
3. 设置 `status: active`、`visibility: public`。
4. 提交并推送，检查目录更新和网站部署结果。

**草稿转正式稿**

1. 将文件从 `_drafts` 移到对应年份目录。
2. 整理正式文件名、`id` 和 metadata，设置 `status: active`、`visibility: public`。
3. 提交并推送，检查目录更新和网站部署结果。

> **草稿位置**：只改状态、不移出 `_drafts`，不会进入目录。
>
> **目录更新**：[目录任务](https://github.com/fivsevn-agy/fivsevn-devlog/actions/workflows/publish-pages.yml)扫描文章，由[索引脚本](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/scripts/update_module_indexes.py)读取标题、日期和状态等 metadata，重算 [`index.md`](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/posts/index.md) 的文章列表；有差异才自动提交。
>
> **网页发布**：网站构建时，[Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll)把 Markdown 转成 HTML，GitHub Pages 提供访问。目录更新与网站部署分开检查，长文发布不经过 WordPress。

### 修改文章

按需要选择对应操作，完成后提交并推送，再检查目录和实际页面：

1. **修改正文**：编辑原文件，保留文件名、`id`、`created`，手动维护 `updated`。
2. **修改标题**：同时修改 metadata 的 `title` 和正文 `# 标题`；不必改文件名。
3. **修改日期**：按需要维护 `created` 和 `updated`，再核对目录日期与排序。
4. **重命名或移动文件**：调整文件路径，再检查原网址、文章互链和图片路径。
5. **复制为另一篇**：另存文件，为新文章设置新的 `id`，补齐 metadata。
6. **从目录撤下**：设置 `status: hidden`，提交并推送后检查目录。

> **目录收录**：正文或标题改动会更新原目录项，不新增一项；只改标题、保留文件名时，原网址不变。复制成两份且都符合收录条件时，目录会出现两项。
>
> **日期排序**：有有效 `created` 时，仅改 `updated` 不会置顶；改 `created` 会调整目录日期与排序。同一天内，普通文章改标题也可能调整排序。
>
> **撤下范围**：长文的 `status: hidden` 会将文章移出目录，不代表文件私密或原网址失效。
>
> 索引脚本按当前文件重新生成列表，替换原列表，不按标题或 `id` 去重。`title` 提供目录文字，文件路径提供链接，日期决定排序。

---

## 3. 共用备忘

1. **提交**：保存文件，在本地 commit，再推送到对应仓库的 `main`。
2. **目录**：通过文章 metadata 调整收录信息，等待目录任务更新列表。
3. **README**：需要修改使用说明时，直接编辑本文件并提交推送。
4. **上线检查**：打开 [devlog Actions](https://github.com/fivsevn-agy/fivsevn-devlog/actions) 或 [flux Actions](https://github.com/fivsevn/fivsevn-flux/actions)，依次检查处理结果、网站部署和实际页面。

> 只在手机本地保存或 commit，不会启动远端任务；需要完成推送。
>
> 不要手改 [`index.md`](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/posts/index.md) 的 `AUTO-INDEX` 区域，脚本会替换这部分。README 按文件名排除，不作为普通文章收录。

---

核对日期：2026-10-18。
