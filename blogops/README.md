---
id: "blogops-readme"
title: "blogops 板块说明"

module: "blogops"
submodule: "guide"
topic: "guide"

type: "note"
status: "active"
canonical: true

summary: "说明blogops 板块说明。"

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
# blogops 板块说明

```text
fivsevn-devlog/blogops/  主要目录
├── README.md           本说明
├── index.md            后台更新日志（手动维护）
├── content/            关于博客、资源引用等说明
├── docs/               发布与维护步骤、快捷指令
└── legacy/             旧说明与历史方案
```

- **[blogops 页面](https://devlog.fivsevn.com/blogops/)**：记录博客改版、发布流程调整、工具更换等更新。
- **本目录**：保存后台日志与维护说明；这里的“后台”指内容主题，不是私密管理后台。

---

## 1. 记录一次更新

- 打开 [`index.md`](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/blogops/index.md) → 在 `Directory` 顶部添加日期、简短说明和相关链接 → 手动更新 metadata 的 `updated` → 提交并推送到 `main`。
- **小改**：直接修正原条目的错字、表述或链接。
- **后续变化**：另加一条新日期记录，保留旧条目作为历史；过时说明可标注并链接到新版。

> 提交后，站点构建用 [Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll)将 Markdown 转成 HTML → GitHub Pages 展示日志。  
> 日志和顺序由人维护；Git 提交记录不会自动变成日志。现有[目录任务](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/.github/workflows/update-indexes.yml)只处理 posts、natsci、netcom，不重排这里的列表。

## 2. 新建或修改维护说明

- **博客介绍、资源保存与引用说明**：放在 [`content/`](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/blogops/content)。
- **具体操作、发布步骤、快捷指令说明**：放在 [`docs/`](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/blogops/docs)；独立文档按 [metadata 规范](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/spec-content-frontmatter-001.md)填写信息。
- **新文档入口**：需要出现在后台日志时，在 `index.md` 手动补链接；不会自动收录。
- **修改已有文档**：改原文件并更新 `updated`；重命名或移动时，同步修正引用链接。
- **旧方案**：保留在 [`legacy/`](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/blogops/legacy)用于对照，不作为当前操作依据。

> Markdown 文件保存说明 → `index.md` 提供入口 → Pages 展示。改说明不会替你修改发布脚本、定时任务或 WordPress 配置。

## 3. 检查与快速入口

- 保存 → commit → 推送到 `main` → 查看 [Actions](https://github.com/fivsevn-agy/fivsevn-devlog/actions) 的 Pages 构建与部署 → 检查[实际页面](https://devlog.fivsevn.com/blogops/)。
- 日常操作先看各板块 README；历史日志记录当时情况，自动化的实际行为以当前脚本和工作流为准。
- 不写入密码、令牌或其他私密配置。

**内容板块说明**：[posts](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/posts/README.md) · [foodie](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/foodie/README.md) · [natsci](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/natsci/README.md) · [netcom](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/netcom/README.md) · [stills](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/stills/README.md) · [motion](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/motion/README.md)

**近况与资料**：[now](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/now/README.md) · [intake](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/intake/README.md)

**总体说明与规范**：[系统总览](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/system-map.md) · [fivsevn-spec](https://github.com/fivsevn-agy/fivsevn-spec)

---

核对日期：2026-10-13。按当前目录、页面与工作流记录，后续可调整。
