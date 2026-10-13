---
id: "now-readme"
title: "now 板块说明"

module: "now"
submodule: "guide"
topic: "guide"

type: "note"
status: "active"
canonical: true

summary: "说明now 板块说明。"

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
# now 板块说明

```text
fivsevn-devlog/now/
├── README.md   本说明
└── index.md    当前近况页（手动维护）
```

- **[now 页面](https://devlog.fivsevn.com/now/)**：简单告诉来访者最近在做什么、目前是什么状态。
- **[nownownow 项目](https://nownownow.com/about)**：收集个人网站的近况页；五月七日的[项目资料卡](https://nownownow.com/p/kUDQ)链接到本站 `/now/`。
- 这里维护一份当前近况，不必写成长文章，也不作为 posts 时间线使用。

---

## 1. 更新近况

- 打开 [`index.md`](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/now/index.md) → 修改对应区域 → 提交并推送到 `main`。
- **Keepalive**：当前状态或简短问候；修改时手动维护 `updated` 日期。
- **Signal**：最近的一句记录；修改时手动维护 `log` 日期。
- **小改／大改**：都直接改原文件，保留 `/now/` 地址；内容和栏目可随需要增减，不必按日期另建文件。

> 提交后，站点构建用 [Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll)将 `index.md` 转成 HTML → GitHub Pages 更新近况页。  
> Keepalive、Signal 和日期都是手写内容；当前没有定时改日期、自动生成近况或检测在线状态的任务，也不经过 WordPress。

## 2. 维护 nownownow 入口

- **更新近况正文**：只改本站 `index.md`，继续使用已收录的页面地址。
- **修改项目资料卡**：到 nownownow 的资料管理中另行更新，本站文件不会替你修改资料卡。
- **更换域名或页面路径**：同时检查[项目资料卡](https://nownownow.com/p/kUDQ)和站内链接，避免入口指向旧地址。

> nownownow 提供资料卡和近况页链接 → 读者点击后访问本站。正文由本站托管；当前仓库没有向 nownownow 自动回写资料的脚本。

## 3. 检查与维护

- 保存 → commit → 推送到 `main` → 查看 [Actions](https://github.com/fivsevn-agy/fivsevn-devlog/actions) 的 Pages 构建与部署 → 打开[近况页](https://devlog.fivsevn.com/now/)。
- **回看旧内容**：查看 [`index.md` 修改历史](https://github.com/fivsevn-agy/fivsevn-devlog/commits/main/now/index.md)，不必把旧近况全部堆在页面上。
- **改这份说明**：编辑 README；读者的近况正文仍以 `index.md` 为准。

---

核对日期：2026-10-13。按当前页面、项目入口与仓库工作流记录，后续可调整。
