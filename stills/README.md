---
id: "stills-readme"
title: "stills 板块说明"

module: "stills"
submodule: "guide"
topic: "guide"

type: "note"
status: "active"
canonical: true

summary: "说明stills 板块说明。"

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
# stills 板块说明

```text
fivsevn-devlog/stills/
└── README.md                   本说明；不存照片

fivsevn-assets/stills/          作品目录节选
├── README.md
├── 20190407originalfivsevn/    作品集
├── 20260601renminrd/           作品集
├── acornerofhome/             主题照片
├── …                          其他作品目录
└── bygone/                    老照片单图发布入口
```

- **[stills 页面](https://fivsevn.com/stills/)**：摄影作品与照片组，编排和视觉效果在 WordPress 维护。
- **[照片目录](https://github.com/fivsevn/fivsevn-assets/tree/main/stills)**：图片保存在 assets；本 devlog 目录只放说明。
- **[bygone 页面](https://fivsevn.com/stills/bygone/)**：stills 下的老照片分区，单图自动发布，和普通作品集分开处理。

---

## 1. 新建作品集｜手动编排

- 照片放进 [assets/stills 对应作品目录](https://github.com/fivsevn/fivsevn-assets/tree/main/stills) → 提交并推送到 `main`。
- 在 [WordPress 后台](https://fivsevn.com/wp-admin/)新建作品页面 → 引用照片 CDN 链接 → 编排顺序、文字与版式 → 发布。
- 检查 [stills 页面](https://fivsevn.com/stills/)的作品入口，按现有编排补上新作品链接。

> 图片入库只提供可引用的文件 → WordPress 页面引用外链、组织照片组 → 读者在 WordPress 查看作品。  
> 当前[自动发图任务](https://github.com/fivsevn/fivsevn-assets/blob/main/.github/workflows/publish-image-posts.yml)只监听 stills 下的 `bygone/`；上传其他作品目录**不会自动创建作品页面**。流程来源见[发布备忘](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/blogops/docs/publish-memo.md)。

## 2. 新建老照片｜bygone 自动发图

- 照片放进 [`stills/bygone/`](https://github.com/fivsevn/fivsevn-assets/tree/main/stills/bygone) → 提交并推送 → 每张新图片新发一条。
- **标题**：发布前整理文件名；脚本去掉扩展名，并将 `_`、`-` 换成空格。
- **分类与配文**：分类为 `bygone`，无自动标签；不读取提交说明作为配文，文字在 WordPress 添加。

> [图片发布任务](https://github.com/fivsevn/fivsevn-assets/actions/workflows/publish-image-posts.yml)检测图片 → [脚本](https://github.com/fivsevn/fivsevn-assets/blob/main/scripts/publish_image_posts.py)生成引用 CDN 图片的 WordPress 区块 → 用 Actions Secrets 中的账号与应用密码调用 REST API → 新建 `bygone` 帖子。  
> 图片仍在 assets，不上传 WordPress 媒体库；按图片路径生成 slug，查到已有帖子就跳过。

## 3. 修改与撤下

- **作品名称、说明、顺序、版式**：直接修改 WordPress 原作品页面。
- **新增／替换作品照片**：先保存图片，再更新页面的图片链接；普通作品目录不自动同步编排。
- **bygone 标题或配文**：在 WordPress 修改原帖，不靠改文件名或提交说明更新旧帖。
- **重命名／移动照片**：检查所有引用链接；在 `bygone/` 中换成新路径还可能重复发帖。
- **撤下作品**：在 WordPress 处理原页面／帖子，并检查 stills 入口；删除仓库照片不会删除页面。

> WordPress 保存页面与帖子的展示内容，GitHub 保存照片文件；两边不是双向同步。保留被引用的图片路径，不用搬文件来调整页面顺序。

## 4. 检查与维护

- **普通作品集**：检查作品页、照片顺序、图片链接，以及 [stills 入口](https://fivsevn.com/stills/)。
- **bygone**：查看[图片发布任务](https://github.com/fivsevn/fivsevn-assets/actions/workflows/publish-image-posts.yml) → 检查[老照片页面](https://fivsevn.com/stills/bygone/)。
- 通用图片区块与发布规则见 [assets 说明](https://github.com/fivsevn/fivsevn-assets/blob/main/README.md#image-post-automation)；只改本 README 不会发图。

---

核对日期：2026-10-13。按当前目录、脚本与工作流记录，后续可调整。
