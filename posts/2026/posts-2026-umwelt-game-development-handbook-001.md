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
  从概念、设计、原型到制作、验收、发布与维护，解释每个阶段的目标、交付物和衔接。以你正在做的 UMWELT 为贯穿示例，结合 Splatoon、Dead Cells、Hades 等制作记录，附成本与参考资源。
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
description: "以游戏制作的目标、分工和交付关系为主线，理解全流程、成本与验收，附开发者案例和学习资源。"
canonical_url: "https://devlog.fivsevn.com/posts/2026/posts-2026-umwelt-game-development-handbook-001.html"
created: "2026-10-13"
updated: "2026-10-13"
metadata_updated: "2026-10-13"
---

# 游戏开发流程手册｜ChatGPT 写给五月七日的指导笔记 001

**以你正在做的 UMWELT 为例 · 撰写：ChatGPT · 2026-10-13**

**001 制作流程** · [002 软件与成本](posts-2026-umwelt-game-development-handbook-002.html) · [003 运行原理](posts-2026-umwelt-game-development-handbook-003.html) · [004 画面与动画](posts-2026-umwelt-game-development-handbook-004.html) · [005 玩法与叙事](posts-2026-umwelt-game-development-handbook-005.html) · [006 修改与发布](posts-2026-umwelt-game-development-handbook-006.html) · [007 研究与表达](posts-2026-umwelt-game-development-handbook-007.html)

一款游戏从想法变成成品，需要先确定范围，再验证设计和制作方法，随后持续完成内容，并把经过检查的版本交给玩家。流程把这些工作连接起来，使你知道当前已经得到什么成果，以及下一步投入还需要哪些依据。

你可以把具体编程交给开发者或 AI，同时负责作品方向与交付判断。因此，这套手册重点说明系统职责、制作取舍、成本和验收；具体语法、命令与软件操作则留在需要实际使用时查阅。

以下会用你正在做的《等足目赋格》与配套实验室说明工作关系。项目已经区分资料、工作性判断和游戏参数，可以据此继续整理内容。[1](#ref-1) 文中的“新增一段生境观察”用于演示一项任务怎样经过各阶段（实际开发可以多次往返调整，示例也不作为已执行的测试记录）。

<a id="overview"></a>
## 流程总览

为了便于查阅，这里把原型与垂直切片从前期制作中单独列出。你可以按项目规模合并阶段，只要继续保留各阶段需要作出的判断。[2](#ref-2), [3](#ref-3)

| 阶段 | 主要内容 | 交付物 |
| --- | --- | --- |
| [1. 概念与立项](#phase-1) | 确定体验、平台和首版范围 | 概念、范围与风险清单 |
| [2. 前期设计与计划](#phase-2) | 约定规则、资源、分工和制作方式 | 设计文档、技术约定与计划 |
| [3. 原型验证](#phase-3) | 检验核心体验与关键技术假设 | 原型、观察记录与结论 |
| [4. 垂直切片](#phase-4) | 检验目标品质能否稳定制作 | 代表性片段、质量基准与成本估计 |
| [5. 正式制作](#phase-5) | 持续完成并整合功能与内容 | 可运行版本、资源与审查记录 |
| [6. QA、验收与打磨](#phase-6) | 检查功能、体验与剩余风险 | 检查证据、问题清单与验收结论 |
| [7. 发布](#phase-7) | 生成、审核并交付成品 | 发布版本、说明与恢复方案 |
| [8. 维护与复盘](#phase-8) | 修复、扩展、归档或结束支持 | 补丁、兼容记录与复盘 |
| [成本与工具](#cost) | 比较许可、人力、资源与维护成本 | 费用类型与预算项目 |
| [参考与学习资源](#references) | 教材、开发者记录和课程 | 按主题查阅的学习入口 |

各阶段之间会反复迭代。例如，原型结果可能要求缩小范围，试玩也可能要求调整已经完成的内容。因此，测试、来源核查和授权安排宜尽早参与，使问题在仍有调整余地时被发现。宣传与发行也可提前准备，并随成品状态更新对外说明。

<a id="phase-1"></a>
## 1｜Concept：概念与立项

**本阶段确定核心体验，以及第一版准备完成的范围。**

概念说明可以包含目标玩家、主要行为、体验方向、平台、体量和发布方式。再把时间、预算、人员、工具、素材和研究条件放在一起比较，判断这一版能够承担多少工作。

新想法可以分为首版必需、以后扩展和当前不做三类。这样，制作中出现新机会时，就有依据决定是否加入；若加入后超出原有资源，也可以同时调整计划。

以你的生境观察为例，可以先安排一条短路径：玩家观察差异，采取行动，再从反馈继续观察。首版完成一个生境，更多物种与复杂天气留作扩展。涉及真实动物的内容，则继续保留来源与游戏参数的区别，使资料和创作处理能够分别查到。[1](#ref-1)

| 术语 | 定义与解释 |
| --- | --- |
| Concept／概念 | 对作品体验、目标玩家和基本形式的概括 |
| Pitch／提案 | 向合作者、团队或发行方说明项目价值与实施条件 |
| Target Audience／目标受众 | 优先服务的玩家群体 |
| USP／独特卖点 | 作品与其他选择相比值得关注的特点 |
| Design Pillars／设计支柱 | 用于取舍的少数体验原则，例如观察优先于数值竞争 |
| Scope／范围 | 承诺制作的功能、内容、平台和品质边界 |
| Greenlight／立项放行 | 根据当前材料，批准继续投入下一阶段 |

**交付与判断：** 留下概念、首版范围、资源估计与风险排序。继续制作前，明确最需要验证的假设，以及哪些结果会使你调整方案。

<a id="phase-2"></a>
## 2｜Pre-production：前期设计与计划

**本阶段把想法整理为可以分工、接续和验收的约定。**

设计文档说明玩家从哪里进入、能做哪些操作、状态怎样变化，以及体验如何结束。由于玩家还可能中断、返回或重载，设计中也需要安排这些情况。叙事项目则进一步记录节点、条件和分支，使对白能够与玩家行动对应。[4](#ref-4)

技术约定说明运行平台、模块、数据、存档与资源接入关系；美术和声音规范说明风格与交付规格。它们会随设计变化而更新，因此应标明当前采用的版本，并把旧方案保留为历史记录。

### 分工与交接

| 职责 | 主要内容 |
| --- | --- |
| 制作人／Producer | 协调范围、人员、预算、进度与交付 |
| 游戏设计师／Game Designer | 设计操作、规则与体验结构 |
| 叙事设计师／Narrative Designer | 组织故事、状态、选择与交互的关系 |
| 程序开发 | 实现系统及其连接，处理运行与数据 |
| 美术与动画 | 制作视觉资源、动作和表现 |
| 音频 | 制作声音，并安排与游戏状态的连接 |
| 技术美术／Technical Artist | 衔接视觉制作与运行要求，处理相关工具和流程 |
| QA 与测试 | 提供质量风险、检查方法和验证信息 |

小团队可以由一人承担多个职责，但每项交付仍需要明确由谁决定、谁制作、谁检查。岗位数量可以合并，交接关系则应保留。[2](#ref-2)

你在新增生境时，也需要先区分已有规则下的内容扩展与新的功能需求，再检查稳定标识、实验室、语言和存档。这样，文字、美术与程序才能围绕同一项功能接续工作。[5](#ref-5)

| 术语 | 定义与解释 |
| --- | --- |
| GDD／游戏设计文档 | 记录玩法、规则、内容与体验目标 |
| TDD／技术设计文档 | 记录技术安排（另一语境中也可指测试驱动开发） |
| Art Bible／美术规范 | 统一风格与资源交付标准的参考 |
| UI／界面；UX／使用体验 | UI 是控件和信息，UX 包括理解、操作与反馈的整体体验 |
| Pipeline／制作管线 | 内容从源文件到游戏成品的处理和交付步骤 |
| Data Contract／数据约定 | 规定字段、含义、稳定标识与兼容条件 |
| Milestone／里程碑 | 有明确成果和继续条件的检查点 |
| Dependency／依赖 | 一项工作需要的其他成果或前提 |

**交付与判断：** 准备简版设计、资源规格、技术约定和分工计划；尚未确定的关键问题进入下一阶段验证。

<a id="phase-3"></a>
## 3｜Prototype：原型验证

**本阶段用较小投入检查关键假设。**

原型可以针对操作理解、体验节奏或技术可行性。先写下需要观察的结果，再选择临时素材、纸面流程或简化程序，就能把投入集中在当前最不确定的部分。

**《Splatoon》的早期原型说明了这种先后关系。** 任天堂的开发者访谈介绍，团队曾用黑白方块代替角色，让它们喷射墨水、争夺地面区域。此时核心规则已经能够尝试，后来才逐步形成玩家熟悉的角色形象。[21](#ref-21) 因此，原型的视觉完成度可以暂时让位于验证目标；重要的是它能否呈现正在测试的关系。

你的观察游戏也可以先用简化背景和动物形象完成“观察—操作—反馈—继续”的短循环。让未参与制作的人尝试，记录他们在哪里犹豫或误解，再判断需要修改规则、文字还是反馈。

视觉、机制与性能可以分别做小样。每个小样只覆盖部分问题，因此一段画面得到认可后，还要继续验证输入、进度和长期内容量。把结论限定在实际检查范围内，下一步计划才有可靠依据。[3](#ref-3)

| 术语 | 定义与解释 |
| --- | --- |
| Prototype／原型 | 用于检验设计或技术假设的模型 |
| PoC／概念验证 | 侧重确认方案可行，与原型的用法可能交叉 |
| Mechanic／机制 | 具体操作与规则之间的关系 |
| Core Loop／核心循环 | 反复出现的玩家行为与反馈结构 |
| Playtest／试玩测试 | 通过实际参与观察理解、节奏和体验 |
| Timebox／限时验证 | 预先限定投入，到期根据结果决定下一步 |
| MVP／最小可行产品 | 用较小产品验证价值等假设，是否采用取决于项目目标 |

**交付与判断：** 保存原型、验证目标、观察记录与决定。临时内容是否继续使用，应根据后续要求判断；完成验证后舍弃原型，也可以是合理结果。

<a id="phase-4"></a>
## 4｜Vertical Slice：垂直切片

**本阶段通过一小段代表性内容，进一步检查目标品质与制作能力。**

原型主要检验想法是否成立，垂直切片则把交互、画面、声音、文字和必要的保存功能接到一起，尝试达到准备长期采用的品质。制作这段内容时，还可以记录步骤、返工与成本，估计后续怎样持续产出。[3](#ref-3)

例如，你可以选一段生境观察，从正常入口开始，一直做到反馈、保存和资料查阅。再加入有代表性的长文本、声音和手机布局，以检查不同环节能否共同工作。选择有代表性的困难，比只展示最容易完成的一部分更有助于估算后续工作。

**《Dead Cells》的动画制作记录可以帮助理解“可持续制作”。** 作者选择便于反复调整动作的流程，使玩法变化时仍能修改已有资源。[18](#ref-18) 这一点适合用于切片验收：除了检查当前效果，还要实际尝试一次修改，确认成本是否可承受。

| 术语 | 定义与解释 |
| --- | --- |
| Vertical Slice／垂直切片 | 内容范围较小，但贯通主要制作环节并接近目标品质 |
| Horizontal Slice／水平切片 | 覆盖较多系统或流程，而各部分可能仍较粗略 |
| Demo／演示或试玩版 | 描述面向展示或体验的用途，内容成熟度需另说明 |
| Quality Bar／质量基准 | 供后续内容比较的完成标准 |
| Production-ready／具备生产条件 | 制作方法、工具与流程能够支持继续产出 |

**交付与判断：** 形成代表性片段、质量基准与成本估计。小型项目可以把原型和切片合并制作，同时分别确认体验与生产两方面的结论。

<a id="phase-5"></a>
## 5｜Production：正式制作与迭代

**本阶段按照已验证的方式，持续完成和整合功能与内容。**

每轮先确定有限任务，说明影响范围和验收结果，再进行实现、接入、审查与测试。新想法可以先进入待办记录；决定加入时，再调整资源和计划，避免不同参与者对交付范围产生分歧。

功能与内容也需要分别估算。增加一种角色外观可能沿用现有操作，而增加一种控制方式可能影响输入、动画和存档。美术源文件与运行资源同样各有用途：修改源工程后，需要重新导出并检查成品，再交给游戏使用。

**《Hades》把持续迭代与公开反馈结合起来。** Supergiant 说明，作品从结构和叙事安排上就考虑了抢先体验期间的扩展，以便根据玩家反馈逐步发展。[22](#ref-22) 这说明发布方式可以反过来影响制作计划：若准备边开发边公开，就应提前安排可扩展的内容结构与反馈处理，而不是等公开之后才临时决定。

### 把一项需求写成验收约定

| 项目 | 演示性约定 |
| --- | --- |
| 任务 | 为你的游戏新增一段生境观察 |
| 范围 | 一个入口、一段观察、一组反馈，其他生境保持原有行为 |
| 功能结果 | 可以从正常入口进入并完成，每次操作产生一次预期变化 |
| 数据结果 | 保存和恢复后，进度与反馈一致 |
| 显示结果 | 目标语言和屏幕中，文字、按钮与场景正常使用 |
| 兼容结果 | 支持范围内的旧存档和未修改内容继续按约定运行 |
| 证据 | 交付版本、执行过的检查、必要截图和待验证部分 |

验收标准描述这一项任务的结果，完成定义／DoD 则规定项目共同的交付底线，例如审查、检查和文档同步。两者一起使用，可以同时明确具体要求与共同质量条件。[6](#ref-6)

版本控制保存每组变化，持续集成自动执行已配置的检查。它们使迭代便于追踪；设计与实际体验的判断，则继续通过审查和试玩完成。[7](#ref-7), [8](#ref-8)

| 术语 | 定义与解释 |
| --- | --- |
| Feature／功能；Content／内容 | 系统提供的能力，以及利用这些能力组织的具体体验 |
| Asset／资源 | 图像、模型、动作、音频和字体等内容 |
| Backlog／待办池；Ticket／任务单 | 排序后的工作集合，以及一项工作或问题的记录 |
| Iteration／迭代；Sprint／冲刺 | 迭代是反复交付和调整；Sprint 是 Scrum 中有特定规则的固定周期 |
| Commit／提交；Branch／分支 | 一组版本变化记录，以及相对独立的修改路线 |
| Merge／合并；PR／合并请求 | 整合变化，以及提出和审查待整合变化的记录 |
| Code Review／代码审查 | 检查实现、风险与维护条件，随后还需验证运行结果 |
| Build／构建 | 生成交付文件的过程，也可指生成的那个版本 |
| CI／持续集成 | 频繁整合变更，并自动执行相应检查 |
| CD／持续交付或持续部署 | 前者保持可发布状态，后者按配置把通过检查的结果部署出去 |
| Refactoring／重构 | 调整内部组织，同时保留约定的外部行为 |
| Technical Debt／技术债务 | 会增加后续修改与维护负担的实现或流程问题 |
| Scope Creep／范围蔓延 | 新要求持续加入，但资源与计划没有相应调整 |

运行系统的细节可以继续看 [003](posts-2026-umwelt-game-development-handbook-003.html)。在本阶段，你先确认每轮成果都能接回完整体验，再安排下一组内容。

<a id="phase-6"></a>
## 6｜QA、验收与打磨

**本阶段把质量要求转为检查，再根据结果处理问题与风险。**

QA／质量保证关注过程中的预防和改进，QC／质量控制关注成果质量，测试则提供具体检查结果。三者相互联系：流程使问题更容易预防和发现，检查结果又用于调整流程与成品。[9](#ref-9)

| 检查方式 | 主要内容 |
| --- | --- |
| 单元、集成与端到端检查 | 局部规则、模块协作和完整操作链 |
| 冒烟检查 | 快速确认启动、关键资源和主要流程 |
| 功能与边界检查 | 正常操作、连续输入、中断和失败 |
| 修复复测与回归 | 确认原问题已修复，并检查其他部分是否受到影响 |
| 兼容性 | 约定系统、浏览器、屏幕与输入方式 |
| 性能 | 加载、执行时间、内存与长时间运行 |
| 叙事与本地化 | 条件、分支、人物反应、译文、字体与布局 |
| 易用性与试玩 | 玩家理解、操作和体验目标 |
| 无障碍 | 可读文字、对比度、替代输入、声音和运动效果 |
| 安全、隐私与资料 | 外部输入、秘密、个人信息和事实依据 |

这些检查可以交叉安排。比如文字过小既影响易用性，也影响无障碍；修复后还需在目标设备和语言中复测。Xbox 的公开指南提供了相关方向，可以帮助你列出实际检查项目。[10](#ref-10)

你的仓库把普通自动检查和浏览器回归分开，说明它们各自覆盖不同条件。[11](#ref-11) 自动检查通过后，仍需根据改动补充画面和操作检查；使用设备模拟时，也应说明模拟了哪些条件，再另外记录真实手机上的结果。[12](#ref-12)

### 问题记录与处理

缺陷可以按登记、排序、定位、修复、复测和关闭推进。尚未复现或决定暂缓的问题也保留原因，以便以后继续调查。严重程度说明影响，优先级说明处理顺序，两者应按项目情况分别判断。[9](#ref-9)

| 记录 | 需要包含的内容 |
| --- | --- |
| 身份 | 编号、标题、发现时间与版本 |
| 环境 | 设备、系统、浏览器及必要设置 |
| 前提与步骤 | 问题前的状态，以及可以重复执行的操作 |
| 预期与实际 | 原本应有的结果，以及实际看到的现象 |
| 证据 | 日志、存档、截图或录屏，附复现情况 |
| 处置 | 影响、优先级、负责人和验证结果 |

记录现象后，可以另外写出原因假设。这样，调查者既知道问题如何出现，也能够检验解释是否成立。检查结果同样要附范围；在某些条件下没有发现问题，表示这些检查已通过，其他条件再按风险安排。

### 阶段与质量状态

| 名称 | 可采用的项目定义 |
| --- | --- |
| Alpha／阿尔法 | 主要功能能够共同运行，允许仍有临时资源或未完内容 |
| Feature Complete／功能齐备 | 约定功能已实现，内容和质量继续检查 |
| Beta／贝塔 | 功能与内容接近齐备，主要处理缺陷、兼容和体验 |
| Content Complete／内容齐备 | 计划内容已接入，继续校对和打磨 |
| Freeze／冻结 | 对新增与修改设置更严格条件，同时保留必要修复途径 |
| Blocker／阻断问题 | 阻止必要测试、推进或发布的问题 |
| Softlock／软锁 | 程序仍运行，但玩家无法正常继续 |
| Baseline／基线 | 用于比较的参考版本或结果 |
| Profiling／性能分析 | 测量开销，定位需要优化的部分 |
| Polish／打磨 | 改进妨碍目标体验的细节 |

不同团队对 Alpha、Beta 的使用范围可能不同，因此应在计划中明确自己的进入与完成条件。[3](#ref-3)

打磨也应回到体验目标。例如，你的观察游戏可以优先改善文字、触碰反馈和等待节奏，再决定增加哪些视听效果。最后把通过、失败和待验证的项目一起整理，便能据此决定继续修复还是准备发布。

<a id="phase-7"></a>
## 7｜Release：发布准备与分发

**本阶段把经过验证的内容整理为玩家能够取得、运行和恢复的成品。**

先确定候选版本，再生成实际交付文件。因为导出会处理路径、压缩、字体或平台设置，所以开发目录中的检查还需要延伸到最终成品。你的网页发布流程也会准备站点、处理字体和资源标识，因此最后应检查完成这些处理的站点。[13](#ref-13)

**《Baldur’s Gate 3》的 Hotfix 4 事件可以说明这个关系。** Larian 的复盘介绍，临近发布时重新构建的版本与此前测试对象之间出现了问题，回退又牵涉部分玩家存档。[19](#ref-19) 因而，发布前既要确认验证的是哪一份文件，也要准备数据兼容与恢复方法（案例发生于 2023 年，修正版本随后重新发布）。

| 发布检查 | 主要内容 |
| --- | --- |
| 体验与数据 | 首次进入、退出、恢复、更新与必要的离线行为 |
| 平台条件 | 输入、性能、签名、开发者资格与审核要求 |
| 发布材料 | 说明、截图、预告、系统要求、已知问题与反馈方式 |
| 权限与来源 | 素材、字体、程序、声音和个人资料的公开条件 |
| 恢复能力 | 上个稳定成品、回退步骤与玩家数据处理 |

网页还有自己的运行条件。例如，声音播放可能需要玩家手势，本地存档则与网站来源和浏览器存储有关；这些安排需要在首次进入与恢复体验中检查。[14](#ref-14), [15](#ref-15)

商店发布进一步涉及产品说明与构建审核。Steam 将商店页和游戏构建分别检查，因此可以先把两类工作分开准备，再确认对外描述与成品一致。[16](#ref-16)

| 术语 | 定义与解释 |
| --- | --- |
| RC／候选发布版本 | 用于发布前验证的候选，发现问题后继续修订 |
| Release Build／发布构建 | 按正式配置生成的成品，其质量由相应检查确认 |
| Artifact／构建产物 | 自动流程输出的站点、安装包或其他文件 |
| Tag／标签 | 为特定版本设置便于识别的名称 |
| Deployment／部署；Release／发布 | 将成品放入环境，以及向玩家提供版本，两者时间可以不同 |
| Certification／平台认证 | 验证特定平台的技术或发行要求 |
| Rollback／回退 | 恢复到之前的程序或配置，同时处理必要的数据兼容 |
| Early Access／抢先体验 | 在开发期间向玩家提供可玩版本，并明确当前状态与后续安排 |

前面提到的《Hades》说明，抢先体验可以服务于迭代计划；具体发行时，还需要准确说明当前内容与限制。[17](#ref-17), [22](#ref-22) 完成部署后，再从公开入口访问或下载，确认玩家取得的是预期版本。

<a id="phase-8"></a>
## 8｜Maintenance：维护、扩展与复盘

**发布后继续处理反馈，并为修复、扩展和结束支持划定范围。**

玩家反馈可能涉及缺陷、设备差异、设计偏好或新内容建议。先判断它属于哪一类，再决定由谁处理和采用什么验证方式，可以避免把所有意见都直接变成功能任务。

**《Hades》在 1.0 发布说明中仍安排了后续支持。** 团队当时提出先关注公开版本的稳定性与平衡问题，再通过补丁处理反馈。[23](#ref-23) 这说明正式发布之后，工作会从大量新增内容转向观察实际使用并解决问题，计划中应预留这部分时间。

你继续扩展《等足目赋格》时，也可以先确认资料与设计，再接入物种、生境或结局，同时检查语言、实验室和旧存档。若资料修订影响了已有解释，就在更新说明中写清它涉及资料、视觉还是游戏规则。[5](#ref-5), [11](#ref-11)

| 术语 | 定义与解释 |
| --- | --- |
| Patch／补丁 | 对已有版本的修复或调整 |
| Hotfix／紧急修复 | 优先处理紧迫问题，并执行相应的必要验证 |
| Changelog／变更记录 | 不同版本修改内容的历史 |
| Release Notes／发行说明 | 面向一次交付说明功能、修复、限制和注意事项 |
| Migration／迁移 | 将旧数据转换为新结构，并处理失败与兼容情况 |
| LiveOps／持续运营 | 持续安排活动、内容或服务，是否采用由作品需求决定 |
| Postmortem／复盘 | 根据实际过程分析效果、成本、返工与改进 |
| EOL／结束支持 | 明确某个产品或版本停止支持后的范围与影响 |

复盘时可以比较计划与实际投入，记录哪些制作方式可复用、哪些地方反复返工。结束维护时，则保留必要的成品、源资料和说明，让之后的访问与维护仍有依据。

<a id="cost"></a>
## 成本与工具

开发成本来自软件，也来自制作、测试、资料和长期维护。为了比较工具，应先区分它的许可条件，再估算采用后仍需完成的工作。下面列出相关代表工具，完整目录见 [002](posts-2026-umwelt-game-development-handbook-002.html#cost-legend)（费用形式记录日期：2026-10-13）。

| 工具／平台 | 开放情况 | 费用与使用范围 |
| --- | --- | --- |
| [Unity](https://unity.com/products) | 专有 | 条件免费，以及适用的付费席位方案 |
| [Godot](https://godotengine.org/license/) | 开源，MIT | 引擎免费，素材、平台适配和人力另计 |
| [Blender](https://www.blender.org/about/license/) | 开源 | 软件免费，视觉生产仍需制作时间与设备 |
| [Git](https://git-scm.com/about) | 开源 | 软件免费，托管与备份另计 |
| [GitHub](https://github.com/pricing)／[Actions](https://docs.github.com/en/billing/concepts/product-billing/github-actions)／[Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) | 平台与云服务 | 免费适用范围、额度和付费方案分别核对 |
| [Node.js](https://nodejs.org/en/about)／[Playwright](https://playwright.dev/) | 开源 | 工具免费，设备与执行资源可能收费 |
| [Steamworks](https://partner.steamgames.com/doc/gettingstarted) | 平台工具与服务 | 文档免费，发行接入和销售等按平台协议 |

例如，《Cuphead》的制作访谈同时涉及手绘动画与 Unity 集成。[20](#ref-20) 因而，估算这类作品时，要分别计算美术生产与游戏接入；引擎许可只是其中一个项目。

你的预算可以记录人力、工具、素材、设备、测试、本地化、宣传和维护。采用外包时，再约定源文件、修改轮次和使用范围。把这些成本与首版范围一起调整，才能判断方案是否可持续。

<a id="daily-use"></a>
## 日常使用：一次交付的最小记录

对小型项目，可以将资料集中为概念与范围、设计与接口、任务与缺陷、验证证据、版本与来源五类。管理形式可以简化，只要当前有效内容和修改历史仍然明确。

一次修改可以依次完成：确定目的和保留范围，分析影响，写验收要求，实施与审查，执行检查，记录限制，再发布并核对公开入口。

**实现完成说明修改已经产生，验收通过说明约定检查已完成，发布与公开核对则确认成品已经按预期交给玩家。** 这些步骤彼此接续，因此交付报告最好分别记录状态，使你能够看出当前成果与下一步工作。

<a id="references"></a>
## 参考文献与学习资源

以下将流程教材、官方方法和实际制作记录对应到各节。你可以先读概览，再选择一个与当前任务相近的案例深入（网页查阅日期：2026-10-13；自己的游戏资料固定到提交 `0bbe083`）。

<a id="ref-1"></a>
**[1] fivsevn. _UMWELT README_.** [项目说明](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/README.md)。用于对照你的作品组成、资料与模拟边界。

<a id="ref-2"></a>
**[2] Bramble, Russell. _The Seven Stages of Game Development_（2023-05-10）. GameMaker.** [英文概览](https://gamemaker.io/en/blog/stages-of-game-development)。免费。先理解阶段与职责，再结合自己的规模调整工作安排。

<a id="ref-3"></a>
**[3] Kraj, Nicolas. _Game Development Process: Keys for a Better Pipeline_.** [GDKeys 作者文章](https://gdkeys.com/game-development-process/)。英文，免费。重点是原型、切片与生产阶段怎样衔接。

<a id="ref-4"></a>
**[4] Hall, Jason T. _Develop Games_.** [开发者资源](https://develop.games/)。英文，免费。按设计、范围和独立制作等问题查阅。

<a id="ref-5"></a>
**[5] fivsevn. _UMWELT：扩展工作流_.** [固定版本](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/docs/expansion-guide.md)。对应你新增内容时的模块、资料、语言和存档安排。

<a id="ref-6"></a>
**[6] Schwaber, Ken；Sutherland, Jeff. _The Scrum Guide_（2020）.** [官方英文文本](https://scrumguides.org/scrum-guide.html)。免费。主要查阅待办、Sprint 与完成定义；采用其中方法时，明确自己使用的具体部分即可。

<a id="ref-7"></a>
**[7] Chacon, Scott；Straub, Ben. _Pro Git_，第 2 版.** [英文在线全文](https://git-scm.com/book/en/v2)。在线免费，纸书可购买或借阅。先理解版本、提交和分支概念。

<a id="ref-8"></a>
**[8] GitHub. _Continuous Integration_.** [英文说明](https://docs.github.com/en/actions/get-started/continuous-integration)。免费。重点是自动检查与交付版本的对应关系。

<a id="ref-9"></a>
**[9] ISTQB. _Certified Tester Foundation Level Syllabus_，v4.0.1（2024）.** [官方英文入口](https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/)。大纲可免费查阅，培训和考试另计。用于测试、质量、风险与缺陷记录的术语参考。

<a id="ref-10"></a>
**[10] Microsoft. _Xbox Accessibility Guidelines_.** [英文指南](https://learn.microsoft.com/en-us/xbox/accessibility/guidelines)。免费。按文字、输入、声音和运动等需求查阅，再安排实际检查。

<a id="ref-11"></a>
**[11] fivsevn. _UMWELT: Test Layout_.** [固定版本](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/tests/README.md)。阅读检查范围与限制，了解你自己的验证体系。

<a id="ref-12"></a>
**[12] Microsoft. _Emulation_. Playwright Documentation.** [英文文档](https://playwright.dev/docs/emulation)。免费。了解浏览器模拟能够配置哪些条件，并与真机结果比较。

<a id="ref-13"></a>
**[13] fivsevn. _UMWELT: Static Deployment and Asset Identity_.** [固定版本](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/docs/deployment.md)。用于比较源文件、发布处理和最终站点。

<a id="ref-14"></a>
**[14] MDN contributors. _Autoplay Guide for Media and Web Audio APIs_.** [英文文档](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Autoplay)。免费。理解玩家手势与网页声音播放的关系。

<a id="ref-15"></a>
**[15] MDN contributors. _Window: localStorage Property_.** [英文文档](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)。免费。用于本地保存范围、网站来源和进度恢复。

<a id="ref-16"></a>
**[16] Valve. _Review Process_. Steamworks Documentation.** [英文流程](https://partner.steamgames.com/doc/store/review_process)。免费。了解商店材料和游戏构建的不同审核内容。

<a id="ref-17"></a>
**[17] Valve. _Early Access_. Steamworks Documentation.** [英文说明](https://partner.steamgames.com/doc/store/earlyaccess)。免费。理解开发中发行与当前内容说明的关系。

<a id="ref-18"></a>
**[18] Vasseur, Thomas. _Art Design Deep Dive: Using a 3D Pipeline for 2D Animation in Dead Cells_（2018-01-25）.** [作者原文](https://www.gamedeveloper.com/production/art-design-deep-dive-using-a-3d-pipeline-for-2d-animation-in-i-dead-cells-i-)。英文，免费。重点看反复调整与制作方法的联系，视觉细节在 [004](posts-2026-umwelt-game-development-handbook-004.html) 展开。

<a id="ref-19"></a>
**[19] Larian Studios. _Hotfix 4 Redeployed_（2023-08-17）.** [官方复盘](https://baldursgate3.game/news/hotfix-4-redeployed_86)。英文，免费。理解测试对象、重新构建和回退数据之间的联系（历史版本事件）。

<a id="ref-20"></a>
**[20] Unity／Studio MDHR. _Cuphead — Made with Unity_.** [制作访谈](https://unity.com/made-with-unity/cuphead)。英文，免费。用于比较美术制作与游戏接入的工作。

<a id="ref-21"></a>
**[21] Nintendo. _Iwata Asks: Splatoon — 1. It Started With Tofu_.** [任天堂官方英文访谈](https://www.nintendo.com/en-gb/Iwata-Asks/Iwata-Asks-Splatoon/Splatoon/1-It-Started-With-Tofu/1-It-Started-With-Tofu-1021365.html)。免费。通过方块原型理解先验证规则、再发展角色表现的过程。

<a id="ref-22"></a>
**[22] Supergiant Games. _Hades FAQ_.** [官方说明](https://www.supergiantgames.com/blog/hades-faq/)。英文，免费。阅读 Early Access 与叙事组织部分，理解发布方式怎样参与制作计划。

<a id="ref-23"></a>
**[23] Supergiant Games. _Hades: Now Out of Early Access!_（2020-09-17）.** [发行说明](https://www.supergiantgames.com/blog/hades-now-out-of-early-access/)。英文，免费。关注正式发行后继续安排的支持工作。

### 教材与公开课程

| 资源 | 获取方式 | 推荐内容 |
| --- | --- | --- |
| **Heather Chandler，_The Game Production Toolbox_（2019）**，[出版社与目录](https://www.routledge.com/Game-Production-Proven-Business-Techniques-to-Produce-the-Best-Games/Chandler/p/book/9781138341708) | 英文，书籍购买或借阅，目录免费 | 系统认识计划、分工、预算、质量和交付 |
| **Tracy Fullerton，_Game Design Workshop_，第 5 版（2024）**，[出版社](https://www.routledge.com/Game-Design-Workshop-A-Playcentric-Approach-to-Creating-Innovative-Games/Fullerton/p/book/9781032607009) | 英文，书籍购买或借阅 | 体验目标、原型、试玩与迭代 |
| **Philip B. Tan、Jason Begy，MIT CMS.608 _Game Design_（2010 秋）**，[公开课程](https://ocw.mit.edu/courses/cms-608-game-design-fall-2010/) | 英文，课程资料、录音和项目示例免费 | 从规则、非数字原型和测试理解设计过程 |
| **Martin Jonasson、Petri Purho，_Juice It or Lose It_，GDC Europe 2012**，[演讲](https://gdcvault.com/play/1016789/Juice-It-or-Lose) | 英文，该条目免费 | 观察不同反馈怎样改变交互感受，再按作品节奏选择 |

**阅读顺序：** 先用 [2] 建立流程概览，再看 [21] 的原型和 [19] 的发布事件。需要系统整理制作时选择 Chandler，设计与试玩方面则继续阅读 Fullerton 或 MIT 课程。

[下一篇：软件地图与成本 002](posts-2026-umwelt-game-development-handbook-002.html) · [返回流程总览](#overview) · [返回个人笔记目录](../index.html)
