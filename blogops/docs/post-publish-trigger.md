---
id: blogops-docs-post-publish-trigger-001
title: Post 发布 trigger 维护手册

module: blogops
submodule: docs
topic: post-publish-trigger

type: note
status: active
canonical: true

summary: >
  说明 fivsevn-devlog 中内容发布后触发自动目录更新的 GitHub Actions 规则，
  包括触发范围、执行流程、与 _drafts/frontmatter/自动目录的关系、日常发布流程与排查方法。

parents: []
related: [system-docs-auto-index-manual-001, blogops-docs-auto-draft-frontmatter-001]

tags: [blogops, docs, automation, publish, trigger, github-actions, index]

audience: [self, internal]
languages: [zh]

maturity: stable
confidence: 0.9
visibility: public
source_of_truth: devlog

created: 2026-06-13
updated: 2026-06-15
---
# Post 发布 trigger 维护手册

本仓库的 post 发布 trigger 用于在内容文件被发布或更新后，自动刷新各板块首页目录。

目标是：

```text
写好文章 frontmatter
↓
将文章放在正式内容目录
↓
设置可发布 status
↓
commit / push 到 main
↓
GitHub Actions 触发目录更新
↓
posts/index.md、natsci/index.md、netcom/index.md 自动同步
```

这套 trigger 不负责写作、不负责补 frontmatter，也不负责把 `_drafts/` 草稿正式发布。

它只负责在正式内容进入仓库后，调用自动目录脚本，把首页目录更新到最新状态。

---

## 1. 当前 trigger 文件

GitHub Actions 文件：

```text
.github/workflows/update-indexes.yml
```

执行脚本：

```text
scripts/update_module_indexes.py
```

自动更新的目标文件：

```text
posts/index.md
natsci/index.md
netcom/index.md
```

其中：

- workflow 负责判断什么时候运行；
- Python 脚本负责判断哪些文章应该进入目录；
- index 文件只保存生成结果。

---

## 2. trigger 触发条件

当前 workflow 在以下情况触发：

```yaml
on:
  push:
    branches:
      - main
    paths:
      - "posts/**/*.md"
      - "natsci/**/*.md"
      - "netcom/**/*.md"
      - "scripts/update_module_indexes.py"
      - ".github/workflows/update-indexes.yml"
  workflow_dispatch:
```

也就是说，只要向 `main` 分支 push，并且改动命中以上路径之一，workflow 就会运行。

常见触发场景：

```text
posts/2026/example.md
natsci/taxonomy/example.md
netcom/rf/example.md
scripts/update_module_indexes.py
.github/workflows/update-indexes.yml
```

此外，也可以在 GitHub Actions 页面手动运行：

```text
workflow_dispatch
```

---

## 3. trigger 和脚本的分工

trigger 只判断“要不要启动 workflow”。

真正判断文章是否进入目录的是：

```text
scripts/update_module_indexes.py
```

因此会出现一种正常情况：

```text
push 命中了 posts/**/*.md
↓
workflow 被触发
↓
脚本扫描后发现没有需要更新的目录内容
↓
不产生 commit
```

这不是错误。

例如，只修改了一个不会显示的隐藏文章，或者只修改了 `_drafts/` 中的文件，workflow 可能会被路径规则唤醒，但脚本最终不会把它放进首页目录。

---

## 4. 执行流程

workflow 的执行顺序是：

1. checkout 仓库；
2. 运行自动目录脚本；
3. 检查三个 index 文件是否发生变化；
4. 如果没有变化，直接退出；
5. 如果有变化，自动提交并 push。

核心命令：

```bash
python scripts/update_module_indexes.py
```

自动提交时只提交以下文件：

```text
posts/index.md
natsci/index.md
netcom/index.md
```

自动 commit message：

```text
chore: update module indexes [skip ci]
```

---

## 5. 哪些发布会进入目录

文章能否进入首页目录，不由 trigger 直接决定，而由 frontmatter 决定。

以下状态会进入目录，并生成可点击链接：

```yaml
status: active
```

```yaml
status: publish
```

```yaml
status: published
```

生成效果：

```md
- 2026.06.13 [文章标题](文章路径.md)
```

链接目标由自动目录脚本决定：译文文章链接仓库内译文页面；非译文且有 `original_url` 时可以链接外部原文。

---

## 6. 哪些状态只显示但不发布链接

以下状态会进入目录，但不生成链接：

```yaml
status: draft
```

生成效果：

```md
- 2026.06.13 文章标题（更新中）
```

这适合公开预告型文章。

注意：这和 `_drafts/` 不是同一件事。

`status: draft` 必须位于正式内容目录中，例如：

```text
posts/2026/example.md
natsci/taxonomy/example.md
netcom/rf/example.md
```

---

## 7. 哪些内容不会被发布

以下状态不会进入目录：

```yaml
status: hidden
status: private
status: archived
status: archive
```

没有 `status` 的文章也不会显示。

以下目录也不会进入目录：

```text
_drafts/
assets/
.github/
.obsidian/
node_modules/
__pycache__/
```

目前 `posts/ai-discourse-analysis/` 也会被 `posts` 目录索引排除。

以下文件名不会被当作文章处理：

```text
index.md
map.md
README.md
.DS_Store
.cache
.gitkeep
```

---

## 8. 和 `_drafts/` 草稿自动 frontmatter 的关系

`_drafts/` 是私有草稿缓冲区。

草稿自动 frontmatter workflow 负责把 `_drafts/` 里的随手草稿整理成统一格式，例如：

```yaml
status: hidden
visibility: private
maturity: draft
```

这些文件不会进入首页目录。

即使 `_drafts/` 文件被路径规则命中，自动目录脚本也会排除 `_drafts/`。

因此：

```text
_drafts/ 自动 frontmatter
≠
正式发布
```

正式发布仍然需要人工移动文件、改正式文件名、改正式 id，并设置公开状态。

---

## 9. 正式发布流程

### 从 `_drafts/` 发布

1. 将草稿移出 `_drafts/`；
2. 放入对应模块的正式内容目录；
3. 改成正式文件名；
4. 修改 frontmatter 中的 `id`，使它和正式文件名一致；
5. 修改 `submodule` 和 `topic`；
6. 设置：

```yaml
status: active
visibility: public
maturity: evolving
```

7. commit 并 push 到 `main`；
8. `update-indexes.yml` 自动运行；
9. 对应首页目录出现可点击链接。

示例：

```text
posts/_drafts/posts-20260613-draft-001.md
```

正式发布为：

```text
posts/2026/posts-20260613-example.md
```

frontmatter 同步改为：

```yaml
id: posts-20260613-example
module: posts
submodule: 2026
topic: example
status: active
visibility: public
maturity: evolving
```

---

### 将公开草稿改为正式文章

如果文章已经位于正式内容目录，并且当前是：

```yaml
status: draft
```

只需要改成：

```yaml
status: active
```

或：

```yaml
status: publish
```

然后 commit / push。

下一次 workflow 运行后，目录会从：

```md
- 2026.06.13 文章标题（更新中）
```

变成：

```md
- 2026.06.13 [文章标题](文章路径.md)
```

---

## 10. 日期读取规则

首页目录排序日期按以下优先级读取：

```text
created > date > updated
```

推荐正式文章至少填写：

```yaml
created: 2026-06-13
updated: 2026-06-13
```

如果没有 `created`，脚本会使用 `date`。

如果没有 `created` 和 `date`，脚本才会使用 `updated`。

不建议只依赖 `updated` 作为发布日期。

---

## 11. 本地手动测试

如果想在 push 前检查 trigger 会产生什么结果，可以在仓库根目录运行：

```bash
python scripts/update_module_indexes.py
```

查看目录文件变化：

```bash
git diff -- posts/index.md natsci/index.md netcom/index.md
```

如果确认无误，可以提交：

```bash
git add posts/index.md natsci/index.md netcom/index.md
git commit -m "chore: update module indexes"
git push
```

正常情况下，不需要手动提交 index 文件。

push 到 `main` 后，GitHub Actions 会自动处理。

---

## 12. 常见排查

### workflow 没有运行

检查：

1. 是否 push 到 `main`；
2. 改动路径是否命中 workflow 的 `paths`；
3. GitHub Actions 是否启用；
4. 是否可以用 `workflow_dispatch` 手动运行。

---

### workflow 运行了，但目录没有变化

检查：

1. 文章是否在正式内容目录，而不是 `_drafts/`；
2. 文件是否是 `.md`；
3. 文件开头是否有 frontmatter；
4. frontmatter 是否有 `title`；
5. 是否有有效日期；
6. `status` 是否是可显示状态；
7. `module` 是否和所在目录一致；
8. 文件名是否不是 `index.md`、`map.md`、`README.md`；
9. 路径是否不在排除目录中。

---

### 文章显示成纯文本，没有链接

检查是否仍然是：

```yaml
status: draft
```

如果要正式发布，改为：

```yaml
status: active
```

或：

```yaml
status: publish
```

---

### 文章完全不显示

优先检查：

```yaml
status: hidden
status: private
status: archived
status: archive
```

以及是否位于：

```text
_drafts/
assets/
```

这些情况都会被自动目录排除。

---

## 13. 快速规则表

| 情况 | workflow 是否可能触发 | 是否进入目录 | 是否生成链接 |
|---|---:|---:|---:|
| 修改 `posts/**/*.md` | 是 | 取决于 frontmatter | 取决于 status |
| 修改 `natsci/**/*.md` | 是 | 取决于 frontmatter | 取决于 status |
| 修改 `netcom/**/*.md` | 是 | 取决于 frontmatter | 取决于 status |
| 修改 `_drafts/*.md` | 是 | 否 | 否 |
| 修改 `assets/` | 可能，取决于路径 | 否 | 否 |
| 修改 `blogops/docs/*.md` | 否 | 否 | 否 |
| `status: active` | 是，若路径命中 | 是 | 是 |
| `status: publish` | 是，若路径命中 | 是 | 是 |
| `status: published` | 是，若路径命中 | 是 | 是 |
| `status: draft` | 是，若路径命中 | 是 | 否 |
| `status: hidden` | 是，若路径命中 | 否 | 否 |
| 没有 frontmatter | 是，若路径命中 | 否 | 否 |
| 没有 title | 是，若路径命中 | 否 | 否 |
| 没有有效日期 | 是，若路径命中 | 否 | 否 |

---

## 14. 推荐发布 frontmatter

### posts 正式文章

```yaml
---
id: posts-20260613-example
title: 文章标题

module: posts
submodule: 2026
topic: example

type: note
status: active
canonical: true

summary: >
  TODO

parents: []
related: []

tags: [posts]

audience: [self]
languages: [zh]

maturity: evolving
confidence: 0.8

visibility: public
source_of_truth: devlog

created: 2026-06-13
updated: 2026-06-13
---
```

### 公开预告文章

```yaml
---
id: posts-20260613-example
title: 文章标题

module: posts
submodule: 2026
topic: example

type: note
status: draft
canonical: true

summary: >
  TODO

parents: []
related: []

tags: [posts]

audience: [self]
languages: [zh]

maturity: draft
confidence: 0.5

visibility: public
source_of_truth: devlog

created: 2026-06-13
updated: 2026-06-13
---
```

---

## 15. 维护原则

1. trigger 只负责启动自动目录更新，不负责判断文章内容质量。
2. 文章是否显示，由 frontmatter 控制。
3. `_drafts/` 是私有草稿区，不参与正式发布。
4. `status: draft` 是公开预告，不是私有草稿。
5. 正式发布时使用 `status: active` 或 `status: publish`。
6. 正式发布时尽量同步维护 `id`、`module`、`submodule`、`topic`、`created`、`updated`。
7. 首页目录不要手动维护，交给 `scripts/update_module_indexes.py` 生成。
8. workflow 文件只维护触发条件和执行流程，不承载目录生成规则。
