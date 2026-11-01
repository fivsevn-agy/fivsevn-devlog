---
id: "blogops-assets-media-reference-001"
title: "博客各类内容的保存和引用方式"

module: "blogops"
submodule: "content"
topic: "media-reference"

type: "note"
status: "draft"
canonical: false

summary: |
  记录博客图片、视频等内容资源的保存位置与引用方式， 以及对应平台和路径维护上的优缺点。

parents: []
related: []

tags: ["blogops", "assets", "images", "video", "cdn", "youtube"]

audience: ["self"]
languages: ["zh"]

maturity: "evolving"
confidence: 0.8

visibility: "public"
source_of_truth: "devlog"

legacy:
  metadata:
    submodule: assets

created: "2026-06-07"
updated: '2026-11-01'
metadata_updated: '2026-11-01'
---

# 博客各类内容的保存和引用方式

| 内容 | 保存位置 |
|---|---|
| Posts 正文与素材 | `fivsevn-devlog/posts/年/月/文章编号/` |
| Fieldlog 图片与配文 | `fivsevn-devlog/natsci/fieldlog/年/月/帖子编号/` |
| Flux、Savour | 各自仓库的帖子发布包 |
| Stills、Bygone、Motion 页面 | `fivsevn-roll` |
| 主页与共用图片 | `fivsevn-assets` |
| 视频 | [YouTube @fivsevn](https://www.youtube.com/@fivsevn)、[@57store.fivsevn](https://www.youtube.com/@57store.fivsevn) |

发布包里的图片使用本站路径；移动素材时同步修改引用。主页共用素材可使用 `https://cdn.jsdelivr.net/gh/fivsevn/fivsevn-assets@main/文件路径`。Motion 由 Roll 同步 YouTube。
