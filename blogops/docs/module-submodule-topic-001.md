---
# ========== Identity ==========
id: module-submodule-topic-001
# ↑ 全仓唯一主键，建议与文件名去掉 .md 后保持一致。
# 建议规则：
# posts：posts-YYYYMMDD-topic-001
# natsci：natsci-submodule-topic-001
# netcom：netcom-submodule-topic-001
# blogops / system 等：module-submodule-topic-001

title: 这里写标题（给人看的，可以是中文，不要太长）

# ========== Taxonomy ==========
module: module-name
# 可选：posts / natsci / netcom / blogops / system / narrative
# ↑ 这里选一个一级模块

submodule: submodule-name
# 举例：
# posts：2026 / 2025 / reading / literature / reflection / project
# natsci：taxonomy / reading / methods / ethnobiology
# netcom：ai / architecture / cs / digital / lora / math / mcu / methods / protocol / rf
# blogops：docs / workflow / ops
# 没有明确二级分类时，可写 general

topic: specific-topic
# 举例：meshtastic / coleoptera / ios-shortcuts / wordpress-mailpost
# ↑ 这里写具体对象/主题，用于聚合与检索

# ========== Document Semantics ==========
type: note
# 可选：note / article / essay / index / log / spec / dataset / howto / release / translation
# ↑ 这里选“这份文档是什么类型”
# - note：学习/碎片化笔记
# - article：成文长文
# - essay：随笔/论述
# - index：目录/索引页
# - log：日志/进展
# - spec：规范/标准
# - dataset：资料表/数据整理
# - howto：操作手册
# - release：发布说明
# - translation：译文

status: hidden
# 可选：hidden / draft / active / published / archived / archive
# ↑ 当前生命周期状态
# - hidden：不进自动 index
# - draft：进自动 index，但通常显示为“更新中”
# - active / published：公开并进入自动 index
# - archived / archive：归档，不进自动 index

canonical: true
# 可选：true / false
# ↑ 是否为权威版本。
# 仓库自写主文档通常 true；译文、外部转载、WordPress 原文为准的历史文章通常 false。

# ========== Summary ==========
summary: >
  这里写 1–2 句摘要：
  这篇内容解决什么问题/结论是什么。
  方便人和 AI 快速扫，不要写背景故事。

# ========== Graph Links ==========
parents: []
# 这里写上级节点 id，通常 0 或 1 个。
# 例：[posts-index]

related: []
# 这里写相关文档 id 列表。
# 例：[system-gov-meta-enums-001, system-gov-commit-message-001]

# ========== Tags ==========
tags: []
# 建议 3–8 个关键词。
# 例：[mesh, lora, workflow, taxonomy]

# ========== Audience / Language ==========
audience: [self]
# 可选：self / public / tutorial / collaborator
# ↑ 给谁看的，可多选。

languages: [zh]
# 可选：zh / en / jp
# ↑ 文档内容语言，可多选。

# ========== Quality / Confidence ==========
maturity: draft
# 可选：draft / evolving / stable / deprecated
# ↑ 内容成熟度。不是 status；status 更像生命周期。

confidence: 0.0
# 0.0 - 1.0
# ↑ 对内容准确性的主观把握。

# ========== Visibility / Source of Truth ==========
visibility: private
# 可选：public / private
# ↑ 是否对外可见。

source_of_truth: devlog
# 可选：devlog / external / mixed / translation
# ↑ 这份内容的权威来源在哪里。
# - devlog：仓库文档为准
# - external：外部材料/外部原文为准
# - mixed：仓库整理 + 外部资料混合
# - translation：译文整理；也可统一用 external

# ========== Dates ==========
created: YYYY-MM-DD
updated: YYYY-MM-DD
# ↑ 新建时两者相同；之后只改 updated。

# ========== External / Translation ==========
original_title:
original_source:
original_publisher:
original_url:
translation_note:
# ↑ 译文、转载、历史 WordPress 文章、外部原文为准的文章使用。
# 若填写 original_url，自动 index 可优先链接到外部原文。
# 译文建议：
# type: translation
# canonical: false
# source_of_truth: external
---

## 标题
  
```
（开场白，随便写）
```
  
正文开始
