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
  按用途认识游戏开发中的软件、引擎、编程语言、程序库与在线服务。解释它们的职责、区别与配合方式，覆盖个人、小团队与大型制作中的主要环节，并附工具官网、易混名称和示例组合。
parents: ["posts-index"]
related: ["posts-2026-umwelt-game-development-handbook-001"]
tags: ["game-development", "software", "tools", "game-engine", "programming", "workflow", "handbook"]
audience: ["self", "public"]
languages: ["zh"]
maturity: "evolving"
confidence: 0.9
visibility: "public"
source_of_truth: "devlog"
lang: "zh-CN"
description: |
  一篇按用途查阅的游戏开发软件地图。解释引擎、语言、库、素材制作、版本管理、测试、联机、发布等概念，附代表工具与官网。
canonical_url: "https://devlog.fivsevn.com/posts/2026/posts-2026-umwelt-game-development-handbook-002.html"
created: "2026-10-13"
updated: "2026-10-13"
metadata_updated: "2026-10-13"
---

# 游戏开发软件地图手册｜ChatGPT 写给五月七日的指导笔记 002

**游戏开发工具的用途、关系与组合 · 撰写：ChatGPT · 2026-10-13**

一款游戏可以使用 Unity 组织场景和运行逻辑，用 C# 编写行为，在 Blender 中制作模型，再通过 Steam 分发。这些名称分别对应**游戏引擎、编程语言、资源制作软件和发布平台**，并不是同一类工具。

[上一篇手册](https://devlog.fivsevn.com/posts/2026/posts-2026-umwelt-game-development-handbook-001.html)介绍制作流程。本篇按用途整理流程中涉及的工具，说明它们的职责、区别及配合方式。

本文覆盖个人、小团队和大型制作中的主要软件类别与代表工具，同时收录相关语言、程序库和在线服务。**覆盖范围是主要工具类别，而非所有产品、插件和公司内部工具。** 同一软件可能承担多种任务，表中以主要用途归类，不按价格、名气或团队规模划分等级。

工具名称的链接指向官网、官方文档或作者项目页，兼作来源与后续查阅入口。产品名称、授权和导出平台可能调整，本文不列精确价格与版本号。**功能定位按 2026-10-13 查阅的资料整理；实际采用前，仍需核对目标版本、授权与平台支持。**

<a id="start"></a>
## 基本概念：引擎、语言与工具的职责

| 名词 | 定义 | 解释 |
| --- | --- | --- |
| 游戏引擎 | 提供游戏运行所需的一组基础系统，通常配有制作工具 | 例如显示画面、播放声音、接收操作；具体使用哪些素材、执行哪些规则，由项目决定 |
| 编辑器 | 供开发者编辑代码、资源或场景的工具 | 例如摆放角色、修改脚本、调整动画；编辑器不一定具有完整的游戏运行系统 |
| 编程语言 | 编写程序时遵循的表达规则 | 用规定的写法描述条件、操作和数据，例如玩家点击后显示下一句对白 |
| 库／程序库 | 可被程序调用的一组现成功能 | 项目通过调用已有功能减少重复编写；这里的“库”不是图片素材库 |
| 框架 | 提供功能并约定程序组织方式的基础结构 | 项目按照框架的结构编写内容和逻辑，不必从空白程序开始组织所有部分 |
| 插件 | 扩展现有软件功能的部件 | 在原有软件中增加某项能力，通常依赖对应的软件环境 |
| SDK，软件开发工具包 | 接入某个平台或功能的一套代码、说明和工具 | 例如接入平台成就或动画功能时，使用厂商提供的程序组件与配套资料 |
| API，应用程序接口 | 软件之间调用功能的约定 | 程序按照规定的名称、参数和返回结果使用功能；API 本身不是一个必须另装的软件 |
| 运行时／Runtime | 游戏或功能实际执行时需要的程序部分 | 制作阶段使用编辑器；成品运行时，由对应程序加载资源并执行功能 |
| 中间件／Middleware | 接入项目、负责专门任务的技术 | 例如把独立的声音、物理或联机系统接入游戏，而不重新实现整套功能 |
| 资源／素材／Asset | 游戏使用的图像、模型、音频、字体等内容 | 这些内容由制作工具生成或整理，再由游戏程序读取和使用 |
| 工具链／制作管线 | 相互配合的工具，以及资源处理与交付流程 | 工具链侧重使用哪些工具，制作管线侧重内容从源文件到游戏成品的处理步骤 |
| 技术栈 | 一个项目组合使用的技术 | 例如所选的语言、框架、数据库和相关工具，而非某个单独的软件 |

这些分类存在交叉。例如 [Phaser 官方](https://docs.phaser.io/phaser/getting-started/what-is-phaser)称它为游戏框架，同时说明它以 JavaScript 库的形式提供。因此，库、框架和引擎不能简单排列成高低等级，应根据实际提供的功能与组织方式区分。

以 Unity 为例，开发者在编辑器中摆放角色、设置场景和调整参数；玩家打开导出的游戏时，无需安装 Unity 编辑器，而是由随成品发布的引擎运行时加载资源、执行脚本并生成画面。角色的台词和点击后的反应，则由开发者编写的内容与规则决定。**因此，编辑器负责供开发者制作和调整游戏内容；引擎提供游戏运行所需的基础系统，其运行时在玩家设备上执行相应功能。** 两者通常包含在同一套产品中，但承担的职责不同。[Unity 官方介绍](https://unity.com/products/unity-engine)

<a id="map"></a>
## 用途分类与章节索引

| 章节 | 主要内容 |
| --- | --- |
| [01 规划与资料](#tools-01) | 设计文档、资料整理、参考图与数值计算 |
| [02 通用引擎](#tools-02) · [03 专用工具与平台](#tools-03) · [04 框架与图形库](#tools-04) | 游戏主体的制作与运行工具 |
| [05 语言与技术名词](#tools-05) · [06 编程工作台](#tools-06) | 编写规则、编辑代码及处理程序依赖 |
| [07 二维绘图](#tools-07) · [08 三维建模](#tools-08) · [09 材质与贴图](#tools-09) · [10 场景与关卡](#tools-10) | 图像、模型、表面效果及游戏环境的制作 |
| [11 角色与动画](#tools-11) · [12 扫描、渲染与特效](#tools-12) | 角色动作、三维重建及画面效果 |
| [13 音频](#tools-13) · [14 交互叙事](#tools-14) · [15 界面与本地化](#tools-15) | 声音、对白、菜单、字体与多语言内容 |
| [16 版本管理](#tools-16) · [17 制作协作](#tools-17) | 文件历史、任务分工、资源审阅与交接 |
| [18 测试与性能](#tools-18) · [19 物理等中间件](#tools-19) | 错误定位、性能测量及专门功能的接入 |
| [20 网络与后台](#tools-20) | 联机同步、账号、服务器与数据存储 |
| [21 构建与发布](#tools-21) · [22 维护与运营](#tools-22) | 生成成品、平台分发、运行监控与玩家反馈 |
| [23 宣传制作](#tools-23) · [24 素材与加工](#tools-24) · [25 AI 辅助](#tools-25) | 宣传内容、现成资源、批量处理与 AI 工具 |
| [授权类型](#licensing) · [组合示例](#combinations) · [易混名称](#confusions) | 使用条件、工具配合方式与名称对照 |

初次阅读可先了解基本概念、02—06 节和组合示例，其余部分按用途查阅。查找具体软件时，可使用浏览器的“在页面中查找”功能。

<a id="tools-01"></a>
## 01｜规划、资料与数值：设计记录与数据整理

这一类工具用于记录设定、编写文档、整理参考资料和计算数值，通常不直接负责游戏运行。

| 工具 | 主要用途 | 解释 |
| --- | --- | --- |
| [Word](https://www.microsoft.com/microsoft-365/word)、[Google Docs](https://workspace.google.com/products/docs/) | 文档编写、评论与修改 | 编写企划、需求、剧情初稿和验收说明 |
| [Notion](https://www.notion.com/product)、[Obsidian](https://obsidian.md/) | 知识整理与关联笔记 | 组织角色、世界观、调查笔记和设计决策 |
| [Excel](https://www.microsoft.com/microsoft-365/excel)、[Google Sheets](https://workspace.google.com/products/sheets/)、[LibreOffice Calc](https://www.libreoffice.org/) | 表格、公式和数据整理 | 列道具数值、计算成长曲线、记录资源清单 |
| [Miro](https://miro.com/)、[FigJam](https://www.figma.com/figjam/)、[draw.io／diagrams.net](https://www.drawio.com/) | 白板、流程图和关系图 | 绘制剧情分支、页面跳转和玩家操作流程 |
| [PureRef](https://www.pureref.com/) | 参考图片整理 | 在同一画布中排列姿态、材质和配色等视觉参考 |
| [Zotero](https://www.zotero.org/) | 文献、来源和引用管理 | 保存资料出处，并将设计依据关联到具体文献 |

**这一环节主要产出文档和数据。** 数据能否直接进入游戏，取决于项目是否具有对应的读取或转换功能；表格中的内容不会自动成为游戏规则。

<a id="tools-02"></a>
## 02｜通用游戏引擎：场景、规则与运行系统

游戏引擎提供可重复使用的图形、声音、输入等基础能力。开发者利用这些系统组织素材和规则，不必从底层重新实现全部功能。游戏的内容、玩法和交互仍需单独设计。

| 引擎 | 主要定位 | 解释 |
| --- | --- | --- |
| [Unity](https://unity.com/products/unity-engine) | 通用二维／三维引擎 | 组织场景、角色、界面和规则；脚本主要使用 C# |
| [Unreal Engine／虚幻引擎／UE](https://www.unrealengine.com/) | 通用实时三维引擎及制作工具 | 提供场景、动画、物理等系统；规则可用 C++、蓝图等方式制作，也可用于非写实风格 |
| [Godot](https://godotengine.org/features/) | 通用二维／三维引擎 | 用场景和节点组织游戏；常见脚本语言是 GDScript、C# |
| [GameMaker](https://gamemaker.io/en) | 以二维制作为核心 | 通过对象、房间、事件等组织项目，支持 GML 代码和图形化逻辑 |
| [GDevelop](https://gdevelop.io/) | 以事件系统为核心的可视化制作 | 用“满足条件 → 执行动作”组织行为，也能扩展功能 |
| [Construct](https://www.construct.net/en) | 浏览器中的游戏制作工具，偏二维 | 用事件表安排逻辑；浏览器是其制作环境，不代表成品只能是静态网页 |
| [Clickteam Fusion](https://www.clickteam.com/clickteam-fusion-2-5) | 事件式游戏与交互应用制作 | 用可视化事件安排规则，与视频合成软件 Fusion 是不同产品 |
| [Defold](https://defold.com/) | 跨平台游戏引擎 | 提供编辑器、资源处理和运行系统，脚本使用 Lua |
| [Cocos Creator](https://www.cocos.com/en/creator) | 二维／三维游戏制作 | 通过可视化编辑器和脚本组织项目；Creator 与旧教程中的 Cocos2d-x 需区分 |
| [LayaAir](https://www.layaair.com/) | 面向跨平台与网页等场景的引擎 | 可用于网页、小游戏等开发场景 |
| [O3DE](https://o3de.org/) | 可扩展的三维引擎 | 提供模块组合、实时内容制作和底层扩展能力 |
| [Stride](https://www.stride3d.net/) | C#／.NET 路线的引擎 | 使用编辑器与引擎系统制作二维、三维项目 |
| [Flax](https://flaxengine.com/) | 三维游戏引擎 | 提供编辑器、渲染和脚本工具，是独立引擎而非 Unity 插件 |
| [Frostbite／寒霜](https://www.ea.com/frostbite)等公司自有引擎 | 针对公司项目和制作流程维护的引擎 | 使用范围与获取方式由所属公司决定，不能按公开通用引擎处理 |

**团队规模不直接决定引擎类型。** 大公司可以使用通用引擎，个人也可以使用完整的三维引擎。选型主要取决于项目需求、现有资产、人员能力、目标平台和维护成本。

蓝图、可视化编程和事件表通过节点或界面设置部分规则，减少直接编写代码的操作。它们改变的是逻辑的编写方式，条件、顺序和结果仍需由开发者确定。

<a id="tools-03"></a>
## 03｜专用制作工具与创作平台

这一类工具预先提供某种作品需要的结构。例如视觉小说工具通常包含对白、选项和存档功能，可减少通用系统的搭建工作。创作平台则可能同时规定作品的运行环境与发布方式。

| 工具／平台 | 主要用途 | 解释 |
| --- | --- | --- |
| [Ren’Py](https://www.renpy.org/) | 视觉小说、对话叙事 | 提供对白、选项等机制；用专用脚本写内容，必要时用 Python 扩展 |
| [RPG Maker／RPG 制作大师](https://www.rpgmakerweb.com/products/rpg-maker-mz) | 以地图、事件、角色等系统制作 RPG | 许多内容在界面中设定；不同代产品的脚本和插件体系需分别确认 |
| [TyranoScript／TyranoBuilder](https://tyranoscript.com/) | 视觉小说制作 | 前者采用脚本方式，后者提供图形化制作界面，是同一生态中的不同操作路线 |
| [Twine](https://twinery.org/) | 非线性文本和互动故事 | 连接文本段落并发布为网页；复杂功能取决于故事格式及扩展 |
| [GB Studio](https://www.gbstudio.dev/) | 制作 Game Boy 风格及相应平台作品 | 围绕特定显示和运行限制安排制作流程 |
| [Bitsy](https://bitsy.org/) | 小型像素探索与叙事 | 用有限的房间、角色和对白组织故事 |
| [PICO-8](https://www.lexaloffle.com/pico-8.php) | 人为限定规格的“幻想主机”创作环境 | 集成代码、绘图和音效工具，在固定限制下制作小型作品 |
| [TIC-80](https://tic80.com/) | 幻想电脑式制作环境 | 同样集成小型游戏制作功能，但规格和生态与 PICO-8 不同 |
| [Roblox Studio](https://create.roblox.com/docs/studio) | 为 Roblox 平台制作体验 | 制作工具与平台的运行、发布规则相连；脚本使用 Luau |
| [UEFN](https://dev.epicgames.com/documentation/en-us/fortnite/unreal-editor-for-fortnite) | 为 Fortnite 制作内容 | 面向特定平台的编辑器与工作流，与独立 UE 项目的发布路线不同 |

**引擎、作品风格与发布平台是不同概念。** 像素画面无法单独说明使用了 PICO-8，文字选项也无法单独说明使用了 Ren’Py；视觉形式与制作工具并非一一对应。

<a id="tools-04"></a>
## 04｜框架、图形库与代码型引擎

这一类工具主要通过代码调用，提供图形、输入、声音或游戏结构等能力。项目可以在这些功能之上组织自己的逻辑，不一定依赖完整的可视化编辑器。各工具的功能范围不同，“库”“框架”“引擎”的命名也存在交叉。

| 工具 | 主要职责 | 解释 |
| --- | --- | --- |
| [Three.js](https://threejs.org/) | JavaScript 三维图形库 | 处理场景、相机、模型、灯光等；玩法与其他系统需要项目另行组织 |
| [Babylon.js](https://www.babylonjs.com/) | 网页三维引擎及相关工具 | 与 Three.js 处在相近技术领域，但提供的系统和工作方式不同 |
| [PlayCanvas](https://playcanvas.com/) | 网页三维引擎及在线编辑器工作流 | 包含引擎与制作工具；引擎本身和托管编辑服务需分别认识 |
| [Phaser](https://docs.phaser.io/phaser/getting-started/what-is-phaser) | 二维网页游戏框架 | 提供场景、输入等游戏功能，不负责三维模型制作 |
| [PixiJS](https://pixijs.com/) | 高性能二维绘制与显示 | 重点负责画面显示，完整玩法仍需项目代码组织 |
| [raylib](https://www.raylib.com/) | 图形、输入、音频等开发库 | 通过代码使用基础功能，不以完整的拖拽式编辑器为主要工作方式 |
| [SDL](https://www.libsdl.org/)、[SFML](https://www.sfml-dev.org/) | 跨平台窗口、输入、图形／音频等基础功能 | 提供基础部件，游戏结构通常需要进一步组织 |
| [LÖVE](https://love2d.org/) | 用 Lua 编写二维游戏的框架 | Lua 负责表达规则，LÖVE 提供游戏功能 |
| [Solar2D](https://solar2d.com/) | Lua 路线的二维游戏引擎 | 通过代码使用引擎能力，属于跨平台制作路线 |
| [MonoGame](https://monogame.net/) | .NET 游戏框架 | 以代码组织为主，不能将其视为自带完整场景编辑器的工具 |
| [libGDX](https://libgdx.com/) | Java 路线的跨平台游戏框架 | Java 是编程语言，libGDX 提供开发游戏的功能与结构 |
| [Bevy](https://bevy.org/) | Rust 路线的游戏引擎 | 采用代码驱动的制作方式，编辑工具与工作流需按项目确认 |
| [HaxeFlixel](https://haxeflixel.com/) | Haxe 路线的二维游戏框架 | Haxe 是编程语言，HaxeFlixel 提供二维游戏结构 |
| [React](https://react.dev/)、[Vue](https://vuejs.org/)、[Svelte](https://svelte.dev/) | 网页界面开发 | 可用于菜单、对话界面或工具页面，本身不是专门的游戏引擎 |

例如，在“React + Three.js”的组合中，React 可以负责组织界面，Three.js 负责三维内容。**两者分别承担界面与图形任务，连接方式由项目代码决定，并不是两个完整游戏引擎的重复使用。**

简单的网页互动也可以直接使用 HTML、CSS 和 JavaScript，不额外加入这些库。是否增加依赖，应以所需功能和项目复杂度为依据。[MDN 对网页技术的说明](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/What_is_JavaScript)

<a id="tools-05"></a>
## 05｜编程语言、数据格式与图形技术

编程语言规定代码的写法，引擎或库提供可调用的功能，编辑器则用于编写和修改代码。三者可以配合使用，但职责不同。

| 名字 | 类别 | 解释 |
| --- | --- | --- |
| [JavaScript／JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript) | 编程语言 | 用于网页交互、Phaser、Three.js，以及部分工具和服务器 |
| [TypeScript／TS](https://www.typescriptlang.org/) | 在 JavaScript 基础上增加类型等开发能力的语言 | 可提前检查将文字误作数字等类型问题；通常处理为 JavaScript 后运行 |
| [C#](https://learn.microsoft.com/en-us/dotnet/csharp/) | 编程语言，读作 C sharp | 用于 Unity，以及支持它的 Godot、Stride、MonoGame 项目 |
| [C++](https://isocpp.org/) | 编程语言 | 用于 UE、引擎底层、高性能系统和原生工具 |
| [C](https://www.iso.org/standard/82075.html) | 编程语言 | 用于系统与基础库、raylib 等路线；与 C++ 是不同语言 |
| [GDScript](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html) | Godot 的脚本语言 | 用于编写 Godot 游戏行为；部分写法与 Python 相似，但不是 Python |
| [GML](https://manual.gamemaker.io/monthly/en/GameMaker_Language/GameMaker_Language_Index.htm) | GameMaker Language | 用于编写 GameMaker 项目逻辑 |
| [Lua](https://www.lua.org/about.html) | 便于嵌入其他程序的脚本语言 | 用于 LÖVE、Defold，以及一些游戏或工具的脚本 |
| [Luau](https://luau.org/) | 从 Lua 发展来的语言 | 用于 Roblox 开发；语法和库与 Lua 并非完全相同 |
| [Python](https://www.python.org/about/) | 通用编程语言 | 用于 Ren’Py 扩展、Blender 自动化、资源批量整理、测试和后台工具 |
| [Rust](https://www.rust-lang.org/)、[Haxe](https://haxe.org/) | 不同的通用编程语言 | 分别用于 Bevy、HaxeFlixel 等技术路线 |
| [Java](https://dev.java/)、[Kotlin](https://kotlinlang.org/)、[Swift](https://www.swift.org/) | 通用及平台开发相关语言 | 用于游戏框架、Android／Apple 平台接入和原生应用开发 |
| [Verse](https://dev.epicgames.com/documentation/en-us/fortnite/verse-language-reference) | Epic 的编程语言 | 用于 UEFN 等相关创作环境 |
| [HTML 与 CSS](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/What_is_JavaScript) | 网页结构的标记语言与外观的样式语言 | HTML 定义图片、按钮等内容结构，CSS 规定位置、颜色和排版 |
| [SQL](https://www.postgresql.org/docs/current/tutorial-sql.html) | 操作关系数据库的语言 | 用于查询玩家记录、道具数据等；SQL 是操作数据的语言，数据库软件负责保存与管理数据 |
| [HLSL](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl)、[GLSL](https://www.khronos.org/opengl/wiki/Core_Language_(GLSL))、[WGSL](https://www.w3.org/TR/WGSL/) | 着色器语言 | 用于编写图形处理器执行的程序，例如计算颜色、光照和变形 |

开发资料中还会出现数据格式和底层技术名称：

| 名字 | 解释 |
| --- | --- |
| JSON、CSV、YAML、TOML | 保存数据或配置的不同格式，例如对白表和设置文件；通常不用于编写整套玩法 |
| Markdown／`.md` | 用简单符号表示标题、链接、列表的文档格式；本篇博客的源文件采用此格式 |
| WebGL、WebGPU、OpenGL、Vulkan、Direct3D、Metal | 与图形处理器交互的接口或标准；引擎或图形库可以基于它们工作，它们本身不是完整的游戏编辑器 |
| WebAssembly／Wasm | 可作为编译目标的执行格式，使其他语言编写的程序在支持它的环境中运行；不属于三维引擎，也不限于游戏用途 |

以网页三维为例，**Three.js 提供三维功能，WebGL／WebGPU 是它可能使用的底层图形接口，GLSL／WGSL 是相关着色器的编写语言。** 这分别对应功能库、底层接口与程序语言。具体支持范围取决于工具版本和渲染后端。[Three.js](https://threejs.org/) · [WebGL](https://www.khronos.org/webgl/) · [WebGPU](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API)

<a id="tools-06"></a>
## 06｜代码编辑、编译与依赖管理

这一类工具用于编写、检查、处理和运行代码。代码编辑器提供编写界面，运行环境执行程序，包管理工具安装外部组件，构建工具则按规定生成可交付文件。

| 工具／类别 | 主要用途 | 解释 |
| --- | --- | --- |
| [VS Code](https://code.visualstudio.com/docs) | 代码编辑器 | 编写代码、查找文件和安装扩展；与 Visual Studio 是不同产品 |
| [Visual Studio](https://visualstudio.microsoft.com/)、[Rider](https://www.jetbrains.com/rider/) | 集成开发环境，简称 IDE | 集中提供代码编写、运行和调试等功能 |
| [Xcode](https://developer.apple.com/xcode/)、[Android Studio](https://developer.android.com/studio) | 平台开发工具 | 处理 Apple／Android 应用的开发、构建和调试；其他引擎导出项目时也可能需要使用 |
| 浏览器、[Node.js](https://nodejs.org/en/about)、[.NET](https://dotnet.microsoft.com/learn/dotnet/what-is-dotnet) | 不同的运行环境或开发平台 | 为相应程序提供执行环境；Node.js 使 JavaScript 能在浏览器之外运行 |
| [npm](https://docs.npmjs.com/about-npm/)、[pnpm](https://pnpm.io/)、[Yarn](https://yarnpkg.com/) | JavaScript 生态的包管理工具 | 安装和管理项目依赖；属于同类工具的不同选择 |
| [pip](https://pip.pypa.io/en/stable/)、[NuGet](https://learn.microsoft.com/en-us/nuget/what-is-nuget)、[Cargo](https://doc.rust-lang.org/cargo/) | 其他语言生态的包／项目工具 | 分别用于 Python、.NET、Rust 等技术路线 |
| [Vite](https://vite.dev/guide/)、[webpack](https://webpack.js.org/) | 网页开发与构建工具 | 提供开发预览，并在发布前处理程序和资源 |
| [GCC](https://gcc.gnu.org/)、[Clang](https://clang.llvm.org/)、[MSVC](https://learn.microsoft.com/en-us/cpp/overview/visual-cpp-in-visual-studio) | 编译工具 | 将相应语言的源代码转换为后续可链接、执行的程序形式 |
| [CMake](https://cmake.org/)、[Gradle](https://gradle.org/)、[MSBuild](https://learn.microsoft.com/en-us/visualstudio/msbuild/msbuild) | 软件构建组织 | 安排文件的处理方式、依赖关系和编译顺序 |
| [Emscripten](https://emscripten.org/docs/introducing_emscripten/about_emscripten.html) | 面向网页等目标的编译工具链 | 可将 C／C++ 项目编译到 WebAssembly 等目标；桌面功能仍需检查网页兼容性 |
| 终端、PowerShell、Bash 等命令行工具 | 输入和执行命令 | 通过文字命令操作文件、启动工具和执行开发任务 |

**依赖**指项目使用的外部程序包。**构建／Build**指按规定处理代码与资源，生成可运行或可交付的结果。编辑器中的运行或导出按钮，可能已在内部调用这些工具。

安装范围应与技术路线对应。例如普通 JavaScript 页面并不需要同时安装 C++、C# 等语言的全部开发工具。

<a id="tools-07"></a>
## 07｜二维绘图与像素画

二维绘图软件用于制作角色立绘、背景、图标和界面素材，像素画工具则侧重像素级绘制与逐帧动画。它们产出图像和动画资源；资源的显示时机与交互行为由游戏程序控制。

| 工具 | 主要用途 | 解释 |
| --- | --- | --- |
| [Photoshop／PS](https://www.adobe.com/products/photoshop.html) | 图像编辑、绘画、合成 | 制作或处理背景、贴图、界面素材等，也可用于照片处理 |
| [Clip Studio Paint／CSP](https://www.clipstudio.net/en/) | 插画、漫画和二维动画 | 制作角色立绘、线稿、表情差分等 |
| [Krita](https://krita.org/en/)、[GIMP](https://www.gimp.org/) | 绘画和图像编辑 | 前者侧重数字绘画，后者是综合图像编辑工具，用途存在交叉 |
| [Procreate](https://procreate.com/procreate) | 平板绘画 | 在 iPad 上绘制角色与场景，再导出资源 |
| [Illustrator／AI](https://www.adobe.com/products/illustrator.html)、[Inkscape](https://inkscape.org/) | 矢量绘图 | 用曲线和形状制作标志、图标等；AI 在此是 Illustrator 的简称 |
| [Affinity](https://www.affinity.studio/) | 矢量、像素图像与版面设计 | 当前统一应用整合这些功能；旧教程中的 Designer、Photo、Publisher 是此前分别命名的应用 |
| [Aseprite](https://www.aseprite.org/) | 像素绘图和逐帧动画 | 按像素绘制角色、道具和动作帧 |
| [LibreSprite](https://libresprite.github.io/)、[Piskel](https://www.piskelapp.com/)、[Pixelorama](https://orama-interactive.itch.io/pixelorama) | 像素绘图与动画 | 与 Aseprite 属于同一工作类别的不同工具选择 |

**DCC，数字内容创作工具**，是绘图、建模、动画等软件的总称，不是一个单独的软件名称。

**位图**由像素组成，**矢量图**记录曲线和形状，因此两者的放大、编辑和导出方式不同。这里区分的是图像组织方式，不是画面品质的等级。

**差分**指同一角色的不同图像版本，例如闭眼、微笑或换装。**逐帧动画**通过连续播放一组画面表现动作。因此，绘图软件负责制作表情和动作资源，游戏程序负责根据对白或状态切换这些资源。

<a id="tools-08"></a>
## 08｜三维建模与雕刻

三维建模用于建立物体的立体形状，数字雕刻通过推拉模型表面塑造形体和细节。模型完成后，还需根据用途处理材质、动作、灯光及导出规格。

| 工具 | 主要用途 | 解释 |
| --- | --- | --- |
| [Blender](https://www.blender.org/) | 建模、雕刻、动画、渲染等综合三维制作 | 可覆盖多种资源制作任务，不限于模型形状 |
| [Maya](https://www.autodesk.com/products/maya/overview) | 三维建模、绑定、动画和特效制作 | 制作角色和动作，也可通过脚本接入团队流程 |
| [3ds Max](https://www.autodesk.com/products/3ds-max/overview) | 三维建模、动画和渲染 | 提供综合三维资源制作功能 |
| [Cinema 4D](https://www.maxon.net/en/cinema-4d) | 三维设计、动画和动态图形 | 用于资源、视觉演示与宣传内容，不负责完整游戏运行 |
| [ZBrush](https://www.maxon.net/en/zbrush)、[Nomad Sculpt](https://nomadsculpt.com/) | 数字雕刻 | 制作皮肤、褶皱等形体细节；高细节模型通常还需按运行要求整理 |
| [3DCoat](https://3dcoat.com/) | 雕刻、拓扑、贴图等 | 处理形体及其后续资源整理工作 |
| [Blockbench](https://blockbench.net/) | 低多边形和方块风格建模、贴图、动画 | 制作由较简单形体构成的角色与物件 |
| [MagicaVoxel](https://ephtracy.github.io/) | 体素建模 | 按三维空间中的格子组织形体，形成具有体积的模型 |

**网格／Mesh**是由点、边、面组成的模型结构；**拓扑**描述这些点和面如何连接；**重拓扑**是重新整理连接结构，例如使雕刻模型更适合动画变形或实时运行。

**制作时使用三维软件，不代表运行时必须采用实时三维。** 例如在 Blender 中建立场景并导出图片后，游戏可以只显示二维图像。《体温调节》讨论过的方案即属于这种分工：Blender 负责源场景，游戏端负责图片显示与交互。

<a id="tools-09"></a>
## 09｜贴图、材质、UV 与烘焙

**贴图**是提供颜色、粗糙程度等表面信息的图像；**材质**规定表面的表现方式；**UV**建立模型表面与二维图片之间的位置对应关系，可理解为将表面展开后安排到图片中；**烘焙**则将部分计算结果提前保存，供后续使用。

| 工具 | 主要用途 | 解释 |
| --- | --- | --- |
| [Substance 3D Painter](https://www.adobe.com/products/substance3d/apps/painter.html) | 三维模型贴图绘制与制作 | 在模型上制作颜色、磨损等表面效果，再导出项目所需贴图 |
| [Substance 3D Designer](https://www.adobe.com/products/substance3d/apps/designer.html) | 节点与参数驱动的材质制作 | 通过规则生成可调整的表面，不必逐笔绘制全部细节 |
| [Substance 3D Sampler](https://www.adobe.com/products/substance3d/apps/sampler.html) | 从图像等输入制作材质 | 将输入素材处理为可用于三维表面的资源 |
| [ArmorPaint](https://armorpaint.org/)、[Mari](https://www.foundry.com/products/mari) | 三维贴图绘制 | 与 Painter 同属模型表面制作方向，流程和侧重点不同 |
| [Material Maker](https://www.materialmaker.org/) | 节点式材质生成 | 组合图像处理与生成规则，形成材质资源 |
| [RizomUV](https://www.rizomuv.com/) | UV 展开与排布 | 将模型表面展开，并安排到二维图片空间中 |
| [Marmoset Toolbag](https://marmoset.co/) | 模型展示、渲染、烘焙与材质相关工作 | 检查模型效果，并输出部分表面细节计算结果 |

**节点**是代表某项操作或数据的图形单元，连线表示数据或执行顺序的流向。材质节点、动画节点和蓝图都可能采用连线界面，但分别处理表面、动作和程序行为等不同对象。

例如，将高细节模型的部分表面信息烘焙到低面数模型的贴图中，可以在较简单的模型上表现细节。**模型负责几何形状，贴图参与表面表现；烘焙并没有把全部几何细节复制到低面数模型上。**

<a id="tools-10"></a>
## 10｜场景、地形与关卡

场景制作侧重环境内容，关卡设计还涉及路线、障碍、触发点和节奏。例如森林场景需要树木与地形，森林关卡则需要进一步安排玩家路线及沿途事件。

| 工具 | 主要用途 | 解释 |
| --- | --- | --- |
| 引擎自带场景／关卡编辑器 | 物体、灯光、触发器和玩法对象的布置 | 制作可与项目规则连接的场景内容 |
| [Houdini](https://www.sidefx.com/products/houdini/) | 程序化三维制作 | 用规则生成或处理建筑、地形等资源；程序化制作与生成式 AI 是不同概念 |
| [Gaea](https://quadspinner.com/)、[World Machine](https://www.world-machine.com/)、[World Creator](https://www.world-creator.com/en/index.phtml) | 地形制作 | 生成山脉形状、地形高度图及相关表面信息 |
| [SpeedTree](https://unity.com/products/speedtree) | 树木与植被制作 | 制作树木模型及相关资源，不负责整套游戏世界的运行 |
| [Tiled](https://www.mapeditor.org/) | 二维瓦片与对象地图编辑 | 制作图块布置、对象位置等数据，再由游戏程序读取 |
| [LDtk](https://ldtk.io/) | 二维关卡编辑 | 制作地图、实体和字段等数据，通过相应方式接入游戏 |
| [TrenchBroom](https://trenchbroom.github.io/) | 面向 Quake 系等工作流的关卡编辑 | 制作特定格式的三维关卡，与通用模型雕刻工具不同 |

**瓦片／Tile**是可以反复拼接的图块；**高度图**通过图片中的数值记录地面高低；**触发器**用于在进入指定区域或满足条件时启动相应行为。

以 Tiled 为例，编辑器可以记录地图图块和对象位置，游戏仍需读取这些数据并实现显示、碰撞等行为。**地图编辑器负责生成地图数据，游戏程序负责解释数据并执行规则。**

<a id="tools-11"></a>
## 11｜角色、绑定、动画与动作捕捉

**绑定／Rigging**为角色建立控制结构；**骨骼动画**通过控制骨架带动形体；**动作捕捉／Mocap**记录真实动作，再将数据用于数字角色。角色形状的制作、控制结构的建立与动作编排是相连但不同的环节。

| 工具 | 主要用途 | 解释 |
| --- | --- | --- |
| [Live2D Cubism](https://www.live2d.com/en/cubism/about/) | 二维角色的变形与控制 | 使绘图产生转头、眨眼等表现，并非将原图自动转换为三维模型 |
| [Spine](https://esotericsoftware.com/) | 二维骨骼动画 | 用骨架控制头部、手臂等图片部件并制作动画 |
| [Rive](https://rive.app/) | 可交互动画与界面 | 根据状态和输入切换表现，而不限于播放固定动画 |
| [Moho](https://moho.lostmarble.com/)、[Toon Boom Harmony](https://www.toonboom.com/products/harmony)、[OpenToonz](https://opentoonz.github.io/e/) | 二维动画制作 | 制作逐帧或绑定类动画，输出与导入方式需按游戏路线安排 |
| Blender、Maya、[Cascadeur](https://cascadeur.com/) | 三维角色动作制作 | 设置关键姿势、调整动作和身体运动；Cascadeur 侧重角色动画辅助 |
| [Character Creator](https://www.reallusion.com/character-creator/)、[VRoid Studio](https://vroid.com/en/studio)、[MetaHuman](https://www.metahuman.com/) | 数字角色制作 | 提供不同风格和流程的角色工具；导出、授权与运行成本需按产品确认 |
| [iClone](https://www.reallusion.com/iclone/) | 实时角色动画与场景演出 | 安排人物表演、动作和镜头，再按项目路线输出 |
| [Marvelous Designer](https://www.marvelousdesigner.com/) | 三维服装设计与布料模拟 | 制作衣服及褶皱；游戏中的实时显示与运动由后续系统处理 |
| [Mixamo](https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html) | 人形角色自动绑定和动作资源 | 主要针对双足人形，不适用于任意动物的自动绑定 |
| [Rokoko Studio](https://www.rokoko.com/products/studio)、[Vicon Shogun](https://www.vicon.com/software/shogun/)、[OptiTrack Motive](https://www.optitrack.com/software/motive) | 动作数据的捕捉、处理与输出 | 常与特定设备和拍摄流程配合；软件与硬件系统需分别考虑 |

**关键帧**记录指定时间点的状态或姿势，软件可以计算部分中间变化。**重定向／Retargeting**将一套动作映射到另一套骨架；骨架比例和命名不同，可能需要调整。

以 Live2D 为例，Cubism Editor 用于制作角色和动画，Cubism SDK 等组件用于将其接入游戏。**编辑器负责生成内容，SDK 提供接入与运行所需的程序组件；完成导出不等于完成游戏集成。** 制作软件与运行组件的许可也需分别核对。[Live2D 官方说明](https://www.live2d.com/en/cubism/about/)

<a id="tools-12"></a>
## 12｜扫描、渲染与特效

**渲染**根据形状、材质、灯光和相机计算画面。**实时渲染**在运行过程中持续生成画面，以响应玩家操作；**离线渲染**提前计算并输出图像或视频，供后续播放和使用。扫描与三维重建用于获取资源，特效工具则用于制作烟雾、火花等视觉表现。

| 工具／模块 | 主要用途 | 解释 |
| --- | --- | --- |
| [RealityScan](https://www.realityscan.com/uses) | 从照片等输入重建三维资源 | 桌面产品旧称 RealityCapture；RealityScan Mobile 是需另外区分的手机产品 |
| [Agisoft Metashape](https://www.agisoft.com/)、[Meshroom／AliceVision](https://alicevision.org/) | 摄影测量与三维重建 | 根据多个角度的照片计算物体形状；成品通常仍需清理、减面和贴图处理 |
| [Cycles](https://docs.blender.org/manual/en/latest/render/cycles/index.html)、[Eevee](https://docs.blender.org/manual/en/latest/render/eevee/index.html) | Blender 的不同渲染系统 | 负责画面计算，而非完整游戏的规则与运行 |
| [Arnold](https://www.autodesk.com/products/arnold/overview)、[V-Ray](https://www.chaos.com/vray)、[Redshift](https://www.maxon.net/en/redshift) | 三维渲染工具 | 用于资源效果、预渲染画面和宣传内容，不一定作为游戏运行时的一部分 |
| [Niagara](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine)、[Unity Visual Effect Graph](https://unity.com/features/visual-effect-graph) | 引擎中的视觉特效制作 | 分别属于对应引擎的工具体系，用于火花、烟雾、能量等动态表现 |
| [Effekseer](https://effekseer.github.io/en/)、[PopcornFX](https://www.popcornfx.com/) | 特效制作及运行集成 | 在专门工具中制作效果，再通过对应运行组件接入项目 |

**粒子系统**管理一组元素的生成、运动与消失，例如火星、雨点和烟尘。粒子可以采用不同的显示形式，视觉特效也不全部由粒子系统实现。

<a id="tools-13"></a>
## 13｜录音、作曲、音效与交互音频

**DAW，数字音频工作站**，用于录音、编曲、剪辑和混音，可在不同轨道中组织对白、乐器与音效。**音频中间件**负责游戏运行时的声音控制，例如根据场景、距离和状态调整播放内容。

| 工具 | 主要用途 | 解释 |
| --- | --- | --- |
| [Audacity](https://www.audacityteam.org/)、[Adobe Audition](https://www.adobe.com/products/audition.html) | 录音、剪辑、修复和音频处理 | 处理对白、剪除多余片段和整理音效 |
| [REAPER](https://www.reaper.fm/)、[Pro Tools](https://www.avid.com/pro-tools)、[Cubase](https://www.steinberg.net/cubase/)、[Nuendo](https://www.steinberg.net/nuendo/) | 综合音频制作 | 提供多轨录音、音乐与声音设计功能，工作流程各有侧重 |
| [Logic Pro](https://www.apple.com/logic-pro/)、[Ableton Live](https://www.ableton.com/en/live/)、[FL Studio](https://www.image-line.com/fl-studio) | 编曲、音乐制作与音频处理 | 编写背景音乐，组织乐器、节奏和音频素材 |
| [Ardour](https://ardour.org/) | 多轨音频工作站 | 提供录音、编辑与混音等功能 |
| [ChipTone](https://sfbgames.itch.io/chiptone)、[FamiStudio](https://famistudio.org/) | 复古音效与芯片音乐制作 | 前者偏向短音效生成，后者偏向特定复古音源风格的音乐 |
| [Soundly](https://getsoundly.com/) | 音效检索、管理和相关制作工作 | 从声音资源中检索和组织项目所需素材 |
| [FMOD Studio](https://www.fmod.com/studio)、[Wwise](https://www.audiokinetic.com/en/) | 交互音频制作与中间件 | 根据游戏场景、距离和状态等控制声音及其变化 |

例如，用 REAPER 制作三层背景音乐，在 FMOD 或 Wwise 中设定各层的加入条件，再由游戏程序传入战斗紧张度。**音频工作站负责制作声音，音频中间件负责安排动态播放规则，游戏程序负责提供触发这些规则的状态。**

只有背景音乐和少量点击音效的作品，可能仅需引擎自带的音频功能。专门中间件应根据交互音频的复杂度选用。

<a id="tools-14"></a>
## 14｜对白与分支叙事

交互叙事工具管理文字、选择、条件和状态之间的关系。例如，某句对白是否出现，可以取决于玩家之前的选择，而不只是文本在文档中的排列顺序。

| 工具 | 主要用途 | 解释 |
| --- | --- | --- |
| [Twine](https://twinery.org/) | 可选择的文本结构 | 连接故事段落，制作网页互动故事或检查分支关系 |
| [ink／Inky](https://www.inklestudios.com/ink/) | 叙事语言与配套编辑器 | ink 用于编写文本、选择和逻辑；Inky 用于编辑与测试相应内容 |
| [Yarn Spinner](https://www.yarnspinner.dev/) | 对话编写与运行集成 | 管理对白、选择和程序调用，其他画面与交互仍由游戏系统处理 |
| [articy:draft](https://www.articy.com/en/) | 可视化叙事、流程与内容数据设计 | 组织角色、分支和条件，再导出或接入项目 |

Ren’Py 与 ink 提供的范围不同。**Ren’Py 提供视觉小说的制作与运行系统，ink 主要提供叙事语言及相关工具。** 前者可以承担作品的主体框架，后者通常用于组织其中的叙事内容。

“脚本”在此也需区分：剧情脚本指故事与对白文本，程序脚本指控制行为的代码。使用完整名称有助于明确交付内容。

<a id="tools-15"></a>
## 15｜界面、字体与本地化

**UI**指用户界面，**UX**关注使用体验，**本地化**使内容适合目标语言与地区。这一环节涉及按钮布局、文字可读性、翻译内容及其在实际界面中的显示。

| 工具／模块 | 主要用途 | 解释 |
| --- | --- | --- |
| [Figma](https://www.figma.com/)、[Penpot](https://penpot.app/) | 界面设计与交互原型 | 设计菜单、对话框和页面流转；原型仍需通过开发转为实际游戏界面 |
| 引擎自带 UI 系统，例如 [Unity UI Toolkit](https://docs.unity3d.com/Manual/UIElements.html)、[Unreal UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/umg-ui-designer-for-unreal-engine) | 游戏运行界面的制作 | 将视觉设计实现为可响应玩家操作的控件 |
| [FontForge](https://fontforge.org/en-US/)、[Glyphs](https://glyphsapp.com/)、[FontLab](https://www.fontlab.com/) | 字体制作与编辑 | 设计字形、字距等；字体文件的使用许可需单独确认 |
| [Crowdin](https://crowdin.com/)、[Weblate](https://weblate.org/en/) | 多语言翻译流程管理 | 组织同一文本的不同语言版本、翻译进度和上下文 |
| [Poedit](https://poedit.com/)、[OmegaT](https://www.omegat.org/) | 翻译文件编辑与辅助翻译 | 利用术语和历史译文等辅助翻译工作 |

**设计工具负责界面方案，游戏 UI 系统负责实际操作，本地化工具负责多语言内容的组织。** 最终仍需在游戏中检查换行、字体缺字、日期与数字格式，以及译文长度变化后的布局。

<a id="tools-16"></a>
## 16｜版本管理

版本管理记录文件的变动及历史，使修改可以追踪、比较和恢复。它既可以管理代码，也可以结合相应工具管理模型、音频等资源。

| 工具／平台 | 主要用途 | 解释 |
| --- | --- | --- |
| [Git](https://git-scm.com/about) | 版本控制 | 在项目中记录文件和修改历史，本身不是网站 |
| [Git LFS](https://git-lfs.com/) | Git 的大文件扩展 | 使模型、音频等大资源采用专门的存储方式；容量和服务条件需另行确认 |
| [GitHub](https://github.com/features)、[GitLab](https://about.gitlab.com/platform/)、[Bitbucket](https://bitbucket.org/product) | 仓库托管、协作与审查 | 围绕版本管理提供在线协作功能，与 Git 本身不同 |
| [GitHub Desktop](https://desktop.github.com/)、[Sourcetree](https://www.sourcetreeapp.com/) | Git 图形客户端 | 通过图形界面操作版本历史，减少直接输入命令的需要 |
| [Perforce P4](https://www.perforce.com/products/p4) | 源码与数字资源版本管理 | 管理代码、二进制资源和权限；旧资料常见 Helix Core 名称 |
| [Unity Version Control](https://docs.unity.com/en-us/unity-version-control) | 面向代码与内容的版本管理 | 旧资料常见 Plastic SCM 名称；与引擎运行时是不同产品职责 |
| [Subversion／SVN](https://subversion.apache.org/) | 集中式版本管理 | 在旧项目或既有团队流程中可能遇到的另一套系统 |

**仓库／Repository**保存项目文件及版本历史；**提交／Commit**记录一组修改；**分支／Branch**承载相对独立的修改路线；**合并／Merge**将变动整合到一起。

代码文本通常可以逐行比较，模型、音频等文件则不一定适合自动合并。**文件锁定**用于约定某份资源当前由谁编辑，以减少多人同时修改产生的冲突。是否采用锁定，取决于文件格式和协作工具。

因此，Git 负责版本记录，GitHub 等平台负责仓库托管与在线协作，图形客户端提供操作这些记录的界面。**版本管理不等于完整备份方案**，原始素材、大文件存储和重要凭据仍需分别确认备份方式。

<a id="tools-17"></a>
## 17｜任务、审片与制作追踪

这一类工具记录任务分工、制作进度、资源版本和审阅结果。例如模型师交付角色后，动画师需要确认接收的版本，负责人需要记录修改意见与批准状态。

| 工具 | 主要用途 | 解释 |
| --- | --- | --- |
| [Jira](https://www.atlassian.com/software/jira)、[Trello](https://trello.com/)、[GitHub Projects](https://github.com/features) | 任务、问题和进度管理 | 将工作拆分为条目，记录负责人、优先级和状态 |
| [Codecks](https://www.codecks.io/) | 面向游戏团队的项目管理 | 通过卡片等方式组织开发任务与反馈 |
| [Flow Production Tracking](https://www.autodesk.com/products/flow-production-tracking/overview) | 资源、镜头、任务和审阅管理 | 旧称 ShotGrid，更早也见 Shotgun；负责制作追踪而非模型制作 |
| [ftrack](https://www.ftrack.com/en/)、[Kitsu](https://www.cg-wire.com/kitsu/) | 创意制作的追踪与审阅 | 关联制作进度、资源版本和反馈 |
| [AYON](https://docs.ayon.dev/) | 跨制作软件的管线组织与集成 | 协调资源在不同工具之间的处理和交付 |
| [Slack](https://slack.com/)、[Microsoft Teams](https://www.microsoft.com/microsoft-teams/group-chat-software)、[Discord](https://discord.com/) | 沟通、会议和协作频道 | 承担讨论和联络；关键决定仍需记录到任务或文档中 |

个人项目可以用一个简单看板合并管理这些事务；大型项目可能将资源审阅、任务管理和工具集成分开。软件数量应由分工和交接需求决定。

<a id="tools-18"></a>
## 18｜调试、测试与性能分析

**调试**用于定位错误原因，**测试**用于检查结果是否符合要求，**性能分析／Profiling**用于测量执行时间、内存等开销。程序能够启动、通过功能检查和达到性能目标，是不同的验证结果。

| 工具／类别 | 主要用途 | 解释 |
| --- | --- | --- |
| [浏览器开发者工具／DevTools](https://developer.chrome.com/docs/devtools) | 报错、网络请求、页面与性能检查 | 查看网页游戏的资源加载、交互执行及运行情况 |
| [Unity Profiler](https://docs.unity3d.com/Manual/Profiler.html)、[Unreal Insights](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine) | 引擎性能分析 | 测量程序各部分的时间和内存开销，为优化提供依据 |
| [RenderDoc](https://github.com/baldurk/renderdoc)、[PIX](https://devblogs.microsoft.com/pix/)、[Nsight Graphics](https://developer.nvidia.com/nsight-graphics) | 图形调试和分析 | 检查一帧画面的绘制过程；支持的系统、接口和硬件各有不同 |
| Xcode／Android Studio 中的性能与调试工具 | 移动平台分析 | 检查手机端的程序和内存等情况，补充电脑预览无法覆盖的验证 |
| [Jest](https://jestjs.io/)、[Vitest](https://vitest.dev/)、[pytest](https://docs.pytest.org/)、[NUnit](https://nunit.org/) | 自动化代码测试 | 自动检查已定义规则的结果，分别对应不同技术生态 |
| [Playwright](https://playwright.dev/)、[Appium](https://appium.io/) | 操作自动化测试 | 前者主要控制浏览器，后者用于应用自动化等场景 |
| [BrowserStack](https://www.browserstack.com/) | 浏览器和设备测试服务 | 提供不同测试环境；设备覆盖与服务范围取决于所选方案 |
| [NVDA](https://www.nvaccess.org/about-nvda/)、[VoiceOver](https://www.apple.com/accessibility/vision/)、[TalkBack](https://support.google.com/accessibility/android/answer/6283677) | 屏幕阅读器 | 辅助检查界面的读屏支持，但不能替代完整的无障碍检查 |

**日志／Log**记录程序执行过程中的信息；**断点／Breakpoint**使程序在指定位置暂停，以便查看当时的状态。两者用于调查原因，隐藏报错文字并不能消除错误本身。

自动化测试重复执行已定义的检查，试玩则用于观察理解、节奏和操作体验。**前者提供特定检查的结果，后者提供实际体验的反馈；两者不能互相替代。**

<a id="tools-19"></a>
## 19｜物理、寻路与其他中间件

物理引擎处理运动、碰撞等模拟，寻路系统计算对象可行走的路线。这些专门能力可以作为项目的一部分接入，无需每次都从底层重新实现。

| 工具／技术 | 主要用途 | 解释 |
| --- | --- | --- |
| [Box2D](https://box2d.org/) | 二维刚体物理 | 处理二维物体的运动与碰撞，不包含完整游戏编辑功能 |
| [Jolt Physics](https://jrouwe.github.io/JoltPhysics/)、[Bullet](https://pybullet.org/wordpress/) | 三维物理等模拟 | 提供模拟能力，剧情、界面等由其他系统承担 |
| [PhysX](https://developer.nvidia.com/physx-sdk) | 物理模拟 SDK | 将物理功能接入项目，与画面渲染工具职责不同 |
| [Rapier](https://rapier.rs/) | 二维／三维物理 | 可作为其他程序的一部分接入，不替代整套游戏结构 |
| [Havok](https://www.havok.com/) | 物理、导航、布料等中间件产品 | 按项目需求接入相应的专门功能 |
| [Recast／Detour](https://recastnav.com/) | 导航网格生成与寻路 | 计算可行走区域和路线，不承担全部角色决策 |
| [Bink、Oodle](https://www.radgametools.com/) | 视频播放、数据压缩等中间件 | 分别解决游戏中的特定播放与资源处理任务 |

引擎可能已集成其中某种技术，也可能采用其他实现。**通用游戏引擎负责组织整体运行，物理或寻路中间件负责其中的专门功能。** 同时使用两者，不代表使用了两个完整游戏引擎。

游戏开发中的“AI”也可能指角色决策、行为树或寻路；这些用法需与聊天模型和生成式 AI 区分。

<a id="tools-20"></a>
## 20｜联机、服务器与数据库

**客户端**是玩家设备上运行的部分，**服务器**是提供远端功能的程序或机器，**数据库**负责有组织地保存与查询数据。例如客户端显示画面并接收操作，远端服务器协调房间与判定结果，数据库保存账号等记录。

| 工具／服务 | 主要用途 | 解释 |
| --- | --- | --- |
| [Photon Fusion／Quantum](https://www.photonengine.com/fusion) | 多人游戏的网络与同步技术 | 协调不同设备的游戏状态；不同产品采用的同步方式不同 |
| [Mirror](https://mirror-networking.com/)、[FishNet](https://fish-networking.gitbook.io/docs) | Unity 多人网络框架 | 为项目增加网络层，账号与运营等功能需另行安排 |
| [Colyseus](https://colyseus.io/) | 多人游戏服务器框架 | 组织房间和状态同步等，与客户端配合运行 |
| [Nakama](https://heroiclabs.com/nakama/) | 游戏后台与多人社交功能 | 提供账号、社交、排行榜和多人等相关能力 |
| [PlayFab](https://learn.microsoft.com/en-us/xbox/playfab/get-started/what-is-playfab)、[Unity Gaming Services](https://unity.com/solutions/gaming-services) | 游戏在线服务 | 按需选用账号、数据、联机和运营等服务 |
| [Epic Online Services／EOS](https://onlineservices.epicgames.com/)、[Steamworks](https://partner.steamgames.com/doc/home) | 平台与在线功能的接口、工具或服务 | 涉及好友、成就、联机等；EOS 与 UE、Steamworks 与 Steam 商店客户端分别属于不同职责 |
| [Firebase](https://firebase.google.com/products-build)、[Supabase](https://supabase.com/) | 通用应用后台服务 | 提供认证、存储、数据库等能力，本身不是完整游戏引擎 |
| [SQLite](https://www.sqlite.org/about.html) | 可嵌入程序的数据库 | 可用于本地数据存储，不要求另设远程服务器 |
| [PostgreSQL](https://www.postgresql.org/about/)、[Redis](https://redis.io/) | 数据库／数据存储系统 | 前者是关系数据库，后者常用于快速数据访问等任务，需按数据与访问需求选择 |
| [Docker](https://www.docker.com/resources/what-container/) | 容器化运行环境 | 将程序及所需环境按规则打包，减少不同机器间的环境差异 |
| [Kubernetes](https://kubernetes.io/docs/concepts/overview/) | 容器化应用管理 | 协调多个程序实例的运行，主要用于相应的服务部署需求 |
| [Amazon GameLift Servers](https://aws.amazon.com/gamelift/servers/)、[Agones](https://agones.dev/) | 游戏服务器托管或编排 | 前者提供托管服务，后者帮助在 Kubernetes 上管理专用游戏服务器 |

纯单机网页游戏可以由浏览器执行规则，并将进度保存在本地。**网页托管服务负责分发文件，应用服务器负责账号或对战等远端功能；使用网页托管不代表必须增加账号后台。**

网络同步通常交换输入、位置或状态等数据，而非互传屏幕视频。状态由谁计算、结果由谁判定，仍需按玩法设计。

<a id="tools-21"></a>
## 21｜自动构建、打包与发布

**构建**处理代码与资源，**打包**整理可交付文件，**部署**将成品放入目标运行环境，**发布**向目标玩家提供版本。开发环境中可以运行的项目，还需经过相应处理和检查，才能交付给玩家。

| 工具／平台 | 主要用途 | 解释 |
| --- | --- | --- |
| 引擎自带导出工具，以及 Xcode、Android Studio 等 | 目标平台程序生成 | 生成网页文件、桌面程序或移动平台工程／应用等 |
| [GitHub Actions](https://github.com/features/actions)、[GitLab CI/CD](https://docs.gitlab.com/ci/)、[Jenkins](https://www.jenkins.io/)、[TeamCity](https://www.jetbrains.com/teamcity/) | 自动构建、测试和发布 | 根据配置执行检查并生成版本，这类流程常称 CI/CD |
| [Electron](https://www.electronjs.org/)、[Tauri](https://tauri.app/) | 使用网页界面等技术制作应用 | 可用于将网页项目组织为桌面应用，需处理相应运行环境和平台集成 |
| [Capacitor](https://capacitorjs.com/) | 网页技术与移动应用平台的桥接 | 在原生应用环境中使用网页内容，并接入设备能力 |
| [Steamworks](https://partner.steamgames.com/doc/home) | Steam 开发者工具、构建分发与平台接入 | 管理上架、测试版本及相关平台功能 |
| [itch.io](https://itch.io/docs/creators/) | 网页或可下载作品发布 | 提供作品页面和文件管理，也可结合 butler 上传工具 |
| [App Store Connect](https://developer.apple.com/app-store-connect/)、[TestFlight](https://developer.apple.com/testflight/) | Apple 平台发布管理与测试分发 | TestFlight 主要承担测试分发，正式上架需经过相应发布流程 |
| [Google Play Console](https://play.google.com/console/about/) | Android 商店发布与管理 | 管理应用、测试轨道和发布等事务 |
| [微信开发者工具](https://developers.weixin.qq.com/minigame/dev/devtools/download.html)、[抖音开发者工具](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/developer-instrument/development-assistant) | 对应平台的小游戏开发与调试 | 检查平台容器、接口和发布要求，普通网页可能需要适配 |
| [GitHub Pages](https://pages.github.com/)、[Cloudflare Pages](https://developers.cloudflare.com/pages/)、[Netlify](https://www.netlify.com/)、[Vercel](https://vercel.com/) | 网站托管与部署 | 承载相应网页项目；后端能力和限制需按服务分别确认 |

**导出工具负责生成平台文件，平台发布流程负责接收和审核相应版本。** 支持导出并不保证满足全部发布条件，还需核对开发者资格、SDK、性能、输入、签名和审核要求；主机开发条件尤其需要单独确认。

CI/CD 将固定检查与交付步骤自动执行。是否自动发布到正式环境，由流程配置决定，而非使用自动化工具后的必然结果。

<a id="tools-22"></a>
## 22｜运行监控、数据分析与玩家反馈

运行监控记录错误和服务状况，数据分析观察已定义的使用行为，社区与客服渠道接收玩家反馈。这些信息为发布后的调查和维护提供依据。

| 工具／服务 | 主要用途 | 解释 |
| --- | --- | --- |
| [Sentry](https://sentry.io/) | 错误、崩溃与性能观测 | 收集相应问题信息，辅助开发者定位原因 |
| [GameAnalytics](https://www.gameanalytics.com/) | 游戏行为与运营数据分析 | 统计定义好的事件，观察玩家流程与变化 |
| [Firebase Crashlytics](https://firebase.google.com/products/crashlytics) | 应用崩溃报告 | 聚合崩溃记录，定位受影响版本与问题 |
| [Prometheus](https://prometheus.io/)、[Grafana](https://grafana.com/grafana/) | 指标采集与可视化 | 观察服务器负载、错误率等运行指标 |
| [Discord](https://discord.com/)、[Discourse](https://www.discourse.org/)、[Zendesk](https://www.zendesk.com/) | 社区交流、论坛或客服工单 | 分别承担不同形式的沟通与反馈处理 |

数据收集应对应明确的调查目的，避免上传不必要的个人信息。每项服务都需要考虑隐私、费用和维护责任。小型作品也可以主要通过主动反馈与试玩记录改进，不必接入完整的数据分析系统。

<a id="tools-23"></a>
## 23｜录屏、剪辑与宣传

这一类工具用于制作演示视频、预告片、商店图和宣传内容。录屏获取实际运行画面，剪辑安排片段顺序与时长，合成和排版工具则处理视觉效果及文字呈现。

| 工具 | 主要用途 | 解释 |
| --- | --- | --- |
| [OBS Studio](https://obsproject.com/) | 录屏、直播和画面组合 | 录制实机操作、窗口和声音，主要负责画面采集与输出 |
| [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve) | 剪辑、调色、合成、音频后期 | 将实机片段组织成视频，并进行相应后期制作 |
| [Adobe Premiere](https://www.adobe.com/products/premiere.html)、[Final Cut Pro](https://www.apple.com/final-cut-pro/)、[Kdenlive](https://kdenlive.org/) | 视频剪辑 | 选择镜头、调整时长、加入字幕和音轨 |
| [After Effects／AE](https://www.adobe.com/products/aftereffects.html)、[Fusion](https://www.blackmagicdesign.com/products/fusion) | 动态图形与合成 | 制作标题动画和叠加效果，与游戏内实时特效系统不同 |
| [FFmpeg](https://ffmpeg.org/)、[HandBrake](https://handbrake.fr/) | 音视频转换与压缩等处理 | FFmpeg 可按命令批量处理，HandBrake 提供视频转码工作流 |
| [Canva](https://www.canva.com/)及二维设计软件 | 海报、商店图与社交媒体内容 | 将画面和文字排版为宣传材料 |

**预渲染宣传片与实机画面需分别标明。** 两者可以使用同一套模型，但制作方式、运行成本和可操作性不同。

<a id="tools-24"></a>
## 24｜素材平台与资源加工

素材平台提供模型、图片、音效和插件等内容，资源加工工具则将所选内容处理为项目需要的格式与规格。资源选择还需考虑风格、许可、兼容性和运行效果。

| 平台／工具 | 主要用途 | 解释 |
| --- | --- | --- |
| [Fab](https://www.fab.com/)、[Unity Asset Store](https://assetstore.unity.com/) | 模型、材质、工具包等资源市场 | 同一市场可能同时提供素材与插件，许可和兼容性需逐项确认 |
| [itch.io Game Assets](https://itch.io/game-assets)、[Kenney](https://kenney.nl/assets) | 二维、三维、界面等游戏资源 | 按资源说明和许可选用，下载权限不等于任意使用权限 |
| [Poly Haven](https://polyhaven.com/) | 模型、纹理、环境照明图等 | 根据用途选择资源类型与分辨率，不必使用最大文件 |
| [Freesound](https://freesound.org/help/faq/) | 声音资源分享 | 不同声音可能使用不同许可，需分别记录来源与使用条件 |
| [TexturePacker](https://www.codeandweb.com/texturepacker) | 精灵图集打包 | 将多张小图排列进大图，并输出位置数据供程序读取 |
| [ImageMagick](https://imagemagick.org/) | 图片批量处理 | 批量执行缩放、格式转换等操作 |

**图集／Atlas**将多张小图组织到一张或一组图像中，程序通过附带的位置数据读取所需部分。它是一种资源组织方式，是否有益需结合实际绘制和加载方式判断。

`.blend`、`.psd` 等通常用于源工程，`.png`、`.webp`、`.glb`、`.gltf`、`.fbx`、`.wav`、`.ogg` 等可用于资源交换或运行。**文件格式规定内容的存储方式，软件负责读写与处理这些内容；扩展名本身不保证兼容。** 例如 glTF 定义三维资源交付格式，实际支持范围仍取决于导出器、导入器和扩展。[glTF 官方说明](https://www.khronos.org/gltf/)

<a id="tools-25"></a>
## 25｜AI 辅助

AI 工具可以参与设计、编程和资源制作，但并不是一种统一的游戏引擎。使用 AI 描述的是制作方法，成品依靠的语言、引擎与运行环境仍需单独说明。

| 工具／类别 | 主要用途 | 解释 |
| --- | --- | --- |
| [ChatGPT](https://openai.com/chatgpt/overview/) | 设计讨论、技术解释、资料整理与辅助编程 | 生成的说明或代码仍需结合项目核查与验证 |
| [Codex](https://openai.com/codex/)、[GitHub Copilot](https://github.com/features/copilot) | 代码阅读、编写和修改 | 实际可读取、运行或提交的内容取决于接入环境与权限 |
| [Cursor](https://cursor.com/) | 带 AI 能力的代码开发环境 | 提供开发辅助，不属于玩家端运行的游戏引擎 |
| [Adobe Firefly](https://www.adobe.com/products/firefly.html)等视觉生成工具 | 概念图、视觉草稿及相关素材制作 | 需要检查风格一致性、可编辑性、授权和运行资源要求 |
| [ComfyUI](https://comfy.org/) | 视觉生成模型与节点工作流的组织 | 连接模型和处理步骤；软件、模型与输出的许可需分别确认 |

AI 任务可以按交付物划分，例如将对白整理为 JSON、为按钮增加重复点击保护、将图片导出为统一尺寸。明确文件、修改范围与预期结果，有助于检查完成情况。

**AI 工具负责辅助生成或修改内容，项目验收负责确认内容是否符合要求。** 程序运行、图片边缘、存档恢复和授权条件等，仍需通过相应检查验证。

<a id="licensing"></a>
## 授权类型：免费、开源与付费

用途说明工具承担的任务，授权规定使用、修改和分发的条件。这是两条不同的分类轴：免费不等于开源，商业软件也不只面向大公司。

| 类型 | 含义 | 解释 |
| --- | --- | --- |
| 免费使用 | 在规定条件下不收使用费 | 仍需确认功能、平台、商业用途等限制 |
| 开源 | 按相应开源许可证开放源码，并授予使用、修改、再分发等权利 | 仍有版权与许可条件，也可以提供收费服务 |
| 源码可见／Source-available | 允许在规定条件下查看源码 | 不自动等于符合开源定义，具体权利取决于许可 |
| 买断／永久许可 | 某个产品或版本的许可按所购条款持续有效 | 不一定包含未来全部大版本与服务 |
| 订阅 | 按期限付费取得使用权或服务 | 停订后的使用、导出和访问条件取决于产品条款 |
| 分成／Royalty | 达到相应条件时按规则支付费用 | 计费范围、门槛和计算方式需按许可确认 |
| 教育／个人／独立开发者版 | 面向特定资格提供的方案 | 可能限制使用者、公司规模、项目类型或收入范围 |

本文按 [Open Source Initiative 的定义](https://opensource.org/osd)使用“开源”一词，而非将所有可见源码都归为开源。选用工具时，应分别查看**编辑器许可、运行组件许可、素材许可与平台服务条款**，它们可能不是同一份文件。

采用前需确认目标系统、导出格式、平台支持、许可条件和持续成本。对已停更或维护不明的工具，还需检查可用版本、依赖环境与迁移方式。历史教程可以说明旧版操作，不能代替当前授权和兼容性核对。

<a id="combinations"></a>
## 开发工具组合示例

以下组合用于说明分工，不是唯一推荐，也不是已验证的现有项目配置。同一职责可以换用其他工具，简单项目可以省略不需要的环节。

### A．图片与对白为主的竖屏网页游戏

**Blender 或二维绘图工具 → 图片资源 → HTML／CSS／JavaScript → 浏览器 → GitHub Pages 等托管服务。**

Blender 负责制作画面；HTML 定义图片、对话框和按钮等内容；CSS 规定外观与布局；JavaScript 处理选择和状态；浏览器运行程序；托管服务向访问者分发文件。VS Code 用于编辑，Git 用于记录修改，不需要作为制作工具安装在玩家设备上。

《体温调节》讨论过的预渲染方案可按这一分工理解：**三维软件负责源场景制作，游戏端使用二维资源完成显示和交互。** 只有运行阶段需要实时三维能力时，才需进一步比较 Three.js 等路线。

### B．以人物对白与分支为核心的视觉小说

**绘图软件制作立绘 → 音频工具制作声音 → Ren’Py 组织对白、选项与运行 → 导出目标平台版本。**

绘图与音频工具提供资源，Ren’Py 提供视觉小说的通用系统，开发者编写故事和条件并验证存档。加入 Live2D 等动画前，仍需确认对应的集成方式与许可。

### C．二维动作或探索游戏

**Aseprite 制作角色 → Tiled／LDtk 或引擎编辑器安排关卡 → Godot／GameMaker／Phaser 等其中一条路线组织玩法 → 对应平台发布。**

斜线表示备选路线，不代表同时使用全部引擎。地图编辑器生成关卡数据，游戏程序读取数据并实现规则。音效可用 Audacity 等工具处理，音乐则由所选音频工作站制作。

### D．可自由转动视角的网页三维互动

**Blender 制作模型 → 导出适合目标的三维资源 → Three.js／Babylon.js／PlayCanvas 等路线加载和显示 → JS／TS 处理交互 → 网页发布。**

玩家在运行过程中改变三维视角或物体状态，因此需要实时图形能力。**Blender 制作模型，网页端的三维系统根据当前视角生成画面；这与直接显示预渲染图片不同。** 是否加入 React 等界面工具，取决于界面结构与复杂度。

### E．多人协作的三维制作项目

**Maya／Blender 等制作形体 → ZBrush 等补充细节 → 材质工具处理表面 → 动画工具制作动作 → Unity／UE 或自有引擎整合 → 测试与发布工具生成交付版本。**

版本管理记录文件变动，制作追踪工具安排审阅，自动构建流程持续生成可测试版本。需要在线功能时，再加入联机与后台服务。不同工具通过明确的资源规格、交付步骤和检查标准连接成制作流程。

<a id="confusions"></a>
## 易混名称与概念对照

| 名称／说法 | 解释 |
| --- | --- |
| Unity、C#、Visual Studio | 分别是引擎、语言和开发工作台，可以配合使用 |
| Java、JavaScript | 两种不同语言，不是完整版与简化版的关系 |
| Three.js、TypeScript | 分别是三维库与语言，可以配合使用 |
| VS Code、Visual Studio | 不同产品，不是同一名称的长短写法 |
| Clickteam Fusion、Photon Fusion、Blackmagic Fusion | 分别属于游戏制作、多人网络和视觉合成方向 |
| Blender、Cycles | 分别是综合制作软件及其包含的渲染系统 |
| Unreal、UEFN | 分别是通用引擎与面向 Fortnite 创作的特定编辑工作流 |
| Git、GitHub、GitHub Pages | 分别负责版本控制、仓库协作和网页托管 |
| ink、Inky | 分别是叙事语言与相应编辑器 |
| Live2D Editor、SDK | 分别是内容制作工具与项目接入／运行组件 |
| AI 文件、游戏 AI、生成式 AI | 可能分别指 Illustrator 文件、角色行为系统和生成内容的人工智能 |
| Unity Version Control／Plastic SCM | 当前产品名与旧资料常见名称，查阅时需注意版本 |
| P4／Helix Core | 当前 Perforce 产品名与旧资料常见名称 |
| Flow Production Tracking／ShotGrid | 当前制作追踪产品名与旧称 |
| RealityScan／RealityCapture | 当前桌面产品名与旧称；RealityScan Mobile 需另外区分 |
| Affinity Designer／Photo／Publisher | 旧资料中的分别命名应用；当前 Affinity 统一应用整合多类功能 |
| Shader／着色器 | 处理图形计算的程序类别，不是某个固定品牌的软件 |
| 插件／素材包 | 插件通常扩展功能，素材包提供内容；一个产品也可能同时包含两者 |
| 开源引擎制作的游戏 | 引擎许可与游戏代码、素材的许可需分别判断 |
| HTML5 游戏 | 对网页游戏技术路线的宽泛称呼，不是具体引擎名称 |
| 3A／AAA | 用于描述项目制作规模等情况，不是引擎、语言或软件质量等级 |

产品改名可参看 [Perforce P4](https://www.perforce.com/products/p4)、[Unity Version Control 文档](https://docs.unity.com/en-us/unity-version-control)、[Flow Production Tracking](https://www.autodesk.com/products/flow-production-tracking/overview)、[RealityScan](https://www.realityscan.com/uses)和 [Affinity](https://www.affinity.studio/)的官方说明。旧名有助于查找历史教程，但旧版操作、许可和兼容条件不一定继续适用。

<a id="finish"></a>
## 项目技术说明示例

介绍项目技术时，分别说明主体框架、编程语言、资源制作与发布方式即可。例如，一个使用预渲染图片的网页项目可以表述为：

> 项目使用 HTML、CSS 和 JavaScript 制作网页交互，没有采用 Unity 等完整游戏引擎。画面在 Blender 中制作并导出为图片，代码使用 VS Code 编辑，通过 Git 管理，最终发布到网页托管服务。

使用通用引擎的项目则可以表述为：

> 游戏主体使用 Unity，脚本使用 C#，模型在 Blender 中制作，贴图在 Painter 中制作，角色动作由动画工具完成后导入。

识别一个工具时，主要确认它所属的制作环节、输出的内容，以及负责接收这些内容的下一项工具。**用途说明它承担的任务，输出说明它交付的成果，连接关系说明它在整个项目中的位置。**

<a id="sources"></a>
## 来源与查阅方式

本文的工具定位优先依据各产品官网、官方文档和作者项目页，来源直接放在对应软件名称上，不另重复完整链接名单。关系解释与组合示例用于说明职责，不代表厂商对任意跨软件组合的兼容承诺。

概念的主要核对入口包括 [Unity 的引擎介绍](https://unity.com/products/unity-engine)、[Godot 的功能说明](https://godotengine.org/features/)、[Phaser 的自我定义](https://docs.phaser.io/phaser/getting-started/what-is-phaser)、[MDN 的网页技术说明](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/What_is_JavaScript)、[Git 文档](https://git-scm.com/about)、[Git LFS](https://git-lfs.com/)、[glTF 规范入口](https://www.khronos.org/gltf/)和 [OSI 开源定义](https://opensource.org/osd)。

资料查阅日期为 **2026-10-13**。本文用于认识工具，不提供价格或平台授权保证；实际采用仍需核对当前版本、许可与项目兼容性，并完成相应测试。
