---
id: "posts-2026-umwelt-game-development-handbook-002"
title: "游戏开发软件地图手册｜ChatGPT 写给五月七日的指导笔记 002"

module: "posts"
submodule: "2026"
topic: "umwelt-game-development-handbook"

type: "note"
status: "active"
canonical: true

summary: |
  按 25 类用途认识游戏开发中的软件、引擎、语言、程序库与在线服务，分别标注开放情况和费用类型。解释职责与组合，附知名游戏案例、教材和官方学习资源，以及《等足目赋格》的实际技术对应。

parents: ["posts-index"]
related: ["posts-2026-umwelt-game-development-handbook-001", "posts-2026-umwelt-game-development-handbook-003", "posts-2026-umwelt-game-development-handbook-004", "posts-2026-umwelt-game-development-handbook-005", "posts-2026-umwelt-game-development-handbook-006", "posts-2026-umwelt-game-development-handbook-007"]
tags: ["game-development", "software", "tools", "game-engine", "licensing", "cost", "handbook"]
audience: ["self", "public"]
languages: ["zh"]
maturity: "evolving"
confidence: 0.9
visibility: "public"
source_of_truth: "devlog"
lang: "zh-CN"
description: "按用途查阅游戏开发工具，直观比较开放情况、费用类型、职责与制作路线，并以等足目赋格作实际对应。"
canonical_url: "https://devlog.fivsevn.com/posts/2026/posts-2026-umwelt-game-development-handbook-002.html"
created: "2026-10-13"
updated: "2026-10-13"
metadata_updated: "2026-10-13"
---

# 游戏开发软件地图手册｜ChatGPT 写给五月七日的指导笔记 002

**游戏开发工具的用途、关系与成本 · 撰写：ChatGPT · 2026-10-13**

[001 制作流程](posts-2026-umwelt-game-development-handbook-001.html) · **002 软件与成本** · [003 运行原理](posts-2026-umwelt-game-development-handbook-003.html) · [004 画面与动画](posts-2026-umwelt-game-development-handbook-004.html) · [005 玩法与叙事](posts-2026-umwelt-game-development-handbook-005.html) · [006 修改与发布](posts-2026-umwelt-game-development-handbook-006.html) · [007 研究与表达](posts-2026-umwelt-game-development-handbook-007.html)

一款游戏可以使用 Unity 组织场景和运行逻辑，用 C# 编写行为，在 Blender 中制作模型，再通过 Steam 分发。这些名称分别对应**游戏引擎、编程语言、资源制作软件和发布平台**，不是同一类工具。

本篇按用途整理个人、小团队和大型制作中可能接触的主要工具类别，同时收录语言、程序库和在线服务。它不要求全部安装，也不声称收尽全球所有插件和内部工具。学习重点是职责、输出、连接和成本，而非各软件的操作步骤。

工具链接指向官网、官方文档或作者项目；特别容易混淆的许可另附专门入口。**资料核对日期为 2026-10-13。费用栏记录计费形式，不是含税报价，也不保证未来价格、资格或平台支持不变。** 本表不是逐份许可证的法律审查，采用前仍应核对目标版本和实际用途。

<a id="start"></a>
## 基本概念：引擎、语言与工具的职责

| 名词 | 定义 | 解释 |
| --- | --- | --- |
| 游戏引擎 | 提供游戏运行所需的一组基础系统，通常配有制作工具 | 提供显示画面、播放声音和接收操作等能力，具体内容与规则由项目决定 |
| 编辑器 | 供开发者编辑代码、资源或场景的工具 | 用于摆放角色、修改脚本和调整动画，不一定具有完整游戏运行系统 |
| 编程语言 | 编写程序时遵循的表达规则 | 用规定的写法描述条件、操作和数据 |
| 库／程序库 | 可被程序调用的一组现成功能 | 项目使用已有功能减少重复开发，不是指图片素材库 |
| 框架 | 提供功能并约定程序组织方式的基础结构 | 项目按照框架安排内容和逻辑 |
| 插件 | 扩展现有软件功能的部件 | 通常依赖对应软件和版本，未必可以单独运行 |
| SDK／软件开发工具包 | 接入某个平台或功能的一套组件、说明和工具 | 例如将平台成就或动画功能接入项目 |
| API／应用程序接口 | 软件之间调用功能的约定 | 规定请求、参数和结果，本身不是必须购买的独立软件 |
| 运行时／Runtime | 游戏或功能实际执行时需要的程序部分 | 成品运行时加载资源并执行相应功能 |
| 中间件／Middleware | 接入项目、承担专门任务的技术 | 例如声音、物理、导航和联机系统 |
| 资源／Asset | 游戏使用的图像、模型、音频、字体等内容 | 由制作工具生成或整理，再由游戏读取 |
| 工具链／制作管线 | 配合使用的工具及其处理、交付流程 | 工具链侧重工具组合，管线侧重源内容到成品的步骤 |
| 技术栈 | 项目组合使用的技术 | 包括语言、框架、数据库和相关工具，不是单一产品 |

分类存在交叉。例如 [Phaser](https://docs.phaser.io/phaser/getting-started/what-is-phaser)自称游戏框架，同时以 JavaScript 库的形式提供。库、框架与引擎不能简单排列成高低等级，应按功能范围和组织方式区分。

以 Unity 为例，开发者在编辑器中摆放角色、设置场景和调整参数；玩家打开导出的游戏时，无需安装 Unity 编辑器，由随成品发布的引擎运行时加载资源、执行脚本并生成画面。角色台词与点击后的反应由项目内容和规则决定。**因此，编辑器负责供开发者制作和调整内容；引擎提供运行所需的基础系统，其运行时在玩家设备上执行相应功能。** 两者通常包含在同一产品中，但职责不同。[Unity 官方介绍](https://unity.com/products/unity-engine)

<a id="cost-legend"></a>
## 成本标注的读法

**开放情况说明源码与使用权的安排，费用类型说明获得软件或服务的成本。** 两者必须分开：免费可以闭源，开源也可以收费。

| 标注 | 解释 |
| --- | --- |
| 开源 | 按相应开源许可证提供代码及使用、修改、再分发等权利，仍需遵守条件 |
| 源码可见 | 可以按规定查看或修改源码，但不应自动称为符合开源定义 |
| 专有 | 主产品按厂商许可提供；可能包含开源组件，但整套产品不能因此视为开源 |
| 混合 | 核心、编辑器、插件、SDK 或云服务采用不同许可，需分开看 |
| 语言／标准 | 不是一套单独销售的软件；编译器、编辑器、SDK 和平台费用另计 |
| 免费 | 所列软件或核心功能不收使用费，不代表素材、服务器和人工免费 |
| 条件免费 | 收入、非商业用途、教育资格、团队规模或功能范围受到限制 |
| 免费＋付费 | 基础版或额度免费，扩展功能、托管或服务收费 |
| 买断／付费许可 | 为某个产品或版本购买使用权，后续升级和服务未必包含 |
| 订阅／按量／分成 | 分别按期限、资源用量或约定收入规则计费 |
| 内部／询价 | 没有适用于普通个人的统一公开获取方式或价格 |

“免费试用”不等于长期免费版本，“个人版”也不自动等于可以用于任何商业项目。表中“开源”主要描述所列核心软件，捆绑组件、商店资源和平台服务需分别确认。开源定义参照 [OSI](https://opensource.org/osd)。

**几个典型对照：** [Godot](https://godotengine.org/license/)是开源且免费；[Defold](https://defold.com/open/)免费但属于源码可见许可；[Aseprite](https://www.aseprite.org/faq/)的源码可查，官方成品付费且再分发有条件；[Ardour](https://ardour.org/faq.html)采用开源许可，但官方完整预编译成品可以收费；[Obsidian](https://obsidian.md/pricing)应用免费而非开源，可选同步和发布服务收费。

<a id="map"></a>
## 用途分类与章节索引

| 章节 | 主要内容 |
| --- | --- |
| [01 规划与资料](#tools-01) | 文档、参考图、文献与数值 |
| [02 通用引擎](#tools-02) · [03 专用工具](#tools-03) · [04 框架与图形库](#tools-04) | 游戏主体的制作与运行 |
| [05 语言与格式](#tools-05) · [06 编程工具](#tools-06) | 规则表达、代码编辑与构建 |
| [07 二维](#tools-07) · [08 三维](#tools-08) · [09 材质](#tools-09) · [10 场景](#tools-10) | 图像、模型、表面与环境 |
| [11 动画](#tools-11) · [12 渲染与特效](#tools-12) | 角色动作与最终画面 |
| [13 音频](#tools-13) · [14 叙事](#tools-14) · [15 界面与本地化](#tools-15) | 声音、文字、操作与语言 |
| [16 版本管理](#tools-16) · [17 制作协作](#tools-17) | 修改记录、任务与交接 |
| [18 测试与性能](#tools-18) · [19 中间件](#tools-19) | 验证与专门运行能力 |
| [20 联机与后台](#tools-20) · [21 发布](#tools-21) · [22 维护](#tools-22) | 服务、交付和运行反馈 |
| [23 宣传](#tools-23) · [24 素材与加工](#tools-24) · [25 AI 辅助](#tools-25) | 辅助制作环节 |
| [授权](#licensing) · [组合](#combinations) · [易混名称](#confusions) | 选择与比较 |
| [知名游戏案例](#known-games) · [参考资源](#sources) | 制作事实与进一步学习 |
| [《等足目赋格》对应](#case-isopoda) | 本项目的实际工具分工 |

初次阅读可以先看基本概念、02—06 和组合示例，其余按用途查阅。具体名称可用浏览器的页面查找功能定位。

<a id="tools-01"></a>
## 01｜规划、资料与数值

这一类用于记录设计、整理参考和计算数值，通常不直接负责游戏运行。文档或表格能否进入游戏，取决于项目有没有相应读取流程。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Word](https://www.microsoft.com/microsoft-365/word)、[Excel](https://www.microsoft.com/microsoft-365/excel) | 文档、资源表和数值计算 | 专有 | 网页基础功能与付费桌面／订阅方案并存，按版本区分 |
| [Google Docs](https://workspace.google.com/products/docs/)、[Sheets](https://workspace.google.com/products/sheets/) | 在线文档、表格与协作 | 服务 | 个人基础使用免费；Workspace、存储和管理能力有付费方案 |
| [LibreOffice Calc](https://www.libreoffice.org/) | 本地表格、公式与数据整理 | 开源 | 免费 |
| [Notion](https://www.notion.com/pricing)、[Obsidian](https://obsidian.md/pricing) | 知识、设定与设计记录 | 专有／服务 | Notion 免费＋订阅；Obsidian 应用免费，可选 Sync、Publish 付费 |
| [Miro](https://miro.com/pricing/)、[FigJam](https://www.figma.com/figjam/) | 白板、流程与关系图 | 专有／服务 | 免费＋付费协作或席位方案 |
| [draw.io／diagrams.net](https://www.drawio.com/) | 流程图、页面与系统关系 | 开源核心 | 核心免费；部分平台集成收费 |
| [PureRef](https://www.pureref.com/download.php) | 在同一画布排列视觉参考 | 专有 | 个人可自定价格；商业使用按团队类别付费，不是一概免费 |
| [Zotero](https://www.zotero.org/) | 文献、出处与引用管理 | 开源 | 本地软件免费；附件云存储扩容收费 |

**文档记录意图，数据记录内容，游戏程序读取已接入的数据并执行规则。** 在表格中新增一行，不等于游戏已经支持这个新对象。

<a id="tools-02"></a>
## 02｜通用游戏引擎

引擎提供图形、声音、输入、场景等基础系统。开发者利用它们组织内容与规则，不必从底层重复实现全部功能；游戏设计和验证仍由项目承担。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Unity](https://unity.com/products) | 通用二维／三维制作，脚本主要使用 C# | 专有 | 条件免费＋付费席位方案；公司资金和收入资格需核对 |
| [Unreal Engine／UE](https://www.unrealengine.com/en-US/license) | 三维场景、动画、物理和可视化逻辑 | 源码可见，专门许可 | 游戏按适用免费范围与分成条款；其他用途的席位规则不同 |
| [Godot](https://godotengine.org/license/) | 二维／三维，以场景和节点组织项目 | 开源，MIT | 免费；外部素材与平台适配另计 |
| [GameMaker](https://gamemaker.io/en/get) | 以二维为核心，通过对象、房间、事件组织内容 | 专有 | 非商业免费；商业许可付费，主机方案另计 |
| [GDevelop](https://gdevelop.io/pricing) | 事件式可视化游戏制作 | 开源核心＋服务 | 核心免费；云端构建、协作等有订阅与额度 |
| [Construct](https://www.construct.net/en/make-games/buy-construct) | 浏览器中的事件式二维制作 | 专有 | 受限免费版＋订阅 |
| [Clickteam Fusion](https://www.clickteam.com/clickteam-fusion-2-5) | 可视化事件组织游戏和应用 | 专有 | 付费许可，导出器与版本能力另看产品 |
| [Defold](https://defold.com/license/) | 编辑器、资源管线与 Lua 运行系统 | 源码可见 | 引擎免费、无游戏许可费或分成；引擎本身的再分发受条款约束 |
| [Cocos Creator](https://www.cocos.com/en/creator) | 二维／三维场景编辑与脚本开发 | 开源引擎核心，编辑器另许可 | 基础引擎路线免费；插件、服务及商业方案另计 |
| [LayaAir](https://www.layaair.com/) | 网页、小游戏等跨平台制作 | 开源内核，IDE 与扩展另看许可 | 内核免费；增值功能、插件与服务按产品 |
| [O3DE](https://o3de.org/)、[Stride](https://www.stride3d.net/) | 可扩展三维引擎；Stride 采用 C#／.NET 路线 | 开源 | 软件免费；生产与平台支持成本另计 |
| [Flax](https://flaxengine.com/licensing/) | 三维引擎、编辑器与脚本系统 | 源码可见，专门许可 | 免费适用范围＋达到条件后的分成，也有定制许可 |
| [Frostbite／寒霜](https://www.ea.com/frostbite)等公司自有引擎 | 为内部项目和管线维护的系统 | 内部专有 | 没有普通个人可统一购买的公开方案 |

团队规模不直接决定工具等级。个人可以使用完整三维引擎，大公司也可以使用公开通用引擎。**工具选择应对应需求与维护能力，而不是模仿另一家公司安装了多少软件。**

蓝图、事件表和可视化编程改变的是逻辑的编写方式。条件、顺序和结果仍需设计；少打代码不等于不需要程序逻辑。

<a id="tools-03"></a>
## 03｜专用制作工具与创作平台

专用工具预先提供某类作品需要的结构，例如对白、选项或地图事件。平台型工具还会与特定运行和发布环境绑定。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Ren’Py](https://www.renpy.org/) | 视觉小说、对白、选项和存档 | 开源 | 引擎免费，可商业使用；素材与附加组件另核对 |
| [RPG Maker／RPG 制作大师](https://www.rpgmakerweb.com/products/rpg-maker-mz) | 地图、角色、事件等预设系统 | 专有，部分脚本可见 | 付费许可，素材与插件另计；不同代产品不能混用 |
| [TyranoScript](https://tyranoscript.com/)、[TyranoBuilder](https://tyranobuilder.com/) | 视觉小说的脚本路线与图形化制作路线 | 前者开源，后者专有 | 前者免费；后者付费许可 |
| [Twine](https://twinery.org/) | 非线性文本与网页互动故事 | 开源 | 免费；故事格式和扩展许可另看 |
| [GB Studio](https://www.gbstudio.dev/)、[Bitsy](https://bitsy.org/) | 特定限制下的小型像素与叙事作品 | 开源 | 免费；目标平台和资源分别核对 |
| [PICO-8](https://www.lexaloffle.com/pico-8.php) | 集成代码、绘图与音效的“幻想主机” | 专有 | 付费许可；免费教育体验不等于完整发行版 |
| [TIC-80](https://tic80.com/) | 集成式幻想电脑创作环境 | 开源核心 | 基础免费；官方 Pro 等版本另收费 |
| [Roblox Studio](https://create.roblox.com/docs/studio) | 制作 Roblox 平台体验，脚本使用 Luau | 编辑器／平台专有，语言等组件开源 | 制作工具免费；平台交易、分配与发布规则另计 |
| [UEFN](https://dev.epicgames.com/documentation/en-us/fortnite/unreal-editor-for-fortnite) | 为 Fortnite 制作内容 | 专有平台工具 | 工具免费；发布资格和收益规则由平台规定 |

**作品风格、制作工具和发布平台分别描述不同对象。** 像素画面不证明使用 PICO-8，有文字选项也不证明使用 Ren’Py。

<a id="tools-04"></a>
## 04｜框架、图形库与代码型引擎

这些工具主要通过代码调用，不一定配备完整的可视化编辑器。功能范围从基础图形、输入，到较完整的游戏结构不等。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Three.js](https://threejs.org/) | JavaScript 三维图形库，处理相机、模型、灯光等 | 开源 | 核心免费；不是另一种编程语言 |
| [Babylon.js](https://www.babylonjs.com/) | 网页三维引擎与配套工具 | 开源 | 核心免费 |
| [PlayCanvas](https://playcanvas.com/plans) | 网页三维引擎与在线协作编辑 | 引擎及编辑器前端开源；托管服务另计 | 引擎免费；编辑服务有免费与付费方案 |
| [Phaser](https://docs.phaser.io/phaser/getting-started/what-is-phaser) | 二维网页游戏框架 | 开源核心 | 核心免费；配套编辑器和商业服务另计 |
| [PixiJS](https://pixijs.com/) | 二维绘制与显示 | 开源 | 免费；完整玩法仍需组织 |
| [raylib](https://www.raylib.com/) | 图形、输入与音频开发库 | 开源 | 免费 |
| [SDL](https://www.libsdl.org/)、[SFML](https://www.sfml-dev.org/) | 跨平台窗口、输入、图形与音频基础能力 | 开源 | 免费；具体捆绑组件按许可 |
| [LÖVE](https://love2d.org/)、[Solar2D](https://solar2d.com/) | Lua 路线的二维框架或引擎 | 开源 | 核心免费；插件或服务可能另计 |
| [MonoGame](https://monogame.net/)、[libGDX](https://libgdx.com/) | 分别用于 .NET 和 Java 路线的游戏框架 | 开源 | 核心免费；主机支持与平台条件另核对 |
| [Bevy](https://bevy.org/)、[HaxeFlixel](https://haxeflixel.com/) | Rust 引擎与 Haxe 二维框架 | 开源 | 核心免费 |
| [React](https://react.dev/)、[Vue](https://vuejs.org/)、[Svelte](https://svelte.dev/) | 网页界面组织，不是专门的游戏引擎 | 开源 | 核心免费；云服务与商业扩展另计 |

例如 React 可以负责菜单与界面，Three.js 负责三维内容，两者由项目代码连接。**界面库组织控件，图形库处理画面，游戏规则由项目安排。** 简单互动也可以直接使用 HTML、CSS 与 JavaScript，不必增加框架。[MDN 网页技术说明](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/What_is_JavaScript)

<a id="tools-05"></a>
## 05｜语言、数据格式与图形技术

语言规定表达方式，工具实现编写与执行。**下表名称本身不是需要逐一购买的制作软件；相应编辑器、编译器、引擎或平台可能收费。**

| 名称 | 类别与主要用途 | 成本对应 |
| --- | --- | --- |
| [JavaScript／JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript)、[TypeScript／TS](https://www.typescriptlang.org/) | 网页交互、工具和服务；TS 增加类型等开发能力 | 有免费的开放实现，TS 工具开源；平台服务另计 |
| [C#](https://learn.microsoft.com/en-us/dotnet/csharp/)、[C++](https://isocpp.org/)、C | 游戏、引擎、系统与原生工具开发中的不同语言 | 语言不按游戏收许可费；编译器、引擎和工具各有许可 |
| [GDScript](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html)、[GML](https://manual.gamemaker.io/monthly/en/GameMaker_Language/GameMaker_Language_Index.htm) | 分别用于 Godot 与 GameMaker 的规则表达 | 前者随开源 Godot；后者按 GameMaker 使用方案 |
| [Lua](https://www.lua.org/about.html)、[Luau](https://luau.org/) | 嵌入式脚本，以及 Roblox 等环境的语言 | 语言实现开源；接入平台不因此成为开源或无费用 |
| [Python](https://www.python.org/about/) | 自动化、资源整理、测试、后台及部分叙事工具 | 开放实现可免费使用；服务与具体产品另计 |
| [Rust](https://www.rust-lang.org/)、[Haxe](https://haxe.org/) | 通用语言，对应 Bevy、HaxeFlixel 等路线 | 有免费开源工具链 |
| [Java](https://dev.java/)、[Kotlin](https://kotlinlang.org/)、[Swift](https://www.swift.org/) | 游戏框架与移动、桌面平台开发 | 有开源工具；Java 发行版和商业支持须分别确认 |
| [Verse](https://dev.epicgames.com/documentation/en-us/fortnite/verse-language-reference) | Epic 创作环境中的语言 | 使用环境与平台条款另看，不能当作完整引擎 |
| [HTML、CSS](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/What_is_JavaScript) | 网页结构与样式 | 标准本身不收制作软件费；浏览器执行相应内容 |
| [SQL](https://www.postgresql.org/docs/current/tutorial-sql.html) | 查询和操作关系数据库的语言 | 数据库产品和托管服务可能收费，不是 SQL 本身的价格 |
| [HLSL](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl)、[GLSL](https://www.khronos.org/opengl/wiki/Core_Language_(GLSL))、[WGSL](https://www.w3.org/TR/WGSL/) | 编写着色器，描述部分图形计算 | 语言与图形平台不同层次，实际工具链另看许可 |

| 其他名称 | 解释 |
| --- | --- |
| JSON、CSV、YAML、TOML | 数据或配置格式，例如对白表和设置，不是完整游戏引擎 |
| Markdown／`.md` | 用简单标记组织文档，本博客源文采用的格式 |
| WebGL、WebGPU、OpenGL、Vulkan、Direct3D、Metal | 图形接口或标准，引擎与图形库可以借助它们工作 |
| WebAssembly／Wasm | 一种执行格式和编译目标，不是专门的三维引擎 |

以网页三维为例，Three.js 提供三维功能，WebGL／WebGPU 提供相关底层图形接口，GLSL／WGSL 用于表达相关计算。**这里分别是功能库、接口和语言，不是三套互相替代的游戏编辑器。** [WebGL](https://www.khronos.org/webgl/) · [WebGPU](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API)

<a id="tools-06"></a>
## 06｜代码编辑、编译与依赖管理

这一类负责编写、检查、处理和运行代码。了解职责即可，不需要为了认识工具而学习每套语法和命令。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [VS Code](https://code.visualstudio.com/docs/supporting/faq) | 编辑代码、查找文件和使用扩展 | Code OSS 核心开源，微软发行版另许可 | 软件免费；扩展和 AI 服务可能另计 |
| [Visual Studio](https://visualstudio.microsoft.com/) | 集成开发、运行和调试 | 专有 | Community 条件免费；其他版本付费 |
| [Rider](https://www.jetbrains.com/rider/buy/) | .NET 与游戏开发工作环境 | 专有 | 非商业用途免费；商业使用订阅 |
| [Xcode](https://developer.apple.com/xcode/) | Apple 平台开发、构建与调试 | 主应用专有，部分工具开源 | 工具免费；设备和正式开发者发布资格另计 |
| [Android Studio](https://developer.android.com/studio) | Android 开发与平台调试 | 开源基础，捆绑 SDK 等另许可 | 工具免费；商店账号和服务另计 |
| [Node.js](https://nodejs.org/en/about)、[.NET](https://dotnet.microsoft.com/learn/dotnet/what-is-dotnet) | JavaScript 与 .NET 程序的运行／开发环境 | 开源核心 | 核心免费；托管与商业支持另计 |
| [npm](https://docs.npmjs.com/about-npm/)、[pnpm](https://pnpm.io/)、[Yarn](https://yarnpkg.com/) | JavaScript 依赖管理 | 开源客户端；注册表服务另看 | 工具免费；私有包与企业服务可能付费 |
| [pip](https://pip.pypa.io/en/stable/)、[NuGet](https://learn.microsoft.com/en-us/nuget/what-is-nuget)、[Cargo](https://doc.rust-lang.org/cargo/) | Python、.NET、Rust 等生态的包管理 | 开源核心 | 工具免费；所安装的包按各自许可 |
| [Vite](https://vite.dev/guide/)、[webpack](https://webpack.js.org/) | 网页开发预览与构建 | 开源 | 免费 |
| [GCC](https://gcc.gnu.org/)、[Clang](https://clang.llvm.org/) | 编译程序 | 开源 | 免费；运行结果和附加库许可需区分 |
| [MSVC](https://learn.microsoft.com/en-us/cpp/overview/visual-cpp-in-visual-studio) | Microsoft C／C++ 工具链 | 专有 | 按所用工具包和开发许可；不等于一定要购买完整 IDE |
| [CMake](https://cmake.org/)、[Gradle](https://gradle.org/)、[MSBuild](https://learn.microsoft.com/en-us/visualstudio/msbuild/msbuild) | 安排构建步骤与依赖 | 开源核心 | 核心免费；商业加速、分析等服务另计 |
| [Emscripten](https://emscripten.org/) | 将相应程序处理为网页等目标形式 | 开源 | 免费；移植与兼容工作仍有成本 |
| [PowerShell](https://learn.microsoft.com/en-us/powershell/)、[Bash](https://www.gnu.org/software/bash/)等 | 通过文字命令操作文件和启动任务 | 当前开源核心；系统内置版本另看 | 通常无需另购；“终端”本身也是工具类别名称 |

**编辑器提供编写界面，运行环境执行程序，包管理器获取组件，构建工具组织处理。** 依赖越多，版本和许可维护也越需要明确，而不是工具数量越多越专业。

<a id="tools-07"></a>
## 07｜二维绘图与像素画

二维绘图制作平面资源，像素画工具侧重像素级绘制与动画帧。图像的触发时机与交互仍由游戏控制。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Photoshop／PS](https://www.adobe.com/products/photoshop.html) | 图像、绘画、合成与贴图 | 专有 | 桌面完整制作主要为订阅，部分免费功能与试用另看 |
| [Clip Studio Paint／CSP](https://www.clipstudio.net/en/) | 插画、漫画、角色差分和二维动画 | 专有 | 买断或订阅依平台与版本，升级另看 |
| [Krita](https://krita.org/en/)、[GIMP](https://www.gimp.org/) | 数字绘画与综合图像编辑 | 开源 | 官网软件免费；部分商店发行可收费 |
| [Procreate](https://procreate.com/procreate) | iPad 绘画 | 专有 | 付费购买，设备另计 |
| [Illustrator／AI](https://www.adobe.com/products/illustrator.html) | 矢量图标、标志与图形 | 专有 | 订阅；这里的 AI 指产品简称 |
| [Inkscape](https://inkscape.org/) | 矢量绘图 | 开源 | 免费 |
| [Affinity](https://www.affinity.studio/) | 统一的矢量、像素与版面制作 | 专有 | 当前应用免费；相关 AI 和服务资格另看；旧三款产品的许可不可直接套用 |
| [Aseprite](https://www.aseprite.org/faq/) | 像素绘图和逐帧动画 | 源码可见，专门许可 | 官方成品付费；自行构建及再分发按条款 |
| [LibreSprite](https://libresprite.github.io/)、[Piskel](https://www.piskelapp.com/)、[Pixelorama](https://orama-interactive.itch.io/pixelorama) | 像素绘图与动画 | 开源 | 免费获取路线；部分商店版本付费支持开发 |

位图记录像素，矢量图记录曲线与形状；差分是同一角色的不同图像版本，逐帧动画是连续播放一组画面。**制作工具产出资源，游戏程序按状态选择显示哪一份资源。**

<a id="tools-08"></a>
## 08｜三维建模与雕刻

建模建立立体形状，雕刻通过推拉表面塑造细节。DCC／数字内容创作工具是这类软件的总称，不是另一个产品。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Blender](https://www.blender.org/about/license/) | 建模、雕刻、动画、渲染等 | 开源 | 软件免费；插件与服务另计 |
| [Maya](https://www.autodesk.com/products/maya/overview)、[3ds Max](https://www.autodesk.com/products/3ds-max/overview) | 综合三维制作 | 专有 | 订阅等商业方案；教育与独立资格另核对 |
| [Cinema 4D](https://www.maxon.net/en/cinema-4d)、[ZBrush](https://www.maxon.net/en/zbrush) | 分别侧重综合三维／动态图形与雕刻 | 专有 | 付费，当前产品方案以订阅为主，旧许可另看 |
| [Nomad Sculpt](https://nomadsculpt.com/) | 数字雕刻 | 专有 | 付费许可，按平台获取 |
| [3DCoat](https://3dcoat.com/) | 雕刻、重拓扑、UV 与贴图 | 专有 | 付费许可／订阅等方案，试用另看 |
| [Blockbench](https://blockbench.net/) | 低多边形、方块风格的建模和动画 | 开源 | 免费 |
| [MagicaVoxel](https://ephtracy.github.io/) | 按三维格子组织体素形体 | 专有免费工具 | 免费使用，具体许可仍需遵守 |

网格由点、边和面组成，拓扑描述它们的连接，重拓扑是调整这些连接以适合变形或运行。**制作时使用三维软件，不代表成品必须实时运行三维模型**；也可以先导出图片，再由二维游戏显示。

<a id="tools-09"></a>
## 09｜贴图、材质、UV 与烘焙

贴图提供颜色、粗糙程度等信息，材质规定表面表现，UV 建立表面与二维图片的位置关系，烘焙将部分计算结果提前保存。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Substance 3D Painter](https://www.adobe.com/products/substance3d/apps/painter.html) | 在模型上制作颜色、磨损与表面贴图 | 专有 | 订阅；部分渠道的版本许可另看 |
| [Substance 3D Designer](https://www.adobe.com/products/substance3d/apps/designer.html)、[Sampler](https://www.adobe.com/products/substance3d/apps/sampler.html) | 节点式材质生成，以及从图像制作材质 | 专有 | 付费产品／套件方案，渠道与版本分别确认 |
| [ArmorPaint](https://armorpaint.org/) | 三维表面绘制与烘焙 | 开源项目 | 源码可免费构建；官方成品按渠道付费 |
| [Mari](https://www.foundry.com/products/mari) | 三维贴图制作 | 专有 | 商业版付费；非商业版有限制 |
| [Material Maker](https://www.materialmaker.org/) | 节点式材质生成 | 开源 | 免费 |
| [RizomUV](https://www.rizomuv.com/) | UV 展开与排布 | 专有 | 付费许可／订阅等方案 |
| [Marmoset Toolbag](https://marmoset.co/) | 展示、渲染、烘焙与表面检查 | 专有 | 付费许可，版本与团队方案另看 |

节点是代表操作或数据的图形单元，连线表达流向。材质节点与逻辑蓝图可以外观相似，但分别处理不同对象。**模型负责几何形状，贴图参与表面表现；烘焙并没有把所有几何细节复制到低面数模型上。**

<a id="tools-10"></a>
## 10｜场景、地形与关卡

场景制作侧重环境内容，关卡设计还涉及路线、障碍、触发和节奏。制作地图数据，与实现地图中的规则是不同环节。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| 引擎内置场景编辑器 | 安排对象、光照和触发区域 | 随对应引擎 | 随引擎许可；外部插件可能另购 |
| [Houdini](https://www.sidefx.com/buy/) | 用规则制作或处理三维资源 | 专有 | 商业版付费，Indie 有资格限制，Apprentice 免费但非商业 |
| [Gaea](https://quadspinner.com/)、[World Machine](https://www.world-machine.com/) | 地形、高度图与表面生成 | 专有 | 受限免费版＋付费版本 |
| [World Creator](https://www.world-creator.com/) | 地形制作 | 专有 | 付费许可，试用与升级条件另看 |
| [SpeedTree](https://unity.com/products/speedtree) | 树木、植被和相关资源 | 专有 | 付费方案，游戏用途与其他版本分别核对 |
| [Tiled](https://www.mapeditor.org/)、[LDtk](https://ldtk.io/) | 二维图块、对象与关卡数据编辑 | 开源 | 软件免费；捐赠或商店支持不等于强制许可费 |
| [TrenchBroom](https://trenchbroom.github.io/) | 面向 Quake 系等格式的三维关卡编辑 | 开源 | 免费；不是通用模型雕刻工具 |

瓦片是可重复拼接的图块，高度图用数值记录地面高低，触发器在条件成立时启动行为。**地图编辑器生成布局数据，游戏程序解释这些数据并执行显示、碰撞和交互。**

<a id="tools-11"></a>
## 11｜角色、绑定、动画与动作捕捉

绑定建立控制结构，骨骼动画通过骨架带动形体，动作捕捉记录真实动作。完成动作资源，不等于已经接入游戏状态。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Live2D Cubism](https://www.live2d.com/en/cubism/comparison/) | 二维角色变形、表情和动作 | 编辑器专有；SDK 专门许可 | 受限 FREE＋付费 PRO；SDK 发布条件另核对 |
| [Spine](https://esotericsoftware.com/spine-purchase) | 二维骨骼动画 | 编辑器专有，运行组件专门许可 | 编辑器付费；试用不等于正式导出资格 |
| [Rive](https://rive.app/pricing) | 可交互动画与界面 | 编辑工具／服务与开源运行组件分开 | 免费＋付费导出、协作等方案 |
| [Moho](https://moho.lostmarble.com/)、[Toon Boom Harmony](https://www.toonboom.com/products/harmony) | 二维绑定或逐帧动画 | 专有 | Moho 付费许可；Harmony 订阅等付费方案 |
| [OpenToonz](https://opentoonz.github.io/e/) | 二维动画生产 | 开源 | 免费 |
| Blender、Maya | 三维绑定和动作 | 分别开源／专有 | 分别免费／付费，见 08 |
| [Cascadeur](https://cascadeur.com/plans) | 角色姿态、动作辅助与清理 | 专有 | 免费版非商业且导出有限；付费方案按资格和功能区分 |
| [Character Creator](https://www.reallusion.com/character-creator/)、[iClone](https://www.reallusion.com/iclone/) | 角色生成、表演、动作与场景演出 | 专有 | 付费许可或订阅；素材与导出许可另核对 |
| [VRoid Studio](https://vroid.com/en/studio) | 风格化人形角色制作 | 专有软件 | 工具免费；附加素材许可另看 |
| [MetaHuman](https://www.metahuman.com/license) | 数字人及相关动画工作流 | 按 Unreal 等专门许可 | 条件免费，达到条件后适用相应许可；不应笼统限制为只能在 UE 使用 |
| [Marvelous Designer](https://www.marvelousdesigner.com/) | 三维服装与布料模拟 | 专有 | 付费方案，商业资格与团队规模需确认 |
| [Mixamo](https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html) | 双足人形自动绑定与动作资源 | 专有服务 | 服务可免费使用；对象范围和资源条款另看 |
| [Rokoko Studio](https://www.rokoko.com/products/studio) | 动作数据采集、清理与输出 | 专有 | 基础免费＋付费能力；捕捉硬件另计 |
| [Vicon Shogun](https://www.vicon.com/software/shogun/)、[OptiTrack Motive](https://www.optitrack.com/software/motive) | 捕捉系统中的动作处理 | 专有 | 商业许可或硬件方案，需按配置询价 |

关键帧记录重要时刻的状态，重定向把动作映射到另一套骨架。**编辑器制作动作，运行组件使动作可被游戏调用，游戏规则决定何时播放或中断。** 软件许可、SDK 许可、角色素材许可不一定是同一份文件。

<a id="tools-12"></a>
## 12｜扫描、渲染与特效

扫描与重建获取形体，渲染根据场景数据计算画面，特效增加动态表现。实时渲染与预先输出图像的离线渲染，服务于不同运行需求。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [RealityScan](https://www.realityscan.com/license) | 照片等输入的三维重建，桌面旧称 RealityCapture | 专有 | 桌面条件免费＋付费；Mobile 是需分别判断的产品 |
| [Agisoft Metashape](https://www.agisoft.com/) | 摄影测量与三维重建 | 专有 | 付费许可 |
| [Meshroom／AliceVision](https://alicevision.org/) | 三维重建框架和图形工作流 | 开源 | 软件免费；计算与数据整理另计 |
| [Cycles](https://docs.blender.org/manual/en/latest/render/cycles/index.html)、[Eevee](https://docs.blender.org/manual/en/latest/render/eevee/index.html) | Blender 中的不同渲染系统 | 开源组件 | 随 Blender 免费 |
| [Arnold](https://www.autodesk.com/products/arnold/overview)、[V-Ray](https://www.chaos.com/vray)、[Redshift](https://www.maxon.net/en/redshift) | 三维画面渲染 | 专有 | 付费许可／订阅；随软件包含的使用范围另看 |
| [Niagara](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine)、[Unity Visual Effect Graph](https://unity.com/features/visual-effect-graph) | 对应引擎中的特效制作 | 随所属引擎许可 | 通常按引擎方案使用，不是另一套完整引擎 |
| [Effekseer](https://effekseer.github.io/en/) | 特效编辑与运行集成 | 开源 | 免费 |
| [PopcornFX](https://www.popcornfx.com/) | 特效制作与跨项目集成 | 专门商业许可 | 编辑器与运行 SDK 按用途、版本和资格分别核对，商业集成可能收费 |

粒子系统管理元素的产生、移动与消失，例如火星和烟尘，但不是所有视觉特效都是粒子。**渲染负责生成画面，玩法系统负责使画面与状态、操作保持对应。**

<a id="tools-13"></a>
## 13｜录音、作曲、音效与交互音频

DAW／数字音频工作站制作和编辑声音，音频中间件安排游戏运行时的动态播放。两者不是同一种播放器。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Audacity](https://www.audacityteam.org/) | 录音、剪辑和音频处理 | 开源 | 免费 |
| [Adobe Audition](https://www.adobe.com/products/audition.html) | 音频编辑、修复和后期 | 专有 | 订阅 |
| [REAPER](https://www.reaper.fm/) | 多轨录音、编辑与混音 | 专有 | 付费许可，有评估期；不能将可继续试用理解为永久免费 |
| [Pro Tools](https://www.avid.com/pro-tools) | 综合音频制作 | 专有 | 免费入门与付费许可／订阅按版本区分 |
| [Cubase](https://www.steinberg.net/cubase/)、[Nuendo](https://www.steinberg.net/nuendo/) | 音乐、音效与媒体音频制作 | 专有 | 付费许可，升级和资源另计 |
| [Logic Pro](https://www.apple.com/logic-pro/) | Apple 平台音乐制作 | 专有 | Mac 单独购买或适用套件订阅，平台方案需区分 |
| [Ableton Live](https://www.ableton.com/en/live/)、[FL Studio](https://www.image-line.com/fl-studio) | 编曲、乐器与节奏制作 | 专有 | 付费版本／许可，附加内容另计 |
| [Ardour](https://ardour.org/faq.html) | 多轨录音与混音 | 开源 | 源码可免费获取；官方完整成品与更新支持有付费路线 |
| [ChipTone](https://sfbgames.itch.io/chiptone) | 复古短音效生成 | 免费工具，未在本表确认开源许可 | 免费使用不等于源码可任意再分发 |
| [FamiStudio](https://famistudio.org/) | 特定复古音源风格音乐 | 开源 | 软件免费 |
| [Soundly](https://getsoundly.com/) | 音效检索、管理与相关制作 | 专有／服务 | 免费＋订阅，音效库许可另看 |
| [FMOD Studio](https://www.fmod.com/licensing) | 动态音乐、声音事件与运行集成 | 专有／专门许可 | 符合条件的项目免费；其他商业项目按许可付费 |
| [Wwise](https://www.audiokinetic.com/en/wwise/pricing/for-games/) | 交互音频和运行中间件 | 专有／专门许可 | 按预算、项目和平台等条件提供免费或付费许可，插件可能另计 |

例如用 REAPER 制作音乐层，在 FMOD 或 Wwise 中定义加入条件，再由游戏传入状态。**音频工作站制作声音，中间件组织播放规则，游戏提供触发规则的状态。** 简单作品可以直接使用引擎或浏览器音频能力。

<a id="tools-14"></a>
## 14｜对白与分支叙事

叙事工具组织文字、选择、条件和状态；对白完成后仍要与画面、输入和存档连接。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Twine](https://twinery.org/) | 文本段落、分支与网页故事 | 开源 | 免费 |
| [ink／Inky](https://www.inklestudios.com/ink/) | 分别是叙事语言和编辑器 | 开源，MIT | 软件免费；出版教材等另计 |
| [Yarn Spinner](https://www.yarnspinner.dev/) | 对话编写与游戏集成 | 开源核心＋商业工具 | 核心免费；Pro、支持和附加产品收费 |
| [articy:draft](https://www.articy.com/en/pricing/) | 角色、流程、分支和内容数据 | 专有 | 受限免费版＋订阅／团队方案，旧产品许可另看 |

**Ren’Py 可以承担视觉小说的主体系统，ink 主要承担叙事部分。** 前者不是单纯的对白编辑器，后者不自动负责游戏的所有画面与操作。

<a id="tools-15"></a>
## 15｜界面、字体与本地化

UI 是界面，UX 关注使用体验，本地化使内容适合目标语言和地区。翻译后是否溢出、字体是否缺字，都属于实际运行需要检查的内容。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Figma](https://www.figma.com/pricing/) | 界面设计与交互原型 | 专有服务 | 免费＋付费席位／功能 |
| [Penpot](https://penpot.app/) | 界面与原型协作 | 开源核心 | 自托管软件免费；托管及商业支持按方案 |
| [Unity UI Toolkit](https://docs.unity3d.com/Manual/UIElements.html)、[Unreal UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/umg-ui-designer-for-unreal-engine) | 游戏实际运行的界面 | 随所属引擎许可 | 按引擎方案使用 |
| [FontForge](https://fontforge.org/en-US/) | 字体制作和编辑 | 开源 | 软件免费，字体内容许可另看 |
| [Glyphs](https://glyphsapp.com/)、[FontLab](https://www.fontlab.com/) | 字形、字距等专业字体制作 | 专有 | 付费许可 |
| [Crowdin](https://crowdin.com/) | 翻译协作、术语与进度 | 专有服务 | 按项目资格有免费方案，其余按订阅／用量 |
| [Weblate](https://weblate.org/en/) | 翻译管理与协作 | 开源核心 | 自托管免费；托管与支持收费 |
| [Poedit](https://poedit.com/) | 翻译文件编辑 | 开源基础＋专有 Pro 功能 | 基础免费，Pro 付费 |
| [OmegaT](https://www.omegat.org/) | 术语与历史译文辅助 | 开源 | 免费 |

**设计工具提供方案，游戏 UI 系统实现操作，本地化工具组织语言内容。** 可点击的设计原型不能直接当成已经完成的游戏界面。

<a id="tools-16"></a>
## 16｜版本管理

版本管理记录文件变动，使修改可比较、追踪和恢复。它不是玩家存档，也不自动构成完整备份。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Git](https://git-scm.com/about)、[Git LFS](https://git-lfs.com/) | 文件历史与大文件扩展 | 开源 | 客户端免费；大文件存储与流量可能收费 |
| [GitHub](https://github.com/pricing)、[Bitbucket](https://bitbucket.org/product) | 仓库托管、协作和审查 | 平台服务 | 免费＋订阅与资源额度 |
| [GitLab](https://about.gitlab.com/pricing/) | 仓库、协作与自动化 | 开源核心＋商业功能／服务 | 免费核心或基础方案；商业与托管方案付费 |
| [GitHub Desktop](https://desktop.github.com/) | Git 图形客户端 | 开源 | 软件免费，连接服务另看 |
| [Sourcetree](https://www.sourcetreeapp.com/) | Git 图形操作界面 | 专有 | 软件免费 |
| [Perforce P4](https://www.perforce.com/products/p4/pricing) | 代码和数字资源版本管理 | 专有 | 小团队条件免费；扩大规模、托管与商业服务付费 |
| [Unity Version Control](https://docs.unity.com/en-us/unity-version-control) | 代码与资源版本管理，旧称 Plastic SCM | 专有服务／软件 | 免费适用范围＋席位、存储等付费方案 |
| [Subversion／SVN](https://subversion.apache.org/) | 集中式版本管理 | 开源 | 软件免费；托管另计 |

仓库保存文件与历史，提交记录一组修改，分支承载独立路线，合并整合变动。**Git 负责版本记录，GitHub 等平台提供托管协作，图形客户端提供操作界面。** 模型、音频等二进制资源未必能像文字一样自动合并，必要时需要文件锁定与交接。

<a id="tools-17"></a>
## 17｜任务、审片与制作追踪

这一类记录分工、进度、资源版本和批准状态，使不同制作环节能够接续工作。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Jira](https://www.atlassian.com/software/jira)、[Trello](https://trello.com/)、[GitHub Projects](https://github.com/features) | 任务、缺陷和进度 | 专有服务 | 免费基础＋付费方案，人数和功能限制分别确认 |
| [Codecks](https://www.codecks.io/) | 游戏项目的任务与反馈 | 专有服务 | 免费适用方案＋订阅 |
| [Flow Production Tracking](https://www.autodesk.com/products/flow-production-tracking/overview) | 资源、镜头、任务与审阅，旧称 ShotGrid／Shotgun | 专有 | 付费订阅或团队方案 |
| [ftrack](https://www.ftrack.com/en/) | 制作追踪与审阅 | 专有 | 付费方案，按产品询价 |
| [Kitsu](https://www.cg-wire.com/kitsu/) | 创意制作任务与审阅 | 开源核心 | 自托管软件免费，托管和支持付费 |
| [AYON](https://docs.ayon.dev/) | 跨制作软件的管线集成 | 混合，开源组件与商业插件并存 | 基础、自托管、商业支持及插件分别看方案 |
| [Slack](https://slack.com/)、[Microsoft Teams](https://www.microsoft.com/microsoft-teams/group-chat-software) | 沟通、会议与协作 | 专有服务 | 免费适用版本＋付费组织方案 |
| [Discord](https://discord.com/) | 讨论、语音和社区 | 专有服务 | 基础免费，可选订阅与增值服务 |

个人项目可以将这些事务集中在一个看板，大型项目可能拆分管理。**软件记录进度与交接信息，负责人仍需作出取舍和批准决定。**

<a id="tools-18"></a>
## 18｜调试、测试与性能分析

调试定位原因，测试检查结果，性能分析测量时间和内存等开销。能够启动、通过功能检查和达到性能目标，是不同结论。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [浏览器 DevTools](https://developer.chrome.com/docs/devtools) | 检查页面、请求、报错和性能 | 随浏览器，开放情况依产品 | 通常无需另购 |
| [Unity Profiler](https://docs.unity3d.com/Manual/Profiler.html)、[Unreal Insights](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine) | 引擎性能测量 | 随引擎许可 | 按引擎和相应模块方案使用 |
| [RenderDoc](https://github.com/baldurk/renderdoc) | 图形调试与帧分析 | 开源 | 免费 |
| [PIX](https://devblogs.microsoft.com/pix/)、[Nsight Graphics](https://developer.nvidia.com/nsight-graphics) | 图形与性能检查 | 厂商工具／专有许可 | 工具可免费获取，支持的平台和硬件有限定 |
| Xcode／Android Studio 分析工具 | 移动设备调试与性能 | 随各产品 | 工具费用见 06，真机另计 |
| [Jest](https://jestjs.io/)、[Vitest](https://vitest.dev/)、[pytest](https://docs.pytest.org/)、[NUnit](https://nunit.org/) | 不同生态中的规则自动测试 | 开源 | 软件免费 |
| [Playwright](https://playwright.dev/)、[Appium](https://appium.io/) | 浏览器或应用的操作自动化 | 开源 | 软件免费，执行资源另计 |
| [BrowserStack](https://www.browserstack.com/) | 浏览器和设备测试服务 | 专有服务 | 付费方案，试用与公益资格另看 |
| [NVDA](https://www.nvaccess.org/about-nvda/) | Windows 屏幕阅读器 | 开源 | 免费，可选支持服务另看 |
| [VoiceOver](https://www.apple.com/accessibility/vision/)、[TalkBack](https://support.google.com/accessibility/android/answer/6283677) | Apple／Android 读屏 | VoiceOver 随专有系统；TalkBack 有开源项目 | 随适用系统免费使用，设备另计 |

日志记录执行信息，断点帮助检查当时状态。**自动化提供已定义检查的结果，试玩提供实际理解与体验反馈。** 使用读屏工具或通过某个测试，不代表全部无障碍问题已经解决。

<a id="tools-19"></a>
## 19｜物理、寻路与其他中间件

物理处理运动和碰撞，寻路计算可通过区域和路线。它们是游戏中的专门能力，不等于一套完整的通用游戏引擎。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Box2D](https://box2d.org/) | 二维刚体物理 | 开源 | 核心免费 |
| [Jolt Physics](https://jrouwe.github.io/JoltPhysics/)、[Bullet](https://pybullet.org/wordpress/) | 三维物理模拟 | 开源 | 核心免费 |
| [PhysX](https://developer.nvidia.com/physx-sdk)、[Rapier](https://rapier.rs/) | 物理 SDK／二维三维模拟 | 开源核心 | 核心免费，附加组件另看许可 |
| [Havok](https://www.havok.com/) | 物理、导航、布料等产品 | 专有中间件 | 商业许可／询价，随引擎包含的版本另看 |
| [Recast／Detour](https://recastnav.com/) | 导航网格与寻路 | 开源 | 免费 |
| [Bink、Oodle](https://www.radgametools.com/) | 视频播放与数据压缩等 | 专有中间件 | 商业许可；部分引擎许可已包含特定使用范围 |

**通用引擎组织整体运行，中间件承担专门功能。** 游戏中的 AI 也可能指角色决策、行为树或寻路，不一定指生成式人工智能。

<a id="tools-20"></a>
## 20｜联机、服务器与数据库

客户端运行在玩家设备上，应用服务器处理远端任务，数据库保存与查询数据。网页文件托管与对战、账号后台不是同一职责。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Photon Fusion／Quantum](https://www.photonengine.com/) | 多人状态同步的不同技术路线 | 专有／专门许可 | 免费适用额度＋按并发、服务或企业方案收费 |
| [Mirror](https://mirror-networking.com/)、[FishNet](https://fish-networking.gitbook.io/docs) | Unity 多人网络框架 | 开源核心 | 核心免费；服务器另计，FishNet 商业附加功能另看 |
| [Colyseus](https://colyseus.io/)、[Nakama](https://heroiclabs.com/nakama/) | 多人服务器、账号与社交相关能力 | 开源核心 | 自托管软件免费；托管、支持和商业功能另计 |
| [PlayFab](https://learn.microsoft.com/en-us/xbox/playfab/get-started/what-is-playfab)、[Unity Gaming Services](https://unity.com/solutions/gaming-services) | 游戏在线服务 | 服务，SDK 等组件另许可 | 免费适用额度＋按量或方案收费 |
| [Epic Online Services／EOS](https://onlineservices.epicgames.com/)、[Steamworks](https://partner.steamgames.com/doc/home) | 好友、成就、在线与平台功能 | 平台／专门许可 | EOS 提供免费服务范围；Steamworks 与发行协议关联，不能混为同一计费方式 |
| [Firebase](https://firebase.google.com/pricing)、[Supabase](https://supabase.com/pricing) | 认证、数据、存储等后台 | Firebase 服务＋开放 SDK；Supabase 开源核心＋服务 | 免费额度＋按量／订阅，自托管仍有基础设施成本 |
| [SQLite](https://www.sqlite.org/about.html)、[PostgreSQL](https://www.postgresql.org/about/) | 本地或服务器数据管理 | 公有领域代码／开放许可 | 软件免费，托管与支持另计 |
| [Redis](https://redis.io/legal/licenses/) | 快速数据存储与访问 | 按版本区分，当前有开源与源码可见许可选项 | 软件与云服务分开；云端有付费方案，旧版许可不能直接套用 |
| [Docker](https://www.docker.com/pricing/) | 打包运行环境 | 开源引擎＋专有 Desktop 等产品 | 引擎免费；Desktop 条件免费／付费，云服务另计 |
| [Kubernetes](https://kubernetes.io/docs/concepts/overview/) | 容器化服务编排 | 开源 | 软件免费，服务器和运维另计 |
| [Amazon GameLift Servers](https://aws.amazon.com/gamelift/servers/)、[Agones](https://agones.dev/) | 游戏服务器托管或编排 | 前者云服务，后者开源 | 前者按资源方案计费；后者软件免费，运行资源另计 |

**托管服务分发文件，应用服务器处理远端功能，本地存储保存本设备中的数据。** 单机网页不一定需要账号后台，加入联机也不会自动解决作弊、同步和数据恢复问题。

<a id="tools-21"></a>
## 21｜自动构建、打包与发布

构建处理代码和资源，打包形成交付文件，部署放入运行环境，发布向玩家提供版本。各阶段需要检查自己的输出。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| 引擎导出、Xcode、Android Studio | 生成目标平台程序或工程 | 随相应工具 | 工具费用见 02、06；平台资格另计 |
| [GitHub Actions](https://docs.github.com/en/billing/concepts/product-billing/github-actions)、[GitLab CI/CD](https://docs.gitlab.com/ci/) | 自动检查与发布 | 服务与开源执行组件分开 | 免费额度＋执行、存储等收费 |
| [Jenkins](https://www.jenkins.io/) | 自行组织自动化流程 | 开源 | 软件免费，机器和维护另计 |
| [TeamCity](https://www.jetbrains.com/teamcity/) | 构建与持续集成 | 专有 | 免费适用版＋付费或云端方案 |
| [Electron](https://www.electronjs.org/)、[Tauri](https://tauri.app/) | 使用网页等技术组织应用 | 开源核心 | 软件免费；签名、打包和平台费用另计 |
| [Capacitor](https://capacitorjs.com/) | 网页界面与移动平台桥接 | 开源核心 | 核心免费；商业插件和服务另计 |
| [Steamworks](https://partner.steamgames.com/doc/gettingstarted) | Steam 构建管理、平台接入和发行 | 平台服务 | 发行接入与销售按平台协议；文档免费 |
| [itch.io](https://itch.io/docs/creators/) | 网页或可下载作品发布 | 平台服务；butler 上传工具开源 | 可免费建立作品页；交易、平台分成与支付费用另看 |
| [App Store Connect](https://developer.apple.com/app-store-connect/)、[TestFlight](https://developer.apple.com/testflight/) | Apple 发布管理与测试分发 | 专有服务 | 正式用途通常与开发者计划资格关联；不是分别购买两个游戏引擎 |
| [Google Play Console](https://play.google.com/console/about/) | Android 商店管理 | 专有服务 | 开发者注册及销售、交易条款另计 |
| [微信开发者工具](https://developers.weixin.qq.com/minigame/dev/devtools/download.html)、[抖音开发者工具](https://developer.open-douyin.com/) | 对应小游戏平台的开发与测试 | 平台工具／专有 | 工具可免费获取；认证、接入和运营规则另核对 |
| [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)、[Cloudflare Pages](https://developers.cloudflare.com/pages/)、[Netlify](https://www.netlify.com/pricing/)、[Vercel](https://vercel.com/pricing) | 网页托管与部署 | 云服务 | 免费适用范围＋资源／方案收费；商业用途、额度和后端能力分别看 |

**导出工具生成平台文件，平台流程接收和审核版本。** 支持某个平台不等于自动具备开发者资格或保证通过审核；主机开发条件尤其需要单独确认。

<a id="tools-22"></a>
## 22｜运行监控、数据分析与反馈

监控记录错误和服务状况，数据分析观察使用行为，社区与客服接收玩家反馈。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Sentry](https://sentry.io/pricing/) | 错误、崩溃与性能观察 | 源码可见的服务核心与开放 SDK 分开 | 自托管与云端条件不同；云端免费额度＋付费 |
| [GameAnalytics](https://www.gameanalytics.com/) | 游戏行为数据分析 | 专有服务 | 免费基础与付费数据／服务方案，按产品核对 |
| [Firebase Crashlytics](https://firebase.google.com/products/crashlytics) | 崩溃聚合与调查 | 服务，SDK 另许可 | 核心崩溃报告免费；关联产品用量可能收费 |
| [Prometheus](https://prometheus.io/)、[Grafana](https://grafana.com/grafana/) | 指标采集与可视化 | 开源核心 | 软件免费；商业功能和托管收费 |
| [Discord](https://discord.com/)、[Discourse](https://www.discourse.org/)、[Zendesk](https://www.zendesk.com/) | 社区、论坛与客服 | Discord／Zendesk 专有，Discourse 开源核心 | Discord 基础免费；Discourse 自托管免费、托管收费；Zendesk 付费 |

数据收集应对应明确目的，并考虑个人信息、费用和维护责任。**工具提供记录与调查能力，不自动提供问题原因，也不自动修好缺陷。**

<a id="tools-23"></a>
## 23｜录屏、剪辑与宣传

录屏取得实际运行画面，剪辑安排顺序与时长，合成和排版制作宣传表现。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [OBS Studio](https://obsproject.com/) | 录屏、直播与画面组合 | 开源 | 免费 |
| [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve) | 剪辑、调色、合成与音频后期 | 专有 | 免费版＋付费 Studio |
| [Adobe Premiere](https://www.adobe.com/products/premiere.html)、[After Effects／AE](https://www.adobe.com/products/aftereffects.html) | 视频剪辑，以及动态图形和合成 | 专有 | 订阅 |
| [Final Cut Pro](https://www.apple.com/final-cut-pro/) | Apple 平台剪辑 | 专有 | Mac 单独购买或适用套件订阅，iPad 与套餐另看 |
| [Kdenlive](https://kdenlive.org/) | 视频剪辑 | 开源 | 免费 |
| [Fusion](https://www.blackmagicdesign.com/products/fusion) | 节点式视觉合成 | 专有 | Resolve 内置与独立 Studio 的取得方式不同，后者付费许可 |
| [FFmpeg](https://ffmpeg.org/)、[HandBrake](https://handbrake.fr/) | 音视频转换与压缩 | 开源，具体构建／组件许可可能不同 | 核心免费；编解码与再分发条件另核对 |
| [Canva](https://www.canva.com/pricing/) | 海报、商店图和社交内容 | 专有服务 | 免费＋订阅，素材许可另看 |

**预渲染宣传片与实机画面需要区分。** 它们可以使用相同素材，但不意味着相同运行成本和可操作性。

<a id="tools-24"></a>
## 24｜素材平台与批量加工

素材平台提供内容，资源加工工具将内容处理为项目需要的形式。平台免费访问不等于平台内所有素材免费或开源。

| 平台／工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Fab](https://www.fab.com/)、[Unity Asset Store](https://assetstore.unity.com/) | 模型、贴图、插件与工具包 | 市场，逐项许可 | 免费与付费资源并存；兼容和许可各自核对 |
| [itch.io Game Assets](https://itch.io/game-assets) | 游戏素材市场 | 逐项许可 | 免费、付费或自定价格 |
| [Kenney](https://kenney.nl/assets)、[Poly Haven](https://polyhaven.com/) | 游戏资源，以及模型、纹理和环境图 | 所列素材采用相应开放内容许可 | 有免费资源；工具、商店内容或服务另看，不能混称“开源软件” |
| [Freesound](https://freesound.org/help/faq/) | 声音资源分享 | 不同声音采用不同许可 | 可免费获取的资源也有署名、用途等区别 |
| [TexturePacker](https://www.codeandweb.com/texturepacker) | 精灵图集与位置数据打包 | 专有 | 免费受限功能＋付费 Pro |
| [ImageMagick](https://imagemagick.org/) | 图片批量缩放、转换与加工 | 开源 | 免费 |

图集把多张小图组织到较大的图像中，并用位置数据定位各部分。源工程如 `.blend`、`.psd` 保留编辑信息，交换或运行资源如 `.png`、`.glb`、`.fbx`、`.wav` 则服务后续使用。**文件格式规定存储方式，软件负责处理内容；扩展名本身不保证所有功能兼容。** [glTF 官方说明](https://www.khronos.org/gltf/)

<a id="tools-25"></a>
## 25｜AI 辅助

AI 可以辅助设计、编程和资源制作，但“AI 做的”并没有说明成品采用什么引擎或运行环境。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [ChatGPT](https://openai.com/chatgpt/overview/) | 讨论、研究辅助、文档与编程协作 | 专有服务 | 免费适用额度＋订阅；API 等使用方式另计 |
| [Codex](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan) | 代码阅读、修改、检查与开发任务 | 服务与客户端分开，部分客户端开源 | 按 ChatGPT 方案额度或 API 等方式计费；客户端开放不代表模型服务免费 |
| [GitHub Copilot](https://github.com/features/copilot) | 编码与开发辅助 | 专有服务 | 免费适用方案＋付费计划／用量 |
| [Cursor](https://cursor.com/pricing) | AI 辅助代码工作环境 | 专有产品，基于开放组件 | 免费受限＋订阅／用量 |
| [Adobe Firefly](https://www.adobe.com/products/firefly.html) | 概念与视觉生成 | 专有服务 | 免费适用额度＋订阅或生成额度 |
| [ComfyUI](https://comfy.org/) | 连接模型与图像处理节点 | 开源核心＋商业云服务 | 本地核心免费；设备、模型、插件与云端用量另计 |

模型、软件、插件与生成内容的许可不能自动视为同一件事。**AI 负责辅助产出，项目验收负责判断是否符合要求；代码运行、来源、风格一致性和数据安全仍需验证。**

<a id="licensing"></a>
## 授权与总成本的比较

| 成本层次 | 需要确认的内容 |
| --- | --- |
| 制作软件 | 可用版本、席位、商业资格与订阅期限 |
| 运行组件 | SDK、中间件及成品分发条件 |
| 素材与字体 | 作者、来源、署名、修改和再分发范围 |
| 平台与服务 | 账号资格、存储、流量、并发、构建和交易费用 |
| 人力与维护 | 学习、接入、返工、迁移、测试与长期支持 |

永久许可不一定包含所有未来升级，教育许可不一定允许商业发行，开源也不意味着没有版权或无需保留声明。**许可费只是总成本的一部分；一个无需购买引擎的项目，仍可能花费大量制作和维护时间。**

为了比较成本，可以分别估算“开始制作时”“正式发行时”“用户或团队扩大后”三个阶段。条件免费工具可能在后两个阶段开始收费；开源自托管工具则可能一直没有许可费，却持续产生服务器和运维成本。

<a id="combinations"></a>
## 开发工具组合示例

以下是分工示意，不是唯一推荐，也不是已经验证的跨软件兼容承诺。斜线表示备选，不表示全部同时使用。

| 路线 | 工具与内容关系 | 主要成本位置 |
| --- | --- | --- |
| 图片与对白网页 | Blender 或绘图工具制作图像 → HTML／CSS／JavaScript 组织交互 → 浏览器运行 → 网页托管 | 软件可采用免费路线；绘图、逻辑、设备和托管用量另计 |
| 视觉小说 | 绘图与音频工具产出资源 → Ren’Py 组织对白、选项和存档 → 平台交付 | 引擎可免费；美术、配音、翻译和附加动画许可另计 |
| 二维动作或探索 | Aseprite 等制作角色 → Tiled／LDtk 或引擎编辑器制作关卡 → Godot／GameMaker／Phaser 中选一路线 | 付费工具不是必需组合；动作、关卡和测试工作仍需预算 |
| 实时网页三维 | Blender 制作模型 → 合适格式导出 → Three.js／Babylon.js／PlayCanvas 处理画面 → JS／TS 组织行为 | 核心可免费，编辑托管、模型制作、性能与兼容另计 |
| 多人协作三维项目 | Maya／Blender → 雕刻和材质工具 → 动画 → Unity／UE／自有引擎 → 测试与发布 | 席位、源素材、协作、平台与维护可能同时产生费用 |

《体温调节》讨论过的预渲染方案属于第一条：三维软件负责源场景，游戏使用导出的二维资源。**制作阶段使用 Blender，不自动推出运行阶段需要 Three.js。**

<a id="confusions"></a>
## 易混名称与概念

| 名称／说法 | 解释 |
| --- | --- |
| Unity、C#、Visual Studio | 引擎、语言、开发环境，可以配合使用 |
| Java、JavaScript | 不同语言，不是完整版与简化版 |
| Three.js、TypeScript | 三维库与语言，不是二选一 |
| VS Code、Visual Studio | 不同产品，不是长短名称 |
| Clickteam Fusion、Photon Fusion、Blackmagic Fusion | 分别是游戏制作、多人网络和视觉合成产品 |
| Blender、Cycles | 综合制作软件与其中的渲染系统 |
| Unreal、UEFN | 通用引擎与特定平台创作工具 |
| Git、GitHub、GitHub Pages | 版本记录、托管协作、网页分发 |
| ink、Inky | 叙事语言与编辑器 |
| Live2D 编辑器、SDK | 内容制作与项目接入／运行组件 |
| AI 文件、游戏 AI、生成式 AI | 可能指 Illustrator 文件、角色决策、生成内容的模型 |
| P4／Helix Core、Unity Version Control／Plastic SCM | 当前产品名称与旧资料常见名称 |
| Flow Production Tracking／ShotGrid／Shotgun | 制作追踪产品的新旧名称 |
| RealityScan／RealityCapture | 桌面产品的新旧名称；Mobile 另分 |
| Affinity Designer／Photo／Publisher | 旧的分别命名应用；当前统一产品与旧许可不同 |
| Shader／着色器 | 程序类别，不是某个固定品牌 |
| 开源引擎制作的游戏 | 引擎、游戏代码、素材的许可需要分别判断 |
| HTML5 游戏、3A／AAA | 前者宽泛描述网页路线，后者描述制作规模等语境，都不是引擎名 |

<a id="known-games"></a>
## 知名游戏的制作对应

只列有官方展示或创作者记录支持的关系。案例说明某项实际用法，不代表该游戏全部平台、后续版本和所有资源都采用完全相同流程，也不构成商业成功由某工具导致的证据。

| 游戏 | 可以确认的对应 | 适合用来理解的内容 |
| --- | --- | --- |
| **Hollow Knight／空洞骑士** | [Unity 官方制作案例](https://unity.com/made-with-unity/hollow-knight) | 引擎组织游戏，手绘视觉与游戏运行是不同工作 |
| **Cuphead／茶杯头** | [Studio MDHR／Unity 访谈](https://unity.com/made-with-unity/cuphead)介绍手绘资源与 Unity 集成 | 传统绘制方法可以与现代游戏引擎配合 |
| **Undertale／传说之下** | [GameMaker 官方作品页](https://gamemaker.io/en/showcase/undertale) | 专注二维的工具也可以承载复杂的玩法和叙事表达 |
| **Brotato／土豆兄弟** | [Godot 官方展示](https://godotengine.org/showcase/)收录该作品 | 免费开源引擎与商业游戏并不矛盾 |
| **Black Myth: Wukong／黑神话：悟空** | [NVIDIA 技术合作方介绍](https://www.nvidia.com/en-us/geforce/news/gfecnt/20248/black-myth-wukong-full-ray-tracing-dlss-3/)确认 UE5 路线 | 通用引擎可以进入大型三维制作，不能据此推断全部美术工具 |
| **Dead Cells／死亡细胞** | [美术 Thomas Vasseur 的制作文章](https://www.gamedeveloper.com/production/art-design-deep-dive-using-a-3d-pipeline-for-2d-animation-in-i-dead-cells-i-)介绍三维到二维动画管线 | 最终像素风格不意味着全部逐像素手绘 |

<a id="finish"></a>
## 项目技术说明的组织方式

介绍项目时，分别说明主体系统、编程语言、视觉制作和发布方式即可。AI 的参与另外描述为开发协作方式，不替代引擎或技术栈说明。

例如，预渲染网页项目可以写为：使用 HTML、CSS 和 JavaScript 组织交互，三维软件提前生成二维资源，浏览器运行，托管服务分发。采用通用引擎的项目则可以分别列出引擎、语言、素材和动画工具。

**用途说明工具承担的任务，输出说明交付的成果，连接关系说明它在项目中的位置，费用类型说明采用它会产生哪些成本。**

<a id="sources"></a>
## 参考文献与学习资源

### 工具与授权来源

表格中的软件名称链接兼作对应来源；关键条款另见 [Unity](https://unity.com/products)、[Unreal](https://www.unrealengine.com/en-US/license)、[Godot](https://godotengine.org/license/)、[Defold](https://defold.com/license/)、[Aseprite](https://www.aseprite.org/faq/)、[Ardour](https://ardour.org/faq.html)、[Live2D](https://www.live2d.com/en/cubism/comparison/)、[Spine](https://esotericsoftware.com/spine-purchase)、[FMOD](https://www.fmod.com/licensing)、[Wwise](https://www.audiokinetic.com/en/wwise/pricing/for-games/)、[Perforce P4](https://www.perforce.com/products/p4/pricing)、[Redis](https://redis.io/legal/licenses/)和 [VS Code](https://code.visualstudio.com/docs/supporting/faq)。这些入口需要按实际采用日期复查。

名称变化与新方案另参见 [PlayCanvas 编辑器前端开放说明（2025）](https://blog.playcanvas.com/playcanvas-editor-frontend-is-now-open-source/)、[Canva 的统一 Affinity 说明](https://www.canva.com/newsroom/news/all-new-affinity/)、[Apple 创作套件与单独购买说明（2026）](https://www.apple.com/uk/newsroom/2026/01/introducing-apple-creator-studio-an-inspiring-collection-of-creative-apps/)、[Reallusion 订阅方案说明（2026）](https://magazine.reallusion.com/2026/01/06/2026-reallusion-software-subscription-options-expanding-your-creative-freedom/)以及 [Codex 方案说明](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan)。旧教程可以解释旧版操作，不保证旧许可仍适用。

### 教材、课程与创作者资源

以下资源分别面向制作、架构、视觉和设计。它们是可独立于 AI 使用的学习材料；本篇提供阅读定位，不声称已经逐章审读全部书籍或看完全部课程。

| 文献或资源 | 获取方式 | 推荐内容 |
| --- | --- | --- |
| **Chandler, Heather. _The Game Production Toolbox_（2019）**，[出版社](https://www.routledge.com/Game-Production-Proven-Business-Techniques-to-Produce-the-Best-Games/Chandler/p/book/9781138341708) | 书籍付费或借阅，目录免费，英文 | 理解工具如何进入制作计划、预算和交付，而非只记名称 |
| **Gregory, Jason. _Game Engine Architecture_，第 4 版**，[作者官网](https://www.gameenginebook.com/) | 两卷书籍付费或借阅，概览免费，英文 | 优先看系统、资源与工具链概述；代码与数学部分可跳过 |
| **Fullerton, Tracy. _Game Design Workshop_，第 5 版（2024）**，[出版社](https://www.routledge.com/Game-Design-Workshop-A-Playcentric-Approach-to-Creating-Innovative-Games/Fullerton/p/book/9781032607009) | 付费或借阅，英文 | 原型、试玩与体验判断；工具选择服务于这些任务 |
| **Chacon, Scott；Straub, Ben. _Pro Git_，第 2 版**，[在线全文](https://git-scm.com/book/en/v2) | 在线免费，有中文入口；纸书另计 | 版本、提交和分支的概念，不必先学全部命令 |
| **MDN Web Docs：游戏与网页技术**，[游戏入口](https://developer.mozilla.org/en-US/docs/Games)、[游戏结构](https://developer.mozilla.org/en-US/docs/Games/Anatomy) | 免费，英文与部分译文 | 分清网页、绘图接口和运行环境 |
| **Unity Learn**，[官方学习平台](https://learn.unity.com/)；**Godot Docs**，[官方文档](https://docs.godotengine.org/en/stable/) | 基础官方内容免费，软件授权另计 | 先看编辑器、场景和资源的用途，再决定是否需要操作教程 |
| **Blender Manual／Blender Studio Training**，[手册](https://docs.blender.org/manual/en/latest/)、[制作课程](https://studio.blender.org/training/) | 手册免费；Studio 免费与订阅内容并存 | 观察资源从源工程到成品的步骤，不要求完整学习建模 |
| **MIT CMS.608 _Game Design_（2010 秋），Philip B. Tan、Jason Begy**，[公开课程](https://ocw.mit.edu/courses/cms-608-game-design-fall-2010/) | 免费课程与课堂媒体，英文 | 从规则和非数字原型理解制作，并非从安装软件开始 |
| **GDC：_Juice It or Lose It_（2012），Martin Jonasson、Petri Purho**，[演讲](https://gdcvault.com/play/1016789/Juice-It-or-Lose) | 该条目免费，英文视频 | 观察视听反馈；GDC 其他条目不一定免费 |
| **Cem Yuksel：_Introduction to Computer Graphics_**，[YouTube 课程](https://www.youtube.com/playlist?list=PLplnkTzzqsZTfYh4UbhLGpI5kGd5oW_Hh) | 免费公开视频，英文 | 选看画面和图形流程的概念；由 [Real-Time Rendering 作者资源页](https://www.realtimerendering.com/)列为学习入口 |

**阅读顺序：** 先按表定位实际项目涉及的工具，再读一篇开发者案例；需要系统知识时选一本对应教材。无需因某工具出现在大型作品中，就同时购买它及整套课程。

<a id="case-isopoda"></a>
## 实际案例：《等足目赋格》的技术对应

本节以 UMWELT 中《等足目赋格》的网页版为例，依据 **2026-10-13** 核对的[固定版本 `0bbe083`](https://github.com/fivsevn/umwelt/tree/0bbe083943a4b307e38e3ea0de435d3d7864a345)。范围限于网页主游戏与配套工具，不混入桌面封装或《体温调节》的拟定方案，也不表示本次重新执行了游戏测试。

### 整体路线

**《等足目赋格》没有采用 Unity、Godot 这类现成的通用游戏引擎，而是直接使用 JavaScript 编写游戏逻辑，通过 Canvas 2D 绘制场景，以 HTML 和 CSS 组织界面。** 输入、状态、叙事、语言、画面与音频分别由项目模块负责。[网页入口](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/index.html) · [模块说明](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/README.md)

浏览器已提供图形、音频和存储等基础能力，因此这不是从零实现全部底层技术。**浏览器提供执行环境，Canvas 等接口提供专门能力，项目代码实现本游戏的内容与规则。**

### 与手册分类对应

| 对应分类 | 本项目的实现与依据 | 费用或许可理解 |
| --- | --- | --- |
| [01 规划与资料](#tools-01) | Markdown 开发记录、来源与数据约定。[文档](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/docs/README.md) | 文档格式不收费；资料获取与整理有时间成本 |
| [02—04 运行结构](#tools-02) | 自定义 JavaScript 模块连接界面、状态与规则。[分工](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/README.md) | 没有这一路线中的通用引擎采购，但仍需开发维护 |
| [05 语言](#tools-05) · [15 界面](#tools-15) | JavaScript、HTML、CSS；界面不全部绘制在画布中。[入口](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/index.html) | 标准本身不收制作许可费 |
| [07 图像](#tools-07) · [11 动画](#tools-11) | 按身体比例、配色、姿态与动作阶段生成像素。[角色](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/sprites.mjs) | 程序化制作，不据此推断采购了某种绘图软件 |
| [10 场景](#tools-10) · [12 渲染](#tools-12) | Canvas 2D 与生境模块组合场景和角色。[场景](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/habitat.mjs) | 使用浏览器能力，性能与制作工作另计 |
| [10 编辑器](#tools-10) | 阿西莫夫环境实验室提供拖动、布置、导入导出。[约定](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/docs/laboratories.md) | 项目专用工具，不能把其开发成本视为零 |
| [13 音频](#tools-13) | Web Audio 与共享模块，点击音效由程序合成。[音频](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/assets/audio/audio-engine.mjs) | 接口本身不收费；其他音源和素材需另看来源 |
| [14 叙事](#tools-14) | 内容数据与状态规则决定观察文本及反馈。[规则](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/engine.mjs) | 写作、组织和分支检查是制作成本 |
| [15 本地化](#tools-15) | 语言模块与文本目录管理多语言显示。[分工](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/README.md) | 未据此确认使用某个付费翻译平台 |
| [20 保存](#tools-20) | localStorage 保存 JSON 形式的进度。[读写](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/game.js) | 本地存档，不是已采购的云存档服务 |
| [16 版本](#tools-16) | Git 与 GitHub 保存项目及修改记录。[仓库](https://github.com/fivsevn/umwelt/tree/0bbe083943a4b307e38e3ea0de435d3d7864a345) | Git 免费，托管按实际账号方案；这里不推断用户账单 |
| [06 开发](#tools-06) · [18 验证](#tools-18) | Node.js 与 Playwright 等检查规则、浏览器和显示。[测试](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/tests/README.md) | 工具开源免费，设备与执行资源另计 |
| [21 发布](#tools-21) · [24 加工](#tools-24) | Actions／Pages 准备站点、字体和资源版本，再分发文件。[发布](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/docs/deployment.md) | 按服务适用范围和额度，不等于无限免费 |
| [25 AI 辅助](#tools-25) | 辅助程序、调试、研究整理与文档。[声明](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/README.md) | 具体服务费用依用户实际方案，不从代码推断 |

未能从材料确认的代码编辑器、绘图软件或宣传工具，不作为已经使用的工具填写。项目采用免费的开发组件，也不自动意味着游戏本身使用开源许可；UMWELT 的源码公开和内容授权以[项目声明](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/README.md)为准。

### 引擎、编辑器与保存的区别

项目中的 `engine.mjs` 处理本游戏的状态与规则，文件名不证明它是一套通用引擎。**该文件承担规则处理，相关模块共同组成项目专用的运行系统。**

环境实验室中的修改可以导出布局，但不会直接写入游戏存档、仓库或自动发布。**环境实验室编辑布局，导出数据记录布局，游戏程序使用已经接入的布局执行规则。** [编辑与发布边界](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/docs/laboratories.md)

GitHub、Pages 与存档也承担不同职责。**GitHub 保存开发版本，Pages 分发网页文件，浏览器本地存储保存该浏览器中的游玩进度。** 清除网站数据可能丢失本地存档，这种存储也不自动跨设备同步。[本地存储说明](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)

### 可直接采用的项目介绍

简短表述：

> 原生 JavaScript + Canvas 2D 制作，没有采用 Unity、Godot 这类通用游戏引擎，游戏逻辑由项目自己的模块实现。

完整表述：

> 《等足目赋格》基于 HTML、CSS 和 JavaScript 开发，以 Canvas 2D 绘制场景，通过程序化像素绘制呈现动物形态与动作。交互、环境状态和叙事推进由项目模块处理，网页版使用浏览器本地存储保存进度，通过 GitHub Pages 发布。开发过程中使用 AI 辅助实现与维护，作品方向和最终版本由作者决定。

以上介绍对应本节列出的实现，不是对全部平台和未来版本的永久描述。**语言说明规则的表达方式，图形接口说明画面的生成方式，运行模块说明游戏的组织方式，发布服务说明成品的交付方式，AI 辅助说明开发中的协作方式。**

[返回用途分类](#map) · [下一篇：运行原理 003](posts-2026-umwelt-game-development-handbook-003.html) · [返回个人笔记目录](../index.html)
