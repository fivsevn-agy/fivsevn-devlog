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
  按 25 类用途认识游戏开发软件、语言、程序库和在线服务，分别比较开放情况与费用类型。在相应环节结合 Hollow Knight、Undertale、Brotato、Stardew Valley、Cuphead 等制作案例，并以你正在做的《等足目赋格》作完整对应。
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
description: "按用途比较游戏开发工具的职责、开放情况与费用，并用制作案例说明它们怎样配合。"
canonical_url: "https://devlog.fivsevn.com/posts/2026/posts-2026-umwelt-game-development-handbook-002.html"
created: "2026-10-13"
updated: "2026-10-13"
metadata_updated: "2026-10-13"
---

# 游戏开发软件地图手册｜ChatGPT 写给五月七日的指导笔记 002

**游戏开发工具的用途、关系与成本 · 撰写：ChatGPT · 2026-10-13**

[001 制作流程](posts-2026-umwelt-game-development-handbook-001.html) · **002 软件与成本** · [003 运行原理](posts-2026-umwelt-game-development-handbook-003.html) · [004 画面与动画](posts-2026-umwelt-game-development-handbook-004.html) · [005 玩法与叙事](posts-2026-umwelt-game-development-handbook-005.html) · [006 修改与发布](posts-2026-umwelt-game-development-handbook-006.html) · [007 研究与表达](posts-2026-umwelt-game-development-handbook-007.html)

介绍一款游戏时，可以同时提到引擎、编程语言、绘图软件和发布平台。它们分别处理不同工作，因此需要先按用途归类，再看彼此怎样配合。例如，Blender 制作模型，Unity 接收模型并组织游戏，C# 用于编写其中的行为，Steam 则提供一种发行途径。

你可以把本篇当作工具地图：遇到一个名称，先找到它负责的环节，再查看交付内容、配合方式与费用。表中覆盖个人、小团队和大型制作的主要工具类别；实际项目只需从中选择与需求相符的组合。

各软件名称链接到官方英文资料、产品页面或作者项目，作为查阅入口。费用栏保留 **2026-10-13** 整理的开放情况与计费形式；由于版本、地区和使用资格会影响条件，采购时还需核对对应方案。游戏案例按开发者记录的制作阶段理解，具体平台与后续版本可能另有安排。

<a id="start"></a>
## 基本概念：引擎、语言与工具的职责

| 名词 | 定义 | 解释 |
| --- | --- | --- |
| 游戏引擎 | 提供游戏运行所需的一组基础系统，通常配有制作工具 | 提供画面、声音和输入等能力，项目利用它们组织具体内容与规则 |
| 编辑器 | 供开发者编辑代码、资源或场景的工具 | 用于摆放角色、修改脚本或调整动作，完成后再由运行系统使用这些内容 |
| 编程语言 | 编写程序时遵循的表达规则 | 用规定的写法描述条件、操作与数据 |
| 库／程序库 | 可被程序调用的一组现成功能 | 例如读取图像或处理三维画面，使项目可以复用已有实现 |
| 框架 | 提供功能并约定程序组织方式的基础结构 | 开发者按照框架安排模块，再加入项目自己的内容和规则 |
| 插件 | 扩展现有软件能力的部件 | 给对应软件增加功能，通常依赖它的版本与运行环境 |
| SDK／软件开发工具包 | 接入某个平台或功能的一套组件、说明与工具 | 例如接入成就、联机或动画时，使用厂商提供的配套材料 |
| API／应用程序接口 | 软件调用功能时遵循的约定 | 规定如何传入信息和取得结果，可以由库、系统或在线服务提供 |
| 运行时／Runtime | 功能实际执行时使用的程序部分 | 在成品中加载资源、执行脚本或处理相应功能 |
| 中间件／Middleware | 接入项目、承担专门任务的技术 | 例如声音、物理、导航和联机系统 |
| 资源／Asset | 游戏使用的图像、模型、声音、字体等内容 | 由制作工具生成或整理，再交给游戏读取 |
| 工具链／制作管线 | 配合使用的工具及其处理、交付流程 | 前者侧重工具组合，后者侧重内容从源文件到成品的步骤 |
| 技术栈 | 项目采用的技术组合 | 可以包括语言、框架、运行环境、数据库与相关工具 |

这些名称有交叉。例如 [Phaser](https://docs.phaser.io/phaser/getting-started/what-is-phaser)既以 JavaScript 库的形式提供，也为游戏安排功能与结构，所以官方称其为游戏框架。遇到类似称呼时，可以先看它提供哪些能力，以及项目还需补充什么，再判断它在工作中的位置。

以 Unity 为例，开发者在编辑器里布置角色、场景和动画；导出后，玩家设备上的运行时读取资源并执行脚本。角色具体说什么、点击后如何回应，则由项目内容与规则决定。**因此，编辑器提供制作和调整内容的界面，引擎提供运行所需的基础系统，项目设计决定这些系统实际执行的内容。** [Unity 官方介绍](https://unity.com/products/unity-engine)

<a id="cost-legend"></a>
## 成本标注的读法

工具的开放情况和费用回答两类问题：前者说明源码及修改、分发权利怎样安排，后者说明取得软件或服务如何计费。两项分开列出，才能看清免费软件、开源软件与商业产品的不同组合。

| 标注 | 解释 |
| --- | --- |
| 开源 | 按相应许可证提供源码，并授予使用、修改与再分发等权利，同时保留许可条件 |
| 源码可见 | 可以在规定范围内查看或修改源码，实际权利按专门许可确定 |
| 专有 | 主产品由厂商按自己的许可提供，捆绑组件可能另有开放许可 |
| 混合 | 核心、编辑器、插件、SDK 或服务采用不同许可，需要分别查看 |
| 语言／标准 | 描述表达规则、接口或格式，费用通常发生在具体实现和服务上 |
| 免费 | 所列软件或核心能力不收使用费，资源、人力与运行环境另计 |
| 条件免费 | 免费使用取决于收入、用途、资格、人数或功能范围 |
| 免费＋付费 | 基础版或额度免费，扩展功能、托管或服务收费 |
| 付费许可 | 为某个产品或版本购买使用权，升级与服务范围另看 |
| 订阅／按量／分成 | 分别按期限、资源用量或约定收入规则计费 |
| 内部／询价 | 获取条件由所属公司或项目方案确定 |

例如，[Godot](https://godotengine.org/license/)采用 MIT 许可并免费提供；[Defold](https://defold.com/license/)同样免费，但适用自己的源码可见许可。[Aseprite](https://www.aseprite.org/faq/)允许按条款取得源码，官方成品则付费提供；[Ardour](https://ardour.org/faq.html)采用开源许可，也为官方完整预编译成品提供付费获取方式。由此可见，是否开源与是否收费需要各自确认。

试用期、个人版和教育版也有不同条件。如果准备商业发行，应进一步查看制作软件、运行组件和素材的适用范围（本篇按 [OSI 的定义](https://opensource.org/osd)使用“开源”一词；表格属于用途与成本概览，具体使用以许可文本为准）。

<a id="map"></a>
## 用途分类与章节索引

| 章节 | 主要内容 |
| --- | --- |
| [01 规划与资料](#tools-01) | 文档、参考图、文献与数值 |
| [02 通用引擎](#tools-02) · [03 专用工具](#tools-03) · [04 框架与图形库](#tools-04) | 游戏主体的制作与运行 |
| [05 语言与格式](#tools-05) · [06 编程工具](#tools-06) | 规则表达、代码编辑和构建 |
| [07 二维](#tools-07) · [08 三维](#tools-08) · [09 材质](#tools-09) · [10 场景](#tools-10) | 图像、模型、表面与环境 |
| [11 动画](#tools-11) · [12 渲染与特效](#tools-12) | 角色动作与画面生成 |
| [13 音频](#tools-13) · [14 叙事](#tools-14) · [15 界面与本地化](#tools-15) | 声音、文字、操作与语言 |
| [16 版本管理](#tools-16) · [17 制作协作](#tools-17) | 修改记录、任务和交接 |
| [18 测试与性能](#tools-18) · [19 中间件](#tools-19) | 验证与专门运行能力 |
| [20 联机与后台](#tools-20) · [21 发布](#tools-21) · [22 维护](#tools-22) | 服务、交付和运行反馈 |
| [23 宣传](#tools-23) · [24 素材与加工](#tools-24) · [25 AI 辅助](#tools-25) | 辅助制作环节 |
| [授权](#licensing) · [组合](#combinations) · [易混名称](#confusions) | 工具选择与比较 |
| [案例查阅](#known-games) · [参考资源](#sources) | 开发者记录、教材与课程 |
| [《等足目赋格》对应](#case-isopoda) | 把工具分工放回你的游戏 |

初次阅读可以先看基本概念、02—06 和组合示例，其余按用途查阅。查具体名称时，可以使用浏览器的页面查找功能。

<a id="tools-01"></a>
## 01｜规划、资料与数值

文档、参考图和表格先帮助你记录设计，再为制作提供内容与条件。若希望其中的数据直接进入游戏，还需要安排相应的读取或转换步骤。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Word](https://www.microsoft.com/microsoft-365/word)、[Excel](https://www.microsoft.com/microsoft-365/excel) | 文档、资源表和数值计算 | 专有 | 网页基础功能与付费桌面／订阅方案按版本区分 |
| [Google Docs](https://workspace.google.com/products/docs/)、[Sheets](https://workspace.google.com/products/sheets/) | 在线文档、表格与协作 | 服务 | 个人基础使用免费，组织管理与扩容有付费方案 |
| [LibreOffice Calc](https://www.libreoffice.org/) | 本地表格、公式与数据整理 | 开源 | 免费 |
| [Notion](https://www.notion.com/pricing)、[Obsidian](https://obsidian.md/pricing) | 设定、知识与设计记录 | 专有／服务 | Notion 免费＋订阅；Obsidian 应用免费，可选同步和发布服务付费 |
| [Miro](https://miro.com/pricing/)、[FigJam](https://www.figma.com/figjam/) | 白板、流程与关系图 | 专有／服务 | 免费基础＋付费协作或席位方案 |
| [draw.io／diagrams.net](https://www.drawio.com/) | 流程图、页面与系统关系 | 开源核心 | 核心免费，部分平台集成收费 |
| [PureRef](https://www.pureref.com/download.php) | 在同一画布整理视觉参考 | 专有 | 个人与商业使用按相应类别定价 |
| [Zotero](https://www.zotero.org/) | 文献、出处与引用管理 | 开源 | 本地软件免费，附件云存储扩容收费 |

以你的物种资料为例，表格可以记录名称、出处和视觉参数；随后由项目把这些字段接入目录与绘制系统。这样，资料整理、数据接入与游戏显示各有清楚的交付位置。

<a id="tools-02"></a>
## 02｜通用游戏引擎

引擎提供图形、声音、输入、场景等基础系统，开发者再利用这些能力组织自己的内容。因此，选择引擎时，可以比较它已经承担哪些工作，以及项目还需完成哪些设计、资源和扩展。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Unity](https://unity.com/products) | 通用二维／三维制作，脚本主要采用 C# | 专有 | 条件免费＋付费席位方案，资格按官方要求 |
| [Unreal Engine／UE](https://www.unrealengine.com/en-US/license) | 三维场景、动画、物理与可视化逻辑 | 源码可见，专门许可 | 游戏按适用免费范围和分成条款，其他用途另有规则 |
| [Godot](https://godotengine.org/license/) | 以场景和节点组织二维／三维项目 | 开源，MIT | 引擎免费，资源与平台适配另计 |
| [GameMaker](https://gamemaker.io/en/get) | 以对象、房间和事件组织二维游戏 | 专有 | 非商业免费，商业许可与主机方案另计 |
| [GDevelop](https://gdevelop.io/pricing) | 事件式可视化制作 | 开源核心＋服务 | 核心免费，云端与协作有付费方案 |
| [Construct](https://www.construct.net/en/make-games/buy-construct) | 浏览器中的事件式二维制作 | 专有 | 受限免费版＋订阅 |
| [Clickteam Fusion](https://www.clickteam.com/clickteam-fusion-2-5) | 通过可视化事件组织游戏和应用 | 专有 | 付费许可，导出器和版本能力分别确认 |
| [Defold](https://defold.com/license/) | 编辑器、资源处理与 Lua 运行系统 | 源码可见 | 引擎免费，使用与再分发遵循专门许可 |
| [O3DE](https://o3de.org/)、[Stride](https://www.stride3d.net/) | 可扩展三维引擎；Stride 采用 C#／.NET 路线 | 开源 | 软件免费，制作与支持另计 |
| [Flax](https://flaxengine.com/licensing/) | 三维引擎、编辑器与脚本系统 | 源码可见 | 免费适用范围＋条件分成，也有定制许可 |
| [Frostbite／寒霜](https://www.ea.com/frostbite) | 面向公司项目与生产流程的自有引擎 | 内部专有 | 按公司内部使用与合作条件安排 |

**《Hollow Knight》采用 Unity，同时在 Photoshop 中制作手绘图像并导出 PNG。** 引擎负责接入资源、组织场景与交互，绘图软件负责产生美术内容。[1](#ref-1) 因而，“用了 Unity”和“用了 Photoshop”可以同时成立：它们描述的是同一作品中的不同环节。

GameMaker 官方展示收录《Undertale》，Godot 官方展示收录《Brotato》。[2](#ref-2), [3](#ref-3) 这些作品可以帮助你认识工具的实际使用范围，但选择自己项目的工具时，还需要继续比较平台、操作形式和维护成本。

可视化事件、蓝图和文字代码都用于表达逻辑。前者把部分条件和操作呈现为节点或表格，后者通过文字写法组织；无论采用哪种方式，触发条件和结果仍需由设计确定。

<a id="tools-03"></a>
## 03｜专用制作工具与创作平台

有些作品反复使用相似结构，例如视觉小说中的对白、选项和存档。专用工具将这些结构预先组织好，让开发者把更多精力放在具体内容上。平台型工具则进一步规定作品在哪里运行与发布。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Ren’Py](https://www.renpy.org/) | 视觉小说的对白、选择、显示与存档 | 开源 | 引擎免费，商业使用与附加资源按各自许可 |
| [RPG Maker](https://www.rpgmakerweb.com/products/rpg-maker-mz) | 地图、角色和事件等预设系统 | 专有，部分脚本可见 | 付费许可，素材和插件另计，版本分别确认 |
| [TyranoScript](https://tyranoscript.com/)、[TyranoBuilder](https://tyranobuilder.com/) | 视觉小说的脚本与图形化制作路线 | 前者开源，后者专有 | 前者免费，后者付费许可 |
| [Twine](https://twinery.org/) | 非线性文本和网页互动故事 | 开源 | 免费，故事格式和扩展另看许可 |
| [GB Studio](https://www.gbstudio.dev/)、[Bitsy](https://bitsy.org/) | 特定规格下的小型像素和叙事作品 | 开源 | 软件免费，资源与平台条件另计 |
| [PICO-8](https://www.lexaloffle.com/pico-8.php) | 集成代码、绘图与音效的幻想主机环境 | 专有 | 完整版付费，教育体验的范围另看 |
| [TIC-80](https://tic80.com/) | 集成式幻想电脑创作环境 | 开源核心 | 基础免费，官方 Pro 等版本另收费 |
| [Roblox Studio](https://create.roblox.com/docs/studio) | 制作 Roblox 平台体验，使用 Luau 等 | 专有平台工具，部分组件开源 | 工具免费，交易和发布按平台规则 |
| [UEFN](https://dev.epicgames.com/documentation/en-us/fortnite/unreal-editor-for-fortnite) | 为 Fortnite 制作体验 | 专有平台工具 | 工具免费，发布资格和收益按平台规则 |

例如，UEFN 提供场景和逻辑制作能力，但所做体验接入的是 Fortnite 平台。理解这一点，就能把“使用哪套编辑工具”和“通过什么平台交给玩家”分开考虑。

像素、手绘或文字叙事也可以由多种工具实现，因此应先说明作品需要哪些操作与表现，再选择预设结构是否适合它。

<a id="tools-04"></a>
## 04｜框架、图形库与代码型引擎

另一类工具主要通过代码调用，提供图形、输入、声音或程序结构。开发者在这些基础上组织项目，可以选择更贴近作品的运行方式，同时承担相应的连接与维护工作。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Three.js](https://threejs.org/) | JavaScript 三维图形库，处理相机、模型和灯光等 | 开源 | 核心免费 |
| [Babylon.js](https://www.babylonjs.com/) | 网页三维引擎与配套工具 | 开源 | 核心免费 |
| [PlayCanvas](https://playcanvas.com/plans) | 网页三维引擎与在线编辑流程 | 开源引擎及编辑器前端，托管另计 | 核心免费，编辑服务有免费和付费方案 |
| [Phaser](https://docs.phaser.io/phaser/getting-started/what-is-phaser) | 二维网页游戏框架 | 开源核心 | 核心免费，配套编辑器和服务另计 |
| [PixiJS](https://pixijs.com/) | 二维绘制与显示 | 开源 | 核心免费 |
| [raylib](https://www.raylib.com/) | 图形、输入和音频开发库 | 开源 | 免费 |
| [SDL](https://www.libsdl.org/)、[SFML](https://www.sfml-dev.org/) | 跨平台窗口、输入、图形与音频能力 | 开源 | 核心免费，捆绑组件另看许可 |
| [LÖVE](https://love2d.org/)、[Solar2D](https://solar2d.com/) | Lua 路线的二维框架或引擎 | 开源 | 核心免费，插件和服务可能另计 |
| [MonoGame](https://monogame.net/)、[libGDX](https://libgdx.com/) | 分别面向 .NET 和 Java 路线的游戏框架 | 开源 | 核心免费，平台支持条件另看 |
| [Bevy](https://bevy.org/)、[HaxeFlixel](https://haxeflixel.com/) | Rust 游戏引擎与 Haxe 二维框架 | 开源 | 核心免费 |
| [React](https://react.dev/)、[Vue](https://vuejs.org/)、[Svelte](https://svelte.dev/) | 组织网页界面及其状态变化 | 开源 | 核心免费，商业扩展与服务另计 |

**MonoGame 官方列出的使用作品包括《Celeste》和《Stardew Valley》。** [4](#ref-4) 它提供的是框架能力，开发者再组织自己的玩法和制作流程。由此可以理解，完整作品既可以通过带有综合编辑器的引擎制作，也可以由框架与项目代码配合完成（不同移植和版本的具体实现需分别查看）。

网页项目中还可以组合不同职责。例如 React 组织菜单，Three.js 处理三维场景，项目代码连接两者的状态。简单的图片与对白交互也可以直接使用 HTML、CSS 和 JavaScript；当已有能力足够时，就可以减少额外依赖。[MDN 说明](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/What_is_JavaScript)

<a id="tools-05"></a>
## 05｜语言、数据格式与图形技术

编程语言规定表达方式，编辑器帮助编写，运行环境负责执行。因此，听到一种语言的名字时，可以继续确认它用于哪套工具或哪一个环节，再判断相应成本。

| 名称 | 类别与主要用途 | 成本对应 |
| --- | --- | --- |
| [JavaScript／JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript)、[TypeScript／TS](https://www.typescriptlang.org/) | 网页交互、工具和服务；TS 增加类型等开发能力 | 有免费开放实现，具体服务与编辑工具另计 |
| [C#](https://learn.microsoft.com/en-us/dotnet/csharp/)、[C++](https://isocpp.org/)、C | 游戏、引擎、系统和原生工具中的不同语言 | 费用由采用的编译工具、引擎和平台决定 |
| [GDScript](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html)、[GML](https://manual.gamemaker.io/monthly/en/GameMaker_Language/GameMaker_Language_Index.htm) | 分别用于 Godot 与 GameMaker | 前者随开源 Godot，后者按 GameMaker 方案使用 |
| [Lua](https://www.lua.org/about.html)、[Luau](https://luau.org/) | 嵌入式脚本，以及 Roblox 等环境中的语言 | 实现开源，平台和附加产品费用另看 |
| [Python](https://www.python.org/about/) | 资源整理、自动化、测试、后台和叙事工具扩展 | 开放实现可免费使用，具体产品与服务另计 |
| [Rust](https://www.rust-lang.org/)、[Haxe](https://haxe.org/) | 通用语言，对应 Bevy、HaxeFlixel 等路线 | 有免费开源工具链 |
| [Java](https://dev.java/)、[Kotlin](https://kotlinlang.org/)、[Swift](https://www.swift.org/) | 游戏框架及移动、桌面平台开发 | 有开放工具，发行版、商业支持与平台条件分别确认 |
| [Verse](https://dev.epicgames.com/documentation/en-us/fortnite/verse-language-reference) | Epic 创作环境中的规则表达 | 按使用环境与平台条款安排 |
| [HTML、CSS](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/What_is_JavaScript) | 网页结构与样式 | 标准本身没有制作软件许可费 |
| [SQL](https://www.postgresql.org/docs/current/tutorial-sql.html) | 查询和操作关系数据库 | 数据库产品与托管服务各有费用 |
| [HLSL](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl)、[GLSL](https://www.khronos.org/opengl/wiki/Core_Language_(GLSL))、[WGSL](https://www.w3.org/TR/WGSL/) | 表达图形处理器执行的计算 | 按采用的图形平台和工具链确认许可 |

| 其他名称 | 解释 |
| --- | --- |
| JSON、CSV、YAML、TOML | 保存数据或配置的格式，例如对白表与设置 |
| Markdown／`.md` | 用标记组织标题、链接和表格等文档内容 |
| WebGL、WebGPU、OpenGL、Vulkan、Direct3D、Metal | 图形接口或标准，供相应引擎与图形库使用 |
| WebAssembly／Wasm | 程序的执行格式和编译目标，可由多种语言生成 |

以网页三维为例，Three.js 提供开发者调用的三维功能，WebGL／WebGPU 提供相关底层接口，着色器语言则用于表达其中的图形计算。它们位于不同层次，因此可以共同参与同一个项目。[WebGL](https://www.khronos.org/webgl/) · [WebGPU](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API)

<a id="tools-06"></a>
## 06｜代码编辑、编译与依赖管理

代码从编写到运行，可能需要下载依赖、检查格式、转换程序和整理资源。下列工具分别承担其中的工作，实际流程可以由编辑器或自动化统一调用。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [VS Code](https://code.visualstudio.com/docs/supporting/faq) | 编辑代码、查找文件和使用扩展 | Code OSS 核心开源，微软发行版另许可 | 软件免费，扩展与 AI 服务可能另计 |
| [Visual Studio](https://visualstudio.microsoft.com/) | 集成编写、运行与调试 | 专有 | Community 条件免费，其他版本付费 |
| [Rider](https://www.jetbrains.com/rider/buy/) | .NET 与游戏开发工作环境 | 专有 | 非商业免费，商业使用订阅 |
| [Xcode](https://developer.apple.com/xcode/) | Apple 平台开发、构建与调试 | 主应用专有，部分组件开源 | 工具免费，设备和正式发布资格另计 |
| [Android Studio](https://developer.android.com/studio) | Android 平台开发与调试 | 开源基础，捆绑 SDK 另许可 | 工具免费，商店和服务另计 |
| [Node.js](https://nodejs.org/en/about)、[.NET](https://dotnet.microsoft.com/learn/dotnet/what-is-dotnet) | 程序运行与开发环境 | 开源核心 | 核心免费，托管和支持另计 |
| [npm](https://docs.npmjs.com/about-npm/)、[pnpm](https://pnpm.io/)、[Yarn](https://yarnpkg.com/) | JavaScript 依赖管理 | 开源客户端，注册表服务另看 | 工具免费，私有包及企业服务可能收费 |
| [pip](https://pip.pypa.io/en/stable/)、[NuGet](https://learn.microsoft.com/en-us/nuget/what-is-nuget)、[Cargo](https://doc.rust-lang.org/cargo/) | Python、.NET 和 Rust 等生态的包管理 | 开源核心 | 工具免费，安装的组件按各自许可 |
| [Vite](https://vite.dev/guide/)、[webpack](https://webpack.js.org/) | 网页预览、程序与资源构建 | 开源 | 免费 |
| [GCC](https://gcc.gnu.org/)、[Clang](https://clang.llvm.org/) | 将源代码编译为后续可执行的程序 | 开源 | 工具免费，附加库与再分发条件另看 |
| [MSVC](https://learn.microsoft.com/en-us/cpp/overview/visual-cpp-in-visual-studio) | Microsoft C／C++ 工具链 | 专有 | 按工具包与开发许可确认 |
| [CMake](https://cmake.org/)、[Gradle](https://gradle.org/)、[MSBuild](https://learn.microsoft.com/en-us/visualstudio/msbuild/msbuild) | 安排构建步骤、文件关系与顺序 | 开源核心 | 核心免费，商业服务另计 |
| [Emscripten](https://emscripten.org/) | 将相应程序处理为网页等目标形式 | 开源 | 工具免费，移植与适配需要另行制作 |
| [PowerShell](https://learn.microsoft.com/en-us/powershell/)、[Bash](https://www.gnu.org/software/bash/)等 | 通过命令启动任务和处理文件 | 当前核心开源，系统版本另看 | 通常无需另购 |

因此，编辑器提供编写界面，包管理工具获取组件，构建工具安排处理，运行环境执行结果。你可以先通过交付记录理解这些步骤；具体命令由开发者操作，所用版本与依赖则需要留在项目说明中。

<a id="tools-07"></a>
## 07｜二维绘图与像素画

绘图软件制作平面资源，像素画工具更侧重像素级编辑与动作帧。成品进入游戏后，再由程序决定显示位置、时机和切换条件。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Photoshop／PS](https://www.adobe.com/products/photoshop.html) | 图像编辑、绘画、合成与贴图 | 专有 | 桌面完整制作主要为订阅 |
| [Clip Studio Paint／CSP](https://www.clipstudio.net/en/) | 插画、角色差分与二维动画 | 专有 | 买断或订阅依平台和版本 |
| [Krita](https://krita.org/en/)、[GIMP](https://www.gimp.org/) | 数字绘画与综合图像编辑 | 开源 | 官网软件免费，部分商店版本可能收费 |
| [Procreate](https://procreate.com/procreate) | iPad 绘画 | 专有 | 付费购买，设备另计 |
| [Illustrator／AI](https://www.adobe.com/products/illustrator.html) | 矢量图标、标志与图形 | 专有 | 订阅 |
| [Inkscape](https://inkscape.org/) | 矢量绘图 | 开源 | 免费 |
| [Affinity](https://www.affinity.studio/) | 统一的矢量、像素与版面制作 | 专有 | 当前应用免费，相关 AI 和服务资格另看 |
| [Aseprite](https://www.aseprite.org/faq/) | 像素绘图与逐帧动画 | 源码可见，专门许可 | 官方成品付费，自行构建和再分发按条款 |
| [LibreSprite](https://libresprite.github.io/)、[Piskel](https://www.piskelapp.com/)、[Pixelorama](https://orama-interactive.itch.io/pixelorama) | 像素绘图和动画 | 开源 | 有免费获取路线，部分商店版本付费支持开发 |

位图记录像素，矢量图记录形状与曲线。差分保存同一角色的不同外观，逐帧动画则通过连续播放一组画面呈现动作。

**《Cuphead》先在纸上制作动画，再进行数字处理并接入 Unity。** [5](#ref-5) 这说明资源可以经过多种制作介质：纸面负责绘制，数字工具负责整理，引擎负责运行。选择流程时，要同时考虑目标风格与后续修改方式。

<a id="tools-08"></a>
## 08｜三维建模与雕刻

建模建立物体的立体形状，雕刻通过调整表面塑造形体与细节。模型完成后，再按用途处理材质、动作和导出。这些软件也常被统称为 DCC，即数字内容创作工具。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Blender](https://www.blender.org/about/license/) | 建模、雕刻、动画与渲染 | 开源 | 软件免费，插件和服务另计 |
| [Maya](https://www.autodesk.com/products/maya/overview)、[3ds Max](https://www.autodesk.com/products/3ds-max/overview) | 综合三维生产 | 专有 | 订阅等商业方案，资格与平台另看 |
| [Cinema 4D](https://www.maxon.net/en/cinema-4d)、[ZBrush](https://www.maxon.net/en/zbrush) | 综合三维与动态图形，以及数字雕刻 | 专有 | 付费方案，当前与历史许可分别确认 |
| [Nomad Sculpt](https://nomadsculpt.com/) | 数字雕刻 | 专有 | 付费许可，按平台获取 |
| [3DCoat](https://3dcoat.com/) | 雕刻、重拓扑、UV 与贴图 | 专有 | 付费许可或订阅等方案 |
| [Blockbench](https://blockbench.net/) | 低多边形、方块风格模型与动画 | 开源 | 免费 |
| [MagicaVoxel](https://ephtracy.github.io/) | 以三维格子组织体素形体 | 专有免费工具 | 免费使用，遵循相应许可 |

网格由点、边和面组成，拓扑描述它们怎样连接，重拓扑则重新安排连接以便变形或运行。

你为《体温调节》讨论过的预渲染方案，就可以在 Blender 中安排场景，再导出二维图像交给网页。三维制作在这里服务于资源生产；运行时使用的是导出的图片，因此是否需要实时三维，应根据玩家实际能够改变什么来判断。

<a id="tools-09"></a>
## 09｜贴图、材质、UV 与烘焙

模型给出形状，表面表现还需要颜色、粗糙程度等信息。贴图保存部分表面信息，材质规定它们怎样参与显示，UV 将模型表面与二维图片位置对应，烘焙则把部分计算提前保存为资源。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Substance 3D Painter](https://www.adobe.com/products/substance3d/apps/painter.html) | 在模型表面制作颜色、磨损等贴图 | 专有 | 订阅或特定渠道版本许可 |
| [Substance 3D Designer](https://www.adobe.com/products/substance3d/apps/designer.html)、[Sampler](https://www.adobe.com/products/substance3d/apps/sampler.html) | 通过节点或输入图像制作材质 | 专有 | 付费产品与套件方案 |
| [ArmorPaint](https://armorpaint.org/) | 三维表面绘制与烘焙 | 开源项目 | 源码可免费构建，官方成品按渠道付费 |
| [Mari](https://www.foundry.com/products/mari) | 三维贴图制作 | 专有 | 商业版付费，非商业版有使用限制 |
| [Material Maker](https://www.materialmaker.org/) | 节点式材质生成 | 开源 | 免费 |
| [RizomUV](https://www.rizomuv.com/) | UV 展开与排布 | 专有 | 付费许可或订阅 |
| [Marmoset Toolbag](https://marmoset.co/) | 展示、渲染、烘焙与表面检查 | 专有 | 付费许可，版本与团队方案另看 |

节点表示一项操作或数据，连线表示信息如何流动。材质节点与游戏逻辑节点外观可能相似，但处理的对象不同，使用时应先确认它们连接的是图像信息还是行为条件。

烘焙可以让较简单的模型表现某些高细节信息，不过几何轮廓仍由模型承担。因此，应分别检查形状和表面效果，再判断哪些细节适合留在模型，哪些适合保存为贴图。

<a id="tools-10"></a>
## 10｜场景、地形与关卡

场景制作安排环境内容，关卡设计进一步组织路线、障碍、触发和节奏。例如森林需要树木与地面，玩家在森林中如何前进和得到线索，则属于关卡中的行为安排。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| 引擎内置场景编辑器 | 安排对象、光照和触发区域 | 随对应引擎 | 按引擎许可，扩展可能另购 |
| [Houdini](https://www.sidefx.com/buy/) | 用规则生成或处理三维资源 | 专有 | 商业付费，Indie 有资格条件，Apprentice 为非商业免费方案 |
| [Gaea](https://quadspinner.com/)、[World Machine](https://www.world-machine.com/) | 地形、高度图与相关表面 | 专有 | 受限免费版＋付费版本 |
| [World Creator](https://www.world-creator.com/) | 地形制作 | 专有 | 付费许可，试用和升级另看 |
| [SpeedTree](https://unity.com/products/speedtree) | 树木、植被和相关资源 | 专有 | 付费方案，用途和版本分别确认 |
| [Tiled](https://www.mapeditor.org/)、[LDtk](https://ldtk.io/) | 二维瓦片、对象和关卡数据 | 开源 | 软件免费，可通过相应渠道支持开发 |
| [TrenchBroom](https://trenchbroom.github.io/) | 面向 Quake 系等格式的三维关卡编辑 | 开源 | 免费 |

瓦片是可重复拼接的图块，高度图记录地面高低，触发器则在条件成立时启动行为。地图编辑器可以生成布置数据，游戏再读取这些数据，处理显示、碰撞与交互。

你的环境实验室也是这类分工的例子：先调整布局并导出，再由开发流程把选定布局接入游戏。编辑时的预览帮助检查布置，实际游戏中的操作则在接入后继续验证。

<a id="tools-11"></a>
## 11｜角色、绑定、动画与动作捕捉

角色形状完成后，需要控制结构来安排动作。绑定建立控制方式，骨骼动画用骨架带动形体，动作捕捉则把实际表演转为可以整理和映射的数据。游戏接入时，再确定动作由什么状态触发和中断。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Live2D Cubism](https://www.live2d.com/en/cubism/comparison/) | 二维角色变形、表情与动作 | 编辑器专有，SDK 专门许可 | 受限 FREE＋付费 PRO，运行集成条件另看 |
| [Spine](https://esotericsoftware.com/spine-purchase) | 二维骨骼动画 | 编辑器与运行组件适用相应许可 | 编辑器付费，正式导出和集成需满足条件 |
| [Rive](https://rive.app/pricing) | 可交互动画与界面 | 编辑工具／服务与开放运行组件分开 | 免费＋付费导出、协作等方案 |
| [Moho](https://moho.lostmarble.com/)、[Toon Boom Harmony](https://www.toonboom.com/products/harmony) | 二维绑定或逐帧动画 | 专有 | 付费许可或订阅，依产品和版本 |
| [OpenToonz](https://opentoonz.github.io/e/) | 二维动画生产 | 开源 | 免费 |
| Blender、Maya | 三维绑定与动作 | 分别开源／专有 | 分别免费／付费，见 08 |
| [Cascadeur](https://cascadeur.com/plans) | 角色姿态、动作辅助与清理 | 专有 | 免费方案有用途和导出限制，付费按资格与能力区分 |
| [Character Creator](https://www.reallusion.com/character-creator/)、[iClone](https://www.reallusion.com/iclone/) | 数字角色、表演和场景演出 | 专有 | 付费许可或订阅，素材与导出条件另计 |
| [VRoid Studio](https://vroid.com/en/studio) | 风格化人形角色制作 | 专有 | 工具免费，附加素材按各自许可 |
| [MetaHuman](https://www.metahuman.com/license) | 数字人及相关动画流程 | 专门许可 | 条件免费，其余按相应产品和使用范围 |
| [Marvelous Designer](https://www.marvelousdesigner.com/) | 三维服装与布料模拟 | 专有 | 付费方案，商业资格和团队条件另看 |
| [Mixamo](https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html) | 双足人形自动绑定与动作资源 | 专有服务 | 可免费使用，对象与资源条件另看 |
| [Rokoko Studio](https://www.rokoko.com/products/studio) | 动作数据采集、清理与输出 | 专有 | 基础免费＋付费能力，捕捉设备另计 |
| [Vicon Shogun](https://www.vicon.com/software/shogun/)、[OptiTrack Motive](https://www.optitrack.com/software/motive) | 捕捉系统中的动作处理 | 专有 | 商业许可或硬件方案，按配置询价 |

关键帧记录重要时刻的姿态，重定向将动作映射到另一套骨架。它们帮助复用和调整动作，最终仍需结合角色比例与玩法节奏检查。

**《Dead Cells》先用三维角色制作动作，再转换为像素图像帧。** 作者选择这条流程，是为了便于反复修改姿态和节奏。[6](#ref-6) 因而，动画工具的价值也体现在返工方式：修改一个动作需要重画多少资源，能否继续复用原有控制结构，都应进入选型判断。

<a id="tools-12"></a>
## 12｜扫描、渲染与特效

扫描和重建取得形体，渲染根据场景生成画面，特效则组织烟尘、火花等变化。实时渲染在游戏运行中计算，离线渲染提前输出图像或视频；采用哪种方式，取决于玩家需要改变哪些内容。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [RealityScan](https://www.realityscan.com/license) | 根据照片等输入重建三维资源，桌面旧称 RealityCapture | 专有 | 桌面条件免费＋付费，Mobile 产品另外区分 |
| [Agisoft Metashape](https://www.agisoft.com/) | 摄影测量与三维重建 | 专有 | 付费许可 |
| [Meshroom／AliceVision](https://alicevision.org/) | 三维重建与图形工作流 | 开源 | 软件免费，计算和清理工作另计 |
| [Cycles](https://docs.blender.org/manual/en/latest/render/cycles/index.html)、[Eevee](https://docs.blender.org/manual/en/latest/render/eevee/index.html) | Blender 中的不同渲染系统 | 开源组件 | 随 Blender 免费 |
| [Arnold](https://www.autodesk.com/products/arnold/overview)、[V-Ray](https://www.chaos.com/vray)、[Redshift](https://www.maxon.net/en/redshift) | 三维画面渲染 | 专有 | 付费许可或订阅，软件内包含的范围另看 |
| [Niagara](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine)、[Unity Visual Effect Graph](https://unity.com/features/visual-effect-graph) | 对应引擎中的特效制作 | 随引擎许可 | 按引擎及相应模块方案使用 |
| [Effekseer](https://effekseer.github.io/en/) | 特效编辑和运行集成 | 开源 | 免费 |
| [PopcornFX](https://www.popcornfx.com/) | 特效制作与集成 | 专门商业许可 | 编辑器、SDK 和商业使用分别核对 |

粒子系统管理许多元素的生成、移动与消失，例如雨点和火星。游戏还可以用图像变化、模型变形或光照完成其他效果。因此，讨论“增加特效”时，先说明希望看见什么变化，再由实现者选择适合的方式。

<a id="tools-13"></a>
## 13｜录音、作曲、音效与交互音频

数字音频工作站／DAW 制作和编辑声音，音频中间件则安排声音在游戏中怎样随状态变化。前者产出素材，后者连接游戏与播放逻辑，两者可以配合使用。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Audacity](https://www.audacityteam.org/) | 录音、剪辑与音频处理 | 开源 | 免费 |
| [Adobe Audition](https://www.adobe.com/products/audition.html) | 音频编辑、修复与后期 | 专有 | 订阅 |
| [REAPER](https://www.reaper.fm/) | 多轨录音、编辑与混音 | 专有 | 付费许可，提供评估期 |
| [Pro Tools](https://www.avid.com/pro-tools) | 综合音频制作 | 专有 | 免费入门与付费版本按方案区分 |
| [Cubase](https://www.steinberg.net/cubase/)、[Nuendo](https://www.steinberg.net/nuendo/) | 音乐、音效与媒体音频 | 专有 | 付费许可，升级和资源另计 |
| [Logic Pro](https://www.apple.com/logic-pro/) | Apple 平台音乐制作 | 专有 | 单独购买或适用的订阅套件，平台分别确认 |
| [Ableton Live](https://www.ableton.com/en/live/)、[FL Studio](https://www.image-line.com/fl-studio) | 编曲、乐器与节奏制作 | 专有 | 付费版本，附加内容另计 |
| [Ardour](https://ardour.org/faq.html) | 多轨录音与混音 | 开源 | 源码可免费获取，官方完整成品有付费路线 |
| [ChipTone](https://sfbgames.itch.io/chiptone) | 复古短音效生成 | 免费工具，开放许可需另核实 | 可免费使用 |
| [FamiStudio](https://famistudio.org/) | 特定复古音源风格的音乐 | 开源 | 免费 |
| [Soundly](https://getsoundly.com/) | 音效检索、管理与制作 | 专有／服务 | 免费＋订阅，音效库许可另看 |
| [FMOD Studio](https://www.fmod.com/licensing) | 动态音乐、声音事件与游戏集成 | 专有／专门许可 | 条件免费，其余商业项目按许可付费 |
| [Wwise](https://www.audiokinetic.com/en/wwise/pricing/for-games/) | 交互音频与运行中间件 | 专有／专门许可 | 按预算、项目和平台等提供免费或付费方案 |

例如，你可以先用音频工具制作几层环境声音，再规定各层在哪种场景状态下播放。游戏提供状态，中间件或项目音频模块据此调整声音。若只有少量音乐和点击音效，也可以直接使用引擎或浏览器的基础音频能力，使流程与实际复杂度相符。

<a id="tools-14"></a>
## 14｜对白与分支叙事

玩家能够选择之后，文本出现的顺序会受到条件与状态影响。因此，叙事工具除了保存文字，还要组织选择、前提与结果，再把相应内容交给游戏显示。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Twine](https://twinery.org/) | 连接文本段落，形成分支和网页故事 | 开源 | 免费 |
| [ink／Inky](https://www.inklestudios.com/ink/) | 叙事语言，以及编写和测试它的编辑器 | 开源，MIT | 软件免费，出版物与支持服务另看 |
| [Yarn Spinner](https://www.yarnspinner.dev/) | 对话编写与游戏集成 | 开源核心＋商业工具 | 核心免费，Pro 和附加产品收费 |
| [articy:draft](https://www.articy.com/en/pricing/) | 角色、分支、流程与内容数据 | 专有 | 受限免费＋付费方案，协作能力分别确认 |

**inkle 的《80 Days》等作品使用 ink 组织分支叙事。** 官方说明将 ink 定位为可以接入游戏引擎的叙事技术，而 Inky 提供编写、预览和导出界面。[7](#ref-7) 因而，语言、编辑器与游戏运行系统可以分别由不同部分承担。

Ren’Py 则把视觉小说常用的显示、对白和存档等能力组织在一起。比较它与 ink 时，应先看希望它承担整个作品的主体，还是只承担其中的叙事部分，再选择配合方式。

<a id="tools-15"></a>
## 15｜界面、字体与本地化

界面把状态与可用操作交给玩家，本地化再使这些信息适合目标语言和地区。翻译后文字长度、日期格式和字体覆盖可能变化，因此语言制作还要与实际布局一起检查。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Figma](https://www.figma.com/pricing/) | 界面设计与交互原型 | 专有服务 | 免费＋付费席位和能力 |
| [Penpot](https://penpot.app/) | 界面与原型协作 | 开源核心 | 自托管软件免费，托管和支持按方案 |
| [Unity UI Toolkit](https://docs.unity3d.com/Manual/UIElements.html)、[Unreal UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/umg-ui-designer-for-unreal-engine) | 游戏运行中的界面 | 随所属引擎 | 按引擎方案使用 |
| [FontForge](https://fontforge.org/en-US/) | 字体制作与编辑 | 开源 | 软件免费，字体内容许可另看 |
| [Glyphs](https://glyphsapp.com/)、[FontLab](https://www.fontlab.com/) | 字形、字距与字体生产 | 专有 | 付费许可 |
| [Crowdin](https://crowdin.com/) | 翻译协作、术语与进度 | 专有服务 | 免费资格与付费订阅、用量方案分别确认 |
| [Weblate](https://weblate.org/en/) | 翻译管理与协作 | 开源核心 | 自托管软件免费，托管和支持收费 |
| [Poedit](https://poedit.com/) | 翻译文件编辑 | 开源基础＋专有 Pro 能力 | 基础免费，Pro 付费 |
| [OmegaT](https://www.omegat.org/) | 术语、历史译文与翻译辅助 | 开源 | 免费 |

设计原型帮助你检查布局和页面流转；接入游戏后，还需要让控件读取真实状态、执行操作，并适配不同文本。由此，设计工具、运行界面和本地化工具形成相互接续的工作，而不是交付一份可点击原型就结束全部制作。

<a id="tools-16"></a>
## 16｜版本管理

多人或长期制作都会不断修改文件。版本管理保存这些变化，使你可以比较新旧内容、追踪原因，并在需要时取回某个版本。素材备份和玩家存档则另外安排，因为它们保存的对象与目的不同。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Git](https://git-scm.com/about)、[Git LFS](https://git-lfs.com/) | 文件历史，以及大文件的存储扩展 | 开源 | 客户端免费，大文件存储和流量可能收费 |
| [GitHub](https://github.com/pricing)、[Bitbucket](https://bitbucket.org/product) | 仓库托管、协作与审查 | 服务 | 免费＋订阅和资源额度 |
| [GitLab](https://about.gitlab.com/pricing/) | 仓库、协作和自动化 | 开源核心＋商业产品 | 免费核心／基础方案，商业和托管另计 |
| [GitHub Desktop](https://desktop.github.com/) | Git 图形客户端 | 开源 | 软件免费，连接服务另看 |
| [Sourcetree](https://www.sourcetreeapp.com/) | Git 图形操作界面 | 专有 | 软件免费 |
| [Perforce P4](https://www.perforce.com/products/p4/pricing) | 代码和数字资源的版本管理 | 专有 | 小团队条件免费，扩大规模或托管服务付费 |
| [Unity Version Control](https://docs.unity.com/en-us/unity-version-control) | 代码和资源版本管理，旧称 Plastic SCM | 专有软件／服务 | 免费适用范围＋席位、存储等收费 |
| [Subversion／SVN](https://subversion.apache.org/) | 集中式版本管理 | 开源 | 软件免费，托管另计 |

提交记录一组修改，分支承载相对独立的路线，合并将变化接回目标版本。图形客户端为这些操作提供界面，托管平台则保存远端记录并组织协作。模型和音频等资源可能难以自动合并，因此团队还可以通过锁定或明确交接减少冲突。

<a id="tools-17"></a>
## 17｜任务、审片与制作追踪

资源完成后，需要交给下一位参与者使用。制作追踪记录任务、版本、意见与批准状态，使大家知道当前采用哪一份文件，以及还有哪些修改尚未完成。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Jira](https://www.atlassian.com/software/jira)、[Trello](https://trello.com/)、[GitHub Projects](https://github.com/features) | 任务、问题与进度 | 专有服务 | 免费基础＋付费方案，人数和能力分别看 |
| [Codecks](https://www.codecks.io/) | 游戏项目的任务与反馈 | 专有服务 | 免费适用方案＋订阅 |
| [Flow Production Tracking](https://www.autodesk.com/products/flow-production-tracking/overview) | 资源、镜头、任务与审阅 | 专有 | 付费订阅或团队方案，旧称 ShotGrid／Shotgun |
| [ftrack](https://www.ftrack.com/en/) | 制作追踪与审阅 | 专有 | 付费方案，按产品询价 |
| [Kitsu](https://www.cg-wire.com/kitsu/) | 创意制作任务与资源审阅 | 开源核心 | 自托管软件免费，托管和支持收费 |
| [AYON](https://docs.ayon.dev/) | 连接不同制作软件的流程 | 混合许可 | 核心、插件、支持和托管分别按方案 |
| [Slack](https://slack.com/)、[Microsoft Teams](https://www.microsoft.com/microsoft-teams/group-chat-software) | 沟通、会议与协作 | 专有服务 | 免费适用版本＋付费组织方案 |
| [Discord](https://discord.com/) | 讨论、语音和社区 | 专有服务 | 基础免费，可选订阅和增值服务 |

个人项目可以把这些记录合并到一个简单看板；分工扩大后，再按需要拆开。工具保存信息，负责人根据这些信息安排优先级和作出决定，两者配合才能推动交付。

<a id="tools-18"></a>
## 18｜调试、测试与性能分析

调试调查原因，测试检查预期结果，性能分析测量时间和内存等开销。一项功能可以分别通过规则、显示和设备检查，因此查看结果时，应同时确认检查了什么版本与范围。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [浏览器 DevTools](https://developer.chrome.com/docs/devtools) | 页面、请求、报错与性能调查 | 随浏览器，许可依产品 | 通常无需另购 |
| [Unity Profiler](https://docs.unity3d.com/Manual/Profiler.html)、[Unreal Insights](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine) | 引擎性能测量 | 随引擎 | 按引擎和模块方案使用 |
| [RenderDoc](https://github.com/baldurk/renderdoc) | 图形调试与画面帧分析 | 开源 | 免费 |
| [PIX](https://devblogs.microsoft.com/pix/)、[Nsight Graphics](https://developer.nvidia.com/nsight-graphics) | 图形与性能检查 | 厂商工具 | 可免费获取，支持平台和设备有条件 |
| Xcode／Android Studio 分析工具 | 移动设备程序与性能检查 | 随各产品 | 工具见 06，真机另计 |
| [Jest](https://jestjs.io/)、[Vitest](https://vitest.dev/)、[pytest](https://docs.pytest.org/)、[NUnit](https://nunit.org/) | 不同生态的自动化测试 | 开源 | 软件免费 |
| [Playwright](https://playwright.dev/)、[Appium](https://appium.io/) | 浏览器或应用操作自动化 | 开源 | 软件免费，执行资源另计 |
| [BrowserStack](https://www.browserstack.com/) | 浏览器和设备测试服务 | 专有服务 | 付费方案，试用和公益资格另看 |
| [NVDA](https://www.nvaccess.org/about-nvda/) | Windows 屏幕阅读器 | 开源 | 软件免费，可选支持服务另看 |
| [VoiceOver](https://www.apple.com/accessibility/vision/)、[TalkBack](https://support.google.com/accessibility/android/answer/6283677?hl=en) | Apple／Android 读屏 | 随系统，部分项目开源 | 随适用系统使用，设备另计 |

日志保存执行信息，断点帮助查看特定时刻的状态。这些材料适合调查程序行为；玩家对目标、节奏和反馈的理解，还需要通过试玩观察。因而，自动检查与实际体验可以分别提供证据，再共同用于验收。

<a id="tools-19"></a>
## 19｜物理、寻路与其他中间件

复杂项目可以把某些专门任务交给独立组件。例如，物理系统计算运动和碰撞，寻路系统计算可行路线，而游戏再决定角色为何移动以及到达后发生什么。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Box2D](https://box2d.org/) | 二维刚体物理 | 开源 | 核心免费 |
| [Jolt Physics](https://jrouwe.github.io/JoltPhysics/)、[Bullet](https://pybullet.org/wordpress/) | 三维物理模拟 | 开源 | 核心免费 |
| [PhysX](https://developer.nvidia.com/physx-sdk)、[Rapier](https://rapier.rs/) | 物理 SDK 与二维／三维模拟 | 开源核心 | 核心免费，附加组件另看 |
| [Havok](https://www.havok.com/) | 物理、导航、布料等产品 | 专有 | 商业许可或询价，引擎内包含的范围另看 |
| [Recast／Detour](https://recastnav.com/) | 导航网格生成与寻路 | 开源 | 免费 |
| [Bink、Oodle](https://www.radgametools.com/) | 视频播放与数据压缩等 | 专有 | 商业许可，部分引擎方案包含特定使用范围 |

引擎可以集成这些组件，再由项目把它们与玩法连接。因此，同一项目列出引擎和物理中间件，通常是在说明总体系统与专门功能的配合。资料中的“游戏 AI”也可能指角色决策、行为树和寻路，阅读时需要结合它实际处理的任务理解。

<a id="tools-20"></a>
## 20｜联机、服务器与数据库

浏览器或游戏客户端在玩家设备上运行。若需要账号、匹配或多人共同活动，就再接入远端服务，并安排数据保存与状态同步。各部分交换的内容取决于玩法和技术结构。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Photon Fusion／Quantum](https://www.photonengine.com/) | 多人状态同步的不同技术路线 | 专有／专门许可 | 免费适用额度＋并发、服务或企业方案 |
| [Mirror](https://mirror-networking.com/)、[FishNet](https://fish-networking.gitbook.io/docs) | Unity 多人网络框架 | 开源核心 | 核心免费，服务器和商业扩展另计 |
| [Colyseus](https://colyseus.io/)、[Nakama](https://heroiclabs.com/nakama/) | 多人服务器、账号与社交能力 | 开源核心 | 自托管软件免费，托管和支持另计 |
| [PlayFab](https://learn.microsoft.com/en-us/gaming/playfab/)、[Unity Gaming Services](https://unity.com/solutions/gaming-services) | 游戏在线服务 | 服务，SDK 等组件另许可 | 免费额度＋用量或方案收费 |
| [Epic Online Services](https://onlineservices.epicgames.com/)、[Steamworks](https://partner.steamgames.com/doc/home) | 好友、成就与平台能力 | 平台／专门许可 | 前者有免费服务范围，后者与发行协议关联 |
| [Firebase](https://firebase.google.com/pricing)、[Supabase](https://supabase.com/pricing) | 认证、数据与存储等后台 | 服务或开源核心＋服务 | 免费额度＋用量／订阅，自托管资源另计 |
| [SQLite](https://www.sqlite.org/about.html)、[PostgreSQL](https://www.postgresql.org/about/) | 本地或服务器数据管理 | 公有领域代码／开放许可 | 软件免费，托管和支持另计 |
| [Redis](https://redis.io/legal/licenses/) | 快速数据存储与访问 | 依版本提供不同许可选项 | 软件、商业支持和云服务分别确认 |
| [Docker](https://www.docker.com/pricing/) | 打包和运行程序环境 | 开源引擎＋专有 Desktop 等产品 | 引擎免费，Desktop 条件免费或付费，云服务另计 |
| [Kubernetes](https://kubernetes.io/docs/concepts/overview/) | 管理容器化程序的运行 | 开源 | 软件免费，服务器和维护另计 |
| [Amazon GameLift Servers](https://aws.amazon.com/gamelift/servers/)、[Agones](https://agones.dev/) | 游戏服务器托管或编排 | 云服务／开源 | 前者按资源计费，后者软件免费而运行资源另计 |

**《Factorio》开发团队介绍过一种只交换玩家输入、各端分别推进模拟的多人结构。** [9](#ref-9) 这可以帮助你理解，联网系统需要先决定交换什么，再确定由谁计算和如何恢复差异，而不是简单地把各端画面互相传送（案例依据当时的开发记录）。

你的单机网页则可以由托管服务分发文件，再让浏览器处理规则和本地存档。若以后需要云存档或账号，再为这些新增职责选择服务即可。

<a id="tools-21"></a>
## 21｜自动构建、打包与发布

构建处理程序与资源，打包形成交付文件，部署将它们放入目标环境，发布再向玩家提供版本。工具可以自动执行这些步骤，但需要由项目定义输入、输出和检查条件。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| 引擎导出、Xcode、Android Studio | 生成目标平台程序或工程 | 随相应工具 | 见 02、06，平台资格另计 |
| [GitHub Actions](https://docs.github.com/en/billing/concepts/product-billing/github-actions)、[GitLab CI/CD](https://docs.gitlab.com/ci/) | 自动检查、构建与交付 | 服务及开放执行组件分开 | 免费额度＋执行、存储等收费 |
| [Jenkins](https://www.jenkins.io/) | 自行组织自动化流程 | 开源 | 软件免费，机器和维护另计 |
| [TeamCity](https://www.jetbrains.com/teamcity/) | 构建与持续集成 | 专有 | 免费适用版＋付费或云端方案 |
| [Electron](https://www.electronjs.org/)、[Tauri](https://tauri.app/) | 使用网页等技术组织应用 | 开源核心 | 软件免费，平台与签名等工作另计 |
| [Capacitor](https://capacitorjs.com/) | 网页界面与移动平台连接 | 开源核心 | 核心免费，商业插件和服务另计 |
| [Steamworks](https://partner.steamgames.com/doc/gettingstarted) | Steam 构建管理、平台接入与发行 | 平台服务 | 文档免费，接入和销售按协议 |
| [itch.io](https://itch.io/docs/creators/) | 网页或可下载作品发布 | 平台服务，butler 上传工具开源 | 作品页可免费建立，交易和平台费用另看 |
| [App Store Connect](https://developer.apple.com/app-store-connect/)、[TestFlight](https://developer.apple.com/testflight/) | Apple 发布管理与测试分发 | 专有服务 | 正式用途通常与开发者计划资格关联 |
| [Google Play Console](https://play.google.com/console/about/) | Android 商店管理 | 专有服务 | 开发者注册及销售、交易条件另看 |
| [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)、[Cloudflare Pages](https://developers.cloudflare.com/pages/)、[Netlify](https://www.netlify.com/pricing/)、[Vercel](https://vercel.com/pricing) | 网站托管与部署 | 云服务 | 免费适用范围＋资源或方案收费 |

**《Baldur’s Gate 3》的 Hotfix 4 复盘说明，构建和验证需要指向同一份交付结果。** 团队在重新构建后遇到问题，回退又影响部分新存档的使用。[8](#ref-8) 因此，自动化生成成品之后，还要检查实际发布文件及其恢复条件（事件发生于 2023 年，修正版本随后重新发布）。

商店和主机平台还有资格、签名与审核要求。导出工具生成的是目标文件，正式发行还要继续完成平台流程，两部分应在计划中分别安排。

<a id="tools-22"></a>
## 22｜运行监控、数据分析与反馈

公开版本会进入更多设备和使用情境。监控记录错误与服务状态，数据分析观察已定义的行为，社区与客服则保留玩家的具体说明。这些材料一起帮助开发者判断问题和修改顺序。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Sentry](https://sentry.io/pricing/) | 错误、崩溃和性能观察 | 服务核心与开放 SDK 分开 | 自托管和云端条件不同，云端免费额度＋付费 |
| [GameAnalytics](https://www.gameanalytics.com/) | 游戏行为数据分析 | 专有服务 | 免费基础与付费数据／服务方案 |
| [Firebase Crashlytics](https://firebase.google.com/products/crashlytics) | 崩溃聚合与调查 | 服务，SDK 另许可 | 核心崩溃报告免费，关联产品可能另收费 |
| [Prometheus](https://prometheus.io/)、[Grafana](https://grafana.com/grafana/) | 指标采集与可视化 | 开源核心 | 软件免费，商业能力和托管另计 |
| [Discord](https://discord.com/)、[Discourse](https://www.discourse.org/)、[Zendesk](https://www.zendesk.com/) | 社区、论坛与客服 | 前后两者专有，Discourse 开源核心 | Discord 基础免费；Discourse 自托管免费、托管收费；Zendesk 付费 |

记录内容应对应明确的问题。例如调查加载失败，需要版本和错误信息；理解某段剧情为何被跳过，还需要玩家的情境说明。事先明确目的，也更容易减少无关数据收集，并估算隐私与服务维护成本。

<a id="tools-23"></a>
## 23｜录屏、剪辑与宣传

录屏取得实际运行画面，剪辑安排片段顺序，合成和排版则组织视觉与文字。宣传由此可以使用实机素材，也可以另行制作演示画面；发布时说明各自性质，有助于玩家理解预期体验。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [OBS Studio](https://obsproject.com/) | 录屏、直播与画面组合 | 开源 | 免费 |
| [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve) | 剪辑、调色、合成与音频后期 | 专有 | 免费版＋付费 Studio |
| [Adobe Premiere](https://www.adobe.com/products/premiere.html)、[After Effects](https://www.adobe.com/products/aftereffects.html) | 视频剪辑，以及动态图形和合成 | 专有 | 订阅 |
| [Final Cut Pro](https://www.apple.com/final-cut-pro/) | Apple 平台剪辑 | 专有 | 单独购买或适用套件订阅，平台方案另看 |
| [Kdenlive](https://kdenlive.org/) | 视频剪辑 | 开源 | 免费 |
| [Fusion](https://www.blackmagicdesign.com/products/fusion) | 节点式视觉合成 | 专有 | Resolve 内置与独立 Studio 按版本区分 |
| [FFmpeg](https://ffmpeg.org/)、[HandBrake](https://handbrake.fr/) | 音视频转换与压缩 | 开源，组件许可可能不同 | 核心免费，编解码和分发条件另核对 |
| [Canva](https://www.canva.com/pricing/) | 海报、商店图与社交内容 | 专有服务 | 免费＋订阅，素材许可另看 |

例如，为你的游戏做短视频时，可以先录制一次完整操作，再剪出能说明玩法的片段。片头和字幕可以在剪辑工具中增加；这些宣传效果与游戏本身运行的效果分别制作，介绍时也应相应区分。

<a id="tools-24"></a>
## 24｜素材平台与批量加工

素材平台提供图像、模型、声音或插件，加工工具再将所选内容整理成项目需要的规格。因为同一平台会收录不同作者与许可的内容，选择时需要逐项保留来源和条件。

| 平台／工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [Fab](https://www.fab.com/)、[Unity Asset Store](https://assetstore.unity.com/) | 模型、贴图、插件与工具包 | 市场，逐项许可 | 免费与付费资源并存 |
| [itch.io Game Assets](https://itch.io/game-assets) | 游戏素材市场 | 逐项许可 | 免费、付费或自定价格 |
| [Kenney](https://kenney.nl/assets)、[Poly Haven](https://polyhaven.com/) | 游戏资源、模型、纹理与环境图 | 按相应开放内容许可 | 有免费资源，工具和附加内容另看 |
| [Freesound](https://freesound.org/help/faq/) | 声音分享 | 不同声音采用不同许可 | 可免费取得，署名和用途条件分别确认 |
| [TexturePacker](https://www.codeandweb.com/texturepacker) | 精灵图集和位置数据打包 | 专有 | 免费受限功能＋付费 Pro |
| [ImageMagick](https://imagemagick.org/) | 图片批量缩放、转换与加工 | 开源 | 免费 |

图集把多张小图排入较大的图像，并附位置数据供程序读取。源工程如 `.blend`、`.psd` 保存编辑信息，`.png`、`.glb`、`.fbx`、`.wav` 等文件则常用于交换或运行。格式规定怎样保存内容，实际工具决定支持哪些部分，所以导出后仍需在目标项目里检查。[glTF 官方说明](https://www.khronos.org/gltf/)

<a id="tools-25"></a>
## 25｜AI 辅助

AI 可以参与资料整理、编程和资源制作。它描述的是开发中的协作方式，成品仍然需要具体语言、引擎或运行环境执行。因此，介绍项目时，可以先列技术栈，再另外说明 AI 参与了哪些工作。

| 工具 | 用途与解释 | 开放情况 | 费用类型 |
| --- | --- | --- | --- |
| [ChatGPT](https://openai.com/chatgpt/overview/) | 讨论、资料辅助、文档和编程协作 | 专有服务 | 免费适用额度＋订阅，其他接入方式另计 |
| [Codex](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan) | 阅读、修改和检查代码，执行开发任务 | 服务与客户端分开，部分客户端开源 | 按账号方案、额度或 API 等方式计费 |
| [GitHub Copilot](https://github.com/features/copilot) | 编码与开发辅助 | 专有服务 | 免费适用方案＋付费计划或用量 |
| [Cursor](https://cursor.com/pricing) | AI 辅助代码工作环境 | 专有产品，基于开放组件 | 免费受限＋订阅或用量 |
| [Adobe Firefly](https://www.adobe.com/products/firefly.html) | 概念与视觉生成 | 专有服务 | 免费适用额度＋订阅或生成额度 |
| [ComfyUI](https://comfy.org/) | 组织模型和图像处理工作流 | 开源核心＋云服务 | 本地核心免费，设备、模型与云端另计 |

生成材料进入项目后，仍需要检查内容、运行结果、风格和使用条件。把 AI 任务写成明确交付物，例如整理对白、处理资源或实现一项操作，再按相应标准检查，就能与其他开发工作采用相同的验收方式。

<a id="licensing"></a>
## 授权与总成本

软件、运行组件、素材和平台可能来自不同提供者，所以需要分别记录它们的费用与许可。把这些条件放到制作计划里，才能看出现在能用什么，以及规模扩大后需要承担什么。

| 成本层次 | 需要确认的内容 |
| --- | --- |
| 制作软件 | 版本、席位、商业资格与订阅期限 |
| 运行组件 | SDK、中间件及成品分发条件 |
| 素材与字体 | 作者、来源、署名、修改与再分发范围 |
| 平台与服务 | 账号资格、存储、流量、并发、构建和交易 |
| 人力与维护 | 学习、接入、返工、迁移、测试和支持 |

例如，永久许可可能只覆盖某个版本，教育方案可能限定用途，开源组件可能要求保留声明。因此，判断时应读到与实际用途有关的条款，再选择合适方案。

你还可以分别估算开始制作、正式发行和规模扩大三个阶段。免费额度可能随着用量增长而不足，自托管开源软件则可能持续产生机器与维护成本。把许可费和持续工作一起估算，才能比较完整成本。

<a id="combinations"></a>
## 开发工具组合示例

下表用几个常见方向说明分工。工具之间能否直接交换资源，还需要以具体版本和格式验证；斜线表示备选路线。

| 路线 | 工具与内容关系 | 主要成本位置 |
| --- | --- | --- |
| 图片与对白网页 | 绘图或 Blender 生成图片 → HTML／CSS／JavaScript 组织交互 → 浏览器运行 → 托管服务分发 | 资源制作、交互实现、设备与托管用量 |
| 视觉小说 | 绘图与音频工具制作资源 → Ren’Py 组织对白、选项和保存 → 平台交付 | 美术、写作、翻译、声音和附加组件 |
| 二维动作或探索 | 像素工具制作角色 → 地图或引擎编辑器安排关卡 → Godot／GameMaker／Phaser 等组织运行 | 动作、关卡、规则和测试 |
| 实时网页三维 | Blender 制作模型 → 导出资源 → Three.js／Babylon.js／PlayCanvas 等显示 → JS／TS 处理行为 | 模型、编辑服务、性能与设备适配 |
| 多人协作三维制作 | 三维、材质与动画工具交付资源 → Unity／UE／自有引擎整合 → 测试和发布 | 席位、资源、协作、平台与长期支持 |

你为《体温调节》讨论的预渲染方案属于第一种分工：三维软件提前生成资源，网页负责显示与交互。若以后允许玩家自由改变三维视角，就需要重新评估运行端的图形能力，因为需求已经从调用固定画面变成持续计算新画面。

<a id="confusions"></a>
## 易混名称与概念

| 名称／说法 | 解释 |
| --- | --- |
| Unity、C#、Visual Studio | 分别是引擎、语言和开发环境，可配合使用 |
| Java、JavaScript | 两种独立语言，各有工具与应用范围 |
| Three.js、TypeScript | 三维库与语言，位于不同层次 |
| VS Code、Visual Studio | 两个不同产品，选择取决于开发需求 |
| Clickteam Fusion、Photon Fusion、Blackmagic Fusion | 分别涉及游戏制作、多人网络和视觉合成 |
| Blender、Cycles | 综合制作软件，以及其中的渲染系统 |
| Unreal、UEFN | 通用引擎，以及面向 Fortnite 的特定创作工具 |
| Git、GitHub、GitHub Pages | 版本记录、仓库协作和网页分发 |
| ink、Inky | 叙事语言，以及编写它的编辑器 |
| Live2D 编辑器、SDK | 内容制作工具，以及运行集成组件 |
| AI 文件、游戏 AI、生成式 AI | 分别可能指 Illustrator 文件、角色决策、生成模型 |
| P4／Helix Core、Unity Version Control／Plastic SCM | 对应产品的新旧名称，操作与许可按版本确认 |
| Flow Production Tracking／ShotGrid／Shotgun | 制作追踪产品在不同阶段采用的名称 |
| RealityScan／RealityCapture | 桌面产品的新旧名称，Mobile 另有产品范围 |
| Affinity Designer／Photo／Publisher | 旧的分别命名应用，当前统一产品的方案另看 |
| Shader／着色器 | 用于图形计算的一类程序，可由不同工具编写 |
| 开源引擎制作的游戏 | 引擎与游戏内容分别适用自己的许可 |
| HTML5 游戏、3A／AAA | 前者概括网页技术路线，后者涉及制作规模等语境 |

<a id="finish"></a>
## 项目技术说明的组织方式

介绍自己的作品时，可以依次说明主体系统、编程语言、资源生产和发布方式。这样的顺序先说明成品怎样组成，再说明素材从哪里来、玩家如何取得。

例如，预渲染网页可以介绍为：三维软件提前制作图片，HTML、CSS 与 JavaScript 组织显示和交互，浏览器执行，托管服务分发。采用通用引擎时，则说明引擎、脚本与素材之间的关系。AI 的参与可以另加一句，描述开发中的辅助工作。

**用途说明工具承担什么，输出说明它交付什么，连接关系说明下一步怎样使用，费用说明采用它的成本。** 这四项足以帮助你先认识一个新工具，再决定是否需要深入学习。

<a id="known-games"></a>
## 制作案例的查阅方式

案例已经放在对应环节中：在 [02](#tools-02) 看引擎与美术的分工，在 [04](#tools-04) 看框架路线，在 [07](#tools-07) 和 [11](#tools-11) 看资源与动作生产，在 [14](#tools-14) 看叙事工具，在 [20](#tools-20) 和 [21](#tools-21) 看同步与发布。阅读时可以先理解该段概念，再查看案例中开发者为何作出这种选择。

<a id="sources"></a>
## 参考文献与学习资源

### 制作案例

<a id="ref-1"></a>
**[1] Unity／Team Cherry. _Hollow Knight — Made with Unity_.** [英文访谈](https://unity.com/made-with-unity/hollow-knight)。免费。本文使用其中关于初代《Hollow Knight》的制作说明，重点是 Photoshop 资源与 Unity 运行的分工。

<a id="ref-2"></a>
**[2] GameMaker／Toby Fox. _Undertale_.** [官方作品展示](https://gamemaker.io/en/showcase/undertale)。英文，免费。用于认识 GameMaker 的实际作品范围。

<a id="ref-3"></a>
**[3] Godot Engine. _Showcase_.** [官方作品目录](https://godotengine.org/showcase/)。英文，免费，包含《Brotato》等作品。与引擎许可说明一起阅读，可以分别理解技术采用与成本条件。

<a id="ref-4"></a>
**[4] MonoGame Foundation. _MonoGame_.** [官方 itch.io 页面](https://monogame.itch.io/) · [框架官网](https://monogame.net/)。英文，免费。官方列出《Celeste》《Stardew Valley》等使用作品，适合对照框架与综合编辑器的不同工作方式。

<a id="ref-5"></a>
**[5] Unity／Studio MDHR. _Cuphead — Made with Unity_.** [制作访谈](https://unity.com/made-with-unity/cuphead)。英文，免费。先看手绘资源怎样经过数字处理进入游戏。

<a id="ref-6"></a>
**[6] Vasseur, Thomas. _Art Design Deep Dive: Using a 3D Pipeline for 2D Animation in Dead Cells_（2018-01-25）.** [作者原文](https://www.gamedeveloper.com/production/art-design-deep-dive-using-a-3d-pipeline-for-2d-animation-in-i-dead-cells-i-)。英文，免费。重点看修改动作的成本与制作路线的联系。

<a id="ref-7"></a>
**[7] inkle. _ink: A Narrative Scripting Language for Games_.** [官方说明与教程](https://www.inklestudios.com/ink/)。英文，软件与基础教程免费，出版物另计。说明 ink、Inky 和引擎集成的职责，并提供作者实际采用的叙事工具。

<a id="ref-8"></a>
**[8] Larian Studios. _Hotfix 4 Redeployed_（2023-08-17）.** [官方复盘](https://baldursgate3.game/news/hotfix-4-redeployed_86)。英文，免费。用于理解构建、验证和回退之间的联系（历史版本事件）。

<a id="ref-9"></a>
**[9] Wube Software. _Friday Facts #188 — Bug, Bug, Desync_（2017-04-28）.** [开发团队原文](https://www.factorio.com/blog/post/fff-188)。英文，免费。用于理解多人同步中交换信息与执行规则的分工。

### 工具与授权资料

表格中的工具链接兼作对应来源。开源与费用的易混情况，可进一步查阅 [OSI](https://opensource.org/osd)、[Godot](https://godotengine.org/license/)、[Defold](https://defold.com/license/)、[Aseprite](https://www.aseprite.org/faq/)、[Ardour](https://ardour.org/faq.html)、[VS Code](https://code.visualstudio.com/docs/supporting/faq)、[Live2D](https://www.live2d.com/en/cubism/comparison/)、[Spine](https://esotericsoftware.com/spine-purchase)、[FMOD](https://www.fmod.com/licensing)、[Wwise](https://www.audiokinetic.com/en/wwise/pricing/for-games/)和 [Redis](https://redis.io/legal/licenses/)的官方材料。实际使用时，先确认版本和用途，再读相应条款。

名称变化及新方案可参见 [PlayCanvas 编辑器前端说明](https://blog.playcanvas.com/playcanvas-editor-frontend-is-now-open-source/)、[Canva 的 Affinity 介绍](https://www.canva.com/newsroom/news/all-new-affinity/)、[Apple 创作应用方案](https://www.apple.com/uk/newsroom/2026/01/introducing-apple-creator-studio-an-inspiring-collection-of-creative-apps/)和 [Codex 使用方案](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan)。旧教程用于理解当时的流程，当前采购和发布则继续核对现行产品条件。

### 教材、课程与作者资源

| 文献或资源 | 获取方式 | 推荐内容 |
| --- | --- | --- |
| **Heather Chandler，_The Game Production Toolbox_（2019）**，[出版社](https://www.routledge.com/Game-Production-Proven-Business-Techniques-to-Produce-the-Best-Games/Chandler/p/book/9781138341708) | 英文，书籍购买或借阅 | 把工具放进制作计划、预算和交付关系中理解 |
| **Jason Gregory，_Game Engine Architecture_，第 4 版**，[作者官网](https://www.gameenginebook.com/) | 英文，两卷书籍购买或借阅，概览免费 | 系统、资源与工具链概述，可先选概念章节 |
| **Tracy Fullerton，_Game Design Workshop_，第 5 版（2024）**，[出版社](https://www.routledge.com/Game-Design-Workshop-A-Playcentric-Approach-to-Creating-Innovative-Games/Fullerton/p/book/9781032607009) | 英文，书籍购买或借阅 | 原型、试玩和体验判断，帮助决定工具应服务于什么任务 |
| **Scott Chacon、Ben Straub，_Pro Git_，第 2 版**，[英文全文](https://git-scm.com/book/en/v2) | 在线免费，纸书另计 | 版本、提交和分支的关系 |
| **MDN Web Docs**，[游戏入口](https://developer.mozilla.org/en-US/docs/Games)、[游戏结构](https://developer.mozilla.org/en-US/docs/Games/Anatomy) | 英文，免费 | 网页、绘图接口与运行环境的分工 |
| **Unity Learn／Godot Docs**，[Unity](https://learn.unity.com/)、[Godot](https://docs.godotengine.org/en/stable/) | 官方基础内容免费 | 编辑器、场景与资源的用途，然后按需要看操作教程 |
| **Blender Manual／Blender Studio Training**，[手册](https://docs.blender.org/manual/en/latest/)、[课程](https://studio.blender.org/training/) | 英文，手册免费，课程依内容有免费与订阅 | 资源从源工程到成品的处理流程 |
| **Philip B. Tan、Jason Begy，MIT CMS.608 _Game Design_（2010 秋）**，[公开课](https://ocw.mit.edu/courses/cms-608-game-design-fall-2010/) | 英文，课程资料和录音免费 | 规则、原型和试玩，为选型提供体验依据 |
| **Martin Jonasson、Petri Purho，_Juice It or Lose It_（2012）**，[GDC 演讲](https://gdcvault.com/play/1016789/Juice-It-or-Lose) | 英文，该条目免费 | 通过演示观察视听反馈的作用 |
| **Cem Yuksel，计算机图形学课程**，[作者课程页与 YouTube 入口](https://www.cemyuksel.com/courses/) | 英文，公开视频可免费查看 | 先看画面形成与图形流程，再按需要深入 |

可以先查自己项目涉及的工具，再选一篇接近当前问题的开发者案例。需要建立系统认识时，再选择相应教材；这样，学习内容会与实际制作决定保持联系。

<a id="case-isopoda"></a>
## 以你正在做的《等足目赋格》作完整对应

你的网页版直接使用 JavaScript 组织观察、交互与状态，Canvas 2D 绘制场景，HTML 和 CSS 安排界面。各部分通过项目模块连接起来，因此可以采用浏览器已有的能力，完成这款游戏需要的运行系统。[网页入口](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/index.html) · [模块说明](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/README.md)

以下将已经核对的实现放回分类表，便于你判断每一种技术的位置（依据 2026-10-13 的[固定仓库版本 `0bbe083`](https://github.com/fivsevn/umwelt/tree/0bbe083943a4b307e38e3ea0de435d3d7864a345)，范围为网页主游戏与配套工具）。

| 对应分类 | 你的实现与依据 | 成本理解 |
| --- | --- | --- |
| [01 规划与资料](#tools-01) | Markdown 开发记录、来源与数据约定。[文档](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/docs/README.md) | 文档格式本身无许可费，整理与核查需要时间 |
| [02—04 运行结构](#tools-02) | 自定义 JavaScript 模块连接界面、状态与规则。[分工](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/README.md) | 这条路线省去通用引擎采购，开发与维护由项目承担 |
| [05 语言](#tools-05) · [15 界面](#tools-15) | HTML 组织画布和控件，CSS 安排显示，JavaScript 处理行为。[入口](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/index.html) | 使用这些标准本身没有制作许可费 |
| [07 图像](#tools-07) · [11 动画](#tools-11) | 按身体比例、颜色、姿态与阶段生成像素。[角色](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/sprites.mjs) | 程序参与视觉生产，相应规则需要制作和检查 |
| [10 场景](#tools-10) · [12 渲染](#tools-12) | Canvas 2D 与生境模块组合环境和角色。[场景](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/habitat.mjs) | 使用浏览器接口，性能与适配工作另计 |
| [10 编辑器](#tools-10) | 环境实验室提供布置、拖动与导入导出。[约定](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/docs/laboratories.md) | 专用工具能够辅助制作，同时需要维护 |
| [13 音频](#tools-13) | Web Audio 与共享模块处理播放、音量和合成点击音效。[音频](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/assets/audio/audio-engine.mjs) | 接口本身无许可费，音源和素材按实际使用确认 |
| [14 叙事](#tools-14) | 内容数据与状态规则决定观察文字及反馈。[规则](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/engine.mjs) | 写作、组织和分支检查属于制作成本 |
| [15 本地化](#tools-15) | 语言模块和文本目录处理语言显示。[分工](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/README.md) | 翻译和布局检查按内容量安排 |
| [20 保存](#tools-20) | localStorage 保存 JSON 形式的进度。[读写](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/game.js) | 进度保存在浏览器本地，云端同步需另行设计 |
| [16 版本](#tools-16) | Git 与 GitHub 保存项目和修改记录。[仓库](https://github.com/fivsevn/umwelt/tree/0bbe083943a4b307e38e3ea0de435d3d7864a345) | Git 免费，托管按账号方案和实际用量 |
| [06 开发](#tools-06) · [18 验证](#tools-18) | Node.js 与 Playwright 等检查规则、操作和显示。[测试](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/tests/README.md) | 工具开源免费，设备和执行资源另计 |
| [21 发布](#tools-21) · [24 加工](#tools-24) | Actions／Pages 准备站点、字体与资源标识，再分发文件。[发布](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/docs/deployment.md) | 按服务适用范围和额度计算 |
| [25 AI 辅助](#tools-25) | 辅助程序、调试、研究整理与文档。[说明](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/README.md) | 按你实际采用的服务方案计算 |

代码能够帮助确认上述技术分工，而具体编辑器、购买记录与服务账单还需查看实际使用记录。因此，表中只把有材料支持的技术写为已采用工具，其余留在前面的可选目录中。

### 在你的项目中区分引擎、编辑器与保存

`engine.mjs` 处理这款游戏的状态和规则，相关模块共同构成运行系统。这里的名称描述它在项目中的职责；若以后希望把它作为其他作品的通用引擎，还需要进一步整理可复用接口、内容导入和制作方式。

环境实验室则承担编辑职责。你在那里调整布局并导出数据，再通过开发流程将选定布局接回游戏。**实验室编辑布置，导出文件保存布置，游戏程序使用已接入的数据执行规则。** 因为编辑与发布之间还有这一步，实验室中的临时改动不会自动修改公开游戏或仓库。[编辑与发布关系](https://github.com/fivsevn/umwelt/blob/0bbe083943a4b307e38e3ea0de435d3d7864a345/isopoda/docs/laboratories.md)

版本和进度也保存不同内容：GitHub 记录开发文件，Pages 向玩家分发网页，浏览器本地存储保留游玩进度。清除网站数据时，进度也可能被删除，因此排查缓存之前应先确认需要保留的存档。[本地存储说明](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)

### 可以采用的介绍

用于简短交流：

> 这是用原生 JavaScript 和 Canvas 2D 做的网页游戏。浏览器提供绘图等基础能力，项目自己的程序负责交互与叙事，没有采用 Unity、Godot 这类通用游戏引擎。

用于较完整的项目介绍：

> 《等足目赋格》使用 HTML、CSS 和 JavaScript 开发，以 Canvas 2D 绘制场景，通过程序化像素绘制呈现动物形态与动作。项目模块处理交互、环境状态和叙事推进，网页版在浏览器本地保存进度，通过 GitHub Pages 发布。开发过程中使用 AI 辅助实现与维护，作品方向和最终版本由作者决定。

这两种介绍分别适合不同篇幅，但都沿用同一条关系：语言表达规则，图形接口生成画面，模块组织运行，平台交付文件，AI 参与制作协作。以后增加新功能或更换发布方式时，再对应更新其中的部分即可。

[返回用途分类](#map) · [下一篇：运行原理 003](posts-2026-umwelt-game-development-handbook-003.html) · [返回个人笔记目录](../index.html)
