---
id: "posts-2026-umwelt-game-development-handbook-001"
title: "游戏开发术语与流程手册｜ChatGPT 写给五月七日的指导笔记 001"
module: "posts"
submodule: "2026"
topic: "umwelt-game-development-handbook"
type: "note"
status: "active"
canonical: true
summary: |
  按开发阶段整理中英日术语，覆盖企划、规则、原型、程序、美术、关卡、动画、叙事、声音、协作、测试、发行和维护。结合具体游戏比较同一问题的不同做法，让术语查阅与完整流程学习相互连接。
parents: ["posts-index"]
related: ["posts-2026-umwelt-game-development-handbook-002"]
tags: ["game-development", "umwelt", "production", "qa", "workflow", "handbook", "glossary"]
audience: ["self", "public"]
languages: ["zh", "en", "ja"]
maturity: "evolving"
confidence: 0.9
visibility: "public"
source_of_truth: "devlog"
lang: "zh-CN"
description: "以中英日术语为入口，完整梳理游戏开发流程，并用具体游戏比较做法、原因和结果。"
canonical_url: "https://devlog.fivsevn.com/posts/2026/posts-2026-umwelt-game-development-handbook-001.html"
created: "2026-10-13"
updated: "2026-10-15"
metadata_updated: "2026-10-15"
---

# 游戏开发术语与流程手册｜ChatGPT 写给五月七日的指导笔记 001

**撰写：ChatGPT · 中英日术语与资料核对：2026-10-15**

**001 术语与流程** · [002 软件与制作能力](posts-2026-umwelt-game-development-handbook-002.html)

游戏开发从**概念、规则、原型和制作样板**开始，经过**程序、资源与内容生产**，再进入**测试、发布和维护**。本篇按这些工作的位置整理术语：查一个词时，可以同时知道它解决什么问题、与哪些工作相连、完成后交给谁。可从目录定位阶段，也可用页面查找（⌘F／Ctrl+F）搜索中、英、日名称。

每个词条包含**含义、具体例子与主要使用阶段**。“例”说明游戏中可观察的玩法或有来源的开发事实；“制作例”借具体游戏的角色、物件或规则说明一种制作方法，不代表原作实际采用该实现。各阶段会反复往返，美术、程序、音频与测试也会并行。

日文采用常见写法或便于检索的对应说法；团队和软件可能使用不同译名，缩写通常保留英文。[\[16\]](#ref-16)、[\[17\]](#ref-17)

<a id="overview"></a>

## 流程与查阅目录

| 流程位置 | 先认识的词 | 这一阶段要弄清什么；留下什么 |
| --- | --- | --- |
| [01 概念与立项](#phase-1) | Concept、Pitch、Scope、Design Pillars | 做什么、给谁玩、承担多大范围；留下概念与边界 |
| [02 玩法与规则](#rules) | Mechanic、Core Loop、Feedback、Progression | 玩家怎样行动、得到什么反馈；留下规则、状态与体验目标 |
| [03 前期制作与计划](#phase-2) | GDD、TDD、Pipeline、Milestone | 由谁制作、怎样交接、先验证什么；留下约定与计划 |
| [04 原型与制作样板](#phase-3) | Prototype、PoC、Vertical Slice、Demo | 体验是否成立、品质能否重复生产；留下可玩验证与成本依据 |
| [05 程序与运行](#runtime) | Engine、State、Event、Save、Networking | 把输入、规则、资源和数据接起来；留下运行系统 |
| [06 美术与资源](#visual-production) | Sprite、Mesh、UV、Material、Rendering | 做出需要的形象并转成游戏资源；留下源工程与导出文件 |
| [07 关卡、动画与表现](#levels-animation) | Level、Blockout、Rig、Keyframe、Hitbox | 组织空间、动作和反馈；留下可玩的场景与行为 |
| [08 叙事、界面与声音](#narrative-audio) | Branch、Flag、UI、L10n、Audio Event | 让内容随状态呈现，并让玩家理解；留下文本、界面和声音连接 |
| [09 正式制作与协作](#phase-5) | Production、Iteration、Version Control、Integration | 持续扩大内容、控制返工；留下不断可玩的版本 |
| [10 测试与打磨](#phase-6) | QA、Playtest、Regression、Profiling | 检查规则、理解、兼容与性能；留下问题、证据和候选版本 |
| [11 发布与发行](#phase-7) | Build、Deploy、Release、Certification | 把检查过的成品交给玩家；留下公开入口和发布版本 |
| [12 维护与结束支持](#phase-8) | Patch、Migration、Rollback、EOL | 修复、兼容、扩展或结束；留下可恢复和可继续使用的项目 |

**跨章节速查：** [核心循环](#core-loop) · [岗位分工](#roles) · [预算与进度](#cost) · [验收](#acceptance) · [游戏类型](#terms) · [参考资料](#references)。查软件、价格形式和扩展名，见 [002](posts-2026-umwelt-game-development-handbook-002.html)。

**易混词对照：** [机制与几种循环](#loops-comparison) · [概念、提案与设计文档](#documents-comparison) · [原型、切片与 Demo](#prototype-comparison) · [对象、组件与实例](#objects-comparison) · [网格、纹理与材质](#surface-comparison) · [测试、试玩与调试](#testing-comparison) · [缩写、存档与版本](#ambiguous-terms)。

<a id="phase-1"></a>

## 01｜概念与立项：确定作品及其边界

概念阶段把题材转成可制作的体验。“关于海上旅行”是主题；“玩家在渡轮上观察邻座、选择回应，并从动作理解关系变化”进一步说明了玩家行为。平台、输入、时长、人数和画面形式会决定后面的工作量。

| 中文 | English | 日本語 | 含义、实例与使用阶段 |
| --- | --- | --- | --- |
| 概念 | Concept | コンセプト | 对作品体验与形式的概括；是规则、美术和规模取舍的起点。<br><strong>例：</strong>[《Baba Is You》](https://www.hempuli.com/baba/)把“移动文字就能改写世界规则”作为可玩的中心想法；题材和关卡围绕这一关系展开。<br>用于：概念与立项。 |
| 高概念 | High Concept | ハイコンセプト | 能用很短说明传达的主要吸引力，例如“通过移动文字改变世界规则”。<br><strong>例：</strong>[《Papers, Please》](https://papersplea.se/)把“当边检员，靠核对证件决定放行”压缩成一句容易理解的体验说明。<br>用于：概念与立项。 |
| 提案／企划案 | Pitch | ピッチ／企画提案 | 向合作者或发行方说明体验、受众、可行性与所需支持；常以演示和简报呈现。<br><strong>制作例：</strong>提案一个[《A Short Hike》](https://ashorthike.com/)式登山游戏，要展示攀爬、滑翔小样，并说明岛屿规模、所需人员和制作时间。<br>用于：概念与立项。 |
| 目标受众 | Target Audience | ターゲット層 | 优先服务的玩家；影响操作门槛、信息量、设备和内容表达。<br><strong>例：</strong>[《Celeste》](https://www.celestegame.com/)的连续跳跃重在动作练习，[《Baba Is You》](https://www.hempuli.com/baba/)的推词谜题重在规则推理；两者需要验证的玩家能力不同。<br>用于：立项、原型试玩与发行。 |
| 独特卖点 | USP — Unique Selling Proposition | 独自のセールスポイント | 与其他选择相比值得关注的特点；需要由实际体验支持。<br><strong>例：</strong>[《Return of the Obra Dinn》](https://obradinn.com/)让玩家进入定格的死亡现场推断身份，“怎样调查”比泛称“侦探游戏”更能说明特点。<br>用于：概念与立项。 |
| 设计支柱 | Design Pillars | デザインピラー | 少数持续用于取舍的原则，如“观察先于解释”“失败后迅速重试”。<br><strong>例：</strong>从[《Celeste》](https://www.celestegame.com/)可归纳“允许迅速重试”的取舍原则；它会影响房间长度、重生位置和过场等待，而非只影响难度数值。<br>用于：概念与立项。 |
| 游戏类型 | Genre | ゲームジャンル | 对常见玩法结构的分类；动作、解谜、经营等可混合，标签本身不能代替规则说明。<br><strong>例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)同时包含动作、探索和能力解锁；[《Slay the Spire》](https://store.steampowered.com/app/646570/Slay_the_Spire/)则把卡牌战斗与多轮重新构筑牌组结合。<br>用于：立项与玩法沟通。 |
| 平台 | Platform | プラットフォーム | 成品运行和分发的环境，如桌面、浏览器、手机、主机；会影响输入、性能和发布。<br><strong>例：</strong>[《Minecraft》](https://www.minecraft.net/en-us/about-minecraft)的 Java 与 Bedrock 版支持范围、输入与互联条件有区别；决定平台时要同时说明版本。[\[21\]](#ref-21)<br>用于：立项、技术选型与发布。 |
| 范围 | Scope | スコープ／制作範囲 | 本次承诺的功能、内容、平台和品质；应尽量写成可核对数量。<br><strong>制作例：</strong>以[《A Short Hike》](https://ashorthike.com/)式小岛为参照，明确“一座岛、三种移动方式、多少人物”；这些数量才能进入排期。<br>用于：立项、计划与变更评估。 |
| 范围膨胀 | Scope Creep | スコープクリープ | 新需求不断加入而预算、期限没有相应调整；小功能也可能产生大量组合工作。<br><strong>制作例：</strong>给[《星露谷物语》](https://www.stardewvalley.net/)式农场临时增加多人合作，会连带改变时间推进、共同物品、存档和断线处理。<br>用于：计划与整个制作过程。 |
| 约束 | Constraint | 制約 | 时间、人力、设备、许可和艺术方向等边界；约束直接参与设计。<br><strong>例：</strong>[《A Short Hike》](https://ashorthike.com/)初版四个月的期限影响了空间、美术和写作取舍；期限参与形成作品规模。[\[1\]](#ref-1)<br>用于：立项与整个制作过程。 |
| 风险 | Risk | リスク | 可能影响交付的不确定事项；按发生可能性与影响排序，安排验证。<br><strong>制作例：</strong>[《Baba Is You》](https://www.hempuli.com/baba/)式规则改写若允许两条互相冲突的句子，先验证冲突怎样处理，再制作大量谜题。<br>用于：立项、原型与里程碑评估。 |
| 可行性 | Feasibility | 実現可能性 | 技术能否实现、制作资源是否足够、长期是否可承担；三个问题分别检查。<br><strong>制作例：</strong>[《Return of the Obra Dinn》](https://obradinn.com/)式调查要同时验证线索能否被看懂、现场能否做完、目标设备能否流畅显示。<br>用于：概念与立项。 |
| 立项放行 | Greenlight | 企画承認／グリーンライト | 根据现有材料决定继续投入；可以只批准下一段验证工作。<br><strong>制作例：</strong>[《A Short Hike》](https://ashorthike.com/)式小样已证明攀爬和滑翔有趣，团队才批准扩展岛屿；这是下一段投入的决定。<br>用于：概念与立项。 |

### 同一个问题：场景有限，怎样仍有足够的内容

| 游戏与玩家行为 | 具体做法 | 为什么能形成内容；结果与代价 |
| --- | --- | --- |
| [《Papers, Please》](https://papersplea.se/)：玩家坐在边检窗口，核对证件并决定是否放行 | 地点基本固定，变化来自每日规则、证件矛盾、来访者请求和时间压力 | 同一组检查动作遇到不同条件，就会产生不同判断。场景制作较集中，规则组合、文字和例外测试却会增加 |
| [《A Short Hike》](https://ashorthike.com/)：小鸟在岛上徒步、攀爬和滑翔，目标是登上山顶 | 把收集、相遇和路线选择放进紧凑空间；同一地点可步行经过，也可从高处滑翔返回 | 空间通过不同移动方式反复使用。作者在初版四个月期限内对美术、关卡和写作作出取舍；这种办法要求路线与移动本身有趣。[\[1\]](#ref-1) |
| [《Hades》](https://www.supergiantgames.com/games/hades/)：主角反复尝试逃出冥界，失败后回到家中 | 战斗组合与房间反复出现，角色关系和故事在多次尝试之间继续推进 | 重复挑战与长期变化并存。可重复游玩增加内容寿命，同时需要更多平衡、条件对白与状态检查。[\[2\]](#ref-2) |

三者分别把变化放在**规则与来访者、空间使用方式、多轮战斗与故事状态**里。范围不能只数地图；还要数动作、文本、条件和组合。下一步的规则设计，就是把这些变化写成可以实现的关系。

<a id="rules"></a>

<a id="core-loop"></a>

## 02｜玩法与规则：把体验转成可观察的关系

一项操作需要交代触发条件、当前前提、状态变化、反馈和结束方式。“点击杯子”只是输入；点击后是否抬杯、何时出现对白、连续点击会怎样，才是完整规则。

| 中文 | English | 日本語 | 含义、实例与使用阶段 |
| --- | --- | --- | --- |
| 玩法 | Gameplay | ゲームプレイ | 玩家实际操作、判断和得到反馈的整体过程。<br><strong>例：</strong>[《Papers, Please》](https://papersplea.se/)中拖动证件、比对日期、追问矛盾、盖章与领取工资，合起来构成实际游玩过程。<br>用于：规则设计、原型与调试。 |
| 机制 | Mechanic | メカニクス／ゲームの仕組み | 一项操作与规则的关系，如消耗体力攀爬、移动文字改变属性。<br><strong>例：</strong>[《Baba Is You》](https://www.hempuli.com/baba/)把“WALL IS STOP”拆开，墙就失去阻挡规则；一项局部关系可反复用于不同谜题。<br>用于：规则设计、原型与调试。 |
| 核心循环 | Core Loop | コアループ | 反复连接行动、反馈和下一次选择的结构；一次循环可短至几秒，也可跨一个游戏日。<br><strong>例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)中种植、照料、收获、出售、再投资相互连接；“浇水”是其中一个动作。<br>用于：规则设计、原型与调试。 |
| 外层循环 | Meta Loop | メタループ | 多次核心循环之间的长期安排，如解锁装备、扩建基地和推进关系。<br><strong>例：</strong>[《Hades》](https://www.supergiantgames.com/games/hades/)一轮逃脱结束后回到据点，长期成长和人物关系影响下一轮；它包在单次战斗循环之外。<br>用于：规则设计、原型与调试。 |
| 目标／胜败条件 | Goal / Win & Lose Conditions | 目標／勝利・敗北条件 | 玩家努力达到的状态及本轮何时结束；开放体验也可以有局部目标。<br><strong>例：</strong>[《A Short Hike》](https://ashorthike.com/)的登顶目标允许绕路探索；[《Celeste》](https://www.celestegame.com/)一间挑战房的局部目标是安全抵达出口。<br>用于：规则设计、原型与调试。 |
| 反馈 | Feedback | フィードバック | 让玩家知道行动结果的信息，包括画面、声音、震动、文字和状态变化。<br><strong>例：</strong>[《Celeste》](https://www.celestegame.com/)冲刺后的位移、轨迹和角色状态让玩家确认动作发生；[《Papers, Please》](https://papersplea.se/)盖章后的证件状态确认裁决。<br>用于：规则、界面、动画与声音设计。 |
| 可供性／操作线索 | Affordance / Signifier | アフォーダンス／シグニファイア | 前者指可以做什么，后者指提示玩家如何操作的线索；发光轮廓可能是可点击的提示。<br><strong>例：</strong>[《Portal 2》](https://www.thinkwithportals.com/about.php)的可穿越传送门提供通行可能，门口可见的另一侧空间提示它会通向哪里；能力与提示是两件事。<br>用于：规则设计、原型与调试。 |
| 玩家能动性 | Agency | エージェンシー／主体性 | 玩家能作出有影响的选择，并理解行动与结果的关系。<br><strong>例：</strong>[《80 Days》](https://www.inklestudios.com/80days/)选择路线会改变旅行时间、开销与遭遇；能看到后果，选择才具有可理解的影响。<br>用于：规则设计、原型与调试。 |
| 进程／成长 | Progression | プログレッション／進行・成長 | 能力、资源、剧情或知识怎样随游玩变化；进步不必表现为等级。<br><strong>例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)获得移动能力会打开路线；[《Outer Wilds》](https://www.mobiusdigitalgames.com/outer-wilds.html)常靠学到新信息找到入口；进展可以来自能力，也可以来自知识。<br>用于：规则设计、原型与调试。 |
| 奖励 | Reward | 報酬／リワード | 行动后的有价值结果，如新能力、信息、情感回应或资源。<br><strong>例：</strong>[《A Short Hike》](https://ashorthike.com/)金羽毛扩大攀爬等移动余量；[《Return of the Obra Dinn》](https://obradinn.com/)确认身份带来的是推理进展，未必是一件装备。<br>用于：规则设计、原型与调试。 |
| 风险与回报 | Risk–Reward | リスクとリターン | 可能损失与预期收益的关系；决定冒险是否值得。<br><strong>例：</strong>[《Slay the Spire》](https://store.steampowered.com/app/646570/Slay_the_Spire/)可选择挑战更危险的精英敌人以争取更好的收益；当前生命值会改变这条路线是否值得。<br>用于：规则设计、原型与调试。 |
| 游戏经济 | Game Economy | ゲーム内経済 | 资源怎样产生、交换、消耗和积累；包括货币，也包括体力、时间等。<br><strong>例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)买种子要花钱，种植占土地和天数，照料消耗时间与体力，出售再回收金钱。<br>用于：规则设计、数值测试与维护。 |
| 资源来源／回收口 | Source / Sink | 供給源／消費先 | 资源进入和离开系统的渠道；只增加供给而缺少消耗，可能持续通胀。<br><strong>例：</strong>[《Slay the Spire》](https://store.steampowered.com/app/646570/Slay_the_Spire/)战斗等活动带来金币，商店购买与服务消耗金币；收入渠道和消耗渠道需要一起设计。<br>用于：规则设计、原型与调试。 |
| 平衡／调参 | Balancing / Tuning | バランス調整／パラメータ調整 | 调整规则和数值，使选择、压力与节奏接近目标；不等于所有选项完全一样。<br><strong>制作例：</strong>给[《Slay the Spire》](https://store.steampowered.com/app/646570/Slay_the_Spire/)式卡牌提高伤害，同时改变费用，可能使它从常规进攻变成需要整回合安排的选择。<br>用于：规则设计、原型与调试。 |
| 难度曲线 | Difficulty Curve | 難易度曲線 | 挑战随进程的变化；应结合玩家已学会的能力判断。<br><strong>例：</strong>[《Celeste》](https://www.celestegame.com/)先让玩家熟悉跳跃与冲刺，再把它们接到更复杂的障碍中；难度与已学动作的组合有关。<br>用于：规则设计、原型与调试。 |
| 随机数／种子 | Random Number Generator — RNG / Seed | 乱数／シード値 | 随机过程及其起点；在相同算法和条件下，固定种子有助于复现生成结果。<br><strong>例：</strong>[《Minecraft》](https://www.minecraft.net/en-us/about-minecraft)用种子启动世界生成；相同种子还要配合相同版本与条件才便于复现。官方曾更换生成器，同一种子的地形也随之改变。[\[22\]](#ref-22)<br>用于：规则设计、原型与调试。 |
| 程序化生成 | PCG — Procedural Content Generation | プロシージャル生成／自動生成 | 用规则和数据生成关卡等内容；仍需设计约束、筛选与测试。<br><strong>例：</strong>[《Minecraft》](https://www.minecraft.net/en-us/about-minecraft)用种子与规则组织世界地形；每一片可见山坡无需都由关卡作者逐块手摆。[\[22\]](#ref-22)<br>用于：规则设计、原型与调试。 |
| 涌现 | Emergence | 創発 | 多个简单规则组合后出现未逐一写死的情况；组合越自由，边界测试越重要。<br><strong>例：</strong>[《Minecraft》](https://www.minecraft.net/en-us/about-minecraft)玩家组合方块与红石建造机关；作者提供可组合规则，玩家再形成具体装置。[\[21\]](#ref-21)<br>用于：规则设计、原型与调试。 |
| 游戏手感 | Game Feel | 操作感／ゲームフィール | 输入、运动、碰撞、相机与反馈共同形成的操作感受。<br><strong>例：</strong>[《Celeste》](https://www.celestegame.com/)的起跳、空中移动、碰撞和快速重试共同形成动作体验；只调整跳跃高度无法覆盖全部手感。<br>用于：规则设计、原型与调试。 |
| 容错窗口 | Grace Window | 猶予時間／入力猶予 | 在时间或位置上接受接近玩家意图的操作，减少细小误差带来的失败。<br><strong>例：</strong>[《Celeste》](https://www.celestegame.com/)允许一些接近平台边缘或落地时刻的操作成立；接受意图的时间与位置范围都参与容错。[\[10\]](#ref-10)<br>用于：动作原型与手感打磨。 |
| 输入缓冲 | Input Buffer | 入力バッファ／先行入力 | 暂存过早的输入，在允许执行时使用；如落地前按跳跃，落地时起跳。<br><strong>例：</strong>[《Celeste》](https://www.celestegame.com/)中落地前稍早按下跳跃，输入可被保留至落地执行；解决的是“按得稍早”。[\[10\]](#ref-10)<br>用于：动作实现与手感打磨。 |
| 土狼时间／离边宽限 | Coyote Time | コヨーテタイム | 离开平台边缘后的短暂时间内仍允许跳跃，是动作容错的一种。<br><strong>例：</strong>[《Celeste》](https://www.celestegame.com/)离开平台边缘后仍短暂允许起跳；解决的是“按得稍晚”，与输入缓冲方向相反。[\[10\]](#ref-10)<br>用于：动作实现与手感打磨。 |
| 冷却／无敌帧 | Cooldown / Invincibility Frames | クールダウン／無敵時間 | 再次使用能力前的等待／暂时不受特定伤害的时间；需与动画、输入和反馈对应。<br><strong>制作例：</strong>[《Hades》](https://www.supergiantgames.com/games/hades/)式闪避可分别设置“多久能再用”和“哪段时间避开伤害”；两段时间不必相同。<br>用于：规则设计、原型与调试。 |
| 检定／概率 | Check / Probability | 判定／確率 | 按条件、数值或随机结果决定行动是否成立；需要让玩家理解可预期程度。<br><strong>例：</strong>[《Baldur’s Gate 3》](https://baldursgate3.game/)用掷骰检定判断部分行动是否成功；检查成功率时，要把角色加值与成功门槛一起看。<br>用于：规则设计、原型与调试。 |
| 元游戏／主流打法 | Metagame / Meta | メタゲーム／メタ | 游戏规则之外或长期演化的策略选择，如依据常见对手调整配置；与长期成长循环 Meta Loop 区分。<br><strong>制作例：</strong>分析[《Dota 2》](https://store.steampowered.com/app/570/Dota_2/)某类英雄变常见后其他玩家怎样调整选择，讨论的是对战环境中的策略，而非角色永久升级。<br>用于：平衡测试与发布后观察。 |

### 同一个问题：怎样让玩家愿意再做一轮

| 游戏与一轮行为 | 做法及其作用 | 最后形成的差异 |
| --- | --- | --- |
| [《星露谷物语》](https://www.stardewvalley.net/)：安排一天，种植、采集或交往，再结束当天 | 作物和建筑需要跨日发展，每天的时间与体力有限；今天的选择会改变明天的资源 | 动力来自积累和安排。增加内容时，要检查季节、日程、价格和人物条件 |
| [《Celeste》](https://www.celestegame.com/)：控制少女在短小房间内跳跃、攀爬和冲刺 | 障碍让玩家不断修正路线与按键时机；失败后很快重试。作者还用输入缓冲和离边宽限贴近玩家意图。[\[10\]](#ref-10) | 动力来自“这次更接近成功”。关键工作是动作规则、房间布局和失败成本 |
| [《Return of the Obra Dinn》](https://obradinn.com/)：登船查看死亡现场，推断船员身份和命运 | 同一现场里的服装、站位、声音等信息可以和其他现场互相印证 | 进展主要是理解增加。制作重点转向线索一致性、证据分配和推理反馈 |
| [《Outer Wilds》](https://www.mobiusdigitalgames.com/outer-wilds.html)：驾驶飞船探索处于时间循环中的太阳系 | 行星随时间改变，某次探索得到的信息能改变下一次出发地点与时机 | 玩家带着知识重新规划。比起增加装备数值，更需要检查信息是否能指向新行动。[\[19\]](#ref-19) |

这几种循环分别依靠**积累、熟练、推理、发现**。解释核心循环时，把“重复什么”与“重复以后改变什么”一起写清。

<a id="loops-comparison"></a>

### 放在一起看：机制、核心循环、外层循环与程序循环

用[《星露谷物语》](https://www.stardewvalley.net/)的农作理解四个层次。前三行分析玩家行为，最后一行是实现示例。

| 词 | 具体指什么 | 在哪个阶段讨论 |
| --- | --- | --- |
| 机制 Mechanic | 对一格作物浇水，会改变它当天的生长条件；这是一项局部关系 | 规则设计与原型 |
| 核心循环 Core Loop | 种植、照料、收获、出售，再用收入安排下一轮；多个机制连成反复进行的活动 | 玩法原型与节奏调整 |
| 外层循环 Meta Loop | 多次收获积累资源，再扩大农场、添置设施，改变以后每轮能做的事 | 长期进程与经济设计 |
| 游戏循环 Game Loop | 程序反复接收输入、更新状态、准备画面；即使玩家站着不种地，程序也可能继续更新 | 程序实现与性能检查 |

核心与外层的划分取决于观察尺度；说明时先约定“一轮”指一次行动、一天还是一季。**Metagame** 则常指玩家根据流行策略调整打法，与这两层成长循环另行区分。

<a id="phase-2"></a>

## 03｜前期制作与计划：约定谁做、怎样接、何时检查

前期制作把概念整理成规则、资源规格和生产方法。文档先支持眼前的验证，再随决定更新；未确定的部分明确列为待验证，避免多人各自补全假设。

| 中文 | English | 日本語 | 含义、实例与使用阶段 |
| --- | --- | --- | --- |
| 前期制作 | Pre-production | プリプロダクション | 确定设计、技术、美术方向与生产方法，为大规模制作降低不确定性。<br><strong>制作例：</strong>做[《Hollow Knight》](https://www.hollowknight.com/)式探索游戏前，先试移动、房间连接和一套资源导入方法，再批量增加区域。<br>用于：前期计划与制作协作。 |
| 游戏设计文档 | GDD — Game Design Document | ゲームデザインドキュメント／仕様書 | 记录玩法、内容、规则和体验目标；小项目可以拆成少量专题文档。<br><strong>制作例：</strong>[《Papers, Please》](https://papersplea.se/)式文档写明证件字段、允许放行的条件、错误处罚；它说明游戏规则，不要求先写代码。<br>用于：前期计划与制作协作。 |
| 技术设计文档 | TDD — Technical Design Document | 技術設計書 | 记录系统、数据、依赖与实现安排；TDD 在测试语境另有含义。<br><strong>制作例：</strong>[《Papers, Please》](https://papersplea.se/)式证件游戏的技术文档说明字段怎样存储、规则怎样读取、日期怎样比较；与“处罚多少”分开。<br>用于：前期计划与制作协作。 |
| 美术规范 | Art Bible / Style Guide | アートバイブル／スタイルガイド | 统一形状、色彩、光照、比例及资源规格；供不同作者保持一致。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式手绘项目要约定轮廓粗细、角色尺度和背景层次，使新增角色能放进同一画面。<br>用于：前期计划与制作协作。 |
| 制作管线 | Pipeline | パイプライン | 源工程经过导出、转换、导入和检查，最终进入成品的步骤。<br><strong>例：</strong>[《Dead Cells》](https://dead-cells.com/)三维模型与动作经过渲染生成二维帧；源动作、输出图像和游戏接入构成连续工序。[\[8\]](#ref-8)<br>用于：前期验证与资源生产。 |
| 数据约定 | Data Contract | データ仕様／インターフェース仕様 | 规定字段、类型、单位、编号及缺失值含义；避免两端各自解释。<br><strong>制作例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)式作物表约定编号、售价、生长天数和季节字段，程序与表格作者才能使用同一含义。<br>用于：前期计划与制作协作。 |
| 资源清单 | Asset List | アセットリスト | 记录所需图像、模型、声音、文本与状态；与功能任务相互对应。<br><strong>制作例：</strong>[《Celeste》](https://www.celestegame.com/)式新房间要列出平台、危险物、背景、动作反馈与音效；一张背景图不能代替整间房的资源。<br>用于：前期计划与制作协作。 |
| 里程碑 | Milestone | マイルストーン | 有明确成果和判断条件的检查点，如“完成一段目标品质体验”。<br><strong>制作例：</strong>[《80 Days》](https://www.inklestudios.com/80days/)式旅行项目把“可完成一条含分支的旅程并读档继续”设为检查点，成果比“写了一半”明确。<br>用于：前期计划与制作协作。 |
| 待办列表 | Backlog | バックログ | 尚未完成的需求、任务和问题；记录想法不等于承诺全部制作。<br><strong>制作例：</strong>[《A Short Hike》](https://ashorthike.com/)式小岛可先记录钓鱼、竞速和新人物想法，再按目标选择本轮要做的内容。<br>用于：前期计划与制作协作。 |
| 迭代周期 | Sprint / Iteration | スプリント／イテレーション | 在限定周期内完成一组工作并检查；Sprint 是特定方法中的周期安排。<br><strong>制作例：</strong>[《Baba Is You》](https://www.hempuli.com/baba/)式谜题本轮只处理“规则冲突是否看得懂”，制作、试玩和修改围绕同一问题完成。<br>用于：前期计划与制作协作。 |
| 依赖 | Dependency | 依存関係 | 某项工作需要的前提；例如角色比例会影响动画、碰撞和镜头。<br><strong>制作例：</strong>[《Cuphead》](https://cupheadgame.com/)式首领的体形会影响攻击范围、动画和镜头；大改体形会牵动这些后续工作。<br>用于：前期计划与制作协作。 |
| 关键路径 | Critical Path | クリティカルパス | 决定整体最早完成时间的一组依赖任务；这些任务延误会推迟交付。<br><strong>制作例：</strong>[《80 Days》](https://www.inklestudios.com/80days/)式项目若必须先完成文本导出，才能接入翻译并做语言测试，这条依赖链可能控制交付日期。<br>用于：前期计划与制作协作。 |
| 预留 | Contingency / Buffer | 予備費／バッファ | 为已知不确定性预留预算或时间；应与具体风险联系。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式新区域已能跑通，也为地图死路、旧存档和主机适配留出返工时间。<br>用于：前期计划与制作协作。 |
| 完成标准 | Definition of Done — DoD | 完了の定義 | 团队约定“做完”包含哪些检查与文件；避免只在作者机器上成立。<br><strong>制作例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)式作物做完应包含图像、数据、收获、出售、读档检查，不能只以“表里有一行”判断。<br>用于：前期约定、制作验收与发布。 |
| 验收条件 | Acceptance Criteria | 受け入れ条件 | 某项任务可被接受的具体结果；如读档后仍保持已选对白分支。<br><strong>制作例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)式作物的具体验收可写“成熟后收获一次，背包增加一个对应物品，读档后仍一致”。<br>用于：任务规划与验收。 |
| 外包 | Outsourcing | 外注／アウトソーシング | 将部分制作交给外部作者；需要规格、源文件、许可、修改与验收安排。<br><strong>制作例：</strong>委托[《Cuphead》](https://cupheadgame.com/)式手绘动画时，要交代动作帧数、线条、上色、源文件和修改轮次，而非只说“画得像”。<br>用于：前期计划与制作协作。 |

<a id="documents-comparison"></a>

### 放在一起看：概念、提案、GDD 与 TDD

以[《Papers, Please》](https://papersplea.se/)的边检玩法说明文档分工。下面是按游戏规则整理的制作示例。

| 名称 | 同一项目里会写什么 | 主要使用位置 |
| --- | --- | --- |
| 概念／高概念 | “在边检工作中核对证件、作出裁决”概括体验；“规则要求与来访者处境发生冲突”进一步说明吸引力 | 立项，帮助大家理解要做的作品 |
| 提案 Pitch | 用一段可玩检查流程说明体验，再列受众、规模、预算和所需支持 | 寻找合作者、立项放行 |
| GDD | 证件有哪些字段，怎样算过期，漏检和误拒怎样处理，工作一天如何结束 | 规则设计、制作与验收 |
| TDD | 日期采用什么数据格式，检查规则怎样读取，结果怎样连接工资和存档 | 技术设计与实现 |

把“过期一天是否拒绝”改掉，先影响规则；把日期从文字改为数值，先影响实现。两类改动最后都要在可玩流程中检查。

<a id="roles"></a>

### 岗位名称与职责

| 中文 | English | 日本語 | 含义、实例与使用阶段 |
| --- | --- | --- | --- |
| 制作人 | Producer | プロデューサー | 资源、预算、人员、进度和交付协调；公司间职责范围不同。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式新区域增加敌人后，制作人协调动画、程序和测试的时间，判断是否挤压发布日期。<br>用于：前期分工与整个制作过程。 |
| 总监／导演 | Director | ディレクター | 作品方向与主要创作决定，协调各专业形成一致体验。<br><strong>制作例：</strong>[《Return of the Obra Dinn》](https://obradinn.com/)式调查项目中，导演决定哪些信息由画面、对白或玩家推理承担，以保持整体表达一致。<br>用于：前期分工与整个制作过程。 |
| 游戏设计师 | Game Designer | ゲームデザイナー／プランナー | 规则、操作、数值和体验结构；日本的“プランナー”常承担其中部分工作。<br><strong>制作例：</strong>[《Slay the Spire》](https://store.steampowered.com/app/646570/Slay_the_Spire/)式卡牌设计决定费用、伤害和与其他牌的组合；画卡面属于另一项工作。<br>用于：前期分工与整个制作过程。 |
| 关卡设计师 | Level Designer | レベルデザイナー | 路线、障碍、遭遇、引导与空间节奏。<br><strong>制作例：</strong>[《Celeste》](https://www.celestegame.com/)式房间里决定平台距离、危险物和重生点，使玩家能学习并验证一段动作路线。<br>用于：前期分工与整个制作过程。 |
| 叙事设计师／编剧 | Narrative Designer / Writer | ナラティブデザイナー／シナリオライター | 前者侧重故事与交互系统的关系，后者侧重具体文本；职责可以重叠。<br><strong>制作例：</strong>[《Hades》](https://www.supergiantgames.com/games/hades/)式项目中，前者安排死亡后触发哪段关系变化，后者写出角色实际说的话。<br>用于：前期分工与整个制作过程。 |
| 程序员 | Programmer / Engineer | プログラマー／エンジニア | 实现运行系统、工具及各部分连接。<br><strong>制作例：</strong>[《Baba Is You》](https://www.hempuli.com/baba/)式项目中，让移动文字后的新句子真正改变碰撞与胜利条件，并处理冲突。<br>用于：前期分工与整个制作过程。 |
| 美术师／动画师 | Artist / Animator | アーティスト／アニメーター | 制作视觉资源／动作与表演。<br><strong>制作例：</strong>[《Cuphead》](https://cupheadgame.com/)式首领需要造型、关键姿态和连续动作帧；这些工作决定角色怎样被看见。<br>用于：前期分工与整个制作过程。 |
| 技术美术 | Technical Artist — TA | テクニカルアーティスト | 衔接美术与运行要求，处理材质、绑定、工具和资源流程。<br><strong>制作例：</strong>[《Dead Cells》](https://dead-cells.com/)式三维转二维流程需要控制渲染尺度、法线输出与导入规格，这是美术和技术的连接工作。<br>用于：前期分工与整个制作过程。 |
| 作曲／声音设计 | Composer / Sound Designer | 作曲家／サウンドデザイナー | 音乐／声音素材、交互音频与声音表现。<br><strong>制作例：</strong>[《Untitled Goose Game》](https://goose.game/)式项目既要准备钢琴材料，也要组织物件音效随动作触发；写曲与接入可以由不同人承担。<br>用于：前期分工与整个制作过程。 |
| QA／测试人员 | QA / Tester | QA／テスター | 设计检查、复现问题和提供质量信息；具体修复通常交回制作岗位。<br><strong>制作例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)式项目检查雨天、换季和读档是否破坏作物状态，记录可复现步骤交给相应作者。<br>用于：前期分工与整个制作过程。 |

一人可以承担多个岗位。流程仍要保留**决定、制作、检查**三种职责：否则资源虽然完成了，却可能没有人确认它是否适合游戏。前期约定随后进入原型和制作样板，接受实际检验。

<a id="phase-3"></a>

<a id="phase-4"></a>

<a id="milestones"></a>

## 04｜原型与制作样板：验证体验，也验证生产能力

原型回答“这件事是否成立”；制作样板进一步回答“能否以目标品质持续完成”。两者可以使用同一个小项目，但要分别得到体验与生产的结论。

| 中文 | English | 日本語 | 含义、实例与使用阶段 |
| --- | --- | --- | --- |
| 原型 | Prototype | プロトタイプ／試作 | 用较小投入验证玩法、视觉或技术假设；可以保留，也可以完成验证后舍弃。<br><strong>例：</strong>[《Baba Is You》](https://www.hempuli.com/baba/)的 Game Jam 版本已可推动文字改变规则，用很少内容验证了核心关系。[\[5\]](#ref-5)<br>用于：原型与制作样板。 |
| 纸面原型 | Paper Prototype | ペーパープロトタイプ | 用纸张、卡片等模拟规则或界面；适合先检查关系与信息，无法直接证明实时手感。<br><strong>制作例：</strong>用纸卡模拟[《Slay the Spire》](https://store.steampowered.com/app/646570/Slay_the_Spire/)的手牌、费用和敌人意图，先检查一回合是否有值得权衡的选择。<br>用于：原型与制作样板。 |
| 概念验证 | Proof of Concept — PoC | 概念実証 | 侧重方案能否实现，如目标手机是否能加载某种资源；用法与原型可能交叉。<br><strong>制作例：</strong>[《Outer Wilds》](https://www.mobiusdigitalgames.com/outer-wilds.html)式探索项目先测试移动中的星球能否保持角色稳定站立；只验证技术，不代表探索已经有趣。<br>用于：原型与制作样板。 |
| 灰盒／白盒 | Graybox / Whitebox | グレーボックス／ホワイトボックス | 用简单形状验证尺寸、移动和空间关系；名称不强制对应某种颜色。<br><strong>制作例：</strong>[《Celeste》](https://www.celestegame.com/)式房间先只画矩形平台与危险区，用真实跳跃参数测试能否抵达出口。<br>用于：原型与制作样板。 |
| 占位资源 | Placeholder | 仮素材／プレースホルダー | 暂时代替最终图片、模型、声音和文本；需要注明何时替换。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式原型先用色块代表敌人、短声代表受击；色块可被替换，攻击条件仍能先测试。<br>用于：原型与制作样板。 |
| 限时验证 | Timebox | タイムボックス | 先限制投入，到期根据观察决定继续、改方向或停止。<br><strong>制作例：</strong>给[《Baba Is You》](https://www.hempuli.com/baba/)式新规则两天时间试做三道题，到期判断它能否持续产生有意义的谜题。<br>用于：原型与制作样板。 |
| 垂直切片 | Vertical Slice | バーティカルスライス | 小段内容贯通主要系统并接近成品品质，用来验证完整生产流程。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式一间目标品质房间同时接上战斗、美术、声音、界面和存档，用来验证生产成本。<br>用于：原型与制作样板。 |
| 水平切片 | Horizontal Slice | ホリゾンタルスライス | 较广地覆盖系统或流程，但每部分可能仍粗略；具体范围由团队约定。<br><strong>制作例：</strong>[《80 Days》](https://www.inklestudios.com/80days/)式项目先让多座城市、路线、交易和时间都粗略可用，检查系统之间是否连得起来。<br>用于：原型与制作样板。 |
| 质量基准 | Quality Bar | 品質基準 | 可供后续资源对照的完成程度，如代表性场景、角色与声音样板。<br><strong>制作例：</strong>[《Cuphead》](https://cupheadgame.com/)式项目选一段完成的首领动画，供后来动作对照线条、形变与播放节奏。<br>用于：原型与制作样板。 |
| 具备生产条件 | Production-ready | 本制作に移れる状態 | 方法、工具和规格足以支持重复产出；不能只凭一次漂亮演示判断。<br><strong>制作例：</strong>[《Dead Cells》](https://dead-cells.com/)式动作管线能让第二套武器也按相同步骤出图并导入，才证明方法可复用。<br>用于：原型与制作样板。 |
| 演示／试玩版 | Demo | デモ／体験版 | 描述供人体验的用途；可能来自原型或成品片段，成熟度另行说明。<br><strong>例：</strong>[《DOOM》](https://store.steampowered.com/app/379720/DOOM/)商店提供 Demo，让玩家体验选定内容；“可供试玩”说明用途，不等于它必然是早期原型。<br>用于：原型与制作样板。 |
| 最小可行产品 | Minimum Viable Product — MVP | 実用最小限の製品／MVP | 用较小产品检验价值等假设；“可行”必须对应事先设定的验证目标。<br><strong>制作例：</strong>[《A Short Hike》](https://ashorthike.com/)式作品只保留完整登顶体验，用来验证玩家是否愿意探索；地图小仍需有清楚的体验目标。<br>用于：原型与制作样板。 |
| 游戏创作活动 | Game Jam | ゲームジャム | 在限定时间与主题等条件下制作游戏；适合尝试规则，但不自动完成长期生产验证。<br><strong>例：</strong>[《Baba Is You》](https://www.hempuli.com/baba/)从 Game Jam 小作品发展为正式作品；短期验证之后，还要继续设计关卡和生产流程。[\[5\]](#ref-5)<br>用于：原型与制作样板。 |

<a id="prototype-comparison"></a>

### 放在一起看：原型、概念验证、切片与 Demo

以[《Hollow Knight》](https://www.hollowknight.com/)的“跳跃、挥击、穿过相连房间”说明不同验证目的，以下是制作示例。

| 名称 | 可以做出的同一项目片段 | 要得到的结论 |
| --- | --- | --- |
| 原型 Prototype | 几块平台、一个敌人、能跳跃与攻击的角色 | 操作与挑战是否值得继续；美术可以暂缺 |
| 概念验证 PoC | 在目标设备加载大房间，测量内存与换房耗时 | 技术是否能做到；测试通过还不能证明探索有趣 |
| 水平切片 Horizontal Slice | 多个区域、能力与出口先粗略接通 | 各系统和完整路线能否共同工作 |
| 垂直切片 Vertical Slice | 一小段接近目标品质的探索、战斗、美术、声音和存档 | 各工序能否做完、需要多久、能否再做下一段 |
| 试玩版 Demo | 选取适合公开体验的房间，补上操作说明与结束点 | 目标受众能否理解和体验这段内容 |

原型与 PoC 可以重叠；Demo 说明给谁体验，未规定完成度。把切片直接拿去展示也可能成为 Demo，但仍需检查首次进入时的教学与体验边界。

### 同一个问题：正式美术之前，到底先做什么

- [《Splatoon》](https://www.nintendo.com/en-gb/Games/Wii-U-games/Splatoon-892510.html)让玩家喷墨争夺地面，并在自己的墨水里移动与隐藏。早期用黑白方块测试喷墨和地面占领；俯视时，方块会融进同色墨水，转成三维视角后却仍显眼，于是团队继续尝试伏低、潜入等方式，后来发展为鱿鱼形态。**这里先验证“涂地—隐藏—移动”的关系，角色造型跟着规则发展。**[\[4\]](#ref-4)
- [《Baba Is You》](https://www.hempuli.com/baba/)是推箱式解谜，地图里的文字也能推动。`WALL IS STOP` 让墙阻挡移动，把句子拆开就会改变规则。作者保留的 Game Jam 版本已经能让人尝试这种关系。**这里最先需要的是“文字变化确实改变世界”的可玩谜题**；更多关卡是在已经能操作的关系上扩展。[\[5\]](#ref-5)
- [《A Short Hike》](https://ashorthike.com/)要让玩家在小岛上自由游走并登顶。作者从新原型出发，在较短期限内共同调整移动、岛屿、美术与写作。**这类项目需要及早把移动与空间放在一起试**：一个动作单独顺畅，还不能说明整座岛是否值得探索。[\[1\]](#ref-1)

三者的验证对象分别是**规则之间的关系、可改写的规则、移动与空间体验**。原型据此选最少资源；切片再补上目标画面、声音、界面与存档。切片完成后做第二个同类场景，才能更可靠地估算复用和返工成本。

<a id="runtime"></a>

## 05｜程序与运行：输入怎样变成结果

程序把玩家输入、当前状态、规则和资源连接起来。例如按下“交谈”，先检查是否已经在对白中，再选择文本、显示角色动作，并记录需要长期保存的结果。具体语言和工具见 [002](posts-2026-umwelt-game-development-handbook-002.html#tools-03)。

| 中文 | English | 日本語 | 含义、实例与使用阶段 |
| --- | --- | --- | --- |
| 游戏引擎 | Game Engine | ゲームエンジン | 提供图形、输入、音频、场景等基础能力，项目继续实现自己的规则。<br><strong>例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)把手绘资源交给 Unity，组织显示、交互等能力；Photoshop 则负责制作图像。[\[6\]](#ref-6)<br>用于：前期选型与整个制作过程。 |
| 编辑器／运行时 | Editor / Runtime | エディター／ランタイム | 制作与调试界面／成品执行的程序部分；玩家通常无需安装制作编辑器。<br><strong>制作例：</strong>在编辑器摆放[《Hollow Knight》](https://www.hollowknight.com/)式洞穴，玩家运行成品时探索洞穴；制作界面和成品执行环境职责不同。<br>用于：程序实现与集成。 |
| 框架／程序库 | Framework / Library | フレームワーク／ライブラリ | 框架进一步组织程序结构，库提供可调用功能；具体边界依产品而异。<br><strong>例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)PC 版曾迁到 MonoGame；框架提供运行基础，农作和日历等作品规则仍由项目组织。[\[15\]](#ref-15)<br>用于：技术选型与程序实现。 |
| 脚本 | Script | スクリプト | 表达规则或制作自动化的程序；不是所有脚本都在玩家端运行。<br><strong>制作例：</strong>[《80 Days》](https://www.inklestudios.com/80days/)式故事脚本写“钱足够才显示乘车选项”；批量检查对白编号的脚本则只在制作时使用。<br>用于：程序实现与集成。 |
| 变量类型／数据结构 | Data Type / Data Structure | データ型／データ構造 | 数值、文字等值的类别／组织数据的方法；物品表、背包列表和地图关系会采用不同结构。<br><strong>制作例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)式农场用数值表示天数，用列表组织背包，用位置与记录对应田块；结构跟随要处理的关系。<br>用于：程序实现与集成。 |
| 函数／方法 | Function / Method | 関数／メソッド | 可调用的一组操作／与对象或类型关联的操作；参数是输入，返回值是结果。<br><strong>制作例：</strong>[《Papers, Please》](https://papersplea.se/)式“检查证件是否过期”接收证件日期与当前日期，返回判断结果，供多种证件复用。<br>用于：程序实现与集成。 |
| 类／实体组件系统 | Class / Entity Component System — ECS | クラス／エンティティ・コンポーネント・システム | 类描述对象的数据与行为；ECS 将实体、组件数据与处理系统分开，是另一种组织方式。<br><strong>制作例：</strong>[《Brotato》](https://store.steampowered.com/app/1942280/Brotato/)式大量敌人可按对象类组织，也可按位置、生命等组件与处理系统组织；这是实现方案比较。<br>用于：程序实现与集成。 |
| 编译／解释 | Compilation / Interpretation | コンパイル／インタープリター実行 | 将代码转换为另一种可执行形式／由运行程序解释执行；实际环境可以混合采用。<br><strong>制作例：</strong>[《Baba Is You》](https://www.hempuli.com/baba/)式项目的开发代码先经过工具处理，游戏里的“BABA IS YOU”又由自设规则解释；两层语言不要混淆。<br>用于：程序实现与集成。 |
| 依赖包／插件 | Package / Plugin | パッケージ／プラグイン | 可复用的代码或资源单元／扩展宿主能力的组件；升级要核对接口和许可。<br><strong>例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)使用 PlayMaker 辅助组织行为；更新这类插件时，要检查已有敌人与交互仍能工作。[\[6\]](#ref-6)<br>用于：技术选型、集成与维护。 |
| 游戏循环 | Game Loop | ゲームループ | 程序反复处理输入、更新状态并准备画面的执行过程；与“核心循环”的设计含义不同。<br><strong>制作例：</strong>[《Celeste》](https://www.celestegame.com/)式程序反复读取跳跃输入、更新位置、检测碰撞和呈现画面；“失败再挑战”属于玩法循环。<br>用于：程序实现与集成。 |
| 帧／模拟步 | Frame / Tick | フレーム／ティック | 一次画面更新／一次逻辑模拟更新；两者频率可以不同。<br><strong>例：</strong>[《Cuphead》](https://cupheadgame.com/)手绘动画采用每秒 24 帧的节奏，游戏画面以 60 FPS 运行；动画帧数与显示帧率不同。制作时还要另定物理、规则的模拟步频。[\[7\]](#ref-7)<br>用于：程序实现与集成。 |
| 帧间隔 | Delta Time | デルタタイム／経過時間 | 两次更新的时间差；用于把每秒速度换算成当前更新的移动量。<br><strong>制作例：</strong>[《A Short Hike》](https://ashorthike.com/)式移动若按每秒速度计算，应根据本次间隔换算位移，避免机器帧率改变行走速度。<br>用于：程序实现与集成。 |
| 对象／组件 | Object / Component | オブジェクト／コンポーネント | 对象表示游戏中的事物，组件承担显示、碰撞等部分能力；组织方式随引擎而异。<br><strong>制作例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)式作物对象可由显示、成长、可收获等部分组成；某一部分改变，不必重写整棵作物。<br>用于：程序实现与集成。 |
| 场景／节点 | Scene / Node | シーン／ノード | 组织对象与关系的单位；Godot、Unity 等对“场景”的具体定义不同。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式房间可以组织平台、敌人和出口；进入另一房间时，需要接好出口关系与状态。<br>用于：程序实现与集成。 |
| 实例／预制体 | Instance / Prefab | インスタンス／プレハブ | 由定义创建的具体对象／可重复生成对象结构的模板；Prefab 常见于 Unity。<br><strong>制作例：</strong>[《Brotato》](https://store.steampowered.com/app/1942280/Brotato/)式敌人模板规定外观和基本行为，生成的每只敌人各有位置与生命；模板与实例分别修改。<br>用于：程序实现与集成。 |
| 状态／变量 | State / Variable | 状態／変数 | 当前情况／保存某项值的名称；例如是否拿过钥匙、当前生命值。<br><strong>例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)同一田块可能未种植、已播种、已浇水或已成熟；设计时把这些情况及转换条件明确列出。<br>用于：程序实现与集成。 |
| 有限状态机 | Finite State Machine — FSM | 有限状態機械／ステートマシン | 用有限状态及转换组织行为，如待机→交谈→选择→结束。<br><strong>制作例：</strong>[《Untitled Goose Game》](https://goose.game/)式村民可在“做事—发现鹅—追赶—返回”之间转换；每段状态只接受约定事件。<br>用于：程序实现与集成。 |
| 事件／回调 | Event / Callback | イベント／コールバック | 发生某件事的通知／相应时机调用的处理；常用于连接动画、界面与规则。<br><strong>制作例：</strong>[《Celeste》](https://www.celestegame.com/)式角色落地发出事件，声音与尘土效果分别响应；不必把所有处理写在一个动作里。<br>用于：程序实现与集成。 |
| 接口／开发工具包 | Application Programming Interface — API / Software Development Kit — SDK | API／ソフトウェア開発キット | 软件调用的约定／接入某种能力的工具和组件集合。<br><strong>制作例：</strong>[《Slay the Spire》](https://store.steampowered.com/app/646570/Slay_the_Spire/)式项目要在商店显示成就，SDK 提供接入组件，API 规定怎样提交“某成就完成”的调用。<br>用于：程序实现与集成。 |
| 中间件 | Middleware | ミドルウェア | 提供音频、物理等专门运行能力，接入引擎或项目。<br><strong>例：</strong>[《Untitled Goose Game》](https://goose.game/)用 FMOD 接入动态声音；它承担音频专门工作，完整玩法仍由游戏系统组织，详见 [002 声音案例](posts-2026-umwelt-game-development-handbook-002.html#audio-cases)。<br>用于：程序实现与集成。 |
| 序列化／存档 | Serialization / Save Data | シリアライズ／セーブデータ | 把状态转成可保存格式／保存需要延续的游玩情况；两者并非同义。<br><strong>制作例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)式项目先决定保存日期、背包与田块，再把数据写成文件；格式转换与保存哪些意义分开。<br>用于：前期数据设计、实现与维护。 |
| 稳定标识 | Stable ID | 永続的な識別子 | 在修改名称或顺序后仍能识别同一内容的编号；用于文本、资源和存档引用。<br><strong>制作例：</strong>[《80 Days》](https://www.inklestudios.com/80days/)式文本翻译后改了句子，仍用同一编号关联配音、条件和存档，而非把原句当永久键。<br>用于：前期数据设计、内容制作与维护。 |
| 缓存／对象池 | Cache / Object Pool | キャッシュ／オブジェクトプール | 复用计算或加载结果／复用已经创建的对象，以减少重复工作。<br><strong>制作例：</strong>[《Brotato》](https://store.steampowered.com/app/1942280/Brotato/)式游戏可复用已经读取的纹理，也可复用离场后闲置的弹丸对象；两种复用的对象不同。<br>用于：程序实现与性能优化。 |
| 异步加载 | Asynchronous Loading | 非同期ロード | 资源准备与其他工作交错进行；还需安排等待、失败和资源就绪后的行为。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式换房时可提前准备下一房资源；未准备好时仍要明确等待、取消和失败怎么显示。<br>用于：程序实现与性能优化。 |
| 刚体／触发区域 | Rigid Body / Trigger | 剛体／トリガー | 参与物理运动与碰撞的对象／进入或离开时发出事件的区域；触发区域不一定阻挡移动。<br><strong>制作例：</strong>[《Portal 2》](https://www.thinkwithportals.com/about.php)式方块需要与地面发生物理接触；走到出口触发区域则可只通知流程，不必形成一堵墙。<br>用于：程序实现与集成。 |
| 射线检测 | Raycast | レイキャスト | 沿指定方向查询命中物体，用于指向选择、落地检测或视线判断等。<br><strong>制作例：</strong>[《Minecraft》](https://www.minecraft.net/en-us/about-minecraft)式准星沿视线查询最近可选方块，得到目标位置后再决定放置或破坏。<br>用于：程序实现与集成。 |
| 人工智能／非玩家角色 | Artificial Intelligence — AI / Non-player Character — NPC | 人工知能／ノンプレイヤーキャラクター | 游戏中用于感知和决策的方法／非玩家直接操控的角色；简单角色也可只用固定规则。<br><strong>例：</strong>[《Untitled Goose Game》](https://goose.game/)的村民会对鹅的行为作出反应；制作时把“看见什么、决定什么、怎样行动”拆开。<br>用于：程序实现与集成。 |
| 确定性 | Determinism | 決定性 | 在相同起始条件和输入下得到相同结果；用于复现、回放和某些联机方案。<br><strong>例：</strong>[《Factorio》](https://www.factorio.com/)多人模拟需要各端在相同条件和输入下保持结果一致；相同画面外观并不足以证明内部状态相同。[\[20\]](#ref-20)<br>用于：联机设计、复现与回放。 |
| 客户端／服务端 | Client / Server | クライアント／サーバー | 玩家端／提供服务与协作的端；单机网页也可由服务器分发文件。<br><strong>例：</strong>[《Minecraft》](https://www.minecraft.net/en-us/about-minecraft)多人服务器保存共享世界并协调连接，各玩家客户端显示自己的视角；具体架构依版本与模式。<br>用于：程序实现与集成。 |
| 权威状态 | Authoritative State | 権威を持つ状態／正とする状態 | 多端出现分歧时，以谁的判断为准；常由服务端承担，也有其他架构。<br><strong>制作例：</strong>[《Minecraft》](https://www.minecraft.net/en-us/about-minecraft)式联机中两人同时拾取同一物品，必须约定哪一端决定最终归属，避免两人都拿到。<br>用于：联机架构设计、实现与测试。 |
| 同步／不同步 | Synchronization / Desync | 同期／同期ずれ | 各端保持约定状态一致／计算或数据出现分歧。<br><strong>例：</strong>[《Factorio》](https://www.factorio.com/)某端机器状态与其他端分歧，会出现不同步；需要检查状态与输入，不能只观察网络是否连接。[\[20\]](#ref-20)<br>用于：联机实现与测试。 |
| 延迟／预测／回滚同步 | Latency / Prediction / Rollback Netcode | 遅延／予測／ロールバック方式 | 信息到达需时间；预测先估计结果，回滚方案在收到实际输入后恢复并重算。<br><strong>制作例：</strong>把[《Celeste》](https://www.celestegame.com/)式跳跃做成双人联机，预测可先估计远端动作；收到不同输入后回滚重算，这是示意方案。<br>用于：程序实现与集成。 |

<a id="objects-comparison"></a>

### 放在一起看：对象、组件、预制体、实例与状态

[《Brotato》](https://store.steampowered.com/app/1942280/Brotato/)让角色在一波波敌人中移动、生存。以其中一种敌人为参照，制作时可以这样组织；这不说明原作代码采用该结构。

| 词 | 放在同一种敌人上理解 |
| --- | --- |
| 对象 Object | 程序中代表一只敌人的事物，可以有位置、显示和行为 |
| 组件 Component | 负责显示、移动、生命等工作的部分；“生命组件”只承担其中一项能力 |
| 预制体 Prefab | 约定该类敌人的外观、组件和初始参数，供反复创建；不同引擎的模板名称与机制不同 |
| 实例 Instance | 这次实际出现的某一只敌人；两只来自同一模板，也可以在不同位置、剩余不同生命 |
| 状态 State | 这只敌人目前在追赶、受击还是死亡；通常由多个变量共同表达 |

**缓存与对象池**也可用同一场景区别：多只敌人共用已读取的纹理，是复用资源；弹丸离场后保留对象，下次重设位置再用，是复用实例。两者都用于减少重复工作，需要分别检查资源占用和状态重置。

### 同一个问题：“这次做过的事”需要记住多少

| 游戏与情境 | 哪些继续，哪些重置 | 对设计和实现的含义 |
| --- | --- | --- |
| [《Baba Is You》](https://www.hempuli.com/baba/)：推动文字后发现自己走错了 | 撤销让局部操作退回之前的状态，玩家可立即尝试别的排列 | 重点是能恢复当前谜题的操作过程；试验成本低，便于探索规则 |
| [《Hades》](https://www.supergiantgames.com/games/hades/)：一次逃脱挑战失败 | 本轮战斗配置与长期成长、人物关系分别处理；返回据点后再出发 | “当前这一轮”和“整个存档”需要不同状态范围；失败仍可以带来长期进展 |
| [《星露谷物语》](https://www.stardewvalley.net/)：结束一天后继续经营 | 农场、物品、日期和关系延续到之后的日子 | 状态之间相互关联，修改作物、时间或人物条件时需要检查已有进度 |

这些是玩法层面的状态比较，不据此推断作品的实际代码结构。实现时先决定需要保留的意义，再选存储方式。

[《Factorio》](https://www.factorio.com/)则提供了有开发记录的联机例子：玩家共同建设包含大量机器的工厂。其确定性锁步方案交换输入，让各端按同一规则推进模拟；只要某端计算出现差异，就可能不同步，需要日志和状态对比定位原因。[\[20\]](#ref-20) 这说明“联网”可能改变整个状态验证方法，不能只理解为多加一个房间按钮。

<a id="visual-production"></a>

## 06｜美术与资源：从可编辑内容到游戏画面

美术阶段先确定目标镜头、轮廓、色彩与信息层次，再制作和导出。检查资源时同时看源工程与游戏里的实际显示；导出文件通常只保留源工程中的一部分能力。

### 二维图像与视觉组织

| 中文 | English | 日本語 | 含义、实例与使用阶段 |
| --- | --- | --- | --- |
| 概念美术 | Concept Art | コンセプトアート | 探索造型、氛围和方向的图像；不一定直接作为运行资源。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式区域先比较蘑菇森林和矿洞的形状、色彩与氛围，再决定要生产哪些场景资源。<br>用于：前期美术探索。 |
| 视觉参考板 | Mood Board / Reference Board | ムードボード／リファレンスボード | 把相关形状、材料、色彩与资料放在一起比较，保留来源与用途。<br><strong>制作例：</strong>[《Cuphead》](https://cupheadgame.com/)式角色可并置早期卡通姿态、墨线和配色参考，用来比较方向；参考图不自动成为可用素材。<br>用于：前期视觉探索与外包沟通。 |
| 资源／源工程 | Asset / Source Project | アセット／制作元データ | 游戏使用的内容／保留图层、节点等编辑能力的文件。<br><strong>例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)的 PNG 是进入游戏的图像；包含绘画图层的制作文件保留修改能力，二者用途不同。[\[6\]](#ref-6)<br>用于：资源制作、交接与归档。 |
| 位图／矢量图 | Raster / Vector | ラスター／ベクター | 以像素保存画面／以曲线和形状保存图形；缩放与编辑方式不同。<br><strong>制作例：</strong>[《Papers, Please》](https://papersplea.se/)式证件里的照片适合位图，印章轮廓可用矢量制作，再按目标端支持导出。<br>用于：美术制作与资源导入。 |
| 像素画 | Pixel Art | ドット絵／ピクセルアート | 在有限像素尺度上控制形状、色彩和边缘；低分辨率显示本身不等于经过像素设计。<br><strong>例：</strong>[《Celeste》](https://www.celestegame.com/)人物与平台在小尺度里依靠像素轮廓被辨认；制作时要在实际显示尺寸检查动作与边界。<br>用于：美术制作与资源导入。 |
| 调色板／抖色 | Palette / Dithering | パレット／ディザリング | 使用的颜色集合／用颜色排列模拟过渡；影响清晰度与纹理感。<br><strong>制作例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)式草地先约定几种绿，再决定是否用交错像素过渡；增加颜色与排列已有颜色是不同操作。<br>用于：美术制作与资源导入。 |
| 精灵／精灵表 | Sprite / Sprite Sheet | スプライト／スプライトシート | 游戏中的二维图像表现／把多个帧或图像排列在同一张图里。<br><strong>制作例：</strong>[《Celeste》](https://www.celestegame.com/)式角色跑步可有多张帧，精灵表把这些帧排列在一张图里；运行时按顺序取区域显示。<br>用于：美术制作与资源导入。 |
| 纹理图集 | Texture Atlas | テクスチャアトラス | 将多个纹理区域合并并记录位置；减少切换的效果需结合实际渲染方式判断。<br><strong>制作例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)式菜单把许多物品小图放进图集，并记录区域；合并图片后仍要保留每个物品的对应关系。<br>用于：美术制作与资源导入。 |
| 图块／图块地图 | Tile / Tilemap | タイル／タイルマップ | 可重复使用的小块图像／用排列与数据组成的地图。<br><strong>制作例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)式道路用少量直线、拐角和边缘图块反复拼接；地图数据记录这些块放在哪儿。<br>用于：美术制作与资源导入。 |
| 基点 | Pivot / Origin | ピボット／原点 | 对齐、旋转或放置资源时的参考位置；各帧不一致会造成抖动。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式角色站立和挥击图像都以脚底对齐，换帧才不会无故上下跳动。<br>用于：美术制作与资源导入。 |
| 透明通道 | Alpha Channel | アルファチャンネル | 表示透明程度；透明边缘需要与过滤、背景一起检查。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式角色 PNG 周围保留透明，才能叠在不同洞穴背景上；半透明边缘要检查是否有白边。<br>用于：美术制作与资源导入。 |
| 最近邻／线性过滤 | Nearest / Linear Filtering | 最近傍／線形フィルタリング | 纹理采样方法；前者保留硬像素边界，后者混合邻近颜色。<br><strong>制作例：</strong>放大[《Celeste》](https://www.celestegame.com/)式像素帧时，最近邻保留格子边界，线性过滤会混合相邻像素；按目标画面选择。<br>用于：美术制作与资源导入。 |
| 九宫格缩放 | Nine-slice | 9スライス | 分开处理面板四角、边缘与中心，改变大小时保留边框形状。<br><strong>制作例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)式物品说明框变长时，只拉伸中部和边，保留四角装饰，避免整个边框被拉扁。<br>用于：美术制作与资源导入。 |
| 视差 | Parallax | パララックス／視差 | 不同深度层以不同速度移动，制造空间感；常见于二维背景。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式洞穴前景移动快、远景移动慢，可以让平面分层产生距离感；速度关系由镜头设计决定。<br>用于：美术制作与资源导入。 |

### 三维形体、表面与渲染

| 中文 | English | 日本語 | 含义、实例与使用阶段 |
| --- | --- | --- | --- |
| 网格／多边形 | Mesh / Polygon | メッシュ／ポリゴン | 由顶点、边和面构成的几何形状；多边形数量只是资源成本的一部分。<br><strong>制作例：</strong>[《A Short Hike》](https://ashorthike.com/)式山体可由顶点和面形成轮廓；画在表面的岩石纹理本身不会增加几何凹凸。<br>用于：美术制作与资源导入。 |
| 拓扑／重拓扑 | Topology / Retopology | トポロジー／リトポロジー | 几何连接结构／重新组织连接；影响变形、编辑与运行效率。<br><strong>制作例：</strong>[《Untitled Goose Game》](https://goose.game/)式鹅颈弯曲时，需要适合变形的几何连接；雕刻很细仍可能要重新组织网格。<br>用于：美术制作与资源导入。 |
| 雕刻 | Sculpting | スカルプト | 以推拉、刻画等方式塑造形体；精细结果常需后续整理。<br><strong>制作例：</strong>[《Baldur’s Gate 3》](https://baldursgate3.game/)式角色可先雕出面部体积与褶皱，再为游戏整理拓扑、贴图和运行模型；这是一般制作示例。<br>用于：美术制作与资源导入。 |
| UV 展开 | UV Unwrapping | UV展開 | 建立模型表面与二维纹理位置的对应；需要处理接缝、拉伸和重叠。<br><strong>制作例：</strong>给[《Minecraft》](https://www.minecraft.net/en-us/about-minecraft)式方块角色画衣服，要把模型各面对应到二维贴图位置，避免袖子花纹落到脸上。<br>用于：美术制作与资源导入。 |
| 纹理／材质／着色器 | Texture / Material / Shader | テクスチャ／マテリアル／シェーダー | 图像或采样数据／表面显示参数组合／计算显示结果的程序；三者相互配合。<br><strong>制作例：</strong>[《Portal 2》](https://www.thinkwithportals.com/about.php)式金属方块，划痕图片是纹理，粗糙度等组合是材质设置，计算反光的程序是着色器。<br>用于：美术制作与资源导入。 |
| 基础色／粗糙度／金属度 | Base Color / Roughness / Metallic | ベースカラー／粗さ／メタリック | 常见表面参数；分别参与底色、反射散布和金属表面的描述。<br><strong>制作例：</strong>同一个[《Portal 2》](https://www.thinkwithportals.com/about.php)式金属道具只换底色，未必像塑料；表面反射还与粗糙度、金属度有关。<br>用于：美术制作与资源导入。 |
| 法线／法线贴图 | Normal / Normal Map | 法線／法線マップ | 表面朝向／用纹理改变受光计算中的方向；通常不会改变物体外轮廓。<br><strong>例：</strong>[《Dead Cells》](https://dead-cells.com/)输出法线图辅助二维角色受光；衣物看起来有起伏，不代表外轮廓随之改变。[\[8\]](#ref-8)<br>用于：美术制作与资源导入。 |
| 基于物理的渲染 | PBR — Physically Based Rendering | 物理ベースレンダリング | 用较一致的表面与光照模型组织材质；仍需要正确资源、参数和艺术选择。<br><strong>制作例：</strong>[《Baldur’s Gate 3》](https://baldursgate3.game/)式盔甲和皮革可用一致的光照模型表现不同反射；统一模型仍需各自正确的表面参数。<br>用于：美术制作与资源导入。 |
| 烘焙 | Baking | ベイク／ベイキング | 把部分计算提前写进资源，如法线、光照或动画数据；与现场实时计算分工。<br><strong>制作例：</strong>[《Baldur’s Gate 3》](https://baldursgate3.game/)式高精度雕刻的凹凸可预先转入法线图，让较简模型使用；需检查结果是否与目标模型匹配。<br>用于：美术制作与资源导入。 |
| 环境遮蔽 | Ambient Occlusion — AO | アンビエントオクルージョン | 表现局部遮挡带来的明暗线索；不能替代所有照明和接触阴影。<br><strong>制作例：</strong>[《Portal 2》](https://www.thinkwithportals.com/about.php)式箱子角落与接触地面处可补充遮挡明暗线索；主光照和真实投影仍需分别安排。<br>用于：美术制作与资源导入。 |
| 细节层级 | Level of Detail — LOD | 詳細度レベル／LOD | 按距离等条件使用不同精度资源，降低运行开销并控制切换观感。<br><strong>制作例：</strong>[《A Short Hike》](https://ashorthike.com/)式岛上远树可比近树更简，靠近时切换；检查切换是否跳变，以及是否真正节省开销。<br>用于：模型制作与性能优化。 |
| 剔除 | Culling | カリング | 跳过当前不需要处理或绘制的对象；如视野之外或被遮挡的内容。<br><strong>制作例：</strong>[《Minecraft》](https://www.minecraft.net/en-us/about-minecraft)式世界中视野外的区域可不绘制；是否仍计算其中活动，要由模拟规则另行决定。<br>用于：场景实现与性能优化。 |
| 实时／预渲染 | Real-time / Pre-rendered | リアルタイム／プリレンダリング | 运行时计算画面／提前输出图像或视频；自由视角与交互能力不同。<br><strong>例：</strong>[《Dead Cells》](https://dead-cells.com/)把三维动作提前输出成二维帧；[《Outer Wilds》](https://www.mobiusdigitalgames.com/outer-wilds.html)飞船视角会随玩家转动，需要运行中生成相应画面。<br>用于：美术制作与资源导入。 |
| 后期处理 | Post-processing | ポストプロセス | 对画面进一步处理，如调色、泛光和景深；需要检查文字与交互物可读性。<br><strong>制作例：</strong>[《Return of the Obra Dinn》](https://obradinn.com/)式画面可讨论有限明暗如何保持线索可读；效果处理后，衣饰与人物轮廓仍必须能分辨。<br>用于：美术制作与资源导入。 |
| 色彩空间 | Color Space | 色空間 | 对颜色数值的解释方式；颜色贴图与法线等数据纹理通常采用不同设置。<br><strong>制作例：</strong>[《Portal 2》](https://www.thinkwithportals.com/about.php)式方块的颜色图表示颜色，法线图表示方向数据；以同一颜色转换处理两者可能得到错误表面。<br>用于：资源制作、导入与渲染检查。 |
| 抗锯齿 | Anti-aliasing — AA | アンチエイリアシング | 减轻采样造成的阶梯边缘与闪烁；不同方法在清晰度、拖影和性能间取舍。<br><strong>制作例：</strong>[《A Short Hike》](https://ashorthike.com/)式远处山脊移动时可能出现边缘闪烁；减少闪烁与保留清晰轮廓需要同时比较。<br>用于：美术制作与资源导入。 |
| 光照贴图／反射探针 | Lightmap / Reflection Probe | ライトマップ／リフレクションプローブ | 保存预计算光照／采样环境反射信息；场景或物体变化后可能需要更新。<br><strong>制作例：</strong>[《Portal 2》](https://www.thinkwithportals.com/about.php)式固定房间可预先保存部分照明，反射探针采样周围环境；移动门和人物还需相应动态处理。<br>用于：美术制作与资源导入。 |
| 正交／透视投影 | Orthographic / Perspective Projection | 平行投影／透視投影 | 远近不改变投影比例／远处物体显得更小；影响空间阅读和资源制作。<br><strong>制作例：</strong>制作[《星露谷物语》](https://www.stardewvalley.net/)式俯视格子图时可避免远近缩小；[《Outer Wilds》](https://www.mobiusdigitalgames.com/outer-wilds.html)驾驶飞船观察远处行星则有明显透视关系。<br>用于：美术制作与资源导入。 |
| 分辨率／纹素密度 | Resolution / Texel Density | 解像度／テクセル密度 | 图像像素数量／模型单位长度对应多少纹理像素；影响细节与一致性。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式角色图片的像素数与屏幕占用共同影响清晰度；三维场景还要看每米表面分到多少纹理像素。<br>用于：美术制作与资源导入。 |

<a id="surface-comparison"></a>

### 放在一起看：网格、碰撞体、UV、纹理、材质与着色器

以[《Portal 2》](https://www.thinkwithportals.com/about.php)中可搬动、可压住按钮的方块为参照，下面说明常见制作分工。

| 词 | 在同一个方块上负责什么 | 改错时会看到什么 |
| --- | --- | --- |
| 网格 Mesh | 顶点和面形成可见形体 | 方块的轮廓或表面形状不对 |
| 碰撞体 Collider | 供物理系统判断接触与阻挡的形状 | 看似贴着地面却悬空，或身体穿进外壳 |
| UV | 规定模型表面怎样对应到二维图片 | 图案跑错面、拉伸或接缝明显 |
| 纹理 Texture | 提供颜色、划痕、法线等图像或数据 | 图案内容、细节或方向不对 |
| 材质 Material | 组织着色器、纹理及表面参数 | 图案对了，但表面光泽或粗糙感不合适 |
| 着色器 Shader | 计算像素怎样受光、混合并输出 | 需要的显示方式无法仅靠更换图片得到 |

这些问题主要在**建模、贴图、资源接入与渲染检查**中交叉处理。法线图能改变受光细节，通常不会改变模型轮廓或碰撞形状；碰撞也不会因为画出一条缝就自动出现开口。

### 同一个问题：怎样持续制作大量二维动作

| 游戏、画面与动作需求 | 采用的路径与理由 | 结果及修改时的差异 |
| --- | --- | --- |
| [《Hollow Knight》](https://www.hollowknight.com/)：虫形角色在洞穴中跑跳、挥武器和战斗 | 用 Photoshop 手绘动画，再把 PNG 接入 Unity；团队利用现成功能，把更多精力放在擅长的美术上 | 轮廓和姿态由二维绘制直接控制；改姿态要回到画稿和动画帧。[\[6\]](#ref-6) |
| [《Cuphead》](https://cupheadgame.com/)：杯头角色与夸张变形的敌人进行横向射击战斗 | 纸上绘制动画，再数字上色。团队明确希望通过传统方法接近 1930 年代动画的表现 | 动作的形变与笔触成为风格的一部分，新增或大改动作会影响连续绘制工序。[\[7\]](#ref-7) |
| [《Dead Cells》](https://dead-cells.com/)：像素外观角色频繁更换武器、近身攻击和闪避 | 在三维中制作模型和动作，再转成小尺寸帧。美术师需要在有限人力下快速修改招式 | 调整攻击速度可移动关键帧后重新输出，装备和模型也可复用；小尺寸像素结果仍需检查。[\[8\]](#ref-8) |

三者最终都能用二维帧显示，差别在**姿态从哪里来、什么最值得保留、修改要返回哪个环节**。具体软件职责见 [002 的二维案例](posts-2026-umwelt-game-development-handbook-002.html#art-cases)。

<a id="levels-animation"></a>

## 07｜关卡、动画与表现：让空间和动作能够游玩

环境美术安排可见内容，关卡设计安排路线、目标、障碍与节奏；动画展示动作，规则决定动作何时生效。两组工作都需要在游戏中相互检查。

### 空间与引导

| 中文 | English | 日本語 | 含义、实例与使用阶段 |
| --- | --- | --- | --- |
| 关卡设计 | Level Design | レベルデザイン | 安排空间、遭遇、引导和挑战顺序；关卡不一定是一张独立地图。<br><strong>例：</strong>[《Celeste》](https://www.celestegame.com/)同样的跳跃动作，配上不同平台距离、危险物和出口位置，就成为不同挑战。<br>用于：原型、正式制作与试玩。 |
| 场景布置 | Scene Assembly / Set Dressing | シーン構築／セットドレッシング | 把环境与装饰资源组成画面；装饰可能影响视线、遮挡和碰撞。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式洞穴摆好石柱和植物后，还要确认它们是否遮住敌人、出口或可站立平台。<br>用于：关卡、动画制作与调试。 |
| 粗搭 | Blockout | ブロックアウト | 用简单体块搭建空间，先验证尺度与通行，再细化美术。<br><strong>制作例：</strong>[《Portal 2》](https://www.thinkwithportals.com/about.php)式谜题先用简单房间、按钮和方块跑通因果，再细化墙面与灯光。<br>用于：原型与关卡设计。 |
| 关键路线／支路 | Critical Path / Optional Path | 必須ルート／寄り道 | 完成主要目标所需路线／可选择的探索路线；此处 Critical Path 指游玩路径。<br><strong>例：</strong>[《A Short Hike》](https://ashorthike.com/)以登顶为主目标，沿途收集与相遇允许偏离；支路应能被理解为有意义的选择。<br>用于：关卡、动画制作与调试。 |
| 地标／视线 | Landmark / Sightline | ランドマーク／視線 | 易识别的参照物／玩家从某处能看到的范围；共同支持方向判断。<br><strong>例：</strong>[《A Short Hike》](https://ashorthike.com/)山峰提供远处方向；布置地形时要检查玩家从常见位置是否能看见目标。<br>用于：关卡、动画制作与调试。 |
| 引导／新手教学 | Guidance / Onboarding | 誘導／導入・チュートリアル | 帮助玩家发现目标、学习操作和理解反馈；可通过布局、情境或提示完成。<br><strong>例：</strong>[《Portal 2》](https://www.thinkwithportals.com/about.php)让玩家用传送门解决空间问题；制作同类教学时先安排单一关系，再组合新的障碍。<br>用于：原型、关卡设计与试玩。 |
| 进度门槛 | Gating | ゲーティング／進行制限 | 通过能力、钥匙、知识或任务条件限制推进；门槛应有可理解的解除方式。<br><strong>例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)一些路线需要后来取得的移动能力；设计要检查玩家是否理解“现在到不了，之后可回来”。<br>用于：关卡、动画制作与调试。 |
| 检查点 | Checkpoint | チェックポイント | 失败后恢复的位置或状态；间距决定重复劳动和失败成本。<br><strong>例：</strong>[《Celeste》](https://www.celestegame.com/)失败后通常很快回到当前挑战附近；重试位置直接决定玩家要重复多少已会的动作。<br>用于：关卡、动画制作与调试。 |
| 节奏 | Pacing | ペーシング／緩急 | 挑战、休息、探索、叙事在时间上的安排。<br><strong>例：</strong>[《Hades》](https://www.supergiantgames.com/games/hades/)战斗与返回据点的交谈形成不同强度；连续挑战之间的间隔也属于内容安排。<br>用于：关卡、动画制作与调试。 |
| 遭遇设计 | Encounter Design | エンカウンターデザイン | 安排某段战斗或互动中的对象、空间、行为和时序。<br><strong>制作例：</strong>[《Hades》](https://www.supergiantgames.com/games/hades/)式房间中近战敌人、远程攻击与地形一起改变走位；只增加敌人数量未必产生好挑战。<br>用于：关卡、动画制作与调试。 |
| 导航网格／寻路 | NavMesh / Pathfinding | ナビメッシュ／経路探索 | 可通行区域表示／查找路线的方法；角色为什么移动还由行为系统决定。<br><strong>制作例：</strong>[《Untitled Goose Game》](https://goose.game/)式村民追赶鹅时，寻路查找绕开障碍的路线；是否继续追赶属于行为决策。<br>用于：关卡、动画制作与调试。 |
| 行为树 | Behavior Tree | ビヘイビアツリー／行動木 | 用条件与动作组织角色决策；与实际移动、动画和感知相连接。<br><strong>制作例：</strong>[《Untitled Goose Game》](https://goose.game/)式村民可先判断重要物品是否丢失，再判断是否看见鹅，选择寻找、追赶或返回；这是一种实现方案。<br>用于：关卡、动画制作与调试。 |

### 放在一起看：导航、寻路与行为决策

以[《Untitled Goose Game》](https://goose.game/)里村民追赶鹅为参照，制作时分清三件事：

| 工作 | 具体负责什么 | 对应词 |
| --- | --- | --- |
| 表示可走的地方 | 标出地面、门口等可通行区域 | 导航网格 Navmesh；也可使用格子或其他表示 |
| 找到怎么过去 | 从村民位置找一条绕开桌子、抵达目标的路线 | 寻路 Pathfinding |
| 决定要不要过去 | 鹅已离开视野，是继续追、找回物品还是返回工作 | 状态机 FSM、行为树 Behavior Tree 等决策组织方法 |

路径通畅却不追赶，应先查决策与目标；想追却卡在桌边，再查通行表示、路径和移动。这三层在角色原型、关卡制作与调试时一起验证。

### 动画与动作规则

| 中文 | English | 日本語 | 含义、实例与使用阶段 |
| --- | --- | --- | --- |
| 逐帧动画 | Frame-by-frame Animation | フレーム・バイ・フレーム／コマアニメーション | 逐张安排画面；可以来自手绘，也可以来自三维渲染。<br><strong>例：</strong>[《Cuphead》](https://cupheadgame.com/)连续绘制不同姿态，再把帧放进游戏；角色拉伸的形状直接存在于这些画稿中。[\[7\]](#ref-7)<br>用于：关卡、动画制作与调试。 |
| 关键帧／插值 | Keyframe / Interpolation | キーフレーム／補間 | 指定重要时刻的值或姿态／计算中间变化；节奏取决于两者配合。<br><strong>例：</strong>[《Dead Cells》](https://dead-cells.com/)三维动作可调整关键姿态的时间再重新出图；动作间的补间仍需检查是否符合攻击节奏。[\[8\]](#ref-8)<br>用于：关卡、动画制作与调试。 |
| 骨架／绑定 | Skeleton / Rigging | スケルトン／リギング | 形体的骨骼结构／建立控制关系；控制器不一定直接进入成品。<br><strong>制作例：</strong>[《Untitled Goose Game》](https://goose.game/)式鹅模型需要颈部和翅膀控制；建立骨骼与控制器后，动画师才能方便地反复摆姿态。<br>用于：关卡、动画制作与调试。 |
| 蒙皮／权重 | Skinning / Weight | スキニング／ウェイト | 让网格跟随骨骼／各部分受骨骼影响的比例。<br><strong>制作例：</strong>[《Untitled Goose Game》](https://goose.game/)式鹅模型弯脖子时，颈部网格受哪些骨骼影响、影响多少，由蒙皮权重控制。<br>用于：关卡、动画制作与调试。 |
| 正向／反向运动学 | Forward Kinematics — FK / Inverse Kinematics — IK | フォワード／インバースキネマティクス | 逐级设置关节／根据末端目标求关节姿态；如按手部目标调整手臂。<br><strong>制作例：</strong>[《Baldur’s Gate 3》](https://baldursgate3.game/)式人物握住固定把手，IK 可从手的位置求手臂姿态；逐关节摆手臂则是 FK 路线。<br>用于：关卡、动画制作与调试。 |
| 动画片段／混合 | Clip / Blending | アニメーションクリップ／ブレンド | 一段动作数据／在不同动作之间过渡或组合。<br><strong>制作例：</strong>[《A Short Hike》](https://ashorthike.com/)式角色从走路变成奔跑，可以切换或混合两段动作；动作与实际移动速度仍要对应。<br>用于：关卡、动画制作与调试。 |
| 根运动 | Root Motion | ルートモーション | 由动画中的根部位移驱动角色移动；需与碰撞和控制规则配合。<br><strong>制作例：</strong>[《Hades》](https://www.supergiantgames.com/games/hades/)式突进可以由动画位移驱动，也可由规则驱动再配动作；两种方式都要处理碰撞和中断。<br>用于：关卡、动画制作与调试。 |
| 动画事件 | Animation Event | アニメーションイベント | 在指定动作时刻触发声音、特效或规则；动作速度改变后需要重新核对。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式挥击在特定时刻播放破风声、启用攻击区域；改变动作速度后重新核对时机。<br>用于：关卡、动画制作与调试。 |
| 碰撞体 | Collider | コライダー／衝突形状 | 用于碰撞检测的形状；可以比可见模型简单。<br><strong>制作例：</strong>[《Celeste》](https://www.celestegame.com/)式角色披发的外观可以宽于实际碰撞形状；画面轮廓与阻挡范围承担不同职责。<br>用于：动作原型、程序实现与调试。 |
| 攻击判定／受击判定 | Hitbox / Hurtbox | 攻撃判定／食らい判定 | 攻击生效的区域／可以被命中的区域；术语在项目中可能另有约定。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式挥剑区域是攻击判定，敌人可挨打的范围是受击判定；两者相交且满足规则才算命中。<br>用于：战斗原型、动画接入与平衡测试。 |
| 前摇／生效／后摇 | Startup / Active / Recovery | 発生前／持続／硬直 | 动作准备、判定有效和恢复阶段；与画面总时长分别设计。<br><strong>制作例：</strong>[《Hades》](https://www.supergiantgames.com/games/hades/)式攻击先举武器、再命中、最后收招；能否闪避取消与各阶段允许的输入分别设计。<br>用于：关卡、动画制作与调试。 |
| 顿帧／屏幕震动 | Hit Stop / Screen Shake | ヒットストップ／画面揺れ | 短暂停顿／移动镜头来强化反馈；力度与可读性、舒适度共同考虑。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式命中可用短暂停顿强调冲击，也可震动镜头；两者可分开调，避免遮蔽下一次攻击信息。<br>用于：关卡、动画制作与调试。 |
| 粒子／视觉特效 | Particle / VFX | パーティクル／視覚エフェクト | 控制大量小元素／更广义的视觉效果；烟、火花与魔法可由多种技术组合。<br><strong>制作例：</strong>[《Hades》](https://www.supergiantgames.com/games/hades/)式火花、烟雾与魔法轨迹可以叠在角色动作上；需要同时检查敌人和危险边界是否清楚。<br>用于：关卡、动画制作与调试。 |

### 同一个问题：怎样让玩家知道接下来去哪

- [《Celeste》](https://www.celestegame.com/)把主要动作挑战放在相对紧凑的房间。玩家通常能看到平台、危险与出口，因此可以把注意力放在“这几步怎么连起来”。局部空间适合反复练习，但镜头与障碍必须清楚展示动作条件。
- [《Hollow Knight》](https://www.hollowknight.com/)让玩家在相互连接的洞穴房间中探索。岔路、地图和暂时无法通过的障碍共同形成长线判断：现在继续走，还是获得能力后返回。迷路与重新认识旧地点成为体验的一部分。
- [《A Short Hike》](https://ashorthike.com/)给出登顶方向，同时允许攀爬、绕路和滑翔。山体与可见地形让目标持续存在，沿途活动又支持自由偏离路线。这里需要让地形本身可读，而不是把每段路都变成单一答案。
- [《Outer Wilds》](https://www.mobiusdigitalgames.com/outer-wilds.html)用遗迹信息、声音信号和环境变化引出新目标。某个地点何时可进入也可能是问题的一部分，因此玩家会根据发现改变出发时机。[\[19\]](#ref-19)

这是对公开玩法的比较：**局部出口、互联地图、可见地形、信息线索**分别承担主要引导。关卡工具应当支持这些需要，详见 [002 的地图与关卡工具](posts-2026-umwelt-game-development-handbook-002.html#tools-07)。

<a id="narrative-audio"></a>

## 08｜叙事、界面与声音：让内容跟随状态，并能被理解

文本、界面与声音都需要知道当前发生了什么。叙事读取关系和事件，界面显示可操作的状态，声音响应环境和行动；三者与规则一起制作，才能避免“内容存在，游戏却没有正确调用”。

### 叙事与文本

| 中文 | English | 日本語 | 含义、实例与使用阶段 |
| --- | --- | --- | --- |
| 叙事设计 | Narrative Design | ナラティブデザイン | 安排故事、世界、玩家行为与系统之间的关系。<br><strong>例：</strong>[《Hades》](https://www.supergiantgames.com/games/hades/)把失败后回到据点变成继续认识人物的机会；故事进展与反复挑战相互连接。<br>用于：叙事、界面与声音制作。 |
| 世界观／背景设定 | Worldbuilding / Lore | 世界観構築／設定 | 世界的规则、历史和文化；其中哪些进入游戏，需要继续选择。<br><strong>例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)遗迹与居民让玩家逐步认识衰落王国；背景设定需转为实际可遇见的人、物与信息。<br>用于：叙事、界面与声音制作。 |
| 故事节拍 | Story Beat | ストーリービート | 一次有意义的情节或情绪变化；不必等同于一个场景。<br><strong>例：</strong>[《Return of the Obra Dinn》](https://obradinn.com/)一次身份确认会改变玩家对船上关系的理解；一个重要信息变化也可以构成节拍。<br>用于：叙事、界面与声音制作。 |
| 分支／汇合 | Branch / Reconvergence | 分岐／合流 | 选择后进入不同内容／重新回到共享内容；汇合时仍可保留状态差异。<br><strong>制作例：</strong>[《80 Days》](https://www.inklestudios.com/80days/)式旅行中，乘船和乘火车可最后到同一城市，但保留不同时间、金钱与见闻。<br>用于：叙事、界面与声音制作。 |
| 条件／标记 | Condition / Flag | 条件／フラグ | 判断是否呈现某段内容／记录某事是否发生；是对白和任务连接的基础。<br><strong>制作例：</strong>[《Hades》](https://www.supergiantgames.com/games/hades/)式对白以“是否已经见过某人”为条件；记录这一经历的标记与实际对白内容分开保存。<br>用于：叙事、界面与声音制作。 |
| 对白树 | Dialogue Tree | 会話ツリー | 展示对白节点和选项关系；复杂项目也可能用脚本、表格或其他结构。<br><strong>制作例：</strong>[《Papers, Please》](https://papersplea.se/)式追问证件矛盾，列出玩家提问、来访者回应和后续选项，便于检查有没有走不通的分支。<br>用于：叙事、界面与声音制作。 |
| 环境叙事 | Environmental Storytelling | 環境ストーリーテリング | 通过物件位置、痕迹和空间关系提供故事信息。<br><strong>例：</strong>[《Return of the Obra Dinn》](https://obradinn.com/)现场里人物的位置、物品和动作共同提供线索；玩家通过观察推断发生过什么。<br>用于：叙事、界面与声音制作。 |
| 脚本事件／过场 | Scripted Event / Cutscene | スクリプトイベント／カットシーン | 按预设条件执行的事件／以镜头和表演呈现的段落；需要处理跳过、中断和状态。<br><strong>制作例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)式人物事件开始后，要安排走位、对白、镜头，以及跳过后关系与任务是否正确变化。<br>用于：叙事、界面与声音制作。 |
| 任务系统 | Quest System | クエストシステム | 管理目标、前提、进行状态与奖励；任务文字和实际条件必须一致。<br><strong>制作例：</strong>[《A Short Hike》](https://ashorthike.com/)式居民请求需要区分未接、进行中和已完成；交物品与获得回报都要改变对应状态。<br>用于：叙事、界面与声音制作。 |
| 本地化／国际化 | Localization — L10n / Internationalization — I18n | ローカライズ／国際化 | 为特定语言地区调整内容／让系统能容纳这些变化；包含布局、字体和格式。<br><strong>例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)曾修复匈牙利语版事件软锁；语言替换需要进入实际流程验证，系统也要预留字体和布局能力。[\[15\]](#ref-15)<br>用于：前期系统设计、翻译与语言测试。 |

### 同一个问题：玩家行动不一样，故事怎样跟着变化

| 游戏与玩家行为 | 具体组织方式 | 做法的作用与成本 |
| --- | --- | --- |
| [《80 Days》](https://www.inklestudios.com/80days/)：规划环球旅行路线，同时处理钱、时间和旅途事件 | 城市、路线与选择连接成旅程；ink 支持条件片段、分支和汇合 | 不同选择可以留下影响，又复用后续文本。重点是状态与文字之间的对应，并检查多种路线。[\[3\]](#ref-3) |
| [《Hades》](https://www.supergiantgames.com/games/hades/)：多次战斗后返回同一据点 | 把反复出现的地点与人物变化结合；战斗失败后仍可能接到新的关系和故事内容 | 重复返回仍能带来新信息。成本转向大量状态下的对白安排和连续性检查。[\[2\]](#ref-2) |
| [《Return of the Obra Dinn》](https://obradinn.com/)：以不同顺序调查船员的死亡现场 | 过去发生的事是既定的，玩家改变的是调查顺序与理解 | 历史无需随每次选择重写，但线索必须支持不同发现顺序；“非线性”也可以来自信息获得顺序 |

三者分别让变化落在**旅程与选择、反复游玩中的人物状态、玩家理解**上。编剧要先知道哪一层可以变化，再决定文本和分支体量。若十次二选一始终不汇合，就会形成 1,024 条路径；汇合、条件片段和共享场景可以控制扩张。

### 界面、输入与可读性

| 中文 | English | 日本語 | 含义、实例与使用阶段 |
| --- | --- | --- | --- |
| 用户界面／使用体验 | User Interface — UI / User Experience — UX | ユーザーインターフェース／ユーザー体験 | 控件与信息呈现／理解、操作、反馈的整体体验；界面漂亮并不自动说明操作清楚。<br><strong>例：</strong>[《Papers, Please》](https://papersplea.se/)的证件、规则书和盖章控件是界面；能否迅速比较矛盾、理解处罚则涉及整体使用体验。<br>用于：原型、界面制作与试玩。 |
| 游戏内信息层 | HUD — Heads-up Display | HUD／ゲーム内情報表示 | 游玩中持续或即时显示的生命、地图、弹药等信息。<br><strong>例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)战斗时显示的生命等状态帮助玩家决定是否继续冒险；提示的位置与出现时机要符合战斗节奏。<br>用于：叙事、界面与声音制作。 |
| 线框图／交互原型 | Wireframe / Interactive Prototype | ワイヤーフレーム／インタラクション試作 | 先安排信息结构／再尝试操作和页面流转；仍需连接实际状态。<br><strong>制作例：</strong>[《Papers, Please》](https://papersplea.se/)式界面先用方框安排证件和盖章区，再允许拖动检查，能分别发现布局与操作问题。<br>用于：前期界面设计与试玩。 |
| 响应式布局 | Responsive Layout | レスポンシブレイアウト | 随屏幕和内容改变排列、大小与留白；要检查长文本和不同输入。<br><strong>制作例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)式背包界面换到窄屏时，格子、说明和按钮要重新安排，不能只把整张画面缩小。<br>用于：叙事、界面与声音制作。 |
| 焦点／导航 | Focus / Navigation | フォーカス／ナビゲーション | 当前接受输入的控件／控件之间移动方式；键盘与手柄尤其依赖此关系。<br><strong>制作例：</strong>[《Slay the Spire》](https://store.steampowered.com/app/646570/Slay_the_Spire/)式选牌界面用手柄时，要清楚显示当前选中哪张卡，以及方向键会移到哪里。<br>用于：叙事、界面与声音制作。 |
| 按键重映射 | Input Remapping | キーコンフィグ／入力割り当て変更 | 允许把动作重新分配给按键或控制器输入。<br><strong>制作例：</strong>[《Celeste》](https://www.celestegame.com/)式项目让跳跃对应另一按键后，菜单提示、教程与多个动作同时按下的情况也要重新检查。<br>用于：叙事、界面与声音制作。 |
| 无障碍 | Accessibility | アクセシビリティ | 减少感知、操作和理解障碍，如字幕、字号、替代反馈和输入调整。<br><strong>例：</strong>[《Hades》](https://www.supergiantgames.com/games/hades/)God Mode 提供减伤帮助；[《Celeste》](https://www.celestegame.com/)式项目还可检查输入、字号和反馈通道。不同障碍需要不同调整。[\[2\]](#ref-2)<br>用于：前期设计、制作与试玩。 |
| 世界内界面 | Diegetic UI | ダイジェティックUI／世界内UI | 信息以世界中的物体或装置呈现；仍要确保玩家能读到和操作。<br><strong>例：</strong>[《Papers, Please》](https://papersplea.se/)中的证件和规则书本身就是工作台物品；日期、印章等信息嵌在游戏世界里，仍需清楚可读。<br>用于：叙事、界面与声音制作。 |

### 放在一起看：UI、UX、HUD 与世界内界面

[《Papers, Please》](https://papersplea.se/)的证件、规则书和盖章区都是玩家使用的**界面 UI**；它们作为边检工作台里的物品出现，属于**世界内界面**的例子。证件能否方便并排、文字能否辨认、处罚是否容易理解，则共同影响**使用体验 UX**。UX 涉及完整操作过程。

[《Hollow Knight》](https://www.hollowknight.com/)画面上的生命状态属于**HUD**：持续或按需显示游玩信息。这些词采用不同分类角度；“世界内”说明信息怎样进入场景，“HUD”说明信息层的用途，不能只凭是否显示数字判断。设计时先用界面原型检查摆放，再通过试玩检查理解与操作。

### 声音与交互音频

| 中文 | English | 日本語 | 含义、实例与使用阶段 |
| --- | --- | --- | --- |
| 背景音乐／音效／配音 | Background Music — BGM / Sound Effects — SFX / Voice-over — VO | BGM／SE・効果音／ボイス | 音乐、行动或环境声音、角色语音；音量和优先级可分别管理。<br><strong>例：</strong>[《Untitled Goose Game》](https://goose.game/)钢琴伴奏、物件落地声、鹅叫承担不同信息；鹅叫是角色声效，不能直接等同人声对白配音。<br>用于：声音规划、资源制作与接入。 |
| 环境声／拟音 | Ambience / Foley | 環境音／フォーリー | 空间与环境的声音层／为动作制作或录制的声音，如衣料与脚步。<br><strong>制作例：</strong>[《A Short Hike》](https://ashorthike.com/)式海边的风与海浪建立环境，脚步和衣物动作属于具体行动声音，制作时分别安排。<br>用于：叙事、界面与声音制作。 |
| 数字音频工作站 | Digital Audio Workstation — DAW | デジタルオーディオワークステーション | 录音、编辑、编曲和混音的制作环境；输出素材后还需游戏接入。<br><strong>例：</strong>[《Celeste》](https://www.celestegame.com/)对话音节先在 FL Studio 中合成和录制，再交给 FMOD 组织播放；参见 [002 声音案例](posts-2026-umwelt-game-development-handbook-002.html#audio-cases)。<br>用于：声音素材制作。 |
| 声音事件／参数 | Audio Event / Parameter | オーディオイベント／パラメータ | 可触发的声音行为／影响播放的数值或状态；如速度改变引擎声。<br><strong>例：</strong>[《Untitled Goose Game》](https://goose.game/)物件声音可按运动速度调整；“播放这个物件”是事件，“多快、多强”是影响播放的参数。[见制作访谈](https://fmod.com/blog/untitled-goose-game-interview)。<br>用于：叙事、界面与声音制作。 |
| 自适应音乐 | Adaptive Music | アダプティブミュージック | 音乐随状态变化；可改变层、段落、强度和衔接位置。<br><strong>例：</strong>[《Untitled Goose Game》](https://goose.game/)把预录钢琴材料随行动组织，平静游荡与制造混乱得到不同节奏；音乐与状态相连。[\[18\]](#ref-18)<br>用于：叙事、界面与声音制作。 |
| 分轨／音乐层 | Stem / Layer | ステム／レイヤー | 可独立处理的声部或子混音／运行中可分别控制的层；用法随工程而异。<br><strong>制作例：</strong>[《Hades》](https://www.supergiantgames.com/games/hades/)式战斗音乐可把鼓、低音与旋律分开准备，运行中再按强度启停；这是制作方案示意。<br>用于：叙事、界面与声音制作。 |
| 循环点／交叉淡化 | Loop Point / Crossfade | ループポイント／クロスフェード | 重复播放的边界／两段声音交叠渐变；用于减少突变和接缝。<br><strong>制作例：</strong>[《A Short Hike》](https://ashorthike.com/)式海浪循环首尾要接得上；从海边转到林地时，可让两层环境声短暂交叠渐变。<br>用于：叙事、界面与声音制作。 |
| 总线／混音／空间音频 | Bus / Mixing / Spatial Audio | バス／ミキシング／空間オーディオ | 成组控制声音／安排相对音量和处理／根据位置等组织听觉关系。<br><strong>制作例：</strong>[《Untitled Goose Game》](https://goose.game/)式场景可整体调小环境声来突出鹅叫，再按物件位置安排方向与远近；三项控制并不相同。<br>用于：叙事、界面与声音制作。 |

[《Untitled Goose Game》](https://goose.game/)让玩家扮演鹅，在村庄里偷东西、引人追赶。配乐采用预先录好的钢琴材料，由系统随情境组织，给即兴行动配出接近默片喜剧的节奏。作曲者说明了这种动态音乐怎样借鉴电影伴奏。[\[18\]](#ref-18) 因此，“音乐写完”之后仍有事件、状态与衔接的制作；更多声音方案比较见 [002](posts-2026-umwelt-game-development-handbook-002.html#audio-cases)。

<a id="phase-5"></a>

## 09｜正式制作与协作：把样板扩展成完整作品

正式制作按已经验证的方法增加功能与内容。每轮完成制作、接入和检查，留下可玩的版本；源工程、导出资源和成品分别保存，便于继续修改与追查。

| 中文 | English | 日本語 | 含义、实例与使用阶段 |
| --- | --- | --- | --- |
| 正式制作 | Production | 本制作／プロダクション | 将经过验证的设计与流程扩展成完整项目。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式样板房间验证完后，按相同规格持续制作其他房间，同时定期整合成可玩地图。<br>用于：正式制作与协作。 |
| 迭代 | Iteration | イテレーション／反復改善 | 制作、检查、得到信息后再修改；每轮应有明确问题和范围。<br><strong>制作例：</strong>[《Baba Is You》](https://www.hempuli.com/baba/)式谜题试玩发现提示不清，改文字布局后再让人尝试；一轮修改应能回答原先问题。<br>用于：正式制作与协作。 |
| 功能／内容 | Feature / Content | 機能／コンテンツ | 可复用的能力／利用能力制作的具体材料；新内容也可能引入新功能。<br><strong>制作例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)式游戏新增普通作物多为内容；新增“作物会移动并追人”会引入新行为能力。<br>用于：正式制作与协作。 |
| 接入／整合 | Integration | 組み込み／統合 | 让程序、资源与其他系统一起运行；导出一个文件还没有完成接入。<br><strong>制作例：</strong>[《Cuphead》](https://cupheadgame.com/)式首领动画导出之后，还要接上攻击条件、碰撞、声音和胜败流程，才能成为可玩的首领。<br>用于：正式制作与协作。 |
| 版本管理 | Version Control | バージョン管理 | 记录文件变化、比较和恢复版本，支持多人协作。<br><strong>制作例：</strong>[《80 Days》](https://www.inklestudios.com/80days/)式分支改坏后，可以比较修改前后的文本与规则，恢复相关文件，而不是重新凭记忆写。<br>用于：项目建立至维护结束。 |
| 提交／分支／合并 | Commit / Branch / Merge | コミット／ブランチ／マージ | 保存一组变化／独立推进一条修改线／把修改接回共同版本。<br><strong>制作例：</strong>[《Baba Is You》](https://www.hempuli.com/baba/)式新机制在分支中试做，提交记录每组修改；验证后合回主版本，检查旧谜题仍成立。<br>用于：正式制作与协作。 |
| 审查／合并请求 | Review / Pull Request | レビュー／プルリクエスト | 提出并检查修改；审查结果应对应实际文件和行为。<br><strong>制作例：</strong>[《Slay the Spire》](https://store.steampowered.com/app/646570/Slay_the_Spire/)式卡牌改动提交审查时，给出费用、效果和组合测试；读差异之外还要看实际战斗结果。<br>用于：正式制作与协作。 |
| 冲突／文件锁 | Conflict / File Lock | コンフリクト／ファイルロック | 修改无法自动合并／限制同时修改；模型等二进制工程常需明确交接。<br><strong>制作例：</strong>两人同时修改[《Hollow Knight》](https://www.hollowknight.com/)式同一角色绘画工程，图层变化难自动合并，可以锁文件或约定交接。<br>用于：正式制作与协作。 |
| 备份 | Backup | バックアップ | 独立保存可恢复副本；要覆盖源工程、大资源、依赖和必要配置。<br><strong>制作例：</strong>[《Cuphead》](https://cupheadgame.com/)式制作同时保存纸稿扫描、上色工程和导出帧；只备份成品图片不足以继续原流程修改。<br>用于：整个制作与维护过程。 |
| 单一可信来源 | Single Source of Truth | 一元的な正本管理 | 明确哪份数据或文件是当前依据，减少多个副本各自更新。<br><strong>制作例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)式作物售价以同一数据表为准，商店和物品说明读取它，避免显示价格与成交价格不同。<br>用于：正式制作与协作。 |
| 重构 | Refactoring | リファクタリング | 保持约定行为的前提下调整内部结构，使修改与理解更容易。<br><strong>制作例：</strong>把[《Papers, Please》](https://papersplea.se/)式多种证件重复的日期比较整理成共用处理，同时保持原有判定结果不变。<br>用于：正式制作与协作。 |
| 技术债务 | Technical Debt | 技術的負債 | 增加后续修改负担的设计或实现问题；应结合影响和修复成本处理。<br><strong>制作例：</strong>[《80 Days》](https://www.inklestudios.com/80days/)式项目把同一城市名散写在许多脚本里，后来改名与本地化就要逐处修改，负担逐步增加。<br>用于：正式制作与协作。 |
| 功能冻结／内容冻结 | Feature Freeze / Content Freeze | 機能凍結／コンテンツ凍結 | 暂停新增功能／内容，把精力转向稳定和发布；范围由团队明确。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式作品临近发布，先停止添加新能力，再停止增加房间，集中修复路线与运行问题。<br>用于：正式制作与协作。 |
| 变更请求 | Change Request | 変更要求 | 对已约定内容提出修改，重新评估依赖、成本与验收。<br><strong>制作例：</strong>[《Celeste》](https://www.celestegame.com/)式角色临时增加二段跳，需要重新估算动画、输入、教学和原有房间被绕过的可能。<br>用于：正式制作与协作。 |

### 同一个问题：“再加一个”到底增加多少工作

| 例子 | 可能复用的部分 | 需要继续制作或检查的部分 |
| --- | --- | --- |
| [《星露谷物语》](https://www.stardewvalley.net/)式种植系统新增一种普通作物 | 种植、浇水、成熟与收获规则 | 图像、价格、季节、物品关系；若会追着玩家跑，就已经引入新行为 |
| [《Hollow Knight》](https://www.hollowknight.com/)式探索新增一间房 | 移动、战斗、门和保存系统 | 地形、美术、敌人组合；还要检查已有能力能否绕过障碍 |
| [《Papers, Please》](https://papersplea.se/)式检查新增一种证件 | 展示、比对、裁决的基本能力 | 字段、规则、文字和例外；新字段还可能与旧证件产生交叉条件 |
| [《80 Days》](https://www.inklestudios.com/80days/)式旅行新增一座城市 | 路线与条件叙事框架 | 城市事件、路线、资源变化以及抵达时的多种状态 |

这是基于玩法的制作估算示例，不是这些项目的内部任务记录。判断新增工作时，先看它是否仍在已有规则内，再数资源和组合。

<a id="cost"></a>

### 预算与进度

| 中文 | English | 日本語 | 含义、实例与使用阶段 |
| --- | --- | --- | --- |
| 工时估算 | Effort Estimation | 工数見積もり | 估计完成任务需要多少劳动时间；用实际样板校准。<br><strong>制作例：</strong>[《Dead Cells》](https://dead-cells.com/)式项目先完整做出一套武器动作，记录建模、动画、出图和导入时间，再估算后续规模。<br>用于：正式制作与协作。 |
| 人日／日历工期 | Person-day / Elapsed Time | 人日／所要期間 | 工作量／从开始到结束经过的时间；等待和依赖会让两者不同。<br><strong>制作例：</strong>[《Cuphead》](https://cupheadgame.com/)式动画绘制需要五个人日，若等待上色交接和反馈，五个日历日未必能完成。<br>用于：正式制作与协作。 |
| 预算／消耗速度 | Budget / Burn Rate | 予算／バーンレート | 可用资金／单位时间消耗；与剩余工作和可持续时间一起判断。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式区域每月持续消耗人员与外包费用，剩余资金能支持多久，要与尚未完成的内容一起判断。<br>用于：正式制作与协作。 |
| 制作吞吐量 | Throughput | スループット | 一段时间实际完成并接入多少内容；只数未检查资源会高估进度。<br><strong>制作例：</strong>[《Baba Is You》](https://www.hempuli.com/baba/)式关卡一周设计十道但只有三道通过试玩，当前可用产量应依据通过检查的三道计算。<br>用于：正式制作与协作。 |
| 总拥有成本 | Total Cost of Ownership — TCO | 総保有コスト | 获取、学习、接入、运行和维护的总体成本；软件价格只是其中一项。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式动画工具即使免费，也要计算学习、导出、引擎接入和以后重做资源的成本。<br>用于：选型、预算与维护评估。 |

**剩余工作 ≈ 各类内容数量 × 对应实测工时 ＋ 共用系统 ＋ 整合测试 ＋ 返工与发布预留。** 复杂角色、普通道具和远景分开估算；增加语言、平台或永久分支，也要增加对应验证工作。后续测试根据这些规格判断成品是否达到约定。

<a id="phase-6"></a>

## 10｜测试与打磨：区分规则正确、玩家理解与运行稳定

测试贯穿制作。临近发布时，需要从完整成品重新走主要流程，同时覆盖新存档、旧存档、失败、取消、重试、不同语言与目标设备。

| 中文 | English | 日本語 | 含义、实例与使用阶段 |
| --- | --- | --- | --- |
| 质量保证 | Quality Assurance — QA | 品質保証／QA | 围绕质量建立的过程与检查；测试是其中一部分。<br><strong>制作例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)式作物从规格、编号检查到换季试玩都设检查点，质量工作贯穿制作而非最后集中找错。<br>用于：前期约定至发布后维护。 |
| 调试／测试 | Debugging / Testing | デバッグ／テスト | 寻找并修复原因／检查结果；行业口语中“デバッグ”也可能泛指测试工作。<br><strong>制作例：</strong>[《Papers, Please》](https://papersplea.se/)式过期证件被放行，测试证明结果不符；调试再检查日期比较在哪一步出了问题。<br>用于：制作中的检查与发布前测试。 |
| 试玩 | Playtest | プレイテスト | 观察实际玩家的理解、行为和体验；与自动化检查互补。<br><strong>制作例：</strong>让未玩过[《Baba Is You》](https://www.hempuli.com/baba/)式谜题的人尝试，看他是否意识到文字可推动；功能正确不保证规则容易理解。<br>用于：制作中的检查与发布前测试。 |
| 单元／集成测试 | Unit / Integration Test | 単体／結合テスト | 检查较小规则单元／多个部分一起工作的情况。<br><strong>制作例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)式作物单独检查成熟天数，再检查“浇水—跨日—收获—背包”共同工作。<br>用于：制作中的检查与发布前测试。 |
| 端到端测试 | End-to-end Test — E2E | エンドツーエンドテスト | 从实际入口走一段完整流程，核对各层连接。<br><strong>制作例：</strong>[《80 Days》](https://www.inklestudios.com/80days/)式游戏从新建旅程到选路线、支付、抵达、保存再继续，验证一条完整玩家路径。<br>用于：制作中的检查与发布前测试。 |
| 冒烟测试 | Smoke Test | スモークテスト | 快速确认启动、主要路径等关键能力，判断是否值得继续详细检查。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式新构建先检查启动、移动、战斗、换房和读档；核心路径坏了，就先修复再做细查。<br>用于：制作中的检查与发布前测试。 |
| 回归测试 | Regression Test | リグレッションテスト／回帰テスト | 修改后检查原有行为是否被破坏。<br><strong>制作例：</strong>[《Baba Is You》](https://www.hempuli.com/baba/)式规则解析改动后，除了新题，也重跑原来能解的关卡，确认已有答案没有被无意破坏。<br>用于：每次改动后与发布前。 |
| 功能／体验测试 | Functional / Usability Test | 機能／ユーザビリティテスト | 是否按约定工作／人能否理解和顺利操作；两者问题来源可能不同。<br><strong>制作例：</strong>[《Celeste》](https://www.celestegame.com/)式跳跃能触发是功能问题；玩家总觉得按了却没跳，需要继续检查时机与操作感受。<br>用于：制作中的检查与发布前测试。 |
| 兼容／本地化测试 | Compatibility / Localization QA | 互換性／ローカライズQA | 不同设备和环境／具体语言的文字、布局、语境和流程。<br><strong>例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)匈牙利语版人物事件的软锁说明，默认语言通过也不能替代各语言完整流程检查。[\[15\]](#ref-15)<br>用于：制作中的检查与发布前测试。 |
| 复现步骤／最小复现 | Reproduction Steps / Minimal Repro | 再現手順／最小再現例 | 如何再次触发问题／去掉无关内容后仍出现问题的最小条件。<br><strong>制作例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)式收获错误记录季节、作物、天气与存档；再删去无关田块，看一个作物能否重现。<br>用于：制作中的检查与发布前测试。 |
| 缺陷／严重度／优先级 | Bug / Severity / Priority | 不具合／重大度／優先度 | 不符合约定的问题／影响有多大／先处理哪一个；三者分别记录。<br><strong>制作例：</strong>[《Papers, Please》](https://papersplea.se/)式日期错判会破坏核心裁决，装饰偏一像素影响较小；严重度与先修谁还要结合出现频率。<br>用于：制作中的检查与发布前测试。 |
| 崩溃／卡死／软锁 | Crash / Hang / Softlock | クラッシュ／フリーズ／進行不能 | 程序退出／不再响应／仍运行但无法继续必要进程。<br><strong>制作例：</strong>[《Baba Is You》](https://www.hempuli.com/baba/)式项目退出是崩溃、不响应是卡死、界面还能动却无法继续必要进程是软锁；要分别记录。<br>用于：制作中的检查与发布前测试。 |
| 边界情况 | Edge Case | 境界ケース／例外的な条件 | 极端或少见条件，如空存档、最长文本、快速连点和中途断开。<br><strong>制作例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)式背包全满时收获、最后一天种跨季作物、收获瞬间读档，都需要明确处理规则。<br>用于：制作中的检查与发布前测试。 |
| 自动化测试 | Automated Test | 自動テスト | 由程序重复执行检查；通过只说明已覆盖的条件成立。<br><strong>制作例：</strong>[《Baba Is You》](https://www.hempuli.com/baba/)式项目让程序重放一组移动并比较结果，能反复检查规则；谜题是否好懂仍要真人试玩。<br>用于：制作中的检查与发布前测试。 |
| 遥测／分析 | Telemetry / Analytics | テレメトリ／分析 | 收集与解释运行或行为数据；采集内容、权限和用途应明确。<br><strong>制作例：</strong>[《Celeste》](https://www.celestegame.com/)式项目统计某房间重试位置，帮助定位异常困难处；次数只能指出现象，原因还需观察。<br>用于：获授权的试玩与发布后观察。 |
| 日志／断点 | Log / Breakpoint | ログ／ブレークポイント | 保存执行信息／暂停到指定位置以检查状态。<br><strong>制作例：</strong>[《Papers, Please》](https://papersplea.se/)式错判先记录输入日期和结果，再暂停在比较步骤查看值；一种保留过程，一种现场检查。<br>用于：制作中的检查与发布前测试。 |
| 性能分析 | Profiling | プロファイリング | 测量时间、内存和图形等开销，定位瓶颈。<br><strong>制作例：</strong>[《Factorio》](https://www.factorio.com/)式大型工厂变慢时，分别测量机器模拟、寻路和绘制，避免只凭对象多就猜原因。<br>用于：原型、制作与优化。 |
| 帧率／帧时间 | Frames per Second — FPS / Frame Time | フレームレート／フレーム時間 | 每秒帧数／单帧耗时；平均帧率正常也可能有明显尖峰卡顿。<br><strong>制作例：</strong>[《Celeste》](https://www.celestegame.com/)式动作游戏平均 60 FPS 仍可能偶发卡顿；要查个别帧是否明显超过约 16.7 毫秒。<br>用于：性能目标制定与实机测试。 |
| CPU／GPU 瓶颈 | CPU-bound / GPU-bound | CPU／GPUボトルネック | 处理器计算／图形计算成为主要限制；应依据测量选择优化方向。<br><strong>制作例：</strong>[《Factorio》](https://www.factorio.com/)式工厂可能需要减少模拟计算，[《Hades》](https://www.supergiantgames.com/games/hades/)式大量特效可能要减少图形负担；用测量确认。<br>用于：制作中的检查与发布前测试。 |
| 绘制调用／过度绘制 | Draw Call / Overdraw | ドローコール／オーバードロー | 提交绘制工作／同一像素被重复处理；成本随具体渲染方式变化。<br><strong>制作例：</strong>[《Hades》](https://www.supergiantgames.com/games/hades/)式火焰层层覆盖同一区域会重复处理像素；合批减少提交次数，并不必然消除这些覆盖。<br>用于：制作中的检查与发布前测试。 |
| 内存泄漏／回收 | Memory Leak / Garbage Collection | メモリリーク／ガベージコレクション | 不再需要的内存持续留存／自动回收部分不再使用对象；回收也可能产生耗时。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式进出房间后资源占用一直增加，检查是否仍保留旧引用；自动回收造成的短暂停顿另行测量。<br>用于：制作中的检查与发布前测试。 |
| 长时间测试／压力测试 | Soak / Stress Test | 長時間／ストレステスト | 检查持续运行的累积问题／极端负载下的行为。<br><strong>制作例：</strong>[《Factorio》](https://www.factorio.com/)式工厂持续运行查累积问题，一次放入大量机器查高负载；测试条件和目标不同。<br>用于：制作中的检查与发布前测试。 |
| 打磨 | Polish | ポリッシュ／仕上げ | 改进节奏、反馈、过渡与一致性；建立在主要规则和内容已经成立的基础上。<br><strong>制作例：</strong>[《Celeste》](https://www.celestegame.com/)式角色已能完成关卡后，再改重生等待、镜头、音效和落地反馈，使整段操作更连贯。<br>用于：制作中的检查与发布前测试。 |

<a id="testing-comparison"></a>

### 放在一起看：QA、测试、试玩与调试

假设制作一个[《Papers, Please》](https://papersplea.se/)式证件游戏：过期证件本应被拒绝，却被系统判为有效。

| 工作 | 同一问题下具体做什么 |
| --- | --- |
| QA／质量保证 | 在规则评审、日期实现、改动检查和发布验收中安排质量措施，降低同类错误反复出现的机会 |
| 测试 Test | 准备有效、过期当天、已过期等输入，对照约定的有效期边界检查实际结果 |
| 调试 Debug | 用日志、断点等查出日期在哪一步被比较错，并定位原因 |
| 回归测试 Regression Test | 修复后重测原问题和其他日期、证件类型，检查已有判断是否仍正确 |
| 试玩 Playtest | 观察新人是否知道日期在哪里、为什么被罚；即使程序判定正确，也可能难以理解 |

QA 是贯穿过程的工作；测试与试玩提供不同类型的证据；调试追查实现原因。制作中反复使用，发布前再按风险扩大检查范围。

### 同一个问题：失败太挫折，究竟改哪里

| 游戏与失败情境 | 各自怎么处理 | 为什么适合；最后有什么不同 |
| --- | --- | --- |
| [《Celeste》](https://www.celestegame.com/)：玩家知道要跳到哪里，却可能因细小时间误差失败 | 短距离重试配合输入缓冲、离边宽限和边角修正 | 减少重复赶路与“明明按了却没跳”的挫折，把注意力留在动作学习上；主要挑战仍在操作。[\[10\]](#ref-10) |
| [《Baba Is You》](https://www.hempuli.com/baba/)：玩家试了一种文字排列，发现结果不对 | 允许撤销操作，再尝试另一种排列 | 推理需要试验，撤销减少重摆局面的成本；解题困难仍在理解规则，没有直接给答案 |
| [《Hades》](https://www.supergiantgames.com/games/hades/)：玩家还想看故事，但战斗伤害压力过高 | 可选择 God Mode，以减伤并随死亡提高耐受 | 调整的是承受压力，让玩家更容易继续体验；与修正按键时机、撤销一步操作解决的是不同问题。[\[2\]](#ref-2) |

“降低挫折”可能意味着**减少重复劳动、容纳操作误差、允许试验、降低数值压力**。先观察玩家在哪里受阻，才能判断该改输入、关卡、信息还是参数。

<a id="acceptance"></a>

### 验收怎样连接到发布

一份问题记录至少包含**版本、环境、起始状态、步骤、预期、实际和证据**。修复后先复测原问题，再检查可能受影响的流程。性能比较固定镜头、输入、设备和画质：60 帧每秒平均约为每帧 16.7 毫秒，但单帧波动还要单独观察。

发布判断应能说明：**哪个候选版本，在什么条件下，通过哪些检查，还有哪些未覆盖条件。** 例如网页音频受首次用户操作影响，模拟手机尺寸也不能完全替代真机检查。[\[9\]](#ref-9)、[\[12\]](#ref-12) 这些结果随后决定哪个构建可以发布。

<a id="phase-7"></a>

## 11｜发布与发行：区分文件完成、平台接入和玩家取得

构建生成成品，部署把成品放进运行环境，发布让玩家取得约定版本。产品页、宣传材料、平台接入和审核也需要时间，通常在正式制作期间就开始准备。

| 中文 | English | 日本語 | 含义、实例与使用阶段 |
| --- | --- | --- | --- |
| 构建／打包 | Build / Packaging | ビルド／パッケージ化 | 生成目标程序与资源／组织成可分发形式；不同平台有不同产物。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式工程输出桌面可执行文件与资源，再组织成玩家能取得的下载包；工程目录本身不是交付。<br>用于：原型分享、集成与发布。 |
| 构建产物 | Artifact | ビルド成果物／アーティファクト | 某次构建生成的文件；发布和测试应能追溯到同一份产物。<br><strong>例：</strong>[《Baldur’s Gate 3》](https://baldursgate3.game/)Hotfix 4 的问题说明，测试候选与后来重新构建的文件可能不同；应追踪实际发布的那一份。[\[14\]](#ref-14)<br>用于：发布准备与发行。 |
| 持续集成／交付／部署 | Continuous Integration — CI / Continuous Delivery / Continuous Deployment | 継続的インテグレーション／デリバリー／デプロイ | 自动检查与整合／保持可发布状态／自动部署；CD 需按项目语境区分。<br><strong>制作例：</strong>[《Baba Is You》](https://www.hempuli.com/baba/)式项目每次改规则自动重放旧谜题；测试通过后准备下载包，是否自动公开还由发布安排决定。<br>用于：制作协作与发布。 |
| 部署／发布／发行 | Deploy / Release / Publishing | デプロイ／リリース／パブリッシング | 放入目标环境／开放版本／产品经营与分发支持；职责有交叉但不相同。<br><strong>制作例：</strong>[《80 Days》](https://www.inklestudios.com/80days/)式网页成品上传是部署，开放玩家访问是发布；定价、宣传和渠道合作属于更广的发行工作。<br>用于：发布准备与发行。 |
| Alpha 阶段／Beta 阶段 | Alpha / Beta | アルファ／ベータ | 团队使用的成熟度标签；具体公开范围、功能与品质标准必须另写。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式项目可把“主要路线已通”和“内容齐备、集中修错”分别约为成熟度门槛；标签由团队定义。<br>用于：发布准备与发行。 |
| 功能齐备／内容齐备 | Feature Complete / Content Complete | 機能実装完了／コンテンツ完成 | 约定功能已实现／内容已接入；之后仍要测试、打磨和修复。<br><strong>制作例：</strong>[《Baba Is You》](https://www.hempuli.com/baba/)式引擎已支持全部规则，关卡还没做完，属于功能与内容完成度不同的情况。<br>用于：发布准备与发行。 |
| 候选发布版本 | Release Candidate — RC | リリース候補版 | 准备发布并接受最后检查的具体版本；再修改就需要重新确认。<br><strong>制作例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)式更新选定一个具体构建做旧存档和平台检查；修复后产生的新文件需要再次确认。<br>用于：发布准备与发行。 |
| 母版／发行批准 | Gold Master / Going Gold | マスター／マスターアップ | 达到某种正式生产或发布条件的版本；更新型游戏仍可能继续修补。<br><strong>制作例：</strong>[《Cuphead》](https://cupheadgame.com/)式主机成品达到约定生产或发行条件时标记母版；此后补丁仍需要独立版本和检查。<br>用于：发布准备与发行。 |
| 抢先体验 | Early Access | 早期アクセス | 以明确未完成状态公开提供游戏并继续开发；需要维护当前版本与后续计划。<br><strong>例：</strong>初代[《Hades》](https://www.supergiantgames.com/games/hades/)先公开可玩版本，再持续增加战斗与故事，最终进入 1.0；玩家会参与未完成阶段的体验。[\[2\]](#ref-2)<br>用于：发行计划、公开测试与持续制作。 |
| 平台审核／认证 | Review / Certification | 審査／認証 | 平台对商店内容、功能和技术要求的检查；通过范围以平台说明为准。<br><strong>制作例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)式作品准备 Steam 商店介绍与构建，两部分分别检查；素材描述也要与实际玩法一致。[\[11\]](#ref-11)<br>用于：发布准备与发行。 |
| 移植 | Porting | 移植 | 让作品适应另一个平台的运行、输入和分发条件；不只是重新编译。<br><strong>制作例：</strong>把[《星露谷物语》](https://www.stardewvalley.net/)式桌面操作移到触屏，需要重新安排点选、拖动和界面尺度；重新编译只处理部分工作。<br>用于：平台规划、适配与测试。 |
| 最低／推荐配置 | Minimum / Recommended Requirements | 最低／推奨動作環境 | 对运行条件的说明；应与实测内容、画质和体验目标对应。<br><strong>例：</strong>[《DOOM》](https://store.steampowered.com/app/379720/DOOM/)商店分别列出两类运行条件；制作自己的配置说明时，还要明确测试场景和画质目标。<br>用于：性能目标制定与发布准备。 |
| 商店页／愿望单 | Store Page / Wishlist | ストアページ／ウィッシュリスト | 展示并分发作品／玩家表达关注；数量是信号，不能直接等同销量。<br><strong>例：</strong>[《Slay the Spire》](https://store.steampowered.com/app/646570/Slay_the_Spire/)商店页让人了解构筑卡组与爬塔玩法，愿望单记录关注；关注不等于已购买或实际游玩。<br>用于：发行筹备至发售后。 |
| 宣传片／媒体资料包 | Trailer / Press Kit | トレーラー／プレスキット | 展示体验的视频／供媒体使用的简介、图像和基本信息。<br><strong>制作例：</strong>[《Baba Is You》](https://www.hempuli.com/baba/)式宣传片需要演示推动文字前后的变化；媒体包再提供截图、标志、简介和联系信息。<br>用于：宣传筹备与发布。 |
| 发行商／自行发行 | Publisher / Self-publishing | パブリッシャー／自主販売 | 提供约定发行支持的合作方／自己承担相应工作；具体责任看合作安排。<br><strong>例：</strong>[《DOOM》](https://store.steampowered.com/app/379720/DOOM/)商店把 id Software 列为开发者、Bethesda 列为发行方；两者具体承担哪些工作仍看合作安排。<br>用于：立项预算与发行计划。 |
| 本体／追加内容 | Base Game / Downloadable Content — DLC | 本編／ダウンロードコンテンツ | 基础产品／追加内容；与补丁、免费更新分别安排。<br><strong>制作例：</strong>给[《Hollow Knight》](https://www.hollowknight.com/)式游戏扩展新区域时，明确它随本体更新还是单独取得；“多了内容”不能自动判断销售方式。<br>用于：发布准备与发行。 |
| 买断／免费游玩 | Premium / Free-to-play — F2P | 買い切り／基本プレイ無料 | 先购买本体／可免费开始；后续收费和服务范围仍需分别说明。<br><strong>例：</strong>[《Slay the Spire》](https://store.steampowered.com/app/646570/Slay_the_Spire/)购买本体后游玩，[《Dota 2》](https://store.steampowered.com/app/570/Dota_2/)可免费开始；比较商业模式还需看后续内容和服务怎样收费。<br>用于：立项、商业设计与发行。 |
| 许可证／署名 | License / Attribution | ライセンス／クレジット表記 | 使用与分发条件／按要求标明作者和来源；软件、字体、声音各自核对。<br><strong>制作例：</strong>[《A Short Hike》](https://ashorthike.com/)式项目使用外来字体与环境声时，分别核对使用条件，并把需要的作者信息放入致谢。<br>用于：素材取得、接入与发布。 |
| 年龄分级 | Age Rating | 年齢レーティング | 对内容与适用年龄等作出的分级；平台和地区要求分别确认。<br><strong>制作例：</strong>[《DOOM》](https://store.steampowered.com/app/379720/DOOM/)式作品的暴力表现需要在平台材料中正确申报；不同地区与平台的结果不能直接互换。<br>用于：内容规划与平台发布。 |
| 内容分发网络 | CDN — Content Delivery Network | コンテンツ配信ネットワーク | 从不同节点分发文件以改善获取；更新时还需处理缓存与版本对应。<br><strong>制作例：</strong>[《Minecraft》](https://www.minecraft.net/en-us/about-minecraft)式更新的资源包可通过分发节点送到不同地区；文件缓存仍要与客户端版本对应。<br>用于：发布准备与发行。 |

### 同一个问题：已经能玩，为什么还会在发布时出问题

| 游戏与变更 | 发生了什么、怎样处理 | 对应的发布知识 |
| --- | --- | --- |
| [《Baldur’s Gate 3》](https://baldursgate3.game/)：角色扮演游戏的 Hotfix 4 | 已测试候选后来为改版本号重新构建，出现编译问题；回退期间，部分新存档无法由旧版本读取。团队随后要求候选的任何更改重新接受完整检查 | 测过的构建与实际发布文件必须对应；回退也要考虑新存档。[\[14\]](#ref-14) |
| [《星露谷物语》](https://www.stardewvalley.net/)：PC 版 1.5.5 的运行技术更新 | 从 XNA 迁到 MonoGame，同时修复兼容与本地化等问题 | 玩家看到的内容可能变化不大，运行环境却变了；技术迁移需要重新验证支持条件。[\[15\]](#ref-15) |
| [《Hades》](https://www.supergiantgames.com/games/hades/)：抢先体验到 1.0 | 在公开可玩的阶段持续增加战斗与故事，再进入正式版本 | 公开发布是持续交付方式，团队要同时承担反馈、兼容和未完成内容的制作。[\[2\]](#ref-2) |

Steam 将商店页和构建分别审核，因此介绍材料与程序要分别准备，再检查彼此是否一致。[\[11\]](#ref-11) 发布后从公开入口重新取得成品，确认文件、输入、声音和进度恢复；只检查本地项目无法证明分发成功。

<a id="phase-8"></a>

## 12｜维护、扩展与结束支持

维护先区分缺陷、理解困难、设备差异、偏好和新增需求。补丁处理已确认的问题；扩展内容重新经过范围、依赖、制作与测试。停止扩展时，仍应留下可以恢复和继续使用的项目。

| 中文 | English | 日本語 | 含义、实例与使用阶段 |
| --- | --- | --- | --- |
| 补丁／紧急修复 | Patch / Hotfix | パッチ／ホットフィックス | 修改已发布版本／针对迫切问题快速发布修复；快速仍需明确验证范围。<br><strong>例：</strong>[《Baldur’s Gate 3》](https://baldursgate3.game/)Hotfix 4 处理更新后的运行问题；紧急程度改变处理顺序，仍需验证实际构建。[\[14\]](#ref-14)<br>用于：发布后维护。 |
| 数据迁移 | Data Migration | データ移行 | 把旧结构转成新结构，如存档字段变化；应保存旧数据并验证转换。<br><strong>制作例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)式存档新增作物字段时，为旧记录补上合理默认值，才能继续读取已有农场。<br>用于：发布后维护。 |
| 向后兼容 | Backward Compatibility | 後方互換性 | 新版本能继续处理旧内容或数据；不自动意味着旧程序也能读新数据。<br><strong>制作例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)式农场由新版本读入旧存档是向后兼容；把新存档交给旧程序，还要另查是否支持。<br>用于：发布后维护。 |
| 回退 | Rollback | ロールバック／切り戻し | 恢复之前的程序或配置；已经改变的数据需要单独处理。<br><strong>例：</strong>[《Baldur’s Gate 3》](https://baldursgate3.game/)Hotfix 4 回退期间，较新版本创建的部分存档不能由旧版本读取；程序回退与数据兼容必须一起考虑。[\[14\]](#ref-14)<br>用于：发布后维护。 |
| 在线运营 | Live Operations — LiveOps | ライブ運営／運用 | 持续维护在线内容、活动、服务和运行状态。<br><strong>制作例：</strong>[《Dota 2》](https://store.steampowered.com/app/570/Dota_2/)式持续对战服务需要处理活动、匹配、更新与异常；发行以后仍有持续工作。<br>用于：发布后维护。 |
| 监控／告警 | Monitoring / Alerting | 監視／アラート | 持续观察服务与异常／在指定条件下提醒处理。<br><strong>制作例：</strong>[《Minecraft》](https://www.minecraft.net/en-us/about-minecraft)式服务器持续观察连接和保存失败，达到条件时提醒处理；知道机器在线不代表玩家能正常进服。<br>用于：发布后维护。 |
| 留存／流失 | Retention / Churn | リテンション／離脱 | 某群玩家继续返回／停止使用的情况；先明确时间窗口和统计口径。<br><strong>制作例：</strong>观察[《Hades》](https://www.supergiantgames.com/games/hades/)式新玩家是否在下一次继续挑战，要明确统计哪批玩家和多长时间；单次通关作品另作解释。<br>用于：发布后维护。 |
| 更新记录 | Changelog / Release Notes | 変更履歴／リリースノート | 说明版本变化和必要的兼容信息；服务玩家与维护者。<br><strong>例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)1.5.5 公告列出技术迁移与修复，玩家和模组作者据此判断需要注意的变化。[\[15\]](#ref-15)<br>用于：发布后维护。 |
| 复盘 | Postmortem / Retrospective | ポストモーテム／振り返り | 根据结果检查原先假设、取舍和流程；形成下次可用的判断。<br><strong>例：</strong>[《A Short Hike》](https://ashorthike.com/)作者回看期限、美术和关卡取舍，说明哪些办法支持完成小型开放世界；复盘用于校准下一次判断。[\[1\]](#ref-1)<br>用于：发布后维护。 |
| 停止支持／服务终止 | End of Life — EOL / End of Service | サポート終了／サービス終了 | 停止维护／停止在线服务；要说明对获取、存档和游玩的影响。<br><strong>制作例：</strong>[《Minecraft》](https://www.minecraft.net/en-us/about-minecraft)式自建服务器关闭后，共享世界可能无法继续访问；停止更新单机程序与停服的后果不同。<br>用于：发布后维护。 |
| 归档／保存 | Archiving / Preservation | アーカイブ／保存 | 保存源工程、可运行成品、依赖版本、资源来源与重建说明。<br><strong>制作例：</strong>保存[《Dead Cells》](https://dead-cells.com/)式项目时，除二维成品帧，还要保存三维动作、输出工具与版本，才能重新生产资源。<br>用于：里程碑、发布与结束支持。 |

本地存档还受运行环境影响。例如浏览器 `localStorage` 与站点来源关联，换域名、浏览器或清理站点数据可能让原进度不可见或消失。[\[13\]](#ref-13) 因而长期保存作品时，要同时考虑**制作工程、运行程序、玩家数据和在线依赖**。

<a id="terms"></a>

## 类型名称与易混缩写

类型标签描述不同维度，可以叠加。用它们交流后，仍要具体说明玩家行为；例如“角色扮演”并不能说明战斗是即时还是回合制。

| 中文／常见名称 | English | 日本語 | 类型边界与游戏实例 |
| --- | --- | --- | --- |
| 角色扮演／动作角色扮演 | Role-playing Game — RPG / Action RPG — ARPG | ロールプレイングゲーム／アクションRPG | 角色能力、成长与扮演／结合即时动作的 RPG；RPG 不等于必然有回合制战斗。<br><strong>例：</strong>[《Baldur’s Gate 3》](https://baldursgate3.game/)以角色能力、选择和回合战斗组织冒险；[《Diablo III》](https://diablo3.blizzard.com/en-us/)让玩家即时移动、施放技能并收集装备，是动作角色扮演的例子。<br>用于：立项与玩法沟通。 |
| 第一／第三人称射击 | First-person Shooter — FPS / Third-person Shooter — TPS | 一人称／三人称視点シューティング | 射击玩法与相机位置；FPS 在性能语境中另指每秒帧数。<br><strong>例：</strong>[《DOOM》](https://store.steampowered.com/app/379720/DOOM/)从角色眼前观察并射击；[《Splatoon》](https://www.nintendo.com/en-gb/Games/Wii-U-games/Splatoon-892510.html)在角色身后看喷墨与移动；这里描述的是射击方式与视角。<br>用于：立项与玩法沟通。 |
| 平台跳跃 | Platformer | プラットフォームゲーム／ジャンプアクション | 以跳跃和空间移动为重要挑战，如[《Celeste》](https://www.celestegame.com/)；也可结合探索与战斗。<br><strong>例：</strong>[《Celeste》](https://www.celestegame.com/)把平台间移动、攀爬和冲刺作为主要挑战；成功条件取决于空间路线与操作时机。<br>用于：立项与玩法沟通。 |
| 冒险／指向点击冒险 | Adventure / Point-and-click Adventure | アドベンチャー／ポイント＆クリック | 探索、叙事和解谜等结构／通过指向场景、物品交互推进；“冒险”用法较宽。<br><strong>例：</strong>[《Return to Monkey Island》](https://returntomonkeyisland.com/)通过调查物件、交谈和解谜推进旅程；这些行为与需要连续跳跃的动作冒险有所不同。<br>用于：立项与玩法沟通。 |
| 视觉小说／文字冒险 | Visual Novel / Text Adventure | ビジュアルノベル／テキストアドベンチャー | 以文字、图像和选择等推进／以文字描述与输入或选项组织行动；二者不完全重合。<br><strong>例：</strong>初代[《Doki Doki Literature Club!》](https://ddlc.moe/)以对白、立绘和选择推进；[《80 Days》](https://www.inklestudios.com/80days/)还把文字连接到路线、时间与资源安排。<br>用于：立项与玩法沟通。 |
| 即时／回合制策略 | Real-time Strategy — RTS / Turn-based Strategy — TBS | リアルタイムストラテジー／ターン制ストラテジー | 多方同时推进／按回合推进；重点常在单位、资源与空间决策。<br><strong>例：</strong>[《StarCraft II》](https://starcraft2.blizzard.com/en-us/)持续建造、调兵并回应对手；[《Into the Breach》](https://store.steampowered.com/app/590380/Into_The_Breach/)按回合安排机甲行动，可以在执行前比较局面。<br>用于：立项与玩法沟通。 |
| 多人在线战术竞技 | MOBA — Multiplayer Online Battle Arena | MOBA | 常见结构是队伍控制角色、围绕地图目标对抗；具体人数和规则由作品决定。<br><strong>例：</strong>[《Dota 2》](https://store.steampowered.com/app/570/Dota_2/)玩家各控制英雄，与队友围绕地图资源和目标作决策；单个英雄与团队职责相连。<br>用于：立项与玩法沟通。 |
| 类银河战士恶魔城 | Metroidvania | メトロイドヴァニア | 相连地图、探索与能力获得共同打开路线；回到旧区域也能产生新进展。<br><strong>例：</strong>[《Hollow Knight》](https://www.hollowknight.com/)让新移动能力改变旧地图的可达范围；探索和返回旧区域共同推进进程。<br>用于：立项与玩法沟通。 |
| Roguelike／Roguelite | Roguelike / Roguelite | ローグライク／ローグライト | 常涉及多轮尝试、变化的局面与失败后的重置；两词边界有争议，要具体说明随机、重置与永久成长。<br><strong>例：</strong>[《Slay the Spire》](https://store.steampowered.com/app/646570/Slay_the_Spire/)每轮重新构筑牌组，[《Hades》](https://www.supergiantgames.com/games/hades/)一轮战斗之外保留长期变化；比较时写明重置和保留什么更清楚。<br>用于：立项与玩法沟通。 |
| 沙盒／开放世界 | Sandbox / Open World | サンドボックス／オープンワールド | 强调自由组合行动／强调可自由探索的世界组织；开放地图不自动意味着规则自由。<br><strong>例：</strong>[《Minecraft》](https://www.minecraft.net/en-us/about-minecraft)允许组合方块改造空间；[《A Short Hike》](https://ashorthike.com/)允许自由探索小岛，但不以同等程度的世界改造为重点。<br>用于：立项与玩法沟通。 |
| 模拟／经营 | Simulation / Management | シミュレーション／経営・管理 | 模拟某种系统／围绕资源与组织作决策；日文“シミュレーション”还常出现在策略游戏分类中。<br><strong>例：</strong>[《星露谷物语》](https://www.stardewvalley.net/)围绕作物、季节、钱和时间安排农场；“模拟”说明被组织的系统，还需补充具体规则。<br>用于：立项与玩法沟通。 |
| 实时／回合制 | Real-time / Turn-based | リアルタイム／ターン制 | 时间与行动怎样推进，能用于描述战斗、策略或其他系统；与美术的实时渲染分别理解。<br><strong>例：</strong>[《Celeste》](https://www.celestegame.com/)危险与角色动作持续推进；[《Slay the Spire》](https://store.steampowered.com/app/646570/Slay_the_Spire/)主要按战斗回合安排出牌。两者都可以实时生成屏幕画面。<br>用于：立项与玩法沟通。 |

<a id="ambiguous-terms"></a>

### 容易在不同语境中变义的名称

| 名称 | 放进具体游戏怎样区分 | 查阅位置 |
| --- | --- | --- |
| Core Loop／Game Loop／Meta | 农场种植、收获、再投资是玩家循环；每次更新位置和画面是程序循环；Meta 还可能讨论玩家依据流行打法调整策略 | [规则与循环](#loops-comparison)、[程序](#runtime) |
| TDD | 《Papers, Please》式日期字段与检查方案可写进 **Technical Design Document**；先写日期测试、再实现通过它的代码，则属于 **Test-driven Development**（测试驱动开发／テスト駆動開発） | [文档分工](#documents-comparison)、[测试](#testing-comparison) |
| FPS | “《DOOM》是一款 FPS”指第一人称射击；“运行在 60 FPS”指每秒显示约 60 帧。类型与性能指标需看上下文 | [类型](#terms)、[性能](#phase-6) |
| AI／.ai | 为《Untitled Goose Game》式村民安排追赶决策，是游戏 AI；生成式 AI 制作文本是另一类用途；`.ai` 还可能是 Illustrator 绘图文件 | [程序](#runtime)、[002 格式](posts-2026-umwelt-game-development-handbook-002.html#formats) |
| QA／QC | 《星露谷物语》式项目提前约定各语言如何检查，是质量过程的一部分；逐项检查一份具体候选版本，是结果检查。QA／QC 的岗位边界依团队而异 | [质量与测试](#testing-comparison) |
| 关键路径 Critical Path | 《80 Days》式项目的“文本导出→翻译→语言测试”可能决定工期；《A Short Hike》里通向登顶目标的必要路线，是关卡语境下的关键路线 | [计划](#phase-2)、[关卡](#levels-animation) |
| 原型／切片／Demo／抢先体验 | 《Hollow Knight》式色块房间可验证跳跃，目标品质房间可验证生产，选定片段可用于公开试玩；抢先体验还意味着在正式完成前持续公开提供版本 | [样板比较](#prototype-comparison)、[发行](#phase-7) |
| Alpha／Beta／RC／Early Access | 《Baba Is You》式项目可用 Alpha、Beta 表示约定的成熟度，用 RC 指待发布的具体候选；Early Access 指公开提供未完成作品的发行安排。它们不是统一必经的四级顺序 | [版本与发布](#phase-7) |
| 实时三维／三维预渲染 | 《Outer Wilds》根据玩家视角实时生成画面；《Dead Cells》把三维动作预先输出成二维帧。最终画面是二维，源工程仍可能包含三维制作 | [美术](#visual-production) |
| 状态／标记／存档 | 《Hades》式对白中，“正在交谈”是状态，“见过某人”可由标记记录；哪些记录要在退出后保留，才进入存档设计 | [状态](#runtime)、[叙事](#narrative-audio) |
| 存档／版本管理／备份 | 《星露谷物语》式存档保存玩家农场；版本管理记录开发者怎样修改作物规则；备份在文件或设备损坏后提供可恢复副本 | [程序](#runtime)、[协作](#phase-5) |
| Build／Deploy／Release／Rollback | 《Baba Is You》式网页项目生成可运行文件是构建，放到托管环境是部署，开放入口是发布；出错后恢复旧版是回退，还须检查较新存档能否读取 | [发布](#phase-7)、[维护](#phase-8) |

这条流程最终连接的是：**概念确定取舍，规则定义行为，原型验证体验，切片验证生产，正式制作扩展内容，测试提供发布依据，维护保证后续可用。** 查到单个术语后，可以回到它所在的阶段，确认前提、交付和下一步。

<a id="references"></a>

## 参考资料与继续查阅

案例制作事实来自开发者、工具作者或官方平台；玩法和成本比较是本文分析。工具与发布条件会变化，具体操作使用对应版本的官方文档。资料核对：2026-10-15。

<a id="ref-1"></a>

**[1] Adam Robinson-Yu. _Crafting a Tiny Open World: A Short Hike Postmortem_. GDC 2020.** [演讲入口](https://gdcvault.com/play/1026613/Independent-Games-Summit-Crafting-A)。英文，标为免费内容。看范围、期限、画面和关卡怎样共同决定制作方式。

<a id="ref-2"></a>

**[2] Supergiant Games. _Hades FAQ_.** [官方说明](https://www.supergiantgames.com/blog/hades-faq/)。英文，免费。查抢先体验、叙事组织与 God Mode；本文讨论初代《Hades》。

<a id="ref-3"></a>

**[3] Joseph Humfrey. _Ink: The Narrative Scripting Language Behind 80 Days and Sorcery!_. GDC 2016.** [演讲幻灯片](https://media.gdcvault.com/gdc2016/Presentations/Humfrey_Joseph_Ink_The_Narrative.pdf)。英文，免费。看对白、条件、分支和游戏状态的连接；具体工具见 [ink 文档](https://www.inklestudios.com/ink/)。

<a id="ref-4"></a>

**[4] Nintendo. _Iwata Asks: Splatoon — It Started With Tofu_.** [英文访谈](https://iwataasks.nintendo.com/interviews/wiiu/splatoon/0/1/) · [日文访谈](https://www.nintendo.co.jp/wiiu/interview/agmj/vol1/index2.html)。英文、日文，免费。看喷墨、隐藏与角色形态如何相互影响。

<a id="ref-5"></a>

**[5] Arvi Teikari / Hempuli. _Baba Is You (Jam Build)_.** [作者保留的可玩版本](https://hempuli.itch.io/baba-is-you)。英文，原型可免费体验。可与正式版比较规则表达和内容扩展。

<a id="ref-6"></a>

**[6] Unity / Team Cherry. _Hollow Knight — Made with Unity_.** [制作访谈](https://unity.com/made-with-unity/hollow-knight)。英文，免费。查 Photoshop、PNG 和 Unity 的分工。

<a id="ref-7"></a>

**[7] Unity / Studio MDHR. _Cuphead — Made with Unity_.** [制作访谈](https://unity.com/made-with-unity/cuphead)。英文，免费。查纸上动画、数字上色与游戏集成。

<a id="ref-8"></a>

**[8] Thomas Vasseur. _Art Design Deep Dive: Using a 3D Pipeline for 2D Animation in Dead Cells_（2018）.** [开发者原文](https://www.gamedeveloper.com/production/art-design-deep-dive-using-a-3d-pipeline-for-2d-animation-in-i-dead-cells-i-)。英文，免费。看三维动作转二维帧及其修改方式与局限。

<a id="ref-9"></a>

**[9] Microsoft. _Playwright: Emulation_.** [官方文档](https://playwright.dev/docs/emulation)。英文，免费。查浏览器设备模拟的配置范围；真机检查另行安排。

<a id="ref-10"></a>

**[10] Maddy Thorson. _Celeste & Forgiveness_.** [作者原文](https://www.mattmakesgames.com/articles/celeste_and_forgiveness/index.html)。英文，免费，附动作示例。对照离边跳跃、输入缓冲和边角修正。

<a id="ref-11"></a>

**[11] Valve. _Steamworks: Review Process_.** [官方文档](https://partner.steamgames.com/doc/store/review_process)。英文，免费。分别查商店页与构建审核。

<a id="ref-12"></a>

**[12] MDN. _Autoplay Guide for Media and Web Audio APIs_.** [文档](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Autoplay)。英文，免费。查首次进入时声音启动的条件。

<a id="ref-13"></a>

**[13] MDN. _Window: localStorage_.** [文档](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)。英文，免费。查本地保存、网站来源和浏览器存储行为。

<a id="ref-14"></a>

**[14] Larian Studios. _Hotfix #4: Redeployed_（2023-08-17）.** [官方新闻](https://baldursgate3.game/news/hotfix-4-redeployed_86) · [Steam 官方公告存档](https://store.steampowered.com/news/posts/?appids=1086940&enddate=1692960041&feed=steam_community_announcements)。英文，免费。看重新构建、候选验证与存档兼容。

<a id="ref-15"></a>

**[15] ConcernedApe. _Stardew Valley 1.5.5 Released on PC_（2021-11-30）.** [作者公告](https://www.stardewvalley.net/stardew-valley-1-5-5-released-on-pc/)。英文，免费。看技术迁移、本地化与功能修复怎样进入同一版本。

<a id="ref-16"></a>

**[16] Unity. _用語集 / Glossary_.** [日文术语集](https://docs.unity3d.com/ja/current/Manual/Glossary.html)。免费，可切换语言；用于核对运行、图形等常见名称，具体含义以所用版本为准。

<a id="ref-17"></a>

**[17] Blender Foundation. _Blender Manual: Glossary_.** [日文](https://docs.blender.org/manual/ja/latest/glossary/index.html) · [英文](https://docs.blender.org/manual/en/latest/glossary/index.html)。免费，用于继续查三维、渲染和动画用语。

<a id="ref-18"></a>

**[18] Dan Golding. _Finding Untitled Goose Game’s Dynamic Music in the World of Silent Cinema_（2021）.** [作者论文与摘要](https://research.monash.edu/en/publications/finding-untitled-goose-games-dynamic-music-in-the-world-of-silent/) · [2020 年会议摘要 PDF](https://digraa.org/wp-content/uploads/2020/01/DiGRAA_2020_paper_47.pdf)。英文；摘要免费，期刊全文获取条件另查。看预录音乐怎样响应游戏行动。

<a id="ref-19"></a>

**[19] Mobius Digital. _Outer Wilds_.** [官方介绍](https://www.mobiusdigitalgames.com/outer-wilds.html)。英文，免费。核对时间循环、变化的星球与探索工具；本文据此分析知识和行动的关系。

<a id="ref-20"></a>

**[20] Wube Software. _Friday Facts #188 — Bug, Bug, Desync_（2017）.** [开发记录](https://www.factorio.com/blog/post/fff-188)。英文，免费。看确定性锁步、不同步报告与复现条件。

<a id="ref-21"></a>

**[21] Mojang Studios. _What Is Minecraft?_.** [官方介绍](https://www.minecraft.net/en-us/about-minecraft)。英文，免费。查方块、红石、游玩模式及 Java／Bedrock 的平台与互联范围。

<a id="ref-22"></a>

**[22] Microsoft / Mojang Studios. _World Generation Overview_；_Minecraft Snapshot 21w41a_.** [世界生成文档](https://learn.microsoft.com/en-us/minecraft/creator/documents/world-generation) · [生成器变更公告](https://www.minecraft.net/en-us/article/minecraft-snapshot-21w41a)。英文，免费。查种子与生成规则的关系，并理解为何复现时还要记录版本。

### 需要系统学习时

| 资料 | 阅读重点与获取方式 |
| --- | --- |
| [Tracy Fullerton：Game Design Workshop](https://www.routledge.com/Game-Design-Workshop-A-Playcentric-Approach-to-Creating-Innovative-Games/Fullerton/p/book/9781032607009) | 体验目标、原型、试玩与迭代；英文教材，购买或借阅 |
| [MIT CMS.608：Game Design](https://ocw.mit.edu/courses/cms-608-game-design-fall-2010/) | 通过规则、非数字原型和项目练习理解设计；英文公开课程，资料免费 |
| [Pro Git](https://git-scm.com/book/en/v2) | 提交、分支、协作与恢复；英文在线全文免费 |
| [Xbox Accessibility Guidelines](https://learn.microsoft.com/gaming/accessibility/guidelines) | 按文字、输入、声音等检查实际体验；英文官方指南，免费 |

[查软件、文件与工具搭配：002](posts-2026-umwelt-game-development-handbook-002.html) · [返回术语与流程目录](#overview) · [返回个人笔记目录](../index.html)
