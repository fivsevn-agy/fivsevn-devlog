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
updated: "2026-11-01"
metadata_updated: "2026-11-01"
---

# posts 维护说明

[文章目录](index.md) · [AI 话语分析](ai-discourse-analysis/index.md) · [短内容 Flux](https://flux.fivsevn.com/)

正式发布的文章按年月整理，每篇文章一个发布包。正文、图片、下载文件及专用脚本放在同一个文件夹里，修改或备份时直接处理整个包。

```text
posts/
├── index.md                         文章目录，自动生成列表
├── README.md                        本说明
├── assets/wordpress.css             旧文共用样式，头尾模板在 _layouts/wordpress-post.html
├── 年/月/文章编号/
│   ├── index.md                     正文与 metadata
│   └── assets/                      本篇使用的素材，有需要时创建
├── ai-discourse-analysis/
│   ├── index.md                     栏目目录，自动生成列表
│   └── 年/月/文章编号/
│       ├── index.md
│       └── assets/
├── _drafts/                         草稿区，保持现有方式
└── 2019/、2025/                     原有未列入当前公开目录的存档保留原位
```

## 发布或修改文章

1. 在对应年月下新建一个文章编号文件夹，正文命名为 `index.md`。文章编号发布后保持不变。
2. 在顶部 metadata 中保留唯一 `id`、标题、日期等字段。正式发布使用 `status: active`，并设置 `module: posts`、`canonical: true`、`source_of_truth: devlog`、`filename_policy: entrypoint`。
3. 图片和附件放进本篇的 `assets/`。需要网页专用的 CSS、脚本、字体或数据文件时，也放在本篇包内。
4. 提交到主分支后，现有发布任务会生成目录、构建并部署网站。在 [发布记录](https://github.com/fivsevn-agy/fivsevn-devlog/actions/workflows/publish-pages.yml)确认成功，再检查文章和附件。

旧文章的 `permalink` 保留原有公开网址；整理文件夹不会改变已发布链接。修改旧文时保留 `id`、`created` 和 `permalink`，标题变化不需要改文件夹。正文引用本篇图片时，使用包含发布包的完整站内路径，例如：

```markdown
![图片说明](/posts/2026/06/文章编号/assets/image-01.jpg)
```

链接其他文章时，可使用对方的公开网址；维护目录时使用发布包的 `index.md` 源文件路径，网站构建会按它的 `permalink` 生成正确链接。译文仍保留原作出处、`original_url` 与翻译说明，目录进入仓库中的中文译文。

## WordPress 旧文

当前文章目录里的早期 WordPress 文章已改为独立发布包。正文保留原有段落、图片排列、表格等排版，配图和本地附件随包保存。代码注释风格的头尾由共用模板生成，分类与标签作为文字显示；评论区和分享区不保存。

`original_url` 只记录历史出处，目录和站内文章链接指向本站。修改正文或替换图片直接编辑包内文件，不需要回 WordPress。

## AI 话语分析

在 `ai-discourse-analysis/年/月/文章编号/` 保存每篇分析及其材料，栏目目录独立列出文章。`ai-posts-boot-protocol.md` 继续作为写作辅助资料保留，不加入文章列表。

## 目录与草稿

目录列表由 metadata 自动生成，不手工维护自动标记之间的内容。本地只更新文章目录时运行：

```sh
python scripts/update_module_indexes.py --module posts --module ai-discourse-analysis
```

脚本保留文章时间顺序，同一天的游戏开发手册按分册号排列。隐藏、私密和归档状态不进入目录，草稿区不扫描。

`posts/_drafts/` 中的草稿和现有草稿处理方式保持原样。准备正式发布时，再将完成稿整理成上述发布包。
