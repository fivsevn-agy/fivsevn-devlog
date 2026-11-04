---
id: devlog-readme
title: fivsevn-devlog

module: system
submodule: devlog
topic: null

type: index
status: active
canonical: true

summary: null

parents: []
related: []

tags: []

audience:
- self
- internal
languages:
- zh

maturity: evolving
confidence: null

visibility: public
source_of_truth: devlog

filename_policy: entrypoint

created: null
updated: '2026-11-01'
metadata_updated: '2026-11-01'
---

# fivsevn-devlog

[devlog.fivsevn.com](https://devlog.fivsevn.com/) 的内容与发布仓库。

| 目录 | 用途 |
|---|---|
| [posts](posts/README.md) | 年月发布包：文章、译文、AI 话语分析及随文素材 |
| [natsci](natsci/README.md)、[netcom](netcom/README.md) | 按主题整理的自然科学、通信与工程笔记 |
| [Fieldlog](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/natsci/fieldlog/README.md) | 自然观察图片与配文 |
| [intake](intake/README.md) | 信息来源清单与定时阅读页 |
| [blogops](blogops/README.md)、[now](now/README.md) | 手动维护的后台日志与近况 |
| `scripts/`、`schemas/`、`tests/` | 构建、共享规范副本与检查 |

修改内容后推送到 `main`，在 [Actions](https://github.com/fivsevn-agy/fivsevn-devlog/actions) 查看发布结果。文章目录自动生成；草稿放在各模块的 `_drafts/`，已有草稿资料保持原样。

## Actions

- `Build and deploy devlog`：更新目录，构建文章与 Fieldlog，部署 Pages，核验后清理已发布的上传原图。
- `Build Intake Page`：定时或在来源配置变化后生成阅读页，完成后触发网站部署。
- `Apply Draft Frontmatter`：为新草稿补资料。
- `Check document metadata`、`Check Intake Integrity`：检查资料与来源结构。

[系统总览](system-map.md) · [共享规范](https://github.com/fivsevn-agy/fivsevn-spec)
