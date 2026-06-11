---
id: system-docs-auto-index-manual-001
title: 自动目录维护手册
module: system
submodule: docs
topic: auto-index
type: howto
status: active
canonical: true
summary: >
  说明 fivsevn-devlog 中 posts、natsci、netcom 三个板块的自动目录生成规则，
  包括文件抓取范围、index.md 更新区域、frontmatter 控制字段与日常维护流程。
parents: []
related:
  - spec-gov-meta-frontmatter-001
  - spec-gov-meta-enums-001

tags:
  - system
  - docs
  - automation
  - index
  - frontmatter
audience:
  - self
  - collaborator
languages:
  - zh

maturity: stable
confidence: 0.95

visibility: public
source_of_truth: devlog
created: 2026-06-12
updated: 2026-06-12
---
# 自动目录维护手册

本仓库使用自动目录脚本维护三个主要板块的首页文章列表：

- posts
- natsci
- netcom

自动目录的目标是：  
文章只需要维护 front matter，首页目录由脚本自动生成。

脚本文件：

txt scripts/update_module_indexes.py 

自动执行文件：

txt .github/workflows/update-indexes.yml 

每次向 main 分支 push 后，GitHub Actions 会自动运行脚本，并更新以下文件：

txt posts/index.md natsci/index.md netcom/index.md 

---

## 1. 基本工作方式

自动目录脚本会扫描三个板块下的 Markdown 文件：

txt posts/ natsci/ netcom/ 

然后根据每篇文章的 front matter 判断：

1. 是否应该进入首页目录；
2. 应该进入哪个板块的首页目录；
3. 应该显示成链接还是纯文本；
4. 应该使用哪个日期排序；
5. 标题是否需要附加说明，例如“译文”；
6. 链接应该指向仓库内文章，还是外部地址。

生成结果会写入各板块的 index.md 中。

---

## 2. 自动更新区域

脚本只会修改 index.md 里自动目录标记之间的内容。

### posts

md <!-- AUTO-INDEX:POSTS_RECENT:START --> 自动生成内容 <!-- AUTO-INDEX:POSTS_RECENT:END --> 

### natsci

md <!-- AUTO-INDEX:NATSCI_RECENT:START --> 自动生成内容 <!-- AUTO-INDEX:NATSCI_RECENT:END --> 

### netcom

md <!-- AUTO-INDEX:NETCOM_RECENT:START --> 自动生成内容 <!-- AUTO-INDEX:NETCOM_RECENT:END --> 

不要手动编辑这些标记中间的内容。  
下一次脚本运行时，标记中间的内容会被重新生成并覆盖。

标记外的内容可以正常手动维护，例如：

- 首页介绍；
- 图片；
- Contact；
- Section 专栏；
- 说明文字；
- 其他手写内容。

---

## 3. 哪些文件会被抓取

一个文件会被纳入自动目录候选，需要满足以下条件：

1. 位于 posts/、natsci/ 或 netcom/ 目录下；
2. 是 .md 文件；
3. 不在排除目录中；
4. 文件名不是系统文件名；
5. 文件开头有 front matter；
6. front matter 中有 title；
7. front matter 中有有效日期；
8. front matter 中的 status 是可显示状态。

有效日期字段按优先级读取：

txt created > date > updated 

也就是说，脚本优先使用 created。如果没有 created，再使用 date。如果两者都没有，最后才使用 updated。

---

## 4. 哪些文件不会被抓取

以下目录不会进入自动目录：

txt assets/ _drafts/ .github/ .obsidian/ node_modules/ __pycache__/ 

其中，_drafts/ 是完全排除区。  
即使 _drafts/ 里的文件写了 status: publish，也不会进入首页目录。

目前 posts 下的这个目录也暂时排除：

txt posts/ai-discourse-analysis/ 

以下文件名也不会被抓取：

txt index.md map.md README.md .DS_Store .cache .gitkeep 

因此这些文件不会被当作文章处理：

txt posts/index.md natsci/index.md netcom/index.md posts/map.md natsci/map.md netcom/map.md 

---

## 5. _drafts/ 和 status: draft 的区别

本仓库区分两种草稿状态。

### _drafts/

_drafts/ 是私有缓冲区。

放在这里的文件不会进入首页目录，也不会被脚本处理。

适合放：

- 临时笔记；
- 结构未定的草稿；
- 文件名随意的材料；
- 暂时不希望出现在首页的内容。

示例：

txt natsci/_drafts/tmp.md netcom/_drafts/随手记录.md posts/_drafts/未整理.md 

这些文件不会出现在首页目录中。

### status: draft

status: draft 是“公开预告”状态。

文件必须放在正常内容目录里，例如：

txt natsci/taxonomy/example.md netcom/ai/example.md posts/2026/example.md 

并在 front matter 中设置：

yaml status: draft 

这样文章会出现在首页目录中，但不会生成链接，而是显示为：

md - 2026.03.17 文章标题（更新中） 

适合用于：

- 想让首页显示该主题；
- 文章还没完成；
- 暂时不希望读者点击进入正文；
- 后续只需要把 status 改成 publish 或 active 即可正式发布。

---

## 6. front matter 字段说明

### title

必填。

用于首页目录中的显示标题。

yaml title: 昆虫数据库索引 

生成示例：

md - 2026.03.17 [昆虫数据库索引](taxonomy/example.md) 

---

### module

建议填写。

用于声明文章所属板块。

可用值：

yaml module: posts 

yaml module: natsci 

yaml module: netcom 

如果 module 与文件所在板块不一致，脚本会跳过该文件并输出 warning。

例如，文件在：

txt natsci/taxonomy/example.md 

但 front matter 写成：

yaml module: netcom 

则该文件不会进入 natsci/index.md。

---

### status

强烈建议填写。

status 决定文章是否进入目录，以及是否生成链接。

#### 正式显示并生成链接

以下状态会进入目录，并生成可点击链接：

yaml status: active 

yaml status: publish 

yaml status: published 

生成示例：

md - 2026.03.17 [文章标题](文章路径.md) 

#### 显示但不生成链接

yaml status: draft 

生成示例：

md - 2026.03.17 文章标题（更新中） 

#### 不显示

以下状态不会进入目录：

yaml status: hidden 

yaml status: private 

yaml status: archived 

yaml status: archive 

如果没有写 status，默认不显示在目录中。

---

### created

推荐填写。

表示文章的创建日期，也是自动目录最优先使用的排序日期。

yaml created: 2026-03-17 

目录中会显示为：

txt 2026.03.17 

---

### date

兼容字段。

如果文章没有 created，脚本会使用 date。

yaml date: 2026-03-17 

这个字段主要用于旧文章或迁移文章。

---

### updated

兜底字段。

如果没有 created，也没有 date，脚本才会使用 updated。

yaml updated: 2026-03-17 

不建议只依赖 updated 排序。  
因为 updated 更适合表示最后修改时间，而首页目录通常更适合使用文章创建或发布日期。

---

### type

可选。

目前主要用于标记译文。

如果写成：

yaml type: translation 

标题后会自动加：

txt （译文） 

例如：

yaml title: 澳大利亚被纳入全球鲨鱼与鳐类数据库 type: translation status: active created: 2026-03-14 

生成：

md - 2026.03.14 [澳大利亚被纳入全球鲨鱼与鳐类数据库（译文）](taxonomy/example.md) 

脚本也兼容旧拼写：

yaml type: traslation 

但建议以后统一使用正确拼写：

yaml type: translation 

如果是译文草稿：

yaml type: translation status: draft 

生成：

md - 2026.03.14 澳大利亚被纳入全球鲨鱼与鳐类数据库（译文）（更新中） 

---

### original_url

可选。

用于外部链接文章，主要是 posts 中迁移自 WordPress / Home Blog 的旧文章。

如果 front matter 中有：

yaml original_url: https://example.com/article/ 

并且文章状态是可链接状态：

yaml status: active 

或：

yaml status: publish 

或：

yaml status: published 

目录链接会优先使用 original_url，而不是仓库内 .md 文件路径。

示例：

yaml title: 路灯 module: posts status: published date: 2025-04-09 original_url: https://fivsevn.home.blog/2025/04/09/example/ 

生成：

md - 2025.04.09 [路灯](https://fivsevn.home.blog/2025/04/09/example/) 

如果没有 original_url，则使用仓库内相对路径。

---

## 7. 目录排序规则

目录按日期倒序排列。

也就是说：

txt 新文章在上 旧文章在下 

排序日期来自：

txt created > date > updated 

同一天的文章会继续按标题和路径排序，以保证生成结果稳定。

---

## 8. 目录显示格式

### 正式文章

front matter：

yaml title: 文章标题 status: active created: 2026-03-17 

生成：

md - 2026.03.17 [文章标题](文章路径.md) 

---

### 草稿文章

front matter：

yaml title: 文章标题 status: draft created: 2026-03-17 

生成：

md - 2026.03.17 文章标题（更新中） 

---

### 译文文章

front matter：

yaml title: 文章标题 type: translation status: active created: 2026-03-17 

生成：

md - 2026.03.17 [文章标题（译文）](文章路径.md) 

---

### 译文草稿

front matter：

yaml title: 文章标题 type: translation status: draft created: 2026-03-17 

生成：

md - 2026.03.17 文章标题（译文）（更新中） 

---

### 外链文章

front matter：

yaml title: 文章标题 status: published date: 2025-04-09 original_url: https://example.com/article/ 

生成：

md - 2025.04.09 [文章标题](https://example.com/article/) 

---

## 9. 推荐 front matter 模板

### posts 新文章

yaml --- title: 文章标题 module: posts status: active created: 2026-03-17 updated: 2026-03-17 type: note --- 

### posts 外链旧文章

yaml --- title: 文章标题 module: posts status: published date: 2025-04-09 updated: 2025-04-09 original_url: https://fivsevn.home.blog/example/ --- 

### natsci 文章

yaml --- title: 文章标题 module: natsci status: active created: 2026-03-17 updated: 2026-03-17 type: note --- 

### natsci 译文

yaml --- title: 文章标题 module: natsci status: active created: 2026-03-17 updated: 2026-03-17 type: translation --- 

### netcom 文章

yaml --- title: 文章标题 module: netcom status: active created: 2026-03-17 updated: 2026-03-17 type: note --- 

### 显示为“更新中”的草稿

yaml --- title: 文章标题 module: netcom status: draft created: 2026-03-17 updated: 2026-03-17 type: note --- 

---

## 10. 日常使用流程

### 新增正式文章

1. 把 .md 文件放入对应板块的正常内容目录；
2. 写好 front matter；
3. 设置：

yaml status: active 

或：

yaml status: publish 

4. commit 并 push 到 main；
5. GitHub Actions 自动更新对应的 index.md；
6. 首页目录出现可点击链接。

---

### 新增公开草稿

1. 把 .md 文件放入对应板块的正常内容目录；
2. 写好 front matter；
3. 设置：

yaml status: draft 

4. commit 并 push 到 main；
5. 首页目录出现纯文本条目：

txt 文章标题（更新中） 

---

### 草稿正式发布

把文章 front matter 从：

yaml status: draft 

改成：

yaml status: active 

或：

yaml status: publish 

然后 commit 并 push。

下一次自动更新后，首页目录会从：

md - 2026.03.17 文章标题（更新中） 

变成：

md - 2026.03.17 [文章标题](文章路径.md) 

---

### 不想显示某篇文章

设置：

yaml status: hidden 

或：

yaml status: private 

或：

yaml status: archived 

然后 commit 并 push。

该文章会从首页目录中消失。

---

## 11. 本地手动运行

如果想在本地先检查生成结果，可以在仓库根目录运行：

bash python scripts/update_module_indexes.py 

然后查看改动：

bash git diff -- posts/index.md natsci/index.md netcom/index.md 

确认无误后再提交：

bash git add scripts/update_module_indexes.py posts/index.md natsci/index.md netcom/index.md git commit -m "chore: update module indexes" git push 

正常情况下，不需要手动运行脚本。  
push 到 main 后，GitHub Actions 会自动运行。

---

## 12. 快速规则表

| 情况 | 是否进目录 | 是否加链接 | 显示效果 |
|---|---:|---:|---|
| status: active | 是 | 是 | [标题](路径) |
| status: publish | 是 | 是 | [标题](路径) |
| status: published | 是 | 是 | [标题](路径) |
| status: draft | 是 | 否 | 标题（更新中） |
| status: hidden | 否 | 否 | 不显示 |
| status: private | 否 | 否 | 不显示 |
| status: archived | 否 | 否 | 不显示 |
| 没有 status | 否 | 否 | 不显示 |
| 位于 _drafts/ | 否 | 否 | 不显示 |
| 位于 assets/ | 否 | 否 | 不显示 |
| 文件名是 index.md | 否 | 否 | 不显示 |
| 文件名是 map.md | 否 | 否 | 不显示 |
| type: translation | 是，取决于 status | 取决于 status | 标题后加 （译文） |
| 有 original_url | 是，取决于 status | 是 | 链接优先指向 original_url |

---

## 13. 维护原则

1. 首页目录不手动维护，交给脚本生成。
2. 文章是否显示，由 front matter 控制。
3. _drafts/ 用于完全不公开的临时草稿。
4. status: draft 用于首页可见但不可点击的“更新中”文章。
5. 旧 WordPress / Home Blog 文章使用 original_url 保持外链。
6. 译文统一使用 type: translation。
7. 每篇文章尽量填写 module、status、created、updated，减少歧义。
