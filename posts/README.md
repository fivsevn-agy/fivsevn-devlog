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
updated: "2026-10-18"
metadata_updated: "2026-10-18"
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
├── _flux/
│   └── trigger.md          flux 文字发布入口
└── ai-discourse-analysis/  AI 话语分析独立栏目
```

- **[flux](https://flux.fivsevn.com/)**：随手发文字、图片，直接从 GitHub 发布。
- **[devlog posts](https://devlog.fivsevn.com/posts/)**：保存需要长期整理、修改和查阅的文章。

---

## 1. 短内容｜flux

### 新建文字

继续替换 [`trigger.md`](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/posts/_flux/trigger.md) 正文，保留顶部配置，提交并推送到 `main`。支持 `[文字](网址)` 等 Markdown 格式。入口仍在 devlog 仓库，文件夹为 `_flux`；**不再调用 WordPress**。

flux 约每 5 分钟检查新提交，把每次 trigger 变更保存成独立 Markdown 记录，再构建和部署。GitHub 调度可能延后。相同提交重试不会重复发文，也不会覆盖人工修改；显式 `slug` 仍只创建一次。`status: published` 公开发布，`status: draft` 保存为草稿；公开仓库不提供保密能力，不支持定时发布。

本仓库的 [Check flux trigger](https://github.com/fivsevn-agy/fivsevn-devlog/actions/workflows/publish-wp-trigger.yml) 只校验格式。实际是否上线，检查 [Publish flux](https://github.com/fivsevn/fivsevn-flux/actions/workflows/build.yml) 和 [flux 页面](https://flux.fivsevn.com/)。

顶部配置只需：

```yaml
status: published
title: ""
```

`title` 留空，自动用本次提交时间生成标题，例如 `18 Oct, 2026 06:40`；填写 `title: "今天的随手记"` 则显示自定义标题。下面的实际发布时间由提交时间生成，统一使用 `Asia/Shanghai`。不再需要 `category`、`timezone` 或 `wp_status`。

修改已发布帖子的标题：在 flux 对应 `index.md` 顶部修改 `title`，保留 `date`、`id` 和目录，标题链接、发布时间和排序不变。要让下一条恢复时间标题，把 trigger 的 `title` 清空。

### 新建图片

快捷指令仍选择 [`post/stream`](https://github.com/fivsevn/fivsevn-assets/tree/main/post/stream)，Working Copy 提交并推送。每张新图片生成一条 flux 记录；配文写在提交的 extended description，可用 Markdown。图片复制进 flux 文章包，相同路径不会重复发文。

### 修改、撤下原帖

直接修改 [flux 文章包](https://github.com/fivsevn/fivsevn-flux/tree/main/flux) 中对应的 `index.md`，提交后自动部署。保留目录、id 和 date；不要回头改 trigger 来修改旧帖。撤下网页可设 `status: hidden`，公开仓库和历史仍保留文件。

### 历史记录与 WordPress

2026-10-18 起，flux 独立发布。历史文章包保留原日期和网址，统一由 flux 管理；WordPress 定时同步和全量扫描已停用。以后删除 WordPress 的 posts 不会删除 flux 内容。

操作及构建细节见 [flux README](https://github.com/fivsevn/fivsevn-flux/blob/main/README.md)。

---

## 2. 长文章｜devlog

### 目前的内容

以下是现有内容概览，后续可增减，不必另建分类目录。

- **旧 WordPress 存档**：早期内容按年份保留，见 [2019](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/posts/2019)、[2025](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/posts/2025)；保留原文来源与链接。
- **自己写的文章**：随笔、观察、资料整理与研究笔记，按年份存放。
- **译文存档**：外文材料的中文译稿，使用 `type: translation`，保留原文链接与翻译说明。
- **AI 写给五月七日**：知识讲解、方法手册与指导笔记；沿用“ChatGPT 写给五月七日的……”命名，例如[游戏开发术语与流程手册](https://devlog.fivsevn.com/posts/2026/posts-2026-umwelt-game-development-handbook-001.html)。
- **[AI 话语分析](https://devlog.fivsevn.com/posts/ai-discourse-analysis/)**：AI 辅助拆解公共讨论的论证结构；在首页底部 `Section` 单独列出，[栏目目录](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/posts/ai-discourse-analysis/index.md)独立维护。

### 指导手册的写作与维护约定

本系列直接写给五月七日，重点是理解制作全流程、系统原理、工具成本和验收关系；具体编程可交给实现者完成。涉及自己的作品时，可用“以你正在做的《等足目赋格》为例”引入，并区分已有实现、讨论方案与假设示例。

语言保持简洁、平实，同时写清推理所需的前提和中间关系。比较概念时，先解释各自职责，再用例子连接，最后归纳区别。否定可以用于界定边界，但应交代否定的对象、原因或对照条件。连词按实际的因果、递进、转折或让步关系使用，避免只在跳跃的句子之间机械添加“因此”。补充性的时间和范围说明，适合放在括号中。

表格采用“定义”“解释”“用途”等中性栏目，少用设问和低幼化比喻。外语材料先理解论证关系，再按自然中文组织句子，避免逐词翻译造成的生硬表达。

游戏案例优先采用国外知名作品，并放在正在说明的概念旁边。参考资料除自己的项目外，采用英文、日文等海外作者、开发团队、出版社、大学或机构的一手材料；本系列不采用国产游戏案例或国内文献、教程与资料入口。

各段案例首次介绍游戏时，在游戏名上链接至对应作品的官网、开发商介绍页或官方商店，方便直接查看作品。开发访谈与研究资料继续通过参考编号单独引用；涉及续作或不同版本时，链接应对应正在讨论的那一部作品。

每篇保留参考文献和阅读重点，说明书籍、官方文档、课程或视频的用途及获取方式。引用写成 `[\[1\]](#ref-1)`，连续引用写成 `[\[1\]](#ref-1)、[\[2\]](#ref-2)`，使页面明确显示为 [1]、[2]，避免编号与后文连读。软件的开放情况与费用类型分别标注，保留核对日期和官方入口。

文章更新保留原有文件名、ID、创建日期和网址。目录继续采用较新内容在上方的顺序；同日发布的游戏开发手册按逻辑发布顺序，以较大的编号在前排列。系列保留 001 术语与流程、002 软件地图。001 以中、英、日术语为入口，按开发阶段说明含义、相邻概念、前提与交付；术语覆盖和完整流程都要充分保留。每个词条尽量配具体游戏中的对象、行为或制作实例，并标明主要使用阶段；容易混淆的词放在同一情境中比较。区分可观察的玩法、有来源的开发事实与用于教学的制作示例，不把示意实现写成原作实际技术。002 以广泛的软件覆盖为入口，说明能做什么、输入输出、分工、接入与费用形式，供随时查阅。案例围绕同一个问题并列多款游戏，先交代未玩过也能理解的玩法，再具体说明做法、原因、结果和代价；未公开的开发动机不得写成事实。可以重构文章，不机械追加，不因增加案例而删薄术语或软件目录。正文直接呈现当前有效内容，不加入撤下文章的占位或修改历史。

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
- **日期**：有有效 `created` 时，仅改 `updated` 不会置顶；改 `created` 会调整目录日期与排序。同一天内，普通文章改标题可能调整排序；游戏开发手册保持同日编号倒序。
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

核对日期：2026-10-18。短内容已由 flux 接管，长文流程保持原样。
