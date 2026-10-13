---
id: "posts-2026-umwelt-game-development-handbook-001"
title: "游戏开发流程手册｜ChatGPT 写给五月七日的指导笔记 001"

module: "posts"
submodule: "2026"
topic: "umwelt-game-development-handbook"

type: "note"
status: "active"
canonical: true

summary: |
  从立项、设计、原型、垂直切片到制作、验收、发布与维护，理解游戏开发的职责、交付物和判断标准。以 UMWELT 为贯穿案例，补充知名游戏的制作记录、工具成本及教材和公开视频资源，不展开编程操作。

parents: ["posts-index"]
related: ["posts-2026-umwelt-game-development-handbook-002", "posts-2026-umwelt-game-development-handbook-003", "posts-2026-umwelt-game-development-handbook-004", "posts-2026-umwelt-game-development-handbook-005", "posts-2026-umwelt-game-development-handbook-006", "posts-2026-umwelt-game-development-handbook-007"]
tags: ["game-development", "umwelt", "production", "qa", "workflow", "handbook"]
audience: ["self", "public"]
languages: ["zh"]
maturity: "evolving"
confidence: 0.9
visibility: "public"
source_of_truth: "devlog"
lang: "zh-CN"
description: "从项目负责人的角度理解游戏开发全流程、交付关系、成本和验收，附实际案例与参考资源。"
canonical_url: "https://devlog.fivsevn.com/posts/2026/posts-2026-umwelt-game-development-handbook-001.html"
created: "2026-10-13"
updated: "2026-10-13"
metadata_updated: "2026-10-13"
---

# 游戏开发流程手册｜ChatGPT 写给五月七日的指导笔记 001

**以 UMWELT 为例 · 撰写：ChatGPT · 2026-10-13**

**001 制作流程** · [002 软件与成本](posts-2026-umwelt-game-development-handbook-002.html) · [003 运行原理](posts-2026-umwelt-game-development-handbook-003.html) · [004 画面与动画](posts-2026-umwelt-game-development-handbook-004.html) · [005 玩法与叙事](posts-2026-umwelt-game-development-handbook-005.html) · [006 修改与发布](posts-2026-umwelt-game-development-handbook-006.html) · [007 研究与表达](posts-2026-umwelt-game-development-handbook-007.html)

游戏开发包括确定作品范围、建立制作方式、持续交付内容、验证质量以及发布后维护。**流程的作用，是让每个阶段都有明确的成果和继续投入的依据，而不只是一个完成百分比。**

本系列面向需要理解和管理制作、但不必亲自编写代码的创作者。程序语法、终端命令与软件按钮不作为学习重点；需要掌握的是系统职责、制作取舍、成本和验收方法。

本文以 UMWELT 中的《等足目赋格》及配套实验室为贯穿案例。项目区分科学资料、工作性判断、视觉表现和游戏参数。[1](#ref-1) 下文的“新增一段生境观察”是演示性任务，不是对实际开发顺序的追认，也不是本次运行过的测试报告。

<a id="overview"></a>
## 流程总览

原型和垂直切片通常属于前期制作，这里为方便查阅单独列出。阶段可以合并或反复进行，实际团队应按风险和资源安排；它不是统一的行业强制流程。[2](#ref-2)[3](#ref-3)

| 阶段 | 主要内容 | 交付物 |
| --- | --- | --- |
| [1. 概念与立项](#phase-1) | 确定体验、目标平台与首版范围 | 一页概念、范围与风险清单 |
| [2. 前期设计与计划](#phase-2) | 约定规则、资源、分工与制作方式 | 设计文档、技术约定、制作计划 |
| [3. 原型验证](#phase-3) | 检验核心体验与关键技术假设 | 原型、试玩记录与结论 |
| [4. 垂直切片](#phase-4) | 检验目标品质能否稳定制作 | 代表性片段、质量基准与成本估计 |
| [5. 正式制作](#phase-5) | 持续完成并整合功能与内容 | 可运行版本、资源、审查记录 |
| [6. QA、验收与打磨](#phase-6) | 检查功能、体验与剩余风险 | 测试证据、缺陷清单、放行结论 |
| [7. 发布](#phase-7) | 生成、审核并交付玩家端成品 | 发布版本、说明与恢复方案 |
| [8. 维护与复盘](#phase-8) | 修复、扩展、归档或结束支持 | 补丁、兼容记录与复盘 |
| [成本与工具](#cost) | 比较许可、人力、资源和维护成本 | 费用类型与采购检查 |
| [参考与学习资源](#references) | 教材、开发记录与公开视频 | 按主题查阅的学习入口 |

资料核查、授权、无障碍和测试不应全部推迟到制作结束。宣传与发行准备同样需要提前安排，但不能因此夸大尚未完成的功能。

<a id="phase-1"></a>
## 1｜Concept：概念与立项

**目标：确定核心体验，并给第一版划出边界。**

概念说明至少包含目标玩家、主要行为、体验方向、平台、预计体量和发布方式。限制条件包括时间、预算、人员能力、素材、工具与资料获取。免费作品也会消耗这些资源。

首版范围应区分必须实现、可以延后和明确不做的内容。高风险部分先列出，例如操作理解、设备性能、资料可靠性、内容量与长期维护，而不是按想法出现的顺序全部开工。

**UMWELT 演示。** 首版只完成一个生境和一条可结束的观察路径：玩家观察差异，进行一次操作，得到反馈。更多物种、复杂天气和联网功能暂不纳入。实际生物学资料用于支撑内容，作品内部参数不能直接写成测量结果或饲养标准。[1](#ref-1)

| 术语 | 定义与解释 |
| --- | --- |
| Concept／概念 | 对作品体验、对象和基本形式的概括 |
| Pitch／提案 | 向合作者、团队或发行方说明项目价值与实施条件 |
| Target Audience／目标受众 | 主要服务的玩家群体，而非所有人 |
| USP／独特卖点 | 作品值得被选择的特点，不只是软件或题材名称 |
| Design Pillars／设计支柱 | 少数用于取舍的体验原则，例如观察优先于数值竞争 |
| Scope／范围 | 承诺制作的功能、内容、平台和品质边界 |
| Greenlight／立项放行 | 根据当前证据批准继续投入 |

**交付与放行：** 概念、首版范围、资源估计与风险排序。负责人能够说明继续投入的理由，也知道哪些验证结果会要求缩小或改变方案。

<a id="phase-2"></a>
## 2｜Pre-production：前期设计与计划

**目标：把想法变成可以分工和检查的约定。**

设计文档说明入口、操作、状态变化、结束条件以及中断、失败与恢复行为。叙事项目还需整理节点、条件和分支，不能只交付对白。技术约定记录平台、模块、数据、存档与资源接入关系；美术和声音规范记录风格与交付规格。[4](#ref-4)

文档应随已确认设计更新。历史方案可以保留，但应与当前要求区分，避免程序、美术和测试依据不同版本工作。

### 职责与交接

| 职责 | 主要内容 |
| --- | --- |
| 制作人／Producer | 协调范围、人员、预算、进度和交付 |
| 游戏设计师／Game Designer | 设计规则、操作和体验结构 |
| 叙事设计师／Narrative Designer | 组织故事、状态、选择与交互的关系 |
| 程序开发 | 实现系统及其连接，处理运行与数据 |
| 美术与动画 | 制作视觉资源、动作与表现 |
| 音频 | 制作声音并安排运行时的反馈 |
| 技术美术／Technical Artist | 连接视觉制作与运行要求，处理相关工具和管线 |
| QA 与测试 | 提供质量风险、检查方法和验证信息 |

这些是职责，而非必须招聘的岗位数量。个人可以兼任，但制作、决定和验收的责任仍应明确。[2](#ref-2)

**UMWELT 演示。** 新增生境需要先区分内容扩展与功能扩展，并核对稳定标识、配套实验室、多语言和旧存档。登记名称或加入一段文字，不等于已经完成游戏接入。[5](#ref-5)

| 术语 | 定义与解释 |
| --- | --- |
| GDD／游戏设计文档 | 记录玩法、规则、内容与体验目标 |
| TDD／技术设计文档 | 记录技术安排；该缩写在另一语境也指测试驱动开发 |
| Art Bible／美术规范 | 统一视觉风格与交付标准的参考 |
| UI／界面；UX／使用体验 | 前者是可见控件与信息，后者包含理解、操作与反馈全过程 |
| Pipeline／制作管线 | 内容从源文件到游戏成品的处理和交付步骤 |
| Data Contract／数据约定 | 规定字段、含义、稳定标识与兼容边界 |
| Milestone／里程碑 | 有明确成果和放行条件的检查点 |
| Dependency／依赖 | 一项工作所需要的其他成果或前提 |

**交付与放行：** 简版设计、技术约定、资源规格、分工与里程碑。尚未确定的关键问题明确进入验证，而不是隐藏在笼统的进度描述中。

<a id="phase-3"></a>
## 3｜Prototype：原型验证

**目标：用较小投入消除关键不确定性。**

一个原型应对应有限的验证目标，例如确认触碰反馈能被理解、观察与选择的节奏成立，或目标设备能够运行关键效果。原型可以使用临时素材、纸面流程和简化程序，不必达到最终画面质量。

**UMWELT 演示。** 先完成“观察—操作—反馈—继续观察”的短循环，记录未参与制作的试玩者在哪里停顿、误解或反复尝试。观察型作品可以以注意力和理解为目标，不必把刺激程度作为唯一指标。

外观精美的片段不能替代交互验证；一次完整运行也不能证明长期内容量可承受。原型代码可以保留或舍弃，应依据结构和风险，而不是只依据已经花费的时间。

| 术语 | 定义与解释 |
| --- | --- |
| Prototype／原型 | 用于检验设计或技术假设的模型 |
| PoC／概念验证 | 侧重确认某种方案可行，与原型的用法可能交叉 |
| Mechanic／机制 | 具体操作与规则之间的关系 |
| Core Loop／核心循环 | 玩家反复经历的行为与反馈结构 |
| Playtest／试玩测试 | 通过实际参与观察理解与体验，不只是寻找程序报错 |
| Timebox／限时验证 | 预先限制投入，到期根据证据决定下一步 |
| MVP／最小可行产品 | 用较小产品验证价值等假设，不是所有游戏必经的版本名称 |

**交付与放行：** 原型、验证目标、观察记录和决定。原型的主要价值是减少风险，而不是尽量多留下临时内容。[3](#ref-3)

<a id="phase-4"></a>
## 4｜Vertical Slice：垂直切片

**目标：通过一小段代表性内容，检验目标品质与制作方法。**

切片应接近目标质量，并贯通交互、画面、声音、文字和必要的保存功能。它的作用不仅是证明体验成立，还包括估计下一段内容怎样生产、需要多少工作以及哪里容易返工。[3](#ref-3)

**UMWELT 演示。** 从正常入口开始，完成观察、操作、反馈、保存和资料查阅；加入代表性长文本、声音和手机布局，检查各环节是否能够共同运行。不能只选择最容易展示的一部分，然后把其他困难当成已经解决。

**《Dead Cells》制作案例。** 美术作者介绍的三维到二维动画流程，重视动作调整与反复修改的效率。[18](#ref-18) 它不直接证明某种切片方法，而是说明：制作能力需要在真实的修改与交付中检验，不能只比较单张成图。

| 术语 | 定义与解释 |
| --- | --- |
| Vertical Slice／垂直切片 | 内容范围较小，但贯通主要制作环节并接近目标品质 |
| Horizontal Slice／水平切片 | 覆盖较多系统或流程，但各部分可能较粗略 |
| Demo／演示或试玩版 | 面向展示和体验的版本用途，不等于原型或切片 |
| Quality Bar／质量基准 | 后续内容需要达到的可比较标准 |
| Production-ready／具备生产条件 | 方法、工具与流程能够支持后续持续制作 |

**交付与放行：** 可玩的代表性片段、质量基准、步骤与成本估计。原型主要检验假设，切片进一步检验按目标品质生产的能力；极小项目可以合并执行，但仍要分别确认这两项结论。

<a id="phase-5"></a>
## 5｜Production：正式制作与迭代

**目标：持续交付完整功能与内容，并保持可以整合和验证。**

每轮先确定有限任务，明确影响与验收标准，再完成实现、接入、审查和测试。新想法进入待办记录；若扩大范围，应同时调整预算、时间和验证计划。

功能提供能力，内容利用能力形成具体体验。增加一种角色外观可能复用已有功能，增加一种控制方式则可能影响多个系统。美术源文件与运行资源同样需要区分，不能把源文件整理直接当作成品更新。

### 演示性验收约定

| 项目 | 约定 |
| --- | --- |
| 任务 | 新增一段生境观察 |
| 范围 | 一个入口、一段观察、一组反馈，不改变其他生境 |
| 功能结果 | 可以从正常入口进入并完成，一次操作产生一次预期变化 |
| 数据结果 | 中途保存并恢复后，进度与反馈一致 |
| 显示结果 | 目标语言和屏幕中无缺字、溢出或不可操作区域 |
| 兼容结果 | 未修改内容与支持范围内的旧存档仍按约定运行 |
| 证据 | 交付版本、执行过的检查、截图及未验证部分 |

**验收标准**针对某项需求；**完成定义／DoD**是各任务共用的质量底线，例如完成审查、必要检查和文档同步。两者分别说明这项任务的具体结果与项目共同的交付要求。[6](#ref-6)

版本控制用于记录、比较和恢复修改，持续集成用于自动执行已配置的检查；它们不能代替设计决定与实际试玩。[7](#ref-7)[8](#ref-8)

| 术语 | 定义与解释 |
| --- | --- |
| Feature／功能；Content／内容 | 能力与利用这些能力形成的具体体验 |
| Asset／资源 | 图像、模型、动画、音频和字体等内容 |
| Backlog／待办池；Ticket／任务单 | 前者保存排序后的工作，后者描述一项任务或问题 |
| Iteration／迭代；Sprint／冲刺 | 迭代是反复交付与调整；Sprint 是 Scrum 中有特定规则的固定周期，并非任何赶工阶段 |
| Commit／提交；Branch／分支 | 一组版本记录与相对独立的修改路线 |
| Merge／合并；PR／合并请求 | 整合修改，以及提出和审查待整合修改的记录 |
| Code Review／代码审查 | 检查实现与风险，不等于已运行成品 |
| Build／构建 | 生成可交付程序的过程，也可指生成的版本 |
| CI／持续集成 | 经常整合修改，并自动执行相应检查 |
| CD／持续交付或持续部署 | 前者保持可发布状态，后者按配置将通过检查的版本部署出去 |
| Refactoring／重构 | 调整内部组织，同时维持约定的外部行为 |
| Technical Debt／技术债务 | 可能增加后续修改与维护负担的实现或流程问题 |
| Scope Creep／范围蔓延 | 增加原计划以外的要求，却没有同步调整资源与计划 |

运行相关的状态、事件、渲染和模块关系在 [003](posts-2026-umwelt-game-development-handbook-003.html) 展开，不需要在本篇学习具体编程写法。

**交付与放行：** 每轮形成可运行、可追踪且有验证记录的版本，而不是等所有内容完成后才首次整合。

<a id="phase-6"></a>
## 6｜QA、验收与打磨

**目标：依据证据判断质量与剩余风险。**

QA／质量保证关注过程中的预防与改进，QC／质量控制关注成果质量，测试是重要检查手段。它们有关联，但不是相同概念。[9](#ref-9)

| 检查方式 | 主要内容 |
| --- | --- |
| 单元、集成与端到端检查 | 分别检查局部规则、模块协作和完整操作链 |
| 冒烟检查 | 快速检查启动、关键加载和主要流程 |
| 功能与边界检查 | 同时覆盖正常输入、连续操作、中断和失败 |
| 修复复测与回归 | 分别确认原问题已修复，以及其他行为未被破坏 |
| 兼容性 | 检查约定系统、浏览器、屏幕和输入方式 |
| 性能 | 测量加载、执行时间、内存与长时间运行情况 |
| 叙事与本地化 | 检查分支、条件、人物一致性、译文、字体与布局 |
| 易用性与试玩 | 观察理解、节奏、操作与体验目标 |
| 无障碍 | 检查文字、对比度、替代输入、音量与运动效果 |
| 安全、隐私与来源 | 检查秘密、个人信息、外部输入和事实依据 |

这些不是互斥分类。无障碍检查可以同时涉及界面、输入、声音和测试设备；Xbox 的公开指南可提供检查方向，但不能直接当成认证结论。[10](#ref-10)

**UMWELT 的实际边界。** 仓库把普通自动检查与浏览器回归分开。前者通过，不自动证明视觉、真机或发布成品正确；没有提供比较基线时，也不能声称新旧画面完全相同。[11](#ref-11) 设备模拟可以配置屏幕和输入等条件，但仍需与真实设备验收区分。[12](#ref-12)

### 缺陷处理与记录

可以按登记、排序、定位、修复、复测、必要回归和关闭组织处理。无法复现、暂缓和重复的问题，也应记录原因。严重程度描述影响，优先级描述处理顺序；P0、P1 等编号由项目约定。[9](#ref-9)

| 缺陷记录 | 需要包含的内容 |
| --- | --- |
| 身份 | 编号、标题、发现时间与交付版本 |
| 环境 | 设备、系统、浏览器及必要的设置 |
| 前提与步骤 | 进入问题前的状态，以及可以重复执行的操作 |
| 预期与实际 | 分别记录正确结果与观察到的现象 |
| 证据 | 日志、存档样本、截图或录屏，以及复现次数 |
| 处置 | 影响、优先级、负责人和验证结论 |

记录现象时应与原因猜测分开。删除报错文字不等于修复，未发现问题也不等于证明不存在问题。

### 阶段名称与质量状态

| 名称 | 可采用的项目定义 |
| --- | --- |
| Alpha／阿尔法 | 主要功能能够共同运行，可能仍有临时资源或缺失内容 |
| Feature Complete／功能齐备 | 约定功能已实现，不自动代表内容和质量齐备 |
| Beta／贝塔 | 功能与内容接近齐备，主要处理缺陷、兼容和体验问题 |
| Content Complete／内容齐备 | 计划内容已接入，仍可能需要校对和调整 |
| Freeze／冻结 | 对新增和修改设置门槛，不是绝对禁止修复 |
| Blocker／阻断问题 | 阻止必要测试、推进或发布的问题 |
| Softlock／软锁 | 程序仍运行，但玩家无法按正常流程继续 |
| Baseline／基线 | 用于比较的参考版本或结果 |
| Profiling／性能分析 | 测量开销并定位瓶颈 |
| Polish／打磨 | 消除妨碍目标体验的粗糙处，而非无限增加效果 |

Alpha、Beta 没有跨团队统一的完成百分比，应以项目约定为准。[3](#ref-3)

**交付与放行：** 记录测试对象、范围、结果和未覆盖部分。阻断问题已处理，其余风险有明确的接受、暂缓或修复决定。

<a id="phase-7"></a>
## 7｜Release：发布准备与分发

**目标：交付可以识别、运行和支持的成品。**

发布前固定待交付版本，生成候选成品，再对成品检查。源目录能运行，不保证导出后的路径、压缩资源、字体、离线行为与存档仍然一致。UMWELT 的发布流程会准备站点、处理字体并写入资源版本标识，因此源文件检查与最终成品检查需要分别记录。[13](#ref-13)

**《Baldur’s Gate 3》案例。** Larian 对 2023 年 Hotfix 4 的复盘说明，临近发布的重新构建与已测试候选版之间出现了差异，回退又影响了部分新存档的使用。[19](#ref-19) 它提醒项目同时检查发布版本身份与数据兼容，而不是只确认某次测试曾经通过。

| 发布检查 | 主要内容 |
| --- | --- |
| 体验与数据 | 首次进入、退出、恢复、更新和必要的离线行为 |
| 平台条件 | 输入、性能、签名、开发者资格、审核与内容要求 |
| 发布材料 | 说明、截图、预告、系统要求、已知问题和反馈方式 |
| 权限与来源 | 素材、字体、代码、音频与个人资料的公开边界 |
| 恢复能力 | 上个稳定成品、回退步骤及玩家数据处理 |

网页音频需要考虑自动播放限制；本地存储受来源与浏览器条件影响，不自动提供跨域云存档。[14](#ref-14)[15](#ref-15) 商店发行另有材料和审核，例如 Steam 分别检查商店页与游戏构建。[16](#ref-16)

| 术语 | 定义与解释 |
| --- | --- |
| RC／候选发布版本 | 用于最后验证的候选，发现问题后可以产生下一版 |
| Release Build／发布构建 | 按正式配置生成的成品，不自动代表质量合格 |
| Artifact／构建产物 | 流程输出的站点、安装包或其他文件 |
| Tag／标签 | 为特定提交标注版本名称 |
| Deployment／部署；Release／发布 | 将成品放入环境，与向玩家提供版本，二者不必同时发生 |
| Certification／平台认证 | 满足特定平台的技术或发行要求，不是艺术品质认证 |
| Rollback／回退 | 恢复到之前的程序或配置；数据恢复另行处理 |
| Early Access／抢先体验 | 向玩家提供开发中作品的发行安排，不是 Beta 的同义词 |

抢先体验应准确说明当前可用内容和限制，不能只依靠未来承诺支撑现有产品。[17](#ref-17)

**交付与放行：** 版本与成品对应，材料和已知问题准确，恢复方案明确。部署后从公开入口核对真实访问或下载结果。

<a id="phase-8"></a>
## 8｜Maintenance：维护、扩展与复盘

**目标：控制发布后的风险，保持可持续的支持范围。**

玩家反馈需要区分缺陷、设计分歧、设备问题与新内容建议，再按影响处理。扩展重新经过范围确认、影响分析、实现和验证；不能因为已经上线，就跳过测试和来源检查。

**UMWELT 演示。** 新增物种、环境或结局时，同步检查资料、稳定标识、实验室、语言和存档。资料修订与游戏规则调整应分别说明，不能让旧进度在没有说明的情况下产生新的含义。[5](#ref-5)[11](#ref-11)

| 术语 | 定义与解释 |
| --- | --- |
| Patch／补丁 | 对已有版本进行修复或调整 |
| Hotfix／紧急修复 | 针对需要快速处理的问题，仍需必要验证 |
| Changelog／变更记录 | 保存不同版本的修改历史 |
| Release Notes／发行说明 | 面向某次交付说明功能、修复、限制与注意事项 |
| Migration／迁移 | 将旧数据转换到新结构，需要失败处理与兼容约定 |
| LiveOps／持续运营 | 持续安排活动、内容或服务；不是所有单机项目的必需模式 |
| Postmortem／复盘 | 根据实际过程分析成效、成本、返工与改进 |
| EOL／结束支持 | 明确产品或版本不再继续支持的状态与影响 |

**交付与放行：** 补丁经过相应验证，兼容策略和更新说明清楚。结束维护时保留必要版本、资料与使用说明，支持边界应可查。

<a id="cost"></a>
## 成本与工具：许可费不等于总成本

用途与授权是两个维度。软件可以开源但提供付费成品或托管服务，也可以闭源但在特定条件下免费。以下为本篇涉及或可用于该环节的代表工具；不是声称 UMWELT 已经使用全部工具。标注日期：**2026-10-13**。完整逐项对照见 [002](posts-2026-umwelt-game-development-handbook-002.html#cost-legend)。

| 工具／平台 | 开放情况 | 费用与成本边界 |
| --- | --- | --- |
| [Unity](https://unity.com/products) | 专有软件 | 条件免费；其他适用方案按席位等收费 |
| [Godot](https://godotengine.org/license/) | 开源，MIT | 引擎免费；素材、平台适配和人力另计 |
| [Blender](https://www.blender.org/about/license/) | 开源 | 软件免费；三维生产仍有制作、硬件与维护成本 |
| [Git](https://git-scm.com/about) | 开源 | 软件免费；托管和备份另计 |
| [GitHub](https://github.com/pricing)／[Actions](https://docs.github.com/en/billing/concepts/product-billing/github-actions)／[Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) | 平台与云服务 | 免费适用范围、额度与付费方案并存；仓库、自动执行和网页托管分别判断 |
| [Node.js](https://nodejs.org/en/about)／[Playwright](https://playwright.dev/) | 开源 | 验证工具本身免费；设备和云端执行资源可能收费 |
| [Steamworks](https://partner.steamgames.com/doc/gettingstarted) | 平台工具与服务 | 文档免费；发行接入、销售与服务按平台协议计算 |

《Cuphead》的制作访谈展示了手绘资源与 Unity 的分工。[20](#ref-20) 这里应分别估算美术制作与游戏集成，而不是把引擎免费使用额度理解成整款游戏制作免费。

项目预算至少包括制作人力、工具与插件、素材与授权、设备与平台、测试与本地化、宣传发行以及维护。外包还需约定源文件、修改轮次和使用范围。技术方案的费用不仅是购买金额，还包括更换工具、重复制作和长期支持的成本。

<a id="daily-use"></a>
## 日常使用：一次完整交付的最小记录

小型项目不必为每个术语单独建文档。可以保留五类记录：**概念与范围、设计与接口、任务与缺陷、验证证据、版本与来源**。集中或分开管理均可，关键是当前有效版本明确。

一次修改的基本关系是：明确目的与不改动范围，分析影响，写验收标准，实施与审查，执行验证，记录限制，发布并核对公开结果。

**实现完成说明修改已产生，验收通过说明规定范围内的检查成立，发布完成说明成品已经交给玩家。** AI 或其他协作者都应按同一关系提供交付记录，不能用一句“已完成”替代证据。

<a id="references"></a>
## 参考文献与学习资源

以下区分流程概览、教材、官方方法和实际案例。资料优先来自作者、开发团队、机构或产品官方；“推荐阅读”是本系列的学习建议，不表示所有从业者都使用同一本教材。网页查阅日期：**2026-10-13**。项目案例固定到所列版本，后续维护另查当前内容。

<a id="ref-1"></a>
**[1] fivsevn. _UMWELT README_.** [固定版本](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/README.md)。免费查看。用于作品组成、资料与模拟边界及 AI 辅助说明，不是科学资料逐项认证。

<a id="ref-2"></a>
**[2] Bramble, Russell. _The Seven Stages of Game Development_（2023-05-10）. GameMaker.** [原文](https://gamemaker.io/en/blog/stages-of-game-development)。免费，英文。用于快速认识阶段与协作，不将厂商概览当作统一标准。

<a id="ref-3"></a>
**[3] Kraj, Nicolas. _Game Development Process: Keys for a Better Pipeline_. GDKeys.** [作者文章](https://gdkeys.com/game-development-process/)。免费，英文。重点是原型、切片与生产关卡的区别，属于实践方法而非强制规范。

<a id="ref-4"></a>
**[4] Hall, Jason T. _Develop Games_.** [开发者资源网站](https://develop.games/)。免费，英文。可按主题查设计、范围和独立制作内容；不必从头学习其中所有技术细节。

<a id="ref-5"></a>
**[5] fivsevn. _UMWELT：扩展工作流_.** [固定版本](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/docs/expansion-guide.md)。免费查看。用于新增内容时的模块、资料、语言和存档边界。

<a id="ref-6"></a>
**[6] Schwaber, Ken；Sutherland, Jeff. _The Scrum Guide_（2020）.** [官方文本](https://scrumguides.org/scrum-guide.html)。免费，有多语言版本。主要查阅 Sprint、待办与完成定义；使用看板或迭代不等于完整采用 Scrum。

<a id="ref-7"></a>
**[7] Chacon, Scott；Straub, Ben. _Pro Git_，第 2 版.** [免费在线版](https://git-scm.com/book/en/v2)。有中文入口，纸书可购买或借阅。读版本、提交和分支的概念，命令不是本篇要求。

<a id="ref-8"></a>
**[8] GitHub. _Continuous Integration_.** [官方说明](https://docs.github.com/en/actions/get-started/continuous-integration)。文档免费。重点是自动检查与交付版本的对应关系，服务执行费用另计。

<a id="ref-9"></a>
**[9] ISTQB. _Certified Tester Foundation Level Syllabus_，v4.0.1（2024）.** [官方入口](https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/)。大纲可公开查阅，培训和考试另收费。作为测试、质量、风险和缺陷记录的术语参考，无需为本系列参加认证。

<a id="ref-10"></a>
**[10] Microsoft. _Xbox Accessibility Guidelines_.** [官方指南](https://learn.microsoft.com/en-us/xbox/accessibility/guidelines)。免费。按文字、输入、声音和运动等任务查阅，指南不等于法律或平台认证结论。

<a id="ref-11"></a>
**[11] fivsevn. _UMWELT: Test Layout_.** [固定版本](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/tests/README.md)。免费查看。阅读验证范围与限制，不要求执行具体命令。

<a id="ref-12"></a>
**[12] Microsoft. _Emulation_. Playwright Documentation.** [官方文档](https://playwright.dev/docs/emulation)。免费。用于区分浏览器参数模拟与真实设备验证。

<a id="ref-13"></a>
**[13] fivsevn. _UMWELT: Static Deployment and Asset Identity_.** [固定版本](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/docs/deployment.md)。免费查看。用于源文件、发布处理和最终站点的分工。

<a id="ref-14"></a>
**[14] MDN contributors. _Autoplay Guide for Media and Web Audio APIs_.** [文档](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Autoplay)。免费。只需先理解玩家手势与声音播放限制。

<a id="ref-15"></a>
**[15] MDN contributors. _Window: localStorage Property_.** [文档](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)。免费。用于本地存储边界、来源隔离和数据风险。

<a id="ref-16"></a>
**[16] Valve. _Review Process_. Steamworks Documentation.** [官方流程](https://partner.steamgames.com/doc/store/review_process)。文档免费。区分商店页与游戏构建审核，不是发行费用或时长保证。

<a id="ref-17"></a>
**[17] Valve. _Early Access_. Steamworks Documentation.** [官方说明](https://partner.steamgames.com/doc/store/earlyaccess)。文档免费。理解开发中发行与当前产品承诺之间的关系。

<a id="ref-18"></a>
**[18] Vasseur, Thomas. _Art Design Deep Dive: Using a 3D Pipeline for 2D Animation in Dead Cells_（2018-01-25）.** [作者原文](https://www.gamedeveloper.com/production/art-design-deep-dive-using-a-3d-pipeline-for-2d-animation-in-i-dead-cells-i-)。免费，英文。读制作步骤与返工取舍，具体美术原理在 [004](posts-2026-umwelt-game-development-handbook-004.html) 展开。

<a id="ref-19"></a>
**[19] Larian Studios. _Hotfix 4 Redeployed_（2023-08-17）.** [官方复盘](https://baldursgate3.game/news/hotfix-4-redeployed_86)。免费，英文。读测试版本、重新构建、回退与存档的联系；这是历史事件，非当前缺陷通告。

<a id="ref-20"></a>
**[20] Unity／Studio MDHR. _Cuphead — Made with Unity_.** [制作访谈](https://unity.com/made-with-unity/cuphead)。免费，英文。用于观察手绘资源与游戏集成的不同工作。

### 教材与公开课程

| 资源 | 获取方式 | 推荐阅读内容 |
| --- | --- | --- |
| **Heather Chandler，_The Game Production Toolbox_（2019）**，[出版社与目录](https://www.routledge.com/Game-Production-Proven-Business-Techniques-to-Produce-the-Best-Games/Chandler/p/book/9781138341708) | 英文书籍付费或借阅，目录免费 | 系统认识制作计划、团队协作、预算、质量与交付；优先教材 |
| **Tracy Fullerton，_Game Design Workshop_，第 5 版（2024）**，[出版社](https://www.routledge.com/Game-Design-Workshop-A-Playcentric-Approach-to-Creating-Innovative-Games/Fullerton/p/book/9781032607009) | 英文书籍付费或借阅 | 玩家体验、原型与试玩迭代；不是先学编程的课程 |
| **MIT CMS.608 _Game Design_，Philip B. Tan、Jason Begy（2010 秋）**，[OpenCourseWare](https://ocw.mit.edu/courses/cms-608-game-design-fall-2010/) | 免费课程资料与课堂媒体，英文 | 从规则、非数字原型与项目练习认识设计过程 |
| **Martin Jonasson、Petri Purho，_Juice It or Lose It_，GDC Europe 2012**，[免费视频](https://gdcvault.com/play/1016789/Juice-It-or-Lose) | 该演讲免费，英文 | 观察反馈与打磨的效果；不是要求所有作品增加强烈特效 |

**阅读顺序：** 先用 [2] 理解流程，再选择 Chandler 的教材建立制作全貌；用 [18]、[19] 观察真实取舍。设计和反馈需要深化时，再进入 Fullerton、MIT 课程与 GDC 演讲。

[下一篇：软件地图与成本 002](posts-2026-umwelt-game-development-handbook-002.html) · [返回流程总览](#overview) · [返回个人笔记目录](../index.html)
