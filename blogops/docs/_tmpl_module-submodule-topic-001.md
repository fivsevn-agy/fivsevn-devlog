---
# ========== Identity ==========
id: module-submodule-topic-001
# ↑ 全仓唯一主键（不随文件名变），建议规则：
#   {module}-{submodule}-{topic}-{NNN}
#   NNN 从 001 递增

title: ”这里写标题（给人看的，不要太长）“

# ========== Taxonomy ==========
module: module-name
# 可选：natsci / netcom / posts / blogops / system / narrative
# ↑ 这里选一个一级模块

submodule: submodule-name
# 举例：rf / lora / taxonomy / workflow / ops / security / etc
# ↑ 这里写二级分类；没有就写 general 或留空

topic: specific-topic
# 举例：meshtastic / coleoptera / ios-shortcuts / wordpress-mailpost
# ↑ 这里写“具体对象/主题”，用于聚合与检索

# ========== Document Semantics ==========
type: note
# 可选：note / article / index / log / spec / release
# ↑ 这里选“这份文档是什么类型”
#   - note：学习/碎片化笔记
#   - article：成文长文
#   - index：目录/索引页
#   - log：日志/进展
#   - spec：规范/标准
#   - release：发布说明

status: draft
# 可选：draft / active / archived
# ↑ 这里写当前生命周期状态

canonical: true
# 可选：true / false
# ↑ 是否“权威版本”（同主题多份文档时用；一般 devlog 主文档写 true）

# ========== Summary ==========
summary: >
  这里写 1–2 句摘要：这篇内容解决什么问题/结论是什么。
  （方便我和 AI 快速扫，不要写背景故事）

# ========== Graph Links ==========
parents: []
# 这里写上级节点 id（通常 0 或 1 个）
# 例：[posts-index-001]

related: []
# 这里写相关文档 id 列表
# 例：[system-gov-meta-enums-001, system-gov-commit-message-001]

# ========== Tags ==========
tags: []
# 建议 3–8 个关键词
# 例：[mesh, lora, workflow, taxonomy]

# ========== Audience / Language ==========
audience: [self]
# 可选：self / public / tutorial / collaborator
# ↑ 给谁看的（可多选）

languages: [zh]
# 可选：zh / en / jp
# ↑ 文档内容语言（可多选）

# ========== Quality / Confidence ==========
maturity: evolving
# 可选：draft / evolving / stable / deprecated
# ↑ 这份内容的成熟度（不是 status；status 更像生命周期）

confidence: 0.70
# 0.00 - 1.00
# ↑ 我对内容准确性的主观把握

# ========== Visibility / Source of Truth ==========
visibility: public
# 可选：public / private
# ↑ 是否对外可见

source_of_truth: devlog
# 可选：devlog / site / other
# ↑ 这份内容的“权威来源在哪里”
#   - devlog：仓库文档为准
#   - site：网站发布为准
#   - other：外部材料/第三方为准

# ========== Dates ==========
created: YYYY-MM-DD
updated: YYYY-MM-DD
# ↑ 占位：新建时两者相同；之后只改 updated
---
## 标题

```
（开场白，随便写）
```

正文开始


