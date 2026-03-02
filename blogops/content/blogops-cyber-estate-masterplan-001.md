---
id: blogops-cyber-estate-masterplan-001
title: 五月七日赛博地产总规划说明！

module: blogops
submodule: architecture
topic: cyber-estate-masterplan

type: index
status: active
canonical: true

summary: >
  使用“赛博地产”模型解释博客整体分层结构，
  将 Boot / Spec / Canonical / Stream 等概念
  对应到实际仓库与页面位置，作为长期规划说明文件。

parents: []
related: []

tags: [blogops, cyber-estate, architecture, system-map]

audience: [self, public]
languages: [zh]

maturity: stable
confidence: 0.93

visibility: public
source_of_truth: devlog

created: 2026-03-02
updated: 2026-03-02
---
# 五月七日赛博地产总规划说明！

- 个人内容体系说明。

## 1. 地产定位（Boot）

> Boot 是地产开发总纲，是整块地产的存在理由。

- 对应内容：
  - https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/system/ai-boot-protocol.md

- 本地产定位为：
  - 长期结构化知识系统
  - 多层分区运行
  - 强调可回溯与结构稳定
  - 不以流量为主导

> Boot 的修改属于结构级变更，不因短期内容需求而调整。

---
## 2. 施工标准（Spec）

> Spec 是施工标准。

- 对应内容：
  - https://github.com/fivsevn-agy/fivsevn-spec

- 作用：
  - 规定 frontmatter 结构
  - 规定 id 规则
  - 规定模块划分
  - 规定内容拓扑结构

> 未来扩建内容时，必须遵循该规范。

---
## 3. 地产分区总图（Module Map）

> Module Map 是平面规划图。

- 对应文件：
  - https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/system/module-map.md

- 作用：
  - 定义地产分区
  - 说明各区功能
  - 明确内容流向

> 这是总地图。各分区地图参考各分区文件夹内的 map 文件。

---
## 4. 常设馆藏区（Canonical Archive）

> Canonical Archive 是地产的核心资产！

- 对应内容：
  - https://github.com/fivsevn-agy/fivsevn-devlog

- 功能：
  - 存放长期有效内容
  - 可被引用
  - 有结构 id
  - 不依赖时间背景

> N年后仍有价值的内容，必须进入此区！

---
## 5. 流动街区（Stream）

> Stream 可以热闹！但不承担长期存档的职责。

- 对应内容：
  - https://fivsevn.com/posts
  - https://fivsevn.com/foodie
  - https://fivsevn.com/natsci

- 功能：
  - 快速发布
  - 时间性表达
  - 动态展示

---
## 6. 实验开发区（Narrative Layer）

> Narrative Layer 不属于知识主轴，是允许试错的地块，不会自动进入 Canonical 区。

- 对应页面：
  - https://fivsevn.com/kiosk 及其子页面
  - https://57dayshift.wordpress.com

- 功能：
  - 叙事系统
  - 形式实验
  - 风格偏移

---
## 7. 素材仓储区（Assets）

> Assets 提供材料支持。

- 对应内容：
  - https://github.com/fivsevn/fivsevn-assets

- 功能：
  - 图片
  - 图标
  - 静态文件

---
## 8. 物业控制中心（Internal）

> Internal 为后台运维空间，暂不对访客开放。

- 对应内容：
  - https://github.com/fivsevn/fivsevn-internal

- 功能：
  - 自动发布
  - 运维脚本
  - 操作系统

---
## 9. 内容迁移机制

- 一条内容的典型路径：
  - Step1. 首先发布于流动街区（短内容或图片流）
  - Step2. 重写并进行结构化整理
  - Step3. 升级进入常设馆藏区（[devlog](https://github.com/fivsevn-agy/fivsevn-devlog)）

- 升级意味着：
  - 去时间依赖
  - 强化结构
  - 明确边界
  - 可独立存在

> 不过，简单归档不等于升级。

---
## 10. 地产重量等级

- 按系统影响程度排序：
  -  Boot（总纲）
  -  Spec（施工标准）
  -  Devlog（核心资产）
  -  Module Map（规划图）
  -  Stream（流动街区）
  -  Narrative（实验地块）
  -  Assets（仓储）
  -  Internal（物业系统）

> 越靠前，改动影响越大。

---
## 11. 核心原则

- 本赛博地产遵循三条原则：
  - 分区明确
  - 不混用
  - 升级需主动重构
