---
id: "system-map"
title: "fivsevn 系统总览"

module: "system"
submodule: "root"
topic: "system-map"

type: "note"
status: "active"
canonical: true

summary: "说明fivsevn 系统总览。"

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

created: "2026-06-18"
updated: "2026-10-13"
metadata_updated: "2026-10-13"
---
# fivsevn 系统总览

[五月七日的思考札记](https://fivsevn.com/)是统一入口。本文件说明网站、仓库与各板块的关系；具体操作看各板块 README，不在这里重复维护。

## 1. 当前文件夹

```text
fivsevn-devlog/             主要目录与文件
├── README.md              devlog 首页展示与主站引导
├── system-map.md          本总览
├── posts/                 个人文章、历史存档与短文发布入口
├── foodie/                吃喝板块说明；图片在 assets 仓库
├── natsci/                自然科学长文与板块说明
├── netcom/                通信、计算机与工程长文
├── stills/                摄影板块说明；照片在 assets 仓库
├── motion/                视频板块说明；视频在 YouTube
├── blogops/               后台更新日志与维护说明
├── now/                   当前近况页
├── intake/                来源清单、抓取脚本与生成页面
├── scripts/               草稿、索引与 flux trigger 校验脚本
├── .github/workflows/     GitHub Actions 任务
├── _layouts/              devlog 页面模板
└── assets/                本站样式与现有附件
```

- 本仓库的 `assets/` 与独立的 `fivsevn-assets` 仓库不是同一个位置。
- `foodie/`、`stills/`、`motion/` 目前只放说明；有文件夹不代表另建了 devlog 展示页。

## 2. 网站板块与说明入口

| 板块 | 内容与页面 | 操作说明 |
|---|---|---|
| **posts** | [flux 随手记录](https://flux.fivsevn.com/)；[devlog 长文存档](https://devlog.fivsevn.com/posts/)，含原创、旧文、译文及 AI 笔记，底部另列 AI 话语分析 | [posts README](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/posts/README.md) |
| **foodie** | [吃喝记录](https://fivsevn.com/foodie/)，按图片目录区分标签，WordPress 展示 | [foodie README](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/foodie/README.md) |
| **natsci** | [WordPress 自然观察单图](https://fivsevn.com/natsci/)；[devlog 自然科学长文](https://devlog.fivsevn.com/natsci/) | [natsci README](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/natsci/README.md) |
| **netcom** | [通信、计算机与工程笔记](https://devlog.fivsevn.com/netcom/)，目前只有 devlog 长文 | [netcom README](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/netcom/README.md) |
| **stills** | [摄影作品集](https://fivsevn.com/stills/)，WordPress 手动编排；[bygone 老照片](https://fivsevn.com/stills/bygone/)单图自动发布 | [stills README](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/stills/README.md) |
| **motion** | [视频作品](https://fivsevn.com/motion/)，YouTube 托管，WordPress 嵌入 | [motion README](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/motion/README.md) |
| **blogops** | [后台日志](https://devlog.fivsevn.com/blogops/)，手动记录系统调整，保存维护说明 | [blogops README](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/blogops/README.md) |
| **now** | [当前近况](https://devlog.fivsevn.com/now/)，参与 [nownownow](https://nownownow.com/p/kUDQ)，手动更新 | [now README](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/now/README.md) |
| **intake** | [资料与 RSS 页面](https://devlog.fivsevn.com/intake/)，定时生成，不是永久文章存档 | [intake README](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/intake/README.md) |

- **[flux](https://flux.fivsevn.com/)**：2026-10-18 起独立承接 posts 短文字和图片，直接从 GitHub 发布，历史文章包保留；不再同步 WordPress。
- **[57store](https://fivsevn.com/57store/)**：独立的虚构叙事与创作入口。它与游戏项目各自维护，不混入普通笔记或博客发布流程。
- 以上为当前内容分工，不是固定分类表；新增、合并或撤下板块时再调整。

## 3. 内容放哪里、修改哪里

| 位置 | 保存与维护的内容 |
|---|---|
| **[WordPress 后台](https://fivsevn.com/wp-admin/)** | 主站布局、视觉效果和其他作品页面；posts 短帖已转到 flux |
| **[fivsevn-agy/fivsevn-devlog](https://github.com/fivsevn-agy/fivsevn-devlog)** | 长文 Markdown、板块说明、日志、近况、来源清单与相关脚本；直接改原文件 |
| **[fivsevn/fivsevn-assets](https://github.com/fivsevn/fivsevn-assets)** | 自有图片、照片和静态资源，以及图片／YouTube 自动发帖脚本；页面引用图片链接 |
| **[fivsevn/fivsevn-flux](https://github.com/fivsevn/fivsevn-flux)** | 短帖内容存档、接收流程、页面构建与部署；英文后台维护说明 |
| **[fivsevn-agy/fivsevn-spec](https://github.com/fivsevn-agy/fivsevn-spec)** | metadata、翻译、来源、引用、日期和提交等公共规范；板块说明链接过去，不复制整套规范 |
| **[YouTube @fivsevn](https://www.youtube.com/@fivsevn)** | 视频托管；WordPress 保存嵌入内容，视频原文件另行备份 |

> 日常短帖操作统一看 [posts README](posts/README.md)，flux README 负责英文后台维护说明。同一板块可以跨仓库，但不要求两边各写一份。长文改 devlog，短帖改 flux，主站视觉编排改 WordPress，图片源文件改 assets。

## 4. 发布关系速览

```text
随手文字    trigger.md 提交 → flux 定时接收 Markdown → 构建并部署 GitHub Pages
随手图片    assets/post/stream → flux 定时接收图片与配文 → 构建并部署
其他单图    assets 其他发布目录 → Actions 组装图片与分类 → WordPress 发帖
摄影作品集  assets 保存照片 → WordPress 手动引用、编排并发布
视频作品    YouTube RSS → Actions 读取最新一条 → WordPress 嵌入
长文章      devlog Markdown → 目录任务重算列表；站点构建、部署 → GitHub Pages
日志／近况  手动修改各自 index.md → 站点构建、部署 → GitHub Pages
posts 历史  flux 已保存文章包；WordPress 同步停用，删除原站不影响副本
资料入口    intake/sources.md → 定时抓取与组装 → intake 页面、llm-context.md
```

- **翻译入口**：快捷指令取网页文本、拼提示词 → AI 生成译稿 → 检查后按长文流程保存；不是自动直接发文。
- **自动与手动目录**：posts、natsci、netcom 的文章列表由脚本生成；blogops 日志、now 近况和 AI 话语分析栏目入口手动维护。
- **同步不是全量即时镜像**：扫描范围、频率、补发和撤下规则见各板块 README；不把“已提交”“已同步”“已上线”视为同一状态。
- **intake**：日常维护 [sources.md](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/intake/sources.md)；当前 [Actions](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/.github/workflows/build-news.yml)另生成 [llm-context.md](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/intake/llm-context.md)供 AI 阅读。生成页和上下文文件不手改，读后形成的独立文章再放入 posts、natsci 或 netcom。

## 5. 日常维护与 AI 协作

- **查找顺序**：本总览定位板块 → 板块 README 查操作 → 当前源文件、脚本与工作流核对细节。历史日志与 `legacy/` 不替代现行规则。
- **写作规范**：遵循 [metadata](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/spec-content-frontmatter-001.md)、[翻译](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/spec-content-translation-001.md)与[提交规范](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/gov/spec-commit-message-001.md)。ChatGPT 撰写的指导笔记沿用“ChatGPT 写给五月七日的……”命名，保留具体主题。
- **修改边界**：改说明不等于改脚本；改文章通常保留文件名、`id` 与原始日期，不手改自动生成的列表。维护操作不要夹带一次新发文。
- **公开与授权**：`_drafts`、`hidden`、`private` 等名称或字段不等于访问控制；私密材料另存于权限确认的私密位置。引用、译文与媒体按来源授权和相应 LICENSE 处理。
- **视觉风格**：保留深色、低饱和、代码／界面式表达，以及时间线、手机聊天、观察窗口、照片集等板块差异；不为统一结构而统一所有页面版式。
- **完成检查**：保存 → commit → 推送 → 查看对应 Actions → 检查部署与实际页面。自动回写后先拉取，再继续手改。
- **更新这张图**：只在入口、仓库分工或板块结构改变时修改；具体参数留在板块说明与脚本，不为完整感再增加一套目录或总手册。

---

核对日期：2026-10-18。按当前主站入口、仓库结构与各板块说明整理；独立创作和游戏项目仅保留边界，不在此展开。
