---
id: "posts-2026-umwelt-game-development-handbook-006"
title: "项目阅读、修改与发布实务手册｜ChatGPT 写给五月七日的指导笔记 006"

module: "posts"
submodule: "2026"
topic: "umwelt-game-development-handbook"

type: "note"
status: "active"
canonical: true

summary: |
  面向不亲自编写代码的项目负责人，说明需求、范围、修改差异、验证、提交、部署和回退的关系。以 Baldur’s Gate 3 的补丁复盘及 UMWELT 和博客的实际发布流程为例，附工具成本与学习资源。

parents: ["posts-index"]
related: ["posts-2026-umwelt-game-development-handbook-001", "posts-2026-umwelt-game-development-handbook-002", "posts-2026-umwelt-game-development-handbook-003"]
tags: ["game-development", "production", "qa", "release", "collaboration", "handbook"]
audience: ["self", "public"]
languages: ["zh"]
maturity: "evolving"
confidence: 0.9
visibility: "public"
source_of_truth: "devlog"
lang: "zh-CN"
description: "理解一次游戏修改从需求到上线的全过程，以结果和证据管理开发协作，不展开命令行或编程操作。"
canonical_url: "https://devlog.fivsevn.com/posts/2026/posts-2026-umwelt-game-development-handbook-006.html"
created: "2026-10-13"
updated: "2026-10-13"
metadata_updated: "2026-10-13"
---

# 项目阅读、修改与发布实务手册｜ChatGPT 写给五月七日的指导笔记 006

**以需求、变更与证据组织协作 · 撰写：ChatGPT · 2026-10-13**

[001 制作流程](posts-2026-umwelt-game-development-handbook-001.html) · [002 软件与成本](posts-2026-umwelt-game-development-handbook-002.html) · [003 运行原理](posts-2026-umwelt-game-development-handbook-003.html) · [004 画面与动画](posts-2026-umwelt-game-development-handbook-004.html) · [005 玩法与叙事](posts-2026-umwelt-game-development-handbook-005.html) · **006 修改与发布** · [007 研究与表达](posts-2026-umwelt-game-development-handbook-007.html)

委托他人或 AI 完成实现，不意味着必须先掌握全部编程技术，也不意味着可以省略需求和验收。项目负责人最需要掌握的是：**改动的目的、允许的范围、完成标准，以及目前有哪些证据。**

本篇围绕一次完整修改展开，不提供命令行操作清单。实际按钮和命令由所用工具决定，交付关系则可以保持一致。

| 部分 | 主要内容 |
| --- | --- |
| [1. 认识项目](#read-project) | 入口、模块、源文件、文档与成品 |
| [2. 交付需求](#request) | 将意图写成范围与验收标准 |
| [3. 阅读变更](#change) | 提交、分支、差异与审查 |
| [4. 理解验证](#verification) | 测试结果能够证明什么 |
| [5. 发布与回退](#release) | 构建、部署、公开检查与数据兼容 |
| [6. 本项目对应](#isopoda) | UMWELT 和博客的实际流程 |
| [7. 成本与交接](#cost) | 工具费用与开发交付记录 |
| [参考与学习资源](#references) | 版本管理、测试、发行与复盘资料 |

<a id="read-project"></a>
## 1｜项目阅读不等于逐行读代码

先了解项目由哪些部分组成，以及哪一份资料描述当前有效状态。文件名可以提供线索，但最终职责需要由文档和实际引用关系确认。

| 内容 | 主要用途 | 容易混淆的对象 |
| --- | --- | --- |
| 项目说明 | 介绍作品、入口、许可与维护方式 | 不一定包含完整的实现细节 |
| 运行文件 | 玩家打开作品后实际使用的程序和资源 | 与开发工具、历史草稿不同 |
| 内容与配置 | 保存对白、对象、布局及功能设置 | 修改数据也可能改变游戏行为 |
| 源素材 | 保留可编辑的图片、模型与音频工程 | 与已经导出的运行资源不同 |
| 测试与检查 | 验证规定范围内的行为 | 不是玩家端的新增功能 |
| 发布配置 | 规定怎样生成和分发成品 | 不等于游戏中的玩法规则 |
| 历史记录 | 保存旧设计与旧决策 | 不应自动作为当前要求 |

**入口决定从哪里开始，模块说明由谁负责，发布配置决定哪些文件进入成品。** 只看文件数量或代码行数，无法判断内容是否完整、结构是否可靠。

例如，修改一段已经存在的对白，应先找到其维护位置；新增一种交互则可能需要同时检查输入、状态、反馈和存档。两者不能因为在界面上都只增加一个按钮，就被估算为相同工作量。

<a id="request"></a>
## 2｜把修改意图写成可交付需求

需求不必写成复杂文档，但应说明结果，而不只是“优化一下”。以下模板可以用于人工、外包或 AI 协作。

| 项目 | 需要明确的内容 |
| --- | --- |
| 目的 | 当前问题及希望改善的体验 |
| 修改范围 | 涉及哪些页面、角色、资源或功能 |
| 不改动范围 | 哪些外观、行为、存档和公开入口必须保持 |
| 预期结果 | 正常操作后应出现的具体变化 |
| 边界情况 | 连续操作、中断、失败和重载时如何处理 |
| 验收环境 | 需要检查的设备、屏幕、语言与平台 |
| 交付证据 | 修改说明、差异、测试记录和发布状态 |

演示性需求可以写成：新增一条观察选项，不改变其他生境；选择后记录结果并显示反馈；保存重载后仍保持该结果；目标语言与手机布局没有溢出。是否采用某个函数或内部结构，不必由负责人预先指定。

**需求说明要达到什么结果，技术方案说明怎样实现，验收标准说明怎样判断结果成立。** 除非有明确兼容性要求，不应把未经验证的技术猜测当成唯一允许的实现方法。

<a id="change"></a>
## 3｜修改、提交、分支与审查

版本管理记录修改，使其可以比较和恢复。Git 是版本控制工具，GitHub 等平台提供托管与协作，它们不是同一件事。[1](#ref-1)

| 名词 | 解释 |
| --- | --- |
| 差异／Diff | 新旧版本之间增加、删除或改动的内容 |
| 提交／Commit | 一组可以定位的修改记录 |
| 分支／Branch | 相对独立的修改路线 |
| 合并／Merge | 将一条路线的修改整合到另一条路线 |
| PR／Pull Request | 提出、讨论和审查待合并修改的协作记录 |
| 标签／Tag | 为某个版本设置便于识别的名称 |

审查并不要求负责人读懂所有代码。可以先检查改动是否集中在预期文件、有没有删除不应删除的资源、是否混入无关重构，以及是否提供了对应验证。具体实现质量可由有能力的审查者进一步检查。

同一轮中若把修复按钮、调整视觉、重命名目录和升级依赖混在一起，出现问题时更难确认原因。因此，变更应按完整目的组织，不能以“顺便整理”为由扩大范围。

**提交证明修改已经被记录，合并证明修改已进入目标路线，审查记录说明检查了什么。** 它们都不能单独证明玩家已经取得正确成品。

<a id="verification"></a>
## 4｜测试结果的含义与边界

测试检查特定条件下的结果，质量管理还包含需求澄清、审查、预防和风险处理。通过一套自动检查，不等于所有设备和体验都已验证。[2](#ref-2)

| 检查 | 能提供的主要证据 | 不能单独证明 |
| --- | --- | --- |
| 文件与结构检查 | 引用、数据字段、目录等符合规定 | 游戏体验良好 |
| 规则测试 | 某些输入与状态得到预期结果 | 全部界面和设备均正常 |
| 集成检查 | 多个部分能够共同工作 | 所有边界情况都已覆盖 |
| 浏览器或设备操作测试 | 在指定环境中完成真实操作链 | 所有真实设备完全等同 |
| 视觉比较 | 与指定基线之间的画面差异 | 科学资料或叙事逻辑正确 |
| 试玩 | 玩家理解、节奏与操作感受 | 程序没有任何缺陷 |
| 无障碍检查 | 文字、输入、声音和运动等可用性 | 已自动满足全部法律或平台要求 |

无障碍应进入设计与测试过程，而不是只在发布前增加一个开关。Xbox Accessibility Guidelines 提供可读性、输入、音频等方向的具体检查资源，但其本身不等于认证结果。[3](#ref-3)

持续集成可以自动执行配置好的构建和检查；未配置的检查不会因为出现绿色标志而自动完成。[4](#ref-4) 交付说明应分别写明“执行并通过”“执行失败”“没有执行”“不适用”，不能将后两者合并成“没有问题”。

缺陷记录应包含环境、版本、前提、操作步骤、预期结果、实际结果和证据。严重程度描述影响，优先级描述处理顺序，两者由项目约定，不能只看到 P0、P1 就假定含义一致。

<a id="release"></a>
## 5｜从构建到公开版本

| 状态 | 准确含义 |
| --- | --- |
| 实现完成 | 所需文件或程序修改已产生 |
| 验证通过 | 对指定版本执行的相应检查通过 |
| 已提交或合并 | 修改进入可追踪的版本记录 |
| 构建成功 | 流程成功生成了成品文件 |
| 部署成功 | 成品放入了目标运行环境 |
| 公开核对完成 | 从玩家实际入口检查了可访问性与预期内容 |

**《Baldur’s Gate 3》案例。** Larian 在 2023 年的 Hotfix 4 复盘中说明：候选版经过测试，但临近发布时重新构建的版本出现问题；回退又使部分新补丁存档暂时无法继续使用，之后重新发布修正版本。[5](#ref-5) 这是历史事件，不是当前游戏状态。

由这个案例可以得到两项交付判断：**测试过的版本应与实际发布的版本对应；回退程序时需要另外考虑玩家数据。** “只改了版本号”或“重新打一次包”也不能自动免于检查。

商店发布还有独立要求。例如 Steam 区分商店页面与游戏构建的审核；游戏能运行，并不等于上架材料已经通过。[6](#ref-6) 网页发布则需要检查公开地址、资源加载、缓存与旧入口。

出现旧页面时，应先确定部署是否完成、访问地址是否正确、实际资源版本是什么，再判断缓存问题。清除网站数据可能同时删除本地存档，不应把“清空一切”当作没有代价的排查方式。[7](#ref-7)

<a id="isopoda"></a>
## 6｜UMWELT 与本博客的实际对应

这两个项目都使用版本记录和自动化，但发布对象不同，不能混用流程。[8](#ref-8)[9](#ref-9)

| 项目 | 源内容 | 发布处理 | 应检查的成品 |
| --- | --- | --- | --- |
| 《等足目赋格》网页版 | 游戏代码、内容和资源 | 准备站点、处理字体与资源版本标识 | 入口、交互、显示、声音与存档 |
| devlog 手册 | Markdown 正文与文章 metadata | 更新目录，由 Jekyll 转为网页并部署 | 标题、目录、表格、参考链接与锚点 |

《等足目赋格》的测试文档区分普通自动检查与浏览器回归；浏览器比较还区分是否提供旧版本基线。[8](#ref-8) 因此，“结构检查通过”与“确认新旧画面一致”是不同结论。

博客同样可以出现“源文章已更新，但公开页面尚未核对”的状态。准确说明这一区别，比笼统说“全部完成”更有用。**项目文件是输入，自动化产生发布结果，公开检查确认访问者实际看到的内容。**

本篇引用固定版本作为案例，不代替以后每轮读取当前项目，也不构成本次对游戏运行的测试报告。

<a id="cost"></a>
## 7｜工具成本与交接记录

标注日期：**2026-10-13**。费用类型用于理解成本来源，不是具体采购报价。

| 工具或服务 | 开放情况 | 费用与限制 |
| --- | --- | --- |
| [Git](https://git-scm.com/about) | 开源 | 软件免费，备份与托管资源另计 |
| [GitHub](https://github.com/pricing) | 托管平台 | 免费与付费方案，权限和额度按计划区分 |
| [GitHub Actions](https://docs.github.com/en/billing/concepts/product-billing/github-actions) | 云服务；执行器等组件另有开源部分 | 按适用免费额度、执行环境及用量计费；不能假定所有任务无限免费 |
| [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) | 静态托管服务 | 有适用的免费使用范围；仓库类型、方案及使用限制需确认 |
| [Jekyll](https://jekyllrb.com/) | 开源 | 软件免费；运行它的服务资源另计 |
| [Node.js](https://nodejs.org/en/about)、[Playwright](https://playwright.dev/) | 开源 | 软件免费；真机、云端执行和维护工作另计 |
| 浏览器开发者工具 | 随浏览器提供，开放情况依产品 | 通常无需另购工具许可；并非独立游戏引擎 |
| [Steamworks](https://partner.steamgames.com/doc/gettingstarted) | 平台工具与服务 | 文档可免费查阅；发行涉及接入、销售和平台协议中的费用 |
| AI 开发辅助 | 依产品及接入方式 | 免费额度、订阅或按量计费；具体产品成本见 [002](posts-2026-umwelt-game-development-handbook-002.html#tools-25) |

交接时可以要求以下记录，而不是要求展示全部开发过程：

| 记录 | 最低内容 |
| --- | --- |
| 变更说明 | 改了什么、没有改什么、对应哪项需求 |
| 版本标识 | 工作基线与交付版本的位置 |
| 验证结果 | 环境、执行范围、结果及未覆盖部分 |
| 发布结果 | 是否已部署、是否核对公开入口 |
| 已知限制 | 尚未解决的问题、影响及下一步责任 |
| 恢复方案 | 上个稳定版本及玩家数据的处理边界 |

**AI 可以辅助实现和检查，但“由 AI 完成”不是验收证据。** 无法执行某项测试时应说明限制，不能把代码阅读、模拟推断或未经验证的截图称作真机测试。

<a id="references"></a>
## 参考文献与学习资源

本篇将原始开发记录用于案例，将官方文档与教材用于概念核对。旧版事故、流程和限制均按其发表时间理解。网页查阅日期：**2026-10-13**。

<a id="ref-1"></a>
**[1] Chacon, Scott；Straub, Ben. _Pro Git_，第 2 版.** [在线版](https://git-scm.com/book/en/v2) · [版本管理概述](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)。在线全文免费，有中文译本入口，纸书可购买或借阅。**优先阅读**版本、历史、分支的概念部分，命令操作不是本篇要求。

<a id="ref-2"></a>
**[2] ISTQB. _Certified Tester Foundation Level Syllabus_，v4.0.1（2024）.** [官方认证与大纲入口](https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/)。大纲资料可公开查阅，培训和考试另收费；英文及相应机构译本。用于理解测试、质量、风险和缺陷报告，不要求为本系列参加考试。

<a id="ref-3"></a>
**[3] Microsoft. _Xbox Accessibility Guidelines_.** [官方指南](https://learn.microsoft.com/en-us/xbox/accessibility/guidelines)。免费网页。按文字、输入、音频和运动效果等实际需求查阅，适合作为检查方向，不等于自动获得认证。

<a id="ref-4"></a>
**[4] GitHub. _Continuous Integration_.** [官方文档](https://docs.github.com/en/actions/get-started/continuous-integration)。免费网页。理解自动化在何时执行、检查什么，以及结果对应哪个版本。

<a id="ref-5"></a>
**[5] Larian Studios. _Hotfix 4 Redeployed_（2023-08-17）.** [官方复盘](https://baldursgate3.game/news/hotfix-4-redeployed_86)。免费，英文。**优先案例**：理解重新构建、验证范围、回退与存档之间的关系；无需读取实现代码。

<a id="ref-6"></a>
**[6] Valve. _Review Process_. Steamworks Documentation.** [官方流程](https://partner.steamgames.com/doc/store/review_process)。文档免费，英文及站点提供的语言版本。重点看商店页与构建的不同职责；实际发行条件需按提交时平台规定核对。

<a id="ref-7"></a>
**[7] MDN contributors. _Window: localStorage Property_.** [官方文档](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)。免费网页。理解本地保存的来源与持久化边界，尤其注意排查问题时的数据影响。

<a id="ref-8"></a>
**[8] fivsevn. UMWELT：测试与发布说明.** [测试](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/tests/README.md) · [发布](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/docs/deployment.md)。免费查看，固定提交 `0bbe083`。阅读检查范围和边界即可，不要求执行文中的命令。

<a id="ref-9"></a>
**[9] fivsevn. devlog：posts 板块说明.** [固定版本](https://github.com/fivsevn-agy/fivsevn-devlog/blob/49d5c65ad313e5ff88a8bb4ff4d3ca86b2ea1799/posts/README.md)。免费查看。用于区分文章源文件、自动目录、网页生成和部署；其中 WordPress 是另一条发布流程。

**扩展教材：Chandler, Heather. _The Game Production Toolbox_（2019）.** [出版社与目录](https://www.routledge.com/Game-Production-Proven-Business-Techniques-to-Produce-the-Best-Games/Chandler/p/book/9781138341708)。书籍付费或借阅，目录免费，英文。结合自己的协作需求阅读任务、制作管理、测试与发布相关部分，不必照搬大型团队的岗位数量。

**建议顺序：** 先读 [5] 的实际事故，再用 [1]、[4] 理解交付关系；需要建立质量检查方法时查 [2]、[3]。

[下一篇：研究资料与游戏表达 007](posts-2026-umwelt-game-development-handbook-007.html) · [返回个人笔记目录](../index.html)
