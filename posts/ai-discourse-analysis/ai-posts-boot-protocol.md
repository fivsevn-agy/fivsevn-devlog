---
id: "ai-posts-boot-protocol"
title: "AI文章生成引导协议"

module: "posts"
submodule: "ai-discourse-analysis"
topic: "ai-posts-boot-protocol"

type: "note"
status: "active"
canonical: true

summary: "说明AI文章生成引导协议。"

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

created: "2026-03-06"
updated: "2026-11-01"
metadata_updated: "2026-11-01"
---

# AI 文章骨架提示词

用户提供标题和可选的主题 slug。只生成文章骨架，正文由用户填写。

1. 读取[栏目目录](index.md)和最近 1–3 篇文章，沿用编号与 metadata 风格。下一篇编号取现有最大值加一，补齐三位。
2. 按[frontmatter 规范](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/spec-content-frontmatter-001.md)生成完整 metadata。标题保留用户原文，沿用栏目编号前缀；slug 使用简短的小写英文与连字符。
3. 发布包保存为 `posts/ai-discourse-analysis/YYYY/MM/NNN-topic-slug/index.md`，年月取文章的 `created` 日期。素材放在同包的 `assets/`，正文用 `assets/文件名` 引用。
4. 固定使用 `module: posts`、`submodule: ai-discourse-analysis`、`type: article`、`status: active`、`canonical: true`、`visibility: public`、`source_of_truth: devlog`、`filename_policy: entrypoint`。`id` 沿用 `posts-ai-discourse-analysis-NNN`，日期使用 `YYYY-MM-DD`。
5. 只输出发布包路径和完整 `index.md`，不添加解释，不填写真实正文。

正文骨架：

```markdown
# 本期材料

（待填写）

# 提示词

（待填写）

# 正文

（待填写）
```

栏目目录由发布流程自动更新，无需手动添加条目。修改旧文时保留原 `id`、目录、`created` 和 `permalink`。
