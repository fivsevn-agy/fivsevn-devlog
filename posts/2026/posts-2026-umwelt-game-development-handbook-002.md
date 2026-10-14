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
  按任务查阅游戏引擎、程序、美术、动画、音频、叙事、协作、测试与发布工具，区分开放情况和费用。结合多款知名游戏横向比较制作路线，附文件格式、工具搭配、交接与排错速查。
parents: ["posts-index"]
related: ["posts-2026-umwelt-game-development-handbook-001"]
tags: ["game-development", "software", "tools", "game-engine", "licensing", "cost", "handbook"]
audience: ["self", "public"]
languages: ["zh"]
maturity: "evolving"
confidence: 0.9
visibility: "public"
source_of_truth: "devlog"
lang: "zh-CN"
description: "按用途查游戏开发工具、输出文件、开放情况和费用，用多个游戏案例比较制作路线，并查阅交接与常见问题。"
canonical_url: "https://devlog.fivsevn.com/posts/2026/posts-2026-umwelt-game-development-handbook-002.html"
created: "2026-10-13"
updated: "2026-10-15"
metadata_updated: "2026-10-15"
---

# 游戏开发软件地图手册｜ChatGPT 写给五月七日的指导笔记 002

**撰写：ChatGPT · 工具与费用形式核对：2026-10-15**

[001 制作流程](posts-2026-umwelt-game-development-handbook-001.html) · **002 软件地图与查阅**

查一个工具时，先确认四项：**它处理什么工作，输入与输出是什么，下一步交给谁，使用条件和总成本是什么。** 例如，Blender 制作模型，GLB 承接模型导出，Godot 或 Three.js 读取资源并组织显示，项目代码决定交互，商店或网站把成品交给玩家。

本篇按任务组织，软件名链接到官方产品、手册或许可入口。可以从目录跳到正在做的工作，也可以用浏览器的页面查找搜索软件名、英文缩写或扩展名。表格保留费用形式；具体金额、资格与版本条件在采购或发行时核对官方方案。

<a id="map"></a>
## 查阅目录

| 要处理的工作 | 对应章节 |
| --- | --- |
| 认识引擎、语言、编辑器的关系 | [基本概念](#start) · [开放情况与费用](#cost-legend) |
| 选择游戏主体的制作方式 | [01 通用引擎](#tools-01) · [02 专用工具与框架](#tools-02) |
| 编写程序、理解技术名称 | [03 语言、代码与构建](#tools-03) |
| 整理设计、资料和数值 | [04 规划与研究](#tools-04) |
| 制作图像、模型和场景 | [05 二维](#tools-05) · [06 三维与材质](#tools-06) · [07 关卡与环境](#tools-07) |
| 制作动作、声音与文字 | [08 动画与特效](#tools-08) · [09 音频](#tools-09) · [10 叙事、界面与本地化](#tools-10) |
| 保存、协作、检查和联网 | [11 版本与协作](#tools-11) · [12 测试](#tools-12) · [13 联机与中间件](#tools-13) |
| 把作品交给玩家 | [14 发布与维护](#tools-14) · [15 宣传、素材与辅助加工](#tools-15) |
| 收到陌生文件，或资源显示不对 | [文件格式](#formats) · [排错速查](#troubleshooting) |
| 为项目挑一套工具 | [组合示例](#combinations) · [选型与总成本](#licensing) |
| 区分相似名字，继续阅读 | [易混名称](#confusions) · [案例与学习资料](#sources) |

<a id="start"></a>
## 基本概念：从源文件到玩家

| 概念 | 职责 | 例子与交接 |
| --- | --- | --- |
| 制作软件／DCC | 编辑图像、模型、动作和声音 | Photoshop、Blender、REAPER 产生源工程和可导出的素材 |
| 游戏引擎 | 提供场景、图形、输入、音频等基础能力 | Unity、Godot、Unreal 接入资源，再由项目规则组织体验 |
| 编辑器／IDE | 提供制作、编写和调试界面 | 引擎编辑器摆放场景；VS Code、Rider 编辑代码 |
| 编程语言 | 表达条件、数据和操作的规则 | C#、GDScript、JavaScript、Lua 等用于不同运行环境 |
| 程序库／框架 | 提供现成功能，或进一步约定程序结构 | Three.js 提供三维能力；Phaser 组织二维游戏；项目补上自身规则 |
| 运行时 Runtime | 成品执行时使用的程序部分 | 加载资源、运行脚本、播放动画；玩家通常不需要安装制作编辑器 |
| 插件／SDK／API | 扩展软件／接入功能的工具包／软件之间的调用约定 | 给引擎加插件，通过 SDK 接入平台，再按 API 调用能力 |
| 中间件 Middleware | 承担专门的运行任务 | FMOD 处理交互音频，物理组件处理碰撞与运动 |
| 文件格式 | 约定内容怎样保存与交换 | PNG、GLB、WAV、JSON；兼容范围还要看具体导入器 |
| 发布平台／托管 | 分发成品、处理获取与更新 | itch.io、Steam、网站托管；部分平台还提供账号和社交能力 |

一条简化流程是：**源工程 → 导出资源 → 游戏项目 → 构建与打包 → 发布 → 玩家运行。** 修改源工程后要重新导出，更新项目后要重新生成成品；在编辑器中看到效果后，还需检查玩家实际取得的版本。

### 用几款作品对照这些层次

| 游戏 | 已公开的工具分工 | 可以说明的区别 |
| --- | --- | --- |
| [《Hollow Knight》](https://www.hollowknight.com/) | Photoshop 手绘、PNG 资源、Unity 集成 | 绘图软件与引擎分别承担资源制作和运行。[1](#ref-1) |
| [《Cuphead》](https://cupheadgame.com/) | 纸上动画、Photoshop 上色、Unity 集成 | 相同引擎可以接入不同制作来源与风格。[2](#ref-2) |
| [《UNDERTALE》](https://undertale.com/) | GameMaker 官方作品展示收录 | 通用二维制作环境也能组织具有鲜明规则与叙事的作品。[3](#ref-3) |
| [《Brotato》](https://store.steampowered.com/app/1942280/Brotato/) | Godot 官方作品展示收录 | 开源引擎有商业游戏使用实例；实际选型仍需测试自身需求。[4](#ref-4) |
| [《星露谷物语》](https://www.stardewvalley.net/) | PC 版 1.5.5 从 XNA 迁移至 MonoGame | 框架与项目代码也能组成完整游戏，技术说明需要注明版本。[5](#ref-5) |
| [《Doki Doki Literature Club!》](https://ddlc.moe/) | Ren’Py 官方列举初代桌面版 | 专用引擎可以预先承担对白、显示和存档等常见工作。[6](#ref-6) |

案例用于说明已发生的采用关系。游戏的其他版本、移植和续作可能使用不同工具，不能直接沿用初版资料。

<a id="cost-legend"></a>
## 开放情况与费用的读法

| 标注 | 含义 |
| --- | --- |
| 开源 | 按相应开放许可证提供源码与使用、修改和再分发权利；仍需遵循许可条件 |
| 源码可见 | 可以按专门条款查看或修改源码，权利范围不等同于开源 |
| 专有 | 按厂商许可提供产品；其中部分组件可能另有开放许可 |
| 混合／服务 | 核心、插件、编辑器或托管分别采用不同条款 |
| 免费／条件免费 | 软件不收使用费／免费取决于用途、收入、资格或规模 |
| 付费许可／订阅 | 购买约定版本的使用权／按期限付费；升级和维护范围另查 |
| 额度、按量、分成 | 按资源额度、实际用量或适用收入规则计费 |

**开放情况和费用分开看。** Godot 是免费开源引擎；Unreal 提供源码但采用专门许可；Aseprite 提供源码及自行构建路线，官方成品付费，也限制软件再分发；Blender 的软件许可与用户创作的图像、模型分别处理。[Godot](https://godotengine.org/license/) · [Unreal](https://www.unrealengine.com/license) · [Aseprite](https://www.aseprite.org/faq/) · [Blender](https://www.blender.org/about/license/)

下文“免费”指列出的工具或核心软件，素材、插件、硬件、托管和人力按实际使用另计。

<a id="tools-01"></a>
## 01｜通用游戏引擎

引擎决定主体工程怎样组织、资源怎样接入和成品怎样导出。优先检查目标平台、玩法与画面要求、已有经验、插件支持及维护条件，再比较功能数量。

| 工具 | 主要用途与工作方式 | 开放情况 | 费用形式 |
| --- | --- | --- | --- |
| [Unity](https://unity.com/products) | 二维与三维；场景、组件、资源和 C# 脚本协作 | 专有 | Personal 条件免费；其他适用方案付费 |
| [Unreal Engine／UE](https://www.unrealengine.com/license) | 三维场景、角色、动画与特效；Blueprints 蓝图和 C++ | 源码可见，专门许可 | 游戏按适用免费范围与版税规则；部分其他用途按席位 |
| [Godot](https://godotengine.org/license/) | 二维与三维；节点和场景组织，常用 GDScript 或 C# | 开源，MIT | 引擎免费；具体语言的目标平台支持另查 |
| [GameMaker](https://gamemaker.io/en/get) | 二维；对象、房间、事件、GML 或可视化逻辑 | 专有 | 非商业免费；商业及主机方案分别确认 |
| [GDevelop](https://gdevelop.io/pricing) | 事件式制作，适合从条件与动作组织玩法 | 开源核心＋服务 | 核心免费；云构建、协作等能力按方案 |
| [Construct 3](https://www.construct.net/en/make-games/buy-construct) | 浏览器中的二维事件编辑与导出 | 专有 | 受限免费版＋订阅 |
| [Defold](https://defold.com/license/) | 编辑器与 Lua 脚本协作，常用于二维与轻量项目 | 源码可见，专门许可 | 引擎免费 |

[《Fortnite》](https://www.fortnite.com/)提供了另一种规模的实例：Epic 在 2022 年的官方说明中确认它已采用 Unreal Engine 5。将它与上面的二维作品并列，可以比较大型三维制作与二维项目对引擎的不同需求；UEFN 则是面向 Fortnite 平台的创作工具，发行路径需另作判断。[17](#ref-17)

**交付：** 引擎工程、依赖与资源、构建设置，以及玩家可运行的版本。蓝图或可视化事件同样在表达条件和行为，复杂度仍然需要通过模块与状态管理。

把《Hollow Knight》《Cuphead》《UNDERTALE》《Brotato》并列，可以看到二维画风没有唯一对应的引擎；把《星露谷物语》加入比较，则能看见框架路线。选择时做一个代表性小样：导入一份真实资源，完成一次操作、保存和目标平台导出，再判断工作量。

<a id="tools-02"></a>
## 02｜专用工具、创作平台与代码框架

### 专用制作环境

| 工具 | 适合承担的工作与输出 | 开放情况 | 费用形式 |
| --- | --- | --- | --- |
| [Ren’Py](https://www.renpy.org/) | 视觉小说；对白、选项、角色显示、存档与多平台打包 | 开源 | 引擎免费 |
| [RPG Maker MZ](https://www.rpgmakerweb.com/products/rpg-maker-mz) | 地图、事件、角色、物品和战斗等 RPG 基础系统 | 专有 | 付费许可；素材和插件另计 |
| [Twine](https://twinery.org/) | 非线性文本与互动故事，常导出网页 | 开源 | 免费；故事格式与扩展另查 |
| [GB Studio](https://www.gbstudio.dev/) | 受 Game Boy 规格约束的游戏和相应导出 | 开源 | 软件免费 |
| [Bitsy](https://bitsy.org/) | 小型像素房间、移动、对白和探索故事 | 开源 | 免费 |
| [PICO-8](https://www.lexaloffle.com/pico-8.php) | 集成代码、像素图、地图和音频的幻想主机环境 | 专有 | 完整版付费；教育版范围另查 |
| [Roblox Studio](https://create.roblox.com/docs/studio)／[UEFN](https://dev.epicgames.com/documentation/en-us/fortnite/unreal-editor-for-fortnite) | 分别制作 Roblox、Fortnite 平台中的体验 | 平台工具，专门条款 | 工具可免费取得；发布资格、收益和服务规则另查 |

选专用工具时，先对照自己的主流程与默认能力。视觉小说的对白、回看、选项和存档可能直接复用 Ren’Py；若要把对白嵌入自由移动的游戏，可以考虑独立叙事组件。平台型工具还需要确认成品在哪里运行，以及是否满足自己的独立发行需求。

### 框架与图形库

| 工具 | 承担的能力 | 项目通常还要安排 |
| --- | --- | --- |
| [Phaser](https://docs.phaser.io/phaser/getting-started/what-is-phaser) | JavaScript 二维游戏框架，提供场景、输入和资源等能力 | 玩法、界面、内容结构与发布 |
| [PixiJS](https://pixijs.com/) | 高效二维绘制与显示对象 | 游戏规则、场景流程和所需物理等系统 |
| [Three.js](https://threejs.org/) | JavaScript 三维图形库 | 游戏规则、碰撞、交互、界面和资源流程 |
| [Babylon.js](https://www.babylonjs.com/) | 网页三维引擎与相关工具 | 项目玩法、内容与具体平台适配 |
| [MonoGame](https://docs.monogame.net/articles/tutorials/building_2d_games/01_what_is_monogame/index.html) | .NET 游戏框架，提供图形、输入、音频和内容管线 | 项目结构、编辑方式、关卡和行为系统 |
| [libGDX](https://libgdx.com/) | Java 游戏框架，提供跨平台图形、输入和音频等 | 项目结构、规则、资源与目标平台支持 |
| [LÖVE](https://love2d.org/) | Lua 二维游戏环境 | 游戏结构、内容与所需工具 |
| [raylib](https://www.raylib.com/) | 以代码调用图形、输入、音频等能力 | 玩法、编辑与资源组织 |
| [Bevy](https://bevy.org/) | Rust 游戏引擎，以代码和实体组件系统组织 | 项目内容、工具及所需集成 |

以上核心项目均有免费开源路线，编辑服务、扩展与目标平台支持分别确认。采用库或框架，可以更直接地控制项目结构，同时承担更多连接与维护工作。

[《Celeste》](https://www.celestegame.com/)被 MonoGame 官方列为使用作品；[《星露谷物语》](https://www.stardewvalley.net/)则有从 XNA 迁到 MonoGame 的明确版本记录。再加入采用 libGDX 的[初代《Slay the Spire》](https://megacrit.com/slaythespire/)，可以并列比较 C# 框架和 Java 框架路线；具体移植版本仍需分别核对。[5](#ref-5), [7](#ref-7), [15](#ref-15)

<a id="tools-03"></a>
## 03｜语言、代码编辑与构建

### 先按用途识别语言

| 名称 | 常见位置 | 与相邻工具的关系 |
| --- | --- | --- |
| JavaScript／TypeScript | 网页游戏、界面与开发工具 | JS 在浏览器等环境执行；TS 增加类型检查等开发能力，常在构建时处理成 JS |
| C# | Unity、Godot .NET、MonoGame 等 | 语言相同，使用的引擎接口与项目组织仍不同 |
| C++ | Unreal、引擎与原生组件 | 编译工具生成目标程序，引擎提供相应接口 |
| GDScript／GML | 分别常见于 Godot／GameMaker | 跟随对应工具的语法和运行环境 |
| Lua／Luau | LÖVE、Defold／Roblox 等 | 用于相应环境的脚本与规则；两者需区分 |
| Python | 自动加工、资源检查、工具脚本与 Ren’Py 扩展 | 制作阶段使用 Python，不代表成品也用 Python 运行 |
| Rust／Haxe | Bevy 等／Haxe 生态与框架 | 语言、工具链与目标平台配套使用 |
| HTML／CSS | 网页结构与样式 | 与 JS 一起安排图片、文字、控件和交互 |
| HLSL／GLSL／WGSL | 着色器，表达 GPU 上的图形或计算工作 | 由引擎或图形接口接入；通常不用于整个游戏的叙事与存档 |
| JSON／CSV／YAML／TOML | 数据与配置格式 | 保存物品、对白、设置等，项目程序解释其含义 |

语言名称本身不能确定软件费用。具体成本由编辑器、编译工具、引擎、组件与服务决定。查语言用 [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript)、[TypeScript](https://www.typescriptlang.org/docs/)、[Microsoft C#](https://learn.microsoft.com/en-us/dotnet/csharp/)、[Godot](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html)和对应工具官方文档。

### 代码从编写到运行

| 工具 | 职责与输出 | 开放情况 | 费用形式 |
| --- | --- | --- | --- |
| [VS Code](https://code.visualstudio.com/docs/supporting/faq) | 编辑、搜索、调试与扩展 | Code OSS 开源；微软发行版另许可 | 软件免费；扩展或服务另计 |
| [Visual Studio](https://visualstudio.microsoft.com/)／[Rider](https://www.jetbrains.com/rider/buy/) | 集成开发环境，常用于 .NET 与游戏项目 | 专有 | Community／非商业等免费资格分别核对；商业方案付费 |
| [Xcode](https://developer.apple.com/xcode/)／[Android Studio](https://developer.android.com/studio) | Apple／Android 平台开发、调试与构建 | 产品与组件许可不同 | 工具可免费取得；设备和发行资格另计 |
| [Node.js](https://nodejs.org/en/about)／[.NET](https://dotnet.microsoft.com/learn/dotnet/what-is-dotnet) | 运行程序与支持开发流程 | 开源核心 | 免费；托管与支持另计 |
| [npm](https://docs.npmjs.com/about-npm/)／[pnpm](https://pnpm.io/)、[pip](https://pip.pypa.io/en/stable/)、[NuGet](https://learn.microsoft.com/en-us/nuget/what-is-nuget)、[Cargo](https://doc.rust-lang.org/cargo/) | 分别管理不同生态的依赖与版本 | 开源工具 | 工具免费；包与注册表服务另查 |
| [Vite](https://vite.dev/guide/) | 网页开发预览与生产构建 | 开源 | 免费 |
| [GCC](https://gcc.gnu.org/)／[Clang](https://clang.llvm.org/) | 编译 C、C++ 等源代码 | 开源 | 工具免费；运行库许可另查 |
| [CMake](https://cmake.org/)／[Gradle](https://gradle.org/) | 配置、组织和执行构建 | 开源核心 | 核心免费；商业服务另计 |

**典型交接：** 编辑代码 → 获取约定依赖 → 检查与编译／构建 → 运行 → 调试。版本号、依赖清单和锁定文件应跟项目一起保存，使另一台机器能够重建相同环境。网页项目使用 Node.js 构建，并不意味着玩家访问静态成品时也需要服务器运行 Node.js。

<a id="tools-04"></a>
## 04｜设计文档、资料与数值

| 工具 | 用途与交付 | 开放情况 | 费用形式 |
| --- | --- | --- | --- |
| [Obsidian](https://obsidian.md/pricing) | 本地 Markdown 笔记、设计和链接 | 专有 | 应用免费；同步与发布等服务另计 |
| [Notion](https://www.notion.com/pricing) | 在线文档、知识与任务组织 | 专有服务 | 免费基础＋付费方案 |
| [Google Docs／Sheets](https://workspace.google.com/) | 协作文档、数值和资源表 | 在线服务 | 个人基础使用与付费组织方案区分 |
| [LibreOffice](https://www.libreoffice.org/) | 本地文档与表格，整理数据并导出 CSV 等 | 开源 | 免费 |
| [PureRef](https://www.pureref.com/download.php) | 在同一画布组织视觉参考 | 专有 | 个人与商业类别按当前方案 |
| [Zotero](https://www.zotero.org/) | 文献、来源、笔记和引用 | 开源 | 应用免费；附件存储扩容收费 |
| [diagrams.net／draw.io](https://www.drawio.com/) | 状态、分支、页面与系统流程图 | 开源核心 | 核心免费；部分平台集成收费 |

**交付：** 当前设计、来源、数据字段和资源清单。表格进入游戏前，需要读取或转换步骤，并检查编号、空值、数值范围与多语言对应。图片进入参考板后也要保留来源；参考图与可用于成品的素材有各自的用途和许可。

<a id="tools-05"></a>
## 05｜二维图像、像素画与矢量

| 工具 | 用途与常见输出 | 开放情况 | 费用形式 |
| --- | --- | --- | --- |
| [Photoshop](https://www.adobe.com/products/photoshop/plans.html) | 绘图、合成、贴图；PSD 源工程与导出图像 | 专有 | 完整桌面制作主要为订阅 |
| [Clip Studio Paint](https://www.clipstudio.net/en/purchase/) | 插画、角色差分与逐帧动画 | 专有 | 买断或订阅依平台与版本 |
| [Krita](https://krita.org/en/)／[GIMP](https://www.gimp.org/) | 数字绘画／图像编辑 | 开源 | 官网软件免费 |
| [Aseprite](https://www.aseprite.org/faq/) | 像素、图层、动画帧、标签与图集 | 源码可见，专门许可 | 官方成品付费；自行构建按条款 |
| [Pixelorama](https://orama-interactive.itch.io/pixelorama) | 像素绘画、图层、逐帧动画与图集 | 开源 | 有免费获取路线；商店版本可付费支持 |
| [Inkscape](https://inkscape.org/)／[Illustrator](https://www.adobe.com/products/illustrator.html) | 矢量图标、形状与标志；SVG 或位图导出 | 分别开源／专有 | 分别免费／订阅 |
| [TexturePacker](https://www.codeandweb.com/texturepacker) | 把多张小图打包成图集及位置数据 | 专有 | 受限免费功能＋付费 Pro |

位图保存像素，矢量图保存曲线和形状；精灵图（Sprite）是游戏中使用的二维图像对象；图集（Atlas）把多个图像放在一张或一组纹理中，并用数据说明各区域。

### 三种二维资源来源的比较

| 作品 | 制作路径 | 修改时主要返回哪里 |
| --- | --- | --- |
| [《Hollow Knight》](https://www.hollowknight.com/) | Photoshop 中绘制并整理手绘动画，导出 PNG | 图层、动作帧及其导出设置。[1](#ref-1) |
| [《Cuphead》](https://cupheadgame.com/) | 纸上绘制，再数字上色与整理 | 原画与数字制作环节；需同步帧序列。[2](#ref-2) |
| [《Dead Cells》](https://dead-cells.com/) | 三维模型与动作转成小尺寸图像帧 | 三维源工程与渲染，再检查像素结果。[8](#ref-8) |

三者最终都能交付二维帧，但源文件、返工方法和可以复用的部分不同。若准备外包或长期修改，应同时交接源文件和导出资源。

**导入检查：** 尺寸、透明边缘、色彩、基点、帧序、帧率、过滤和压缩。像素画通常需要明确最近邻采样与缩放策略；是否使用整数倍缩放由目标画面决定。先在游戏实际显示尺寸检查，再看放大的编辑视图。

<a id="tools-06"></a>
## 06｜三维模型、雕刻、材质与渲染

三维资源通常依次处理形状、表面、动作与显示。简单道具可以在一套软件内完成，复杂角色会经过多个专门环节。

| 工具 | 用途与交付 | 开放情况 | 费用形式 |
| --- | --- | --- | --- |
| [Blender](https://www.blender.org/about/license/) | 建模、雕刻、UV、绑定、动画、渲染；保留 `.blend`，导出模型或画面 | 开源 | 软件免费；插件另计 |
| [Maya](https://www.autodesk.com/products/maya/overview)／[3ds Max](https://www.autodesk.com/products/3ds-max/overview) | 综合三维制作、动画与资源生产 | 专有 | 订阅等商业许可 |
| [Blockbench](https://blockbench.net/) | 低多边形与方块风格建模、贴图和动画 | 开源 | 免费 |
| [ZBrush](https://www.maxon.net/en/zbrush)／[Nomad Sculpt](https://nomadsculpt.com/) | 以雕刻方式塑造形体与表面 | 专有 | 付费方案，依产品和平台 |
| [Substance 3D Painter](https://www.adobe.com/products/substance3d/apps/painter.html) | 在模型表面绘制材质，输出颜色、粗糙度等贴图 | 专有 | 订阅或特定渠道许可 |
| [Substance 3D Designer](https://www.adobe.com/products/substance3d/apps/designer.html)／[Material Maker](https://www.materialmaker.org/) | 通过节点生成材质与纹理 | 分别专有／开源 | 分别付费／免费 |
| [RealityScan](https://www.realityscan.com/license) | 从照片等输入重建三维资源 | 专有 | 桌面条件免费或付费；移动产品另看 |
| Blender 的 [Cycles](https://docs.blender.org/manual/en/latest/render/cycles/index.html)／[Eevee](https://docs.blender.org/manual/en/latest/render/eevee/index.html) | 从场景生成画面，采用不同渲染方式 | 开源组件 | 随 Blender 免费 |

### 三维制作中的常见工序

| 工序 | 处理什么 | 需要检查什么 |
| --- | --- | --- |
| 建模／雕刻 | 轮廓、比例、体积与细节 | 相机里是否成立，近景与远景需要多少细节 |
| 拓扑／重拓扑 | 点、边、面的连接与重新组织 | 是否适合变形、编辑与运行预算 |
| UV | 模型表面与二维贴图的位置对应 | 拉伸、接缝、重叠是否符合用途 |
| 贴图与材质 | 图片保存表面信息，材质规定如何参与显示 | 色彩空间、贴图通道、透明与粗糙度 |
| 烘焙 Baking | 把部分计算结果提前写入资源 | 法线、光照或遮蔽信息是否与目标模型对应 |
| LOD／简化 | 为不同距离准备不同细节 | 轮廓与切换是否稳定，是否真正降低开销 |
| 导出与导入 | 在制作软件与游戏之间交换资源 | 单位、坐标轴、变换、材质、动画和外部文件 |

法线贴图可以影响表面受光，物体的外轮廓和实际碰撞仍需要相应几何或碰撞形状。高精度雕刻与扫描结果也常需清理、简化、UV 和材质整理，才能进入实际游戏。

### 三维制作与二维运行怎样组合

[《Dead Cells》](https://dead-cells.com/)用三维动作生成二维图像帧；[《Hollow Knight》](https://www.hollowknight.com/)与[《Cuphead》](https://cupheadgame.com/)的已公开流程从手绘资源出发。[1](#ref-1), [2](#ref-2), [8](#ref-8) 比较它们时，先问资源怎样生产，再问游戏运行时使用什么。

对你的固定镜头场景，可以比较以下三种方案：

| 方案 | 游戏取得的资源 | 优点与制作限制 |
| --- | --- | --- |
| 直接二维绘制 | 背景图、分层图、动作帧 | 直接控制像素与笔触；换角度通常需要重新绘制 |
| 三维预渲染 | 固定镜头图像或帧序列 | 便于统一透视与光照；新视角或光照需要重新输出 |
| 实时三维 | 模型、材质、动画 | 运行时改变相机与光照；需要同时满足设备性能和资源预算 |

这些是可选择的制作方案。也可以混用固定背景与实时角色，但要共同检查透视、遮挡、接触阴影和显示尺度。

<a id="tools-07"></a>
## 07｜场景、地形与关卡

场景安排环境内容，关卡进一步组织路线、目标、障碍、触发与节奏。地面看起来连通时，角色还需要正确的碰撞或可通行数据。

| 工具 | 用途与输出 | 开放情况 | 费用形式 |
| --- | --- | --- | --- |
| 引擎场景编辑器 | 摆放对象、光源、相机、碰撞与触发区域 | 随引擎 | 按对应引擎方案 |
| [Tiled](https://www.mapeditor.org/) | 二维瓦片、对象层与地图属性 | 开源 | 免费，可支持开发 |
| [LDtk](https://ldtk.io/) | 二维关卡、实体与自动图块；JSON 等数据 | 开源 | 免费，可支持开发 |
| [Houdini](https://www.sidefx.com/products/compare/) | 用节点与规则生成、加工地形和其他资源 | 专有 | 商业、Indie 与非商业学习版分别许可 |
| [Gaea](https://quadspinner.com/)／[World Machine](https://www.world-machine.com/) | 地形、高度图与遮罩等输出 | 专有 | 受限免费版＋付费方案 |
| [SpeedTree](https://unity.com/products/speedtree) | 树木、植被及相关模型与纹理 | 专有 | 付费方案 |
| [TrenchBroom](https://trenchbroom.github.io/) | 面向 Quake 等地图格式的三维关卡编辑 | 开源 | 免费 |

**交付：** 布置数据、对象标识、碰撞、触发和目标引擎可读取的资源。Tiled 或 LDtk 的地图通常还需导入器；对象名、属性和事件如何变成游戏行为，由项目约定。

比较[《Celeste》](https://www.celestegame.com/)、[《Hollow Knight》](https://www.hollowknight.com/)和[《A Short Hike》](https://ashorthike.com/)的公开玩法，可以分别观察局部动作挑战、房间之间的连接与探索空间中的路线选择。它们提醒你在选择编辑工具时考虑不同需求：精确摆放、跨场景连接、地形与视线。这里比较的是关卡需求，不据此推断它们采用了表中哪一款地图软件。

<a id="tools-08"></a>
## 08｜动画、绑定与特效

| 工具 | 用途与交付 | 开放情况 | 费用形式 |
| --- | --- | --- | --- |
| Aseprite／Pixelorama／Krita | 逐帧动画、图像序列或图集 | 见 [05](#tools-05) | 按对应工具 |
| [OpenToonz](https://opentoonz.github.io/e/) | 二维动画生产与场景合成 | 开源 | 免费 |
| [Spine](https://esotericsoftware.com/spine-purchase) | 二维骨骼、变形与动画数据 | 编辑器与运行组件分别许可 | 编辑器付费，集成遵循运行许可 |
| [Live2D Cubism](https://www.live2d.com/en/cubism/comparison/) | 分层二维角色的变形、表情与动作 | 编辑器专有；SDK 专门条款 | FREE＋PRO；发行集成条件另查 |
| Blender／Maya | 三维骨架、蒙皮、关键帧与动画片段 | 见 [06](#tools-06) | 按对应工具 |
| [Mixamo](https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html) | 双足人形自动绑定与动作资源 | 专有服务 | 可免费使用；对象与素材条款另查 |
| [Effekseer](https://effekseer.github.io/en/) | 粒子与特效编辑、运行集成 | 开源 | 免费 |
| [Niagara](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine)／[Unity VFX Graph](https://unity.com/features/visual-effect-graph) | 各自引擎中的特效制作 | 随引擎 | 按引擎及模块方案 |

**逐帧动画**逐张安排画面；**骨骼动画**用控制结构带动形体；**变形动画**改变形状或网格；**粒子系统**控制大量元素的产生、运动和消失。它们可以共同使用。

《Cuphead》的纸上帧动画、《Hollow Knight》的数字手绘帧与《Dead Cells》的三维动作转帧，分别体现了不同的姿态制作和修改路径。即使最终都是图像帧，打击生效、脚步声、转向和中断时刻仍需要与游戏状态连接。[1](#ref-1), [2](#ref-2), [8](#ref-8)

**交接检查：** 动作名称、时长、帧率、循环、位移、起止姿态、触发事件和中断条件。骨骼格式还要核对骨架、蒙皮权重及运行组件版本。工具能打开动画文件，只说明读取了部分内容；要在目标角色上检查变形与节奏。

<a id="tools-09"></a>
## 09｜录音、作曲、音效与交互音频

| 工具 | 用途与交付 | 开放情况 | 费用形式 |
| --- | --- | --- | --- |
| [Audacity](https://www.audacityteam.org/) | 录音、剪辑、基础处理与音频导出 | 开源 | 免费 |
| [REAPER](https://www.reaper.fm/purchase.php) | 多轨录音、编辑、混音；项目与分轨 | 专有 | 付费许可，提供评估期 |
| [Ableton Live](https://www.ableton.com/en/live/)／[FL Studio](https://www.image-line.com/fl-studio) | 编曲、乐器、节奏与音乐制作 | 专有 | 付费版本；音源与扩展另计 |
| [Logic Pro](https://www.apple.com/logic-pro/)／[Cubase](https://www.steinberg.net/cubase/) | 综合音乐制作与混音 | 专有 | 依平台与产品采用购买或订阅方案 |
| [FamiStudio](https://famistudio.org/) | NES 风格音源的音乐制作 | 开源 | 免费 |
| [FMOD Studio](https://www.fmod.com/licensing) | 声音事件、参数、动态音乐和游戏集成 | 专有／专门许可 | 条件免费；其他项目按许可 |
| [Wwise](https://www.audiokinetic.com/en/wwise/pricing/for-games/) | 交互音频制作、性能与运行集成 | 专有／专门许可 | 按项目、平台和预算等确认方案 |

数字音频工作站（DAW）负责产生声音素材，中间件负责把声音与游戏事件连接。例如先制作不同音乐层，再由游戏状态控制哪些层播放、怎样衔接。少量背景音乐与点击音可以先采用引擎或浏览器已有能力。

**三种复杂度可以并列比较：**

| 情况 | 制作与接入方式 | 重点 |
| --- | --- | --- |
| 图片与对白小作品 | 导出背景音乐、环境循环与短音效，再由项目播放 | 首次启动、音量、循环接缝与离开场景时的停止 |
| 动作角色 | 把脚步、起跳、冲刺、受击与状态或事件连接 | 声音时机、表面变化与重复播放 |
| 随探索或战斗变化的音乐 | 分轨或事件由参数驱动，在运行中切换或混合 | 节拍衔接、过渡、优先级与性能 |

[《Celeste》](https://www.celestegame.com/)提供了可查阅的实际 FMOD 制作案例：官方教程由参与音效制作的 Kevin Regamey 拆解项目。它可以与同作的 MonoGame 框架采用记录一起看，理解总体运行框架与音频中间件如何分工。[7](#ref-7), [9](#ref-9)

[《LIMBO》](https://playdead.com/games/limbo/)的声音设计师 Martin Stig Andersen 则在 Audiokinetic 访谈中介绍了录音、处理与 Wwise 接入的协作。把它与《Celeste》的 FMOD 项目并列，可以看到不同中间件都要连接声音素材、声音事件和游戏状态；声音风格仍由素材和具体设计决定。[16](#ref-16)

**交付：** 可编辑音频工程、无损母版、运行音频或声音库、事件名称与参数说明。录音采样率、音量、循环点和压缩格式要明确；网页还需检查用户手势与自动播放策略。[MDN 音频启动说明](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Autoplay)

<a id="tools-10"></a>
## 10｜对白、分支叙事、界面与本地化

### 文本怎样进入游戏

| 工具 | 职责与输出 | 开放情况 | 费用形式 |
| --- | --- | --- | --- |
| [Twine](https://twinery.org/) | 以段落和连接组织故事，常可直接导出网页 | 开源 | 免费 |
| [ink／Inky](https://www.inklestudios.com/ink/) | 叙事脚本语言／编写、测试和导出的编辑器 | 开源，MIT | 免费 |
| [Yarn Spinner](https://www.yarnspinner.dev/) | 对白脚本、条件、命令和游戏集成 | 按组件与版本区分 MIT、YSPL 等许可 | 核心工具与付费集成／附加产品分别确认 |
| [articy:draft](https://www.articy.com/en/pricing/) | 人物、流程、分支与结构化叙事数据 | 专有 | 受限免费版＋付费方案 |
| Ren’Py | 把对白与视觉小说显示、选择、保存一起组织 | 见 [02](#tools-02) | 引擎免费 |

Yarn Spinner 部分新产品试用的 [YSPL](https://www.yarnspinner.dev/yspl)带有专门限制；采用时查看具体下载包的许可。不能因为旧版本使用 MIT，就把所有版本和附加产品写成相同许可。

### 几种叙事工具的实际分工

| 游戏 | 已知采用关系 | 适合对照的职责 |
| --- | --- | --- |
| [《80 Days》](https://www.inklestudios.com/80days/) | 开发者介绍了背后的 ink 叙事语言 | 以脚本组织故事条件和分支，接入游戏。[10](#ref-10) |
| [《Night in the Woods》](https://store.steampowered.com/app/481510/Night_in_the_Woods/) | Yarn Spinner 在该作开发期间形成 | 对白工具与完整游戏的场景和交互协作。[11](#ref-11) |
| [《A Short Hike》](https://ashorthike.com/)／[《DREDGE》](https://www.dredge.game/) | Yarn Spinner 官方展示列为使用作品 | 同一种对白工具可以用于不同题材与玩法；完整游戏仍由各自系统组织。[11](#ref-11) |
| [初代《Doki Doki Literature Club!》](https://ddlc.moe/) | Ren’Py 官方列举桌面版 | 专用引擎同时承担对白、角色显示与常见视觉小说功能。[6](#ref-6) |

**交接：** 文本文件、稳定编号、变量、条件、调用命令、翻译表和存档状态。Inky 中可预览的故事，仍需接到游戏里的角色、动画和界面；选择造成的变化，也需要由游戏与叙事运行时一致保存。

### 界面与本地化

| 工具 | 用途与交付 | 开放情况 | 费用形式 |
| --- | --- | --- | --- |
| [Figma](https://www.figma.com/pricing/) | 界面设计、组件、交互原型与资源 | 专有服务 | 免费基础＋付费席位／能力 |
| [Penpot](https://penpot.app/) | 界面与原型协作 | 开源核心 | 自托管软件免费；托管与支持按方案 |
| Unity UI Toolkit／Unreal UMG／Godot Control | 游戏运行中的界面、布局与输入 | 随引擎 | 按对应引擎许可 |
| [Weblate](https://weblate.org/en/)／[Crowdin](https://crowdin.com/) | 翻译协作、术语、校对与进度 | 前者开源核心；后者服务 | 自托管或云端方案分别确认 |
| [Poedit](https://poedit.com/)／[OmegaT](https://www.omegat.org/) | 翻译文件编辑／术语与译文辅助 | 开源基础，Poedit 含付费 Pro | 基础免费；附加能力另计 |
| [FontForge](https://fontforge.org/en-US/) | 字形与字体文件编辑 | 开源 | 软件免费；字体内容许可另查 |

UI 是玩家看见并操作的界面，UX 涉及理解、操作与反馈的整体体验。本地化（Localization／L10n）还包括文字长度、字体、语境和地区格式；国际化（Internationalization／I18n）是让系统能够容纳这些差异的设计工作。

一份可点击的设计稿需要继续接入真实状态。翻译文件也需要在目标场景检查。对白型作品重点查人物语境和选择长度；《Papers, Please》这类信息界面还涉及证件与规则的可读性；动作游戏则要检查提示能否在实际节奏中被读懂。比较这些任务，可以决定先投入文本工具、界面工具，还是运行中的验证。

<a id="tools-11"></a>
## 11｜版本、备份与制作协作

| 工具 | 职责 | 开放情况 | 费用形式 |
| --- | --- | --- | --- |
| [Git](https://git-scm.com/book/en/v2) | 提交、分支、比较与恢复开发文件 | 开源 | 软件免费 |
| [Git LFS](https://git-lfs.com/) | 在 Git 中记录大文件指针，另行存放实际内容 | 开源 | 客户端免费；存储和下载流量另计 |
| [GitHub](https://github.com/pricing)／[GitLab](https://about.gitlab.com/pricing/) | 远端仓库、审查、问题与自动化 | 服务／开源核心＋商业产品 | 免费范围＋付费方案和资源额度 |
| [GitHub Desktop](https://desktop.github.com/) | Git 图形客户端 | 开源 | 免费 |
| [Perforce P4](https://www.perforce.com/products/p4/pricing)／[Unity Version Control](https://docs.unity.com/en-us/unity-version-control) | 代码和大量数字资源的版本管理 | 专有 | 小团队或基础范围免费；扩大规模付费 |
| [Trello](https://trello.com/)／[GitHub Projects](https://github.com/features/issues)／[Codecks](https://www.codecks.io/) | 任务、问题和进度 | 专有服务 | 免费基础或适用范围＋付费方案 |
| [Kitsu](https://www.cg-wire.com/kitsu/) | 资源、任务和审阅状态 | 开源核心 | 自托管软件免费；托管和支持另计 |

**Git 提交保存一组变化，推送把提交送到远端，合并把不同修改接到一起。** PR／合并请求是提出、讨论和审查修改的记录。GitHub 提供托管与协作，GitHub Pages 则分发网站，两者职责不同。

代码等文本通常容易比较，模型、分层图像和音频工程常难以自动合并。多人共同修改这些文件时，可以安排锁定或明确交接。Git LFS 的指针需要对应的实际文件，只有指针的副本无法还原资源。

备份还要覆盖未提交文件、大资源、外部素材和必要的项目设置，并尝试恢复。玩家存档保存游玩进度，应与开发工程的历史分别管理。

<a id="tools-12"></a>
## 12｜调试、测试与性能分析

| 工具 | 用途与证据 | 开放情况 | 费用形式 |
| --- | --- | --- | --- |
| [浏览器 DevTools](https://developer.chrome.com/docs/devtools) | 错误、网络请求、页面状态、内存与时间开销 | 随浏览器 | 通常无需另购 |
| [Unity Profiler](https://docs.unity3d.com/Manual/Profiler.html)／[Unreal Insights](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine) | 引擎运行时间与资源分析 | 随引擎 | 按引擎与相关模块 |
| [RenderDoc](https://github.com/baldurk/renderdoc) | 捕获一帧的图形调用与资源，调查绘制问题 | 开源 | 免费 |
| [PIX](https://devblogs.microsoft.com/pix/)／[Nsight Graphics](https://developer.nvidia.com/nsight-graphics) | 相应图形环境与硬件的调试和性能分析 | 厂商工具 | 可免费取得；支持条件另查 |
| [pytest](https://docs.pytest.org/)／[Vitest](https://vitest.dev/)／[NUnit](https://nunit.org/) | Python／JS、TS／.NET 等生态的自动检查 | 开源 | 免费 |
| [Playwright](https://playwright.dev/) | 浏览器操作、断言、截图与回归检查 | 开源 | 软件免费；执行资源另计 |
| [BrowserStack](https://www.browserstack.com/) | 浏览器与真实设备的远程测试服务 | 专有服务 | 付费方案及适用试用资格 |
| [NVDA](https://www.nvaccess.org/about-nvda/)／系统读屏 | 检查语义、朗读和非视觉操作 | NVDA 开源；其他随系统 | 免费或随适用系统提供 |

调试寻找原因，测试核对结果，性能分析定位开销。日志保存执行信息，断点暂停到某个状态，分析器显示时间或内存使用；它们提供不同证据。

**按现象选工具：** 图片没出现先查路径和请求；点击无反应先查事件与状态；频繁卡顿先看耗时与内存；导入模型发黑先查材质、法线和光照；玩家不知道下一步先观察试玩。最后一种情况需要理解玩家看到的信息，单靠性能或代码检查无法完成判断。

比较[《Celeste》](https://www.celestegame.com/)作者对操作容错的说明与[《星露谷物语》](https://www.stardewvalley.net/)1.5.5 中的本地化软锁修复，可以看到检查同时涵盖操作体验和语言条件下的完整流程。[5](#ref-5), [12](#ref-12) 一个按钮“能触发”之后，还应继续检查时机、状态和玩家是否能理解结果。

<a id="tools-13"></a>
## 13｜物理、寻路、联机与后台

### 专门的运行能力

| 工具 | 负责的部分 | 开放情况 | 费用形式 |
| --- | --- | --- | --- |
| [Box2D](https://box2d.org/) | 二维刚体与碰撞 | 开源 | 免费 |
| [Jolt Physics](https://jrouwe.github.io/JoltPhysics/)／[Rapier](https://rapier.rs/) | 三维或二维／三维物理，依项目区分 | 开源 | 免费 |
| [Recast／Detour](https://recastnav.com/) | 导航网格与寻路 | 开源 | 免费 |
| [Photon](https://www.photonengine.com/) | 多人同步与相关服务，Fusion／Quantum 为不同路线 | 专有／专门条款 | 免费适用范围＋并发或服务费用 |
| [Colyseus](https://colyseus.io/)／[Nakama](https://heroiclabs.com/nakama/) | 多人房间与同步／账号、社交和游戏后台等 | 开源核心 | 自托管软件免费；托管与支持另计 |
| [PlayFab](https://learn.microsoft.com/en-us/gaming/playfab/) | 游戏账号、数据与在线服务 | 服务，SDK 另许可 | 免费额度＋用量或方案 |
| [Supabase](https://supabase.com/pricing) | 认证、数据库、文件存储等后台 | 开源核心＋服务 | 自托管或云端额度与付费方案 |
| [SQLite](https://www.sqlite.org/about.html)／[PostgreSQL](https://www.postgresql.org/about/) | 本地数据库／服务器关系数据库 | 公有领域代码／开放许可 | 软件免费；托管与支持另计 |

物理系统计算运动和接触，游戏规则决定接触后发生什么；寻路寻找可达路线，角色行为决定为什么走过去。引擎可能已经包含相应能力，增加独立组件前应先检查现有功能。

### “联网”要拆成具体需求

| 需求 | 需要的工作 |
| --- | --- |
| 网页单机 | 托管分发文件，客户端执行规则；进度可在本地保存 |
| 云存档 | 账号或身份、上传下载、冲突处理与恢复 |
| 排行榜／异步分享 | 提交与查询数据、验证、排序和滥用处理 |
| 实时多人 | 状态或输入同步、谁作最终判断、延迟、断线与重连 |
| 持续在线世界 | 长期服务器、数据持久化、容量、监控与维护 |

[《Factorio》](https://www.factorio.com/)的开发记录介绍了确定性多人模拟：各端推进模拟并交换玩家行动等信息，计算不一致会形成不同步问题。[13](#ref-13) 这与“把单机存档上传云端”承担的任务不同。挑选联网工具之前，先写明要同步什么、谁保存最终状态、断线后怎样恢复，再估算服务和测试成本。

<a id="tools-14"></a>
## 14｜构建、发布与运行维护

| 工具／服务 | 职责与输出 | 开放情况 | 费用形式 |
| --- | --- | --- | --- |
| 引擎导出工具 | 生成对应平台的程序、资源包或网页 | 随引擎 | 引擎与平台资格分别确认 |
| [GitHub Actions](https://docs.github.com/en/actions)／[GitLab CI/CD](https://docs.gitlab.com/ci/) | 自动检查、构建、保存产物与部署 | 服务与执行组件分开 | 免费额度＋计算、存储等用量 |
| [Jenkins](https://www.jenkins.io/) | 自行运行自动化流程 | 开源 | 软件免费；机器与维护另计 |
| [Electron](https://www.electronjs.org/)／[Tauri](https://tauri.app/) | 用网页界面等技术组织桌面或相应应用 | 开源核心 | 核心免费；签名和适配另计 |
| [itch.io](https://itch.io/docs/creators/getting-started) | 发布网页和可下载作品 | 平台服务 | 可免费建立作品页；交易规则另查 |
| [Steamworks](https://partner.steamgames.com/doc/gettingstarted) | Steam 平台接入、构建和产品管理 | 平台服务／SDK | 接入、销售等按协议 |
| [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)／[Cloudflare Pages](https://developers.cloudflare.com/pages/) | 静态网站部署与分发 | 托管服务 | 免费适用范围；资源与附加服务另计 |
| [App Store Connect](https://developer.apple.com/app-store-connect/)／[Google Play Console](https://play.google.com/console/about/) | 移动商店的产品、测试与发布管理 | 平台服务 | 开发者资格、注册和交易按规则 |
| [Sentry](https://sentry.io/)／[Firebase Crashlytics](https://firebase.google.com/products/crashlytics) | 错误、崩溃与运行反馈 | 服务，组件许可另查 | 免费范围及关联服务／付费方案分别核对 |

构建（Build）生成可交付文件，部署（Deploy）把文件放入目标环境，发布（Release）让玩家取得约定版本。CI 持续集成自动检查变更；CD 可能指持续交付或持续部署，按项目配置理解。

静态托管可以分发 HTML、图片与脚本，但服务器端的账号、数据库和实时房间需要另外提供。把网页包装为桌面应用，也要继续处理窗口、文件、输入、更新和目标系统行为。

**交付检查：** 在实际产物上测试，保存对应版本，从公开入口再次取得文件，并核对存档与回退条件。[《Baldur’s Gate 3》](https://baldursgate3.game/)Hotfix 4 的官方复盘说明，候选通过检查后再重新构建，也可能产生需要重新验证的变化。[14](#ref-14)

<a id="tools-15"></a>
## 15｜录屏、宣传、素材与辅助加工

| 工具／平台 | 用途与交付 | 开放情况 | 费用形式 |
| --- | --- | --- | --- |
| [OBS Studio](https://obsproject.com/) | 实机录屏、直播与画面组合 | 开源 | 免费 |
| [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve) | 剪辑、调色、合成与音频后期 | 专有 | 免费版＋付费 Studio |
| [Kdenlive](https://kdenlive.org/) | 视频剪辑与成片输出 | 开源 | 免费 |
| [Premiere](https://www.adobe.com/products/premiere.html)／[After Effects](https://www.adobe.com/products/aftereffects.html) | 剪辑／动态图形与合成 | 专有 | 订阅 |
| [FFmpeg](https://ffmpeg.org/)／[ImageMagick](https://imagemagick.org/) | 音视频／图像的批量转换与加工 | 开源 | 软件免费；编解码与组件分发条件另查 |
| [Kenney](https://kenney.nl/assets)／[Poly Haven](https://polyhaven.com/license) | 游戏资源／模型、纹理和环境图 | 各自内容许可 | 有免费资源；所用资源逐项留存许可 |
| [Fab](https://www.fab.com/)／[Unity Asset Store](https://assetstore.unity.com/)／[itch.io Assets](https://itch.io/game-assets) | 模型、图像、声音与插件市场 | 逐项许可 | 免费与付费并存 |
| [Freesound](https://freesound.org/help/faq/) | 声音素材检索与分享 | 每项声音许可不同 | 可免费取得；署名和使用范围逐项查 |

宣传需要保存实际运行录屏、剪辑工程和最终视频。剪辑中的镜头、字幕与特效可以另行制作；对外展示时区分实机内容和概念演示，确保观众能判断实际体验。

AI 可以辅助整理资料、编程、查错和批量加工。把任务限定为可检查的输出，例如“一份附来源的数据表”“保留原布局的模型修改”“可运行的一项交互”，再检查文件、来源、风格和运行结果。参与制作的 AI 工具与成品所采用的语言、引擎、发布平台分别记录。

<a id="formats"></a>
## 文件格式速查：收到文件后怎样处理

| 格式 | 常见内容与打开位置 | 交接时的重点 |
| --- | --- | --- |
| `.psd`、`.kra`、`.aseprite`、`.pxo` | Photoshop、Krita、Aseprite、Pixelorama 的编辑工程 | 保留图层、帧和相关设置；导出图像不能完整替代源工程 |
| `.blend`、`.bbmodel` | Blender、Blockbench 工程 | 检查外部贴图、插件、版本与导出方式 |
| `.png` | 无损位图，可带透明 | 尺寸、透明边缘、过滤和色彩 |
| `.jpg`、`.webp` | 压缩图像；WebP 可采用不同压缩与透明方式 | 确认压缩是否损伤文字、像素边界与细节 |
| `.svg` | 矢量图形 | 目标端是否支持字体、滤镜和复杂效果；必要时导出位图 |
| 图集 PNG＋JSON | 多个图像及区域、基点和动画数据 | 图片与数据必须是配套版本，需相应解析器 |
| `.gltf`／`.glb` | glTF 三维交付格式／二进制容器 | GLB 常把模型、贴图等封装在一起；仍要核对依赖、扩展和导入器支持 |
| `.fbx` | 常用于模型、骨架与动画交换 | 单位、轴向、骨架、动画烘焙与材质转换 |
| `.obj` | 常用于静态几何交换 | 配套材质与贴图路径；不承担通常意义的骨架动画交换 |
| `.wav`／`.flac` | 常用于无损音频母版或交换 | WAV 的具体编码需确认；同时记录采样率、声道和循环信息 |
| `.ogg`／`.mp3` | 常用于运行音频 | 编码支持、压缩质量、加载与循环衔接 |
| `.mid` | 音符、节奏与控制数据 | 实际声音取决于音源或合成器；需要音频时继续渲染 |
| `.ink`／`.yarn`／`.rpy` | ink、Yarn、Ren’Py 的脚本 | 配套编译或运行环境、变量与资源引用 |
| `.csv`／`.json` | 表格数据／结构化数据 | 编码、字段、稳定编号、空值和数值类型 |
| `.ttf`／`.otf`／`.woff2` | 字体及网页常用字体格式 | 字符覆盖、嵌入许可、字重与目标端支持 |
| `.exe`／`.app`／`.apk`／网页目录 | 各种成品形式 | 实际平台、依赖、安装与启动方式、资源是否完整 |

文件扩展名只能说明一部分结构。例如，GLB 能保存某些材质与动画，并不意味着 Blender 的所有节点、修改器和模拟都能原样转入游戏。应在导出前确认目标格式与引擎支持，再通过烘焙、转换或重新设置处理差异。[glTF 官方说明](https://www.khronos.org/gltf/) · [Blender glTF 导出手册](https://docs.blender.org/manual/en/latest/addons/import_export/scene_gltf2.html)

### 一份资源的最小交接信息

**资源名称与编号、源文件、导出文件、尺寸或单位、所用版本、导入位置、检查条件、来源与许可。** 动画加帧率与事件，音频加循环与音量，三维加轴向与材质，对白加条件与文本编号。先用一份代表性资源打通交接，再批量制作。

<a id="combinations"></a>
## 工具组合：先选一条完整制作路线

下表给出可实施的组合示例，斜线表示备选。选择一种主路线后，先完成一个可玩小样，再根据实际缺口增加工具。

| 项目方向 | 一条典型路线 | 首先验证的内容 |
| --- | --- | --- |
| 非线性文字故事 | 文档 → Twine → HTML → itch.io 或网站 | 条件、返回、保存及移动阅读 |
| 图片与对白网页 | Krita／Blender → 图像与音频 → HTML、CSS、JS → 网站 | 图像加载、文字布局、输入、声音与进度 |
| 视觉小说 | 绘图＋音频工具 → Ren’Py → 桌面或其他目标平台 | 对白、差分、选项、回看与存档 |
| 像素动作游戏 | Pixelorama／Aseprite → 图集；Tiled／引擎 → 关卡；Godot／GameMaker → 成品 | 动作、碰撞、地图读取与目标设备性能 |
| 实时三维网页 | Blender／Blockbench → GLB → Three.js／Babylon.js＋项目代码 → 网站 | 材质、相机、触控、资源大小与性能 |
| 三维探索游戏 | Blender／Maya → 模型与动作 → Unity／Godot／UE → 平台构建 | 资源导入、角色控制、关卡与存档 |
| 代码主导的二维游戏 | 绘图与音频 → MonoGame／LÖVE／libGDX 等＋项目工具 | 自己需要补哪些编辑、内容与运行系统 |
| 实时多人游戏 | 上述客户端路线＋联网组件＋服务端＋数据库与监控 | 状态同步、延迟、断线恢复、服务容量与维护 |

例如，固定镜头的渡轮场景可以从“图片与对白网页”路线开始；如果需要自由转动视角，再检验实时三维路线。你已经使用的作者工具和可编辑资产也应进入取舍：能沿用的源工程，会影响学习和迁移成本。

<a id="licensing"></a>
## 选型与总成本

### 用同一份小样比较工具

比较两个方案时，使用同一组需求和素材：一个代表性场景、一次操作、一个存档、目标设备与一次正式导出。记录完成时间、需要补写的功能、导入损失、运行表现和再次修改的成本。

优先依次确认：**能否交付目标平台 → 能否实现核心体验 → 能否接入现有资源 → 是否便于持续修改 → 许可与持续成本是否可接受。** 软件学习资料多少、团队是否熟悉、插件能否继续维护，也会影响结果。

### 把成本分开记录

| 成本 | 需要确认的内容 |
| --- | --- |
| 制作软件 | 版本、席位、商业资格、升级与订阅到期后的使用范围 |
| 运行组件 | 插件、SDK、中间件的版本、平台与成品分发条件 |
| 素材和字体 | 作者、来源、修改、署名、嵌入与再分发范围 |
| 运行与发行 | 注册、签名、存储、流量、服务器、构建与交易费用 |
| 学习和接入 | 导入器、转换、人员培训、原有资产迁移 |
| 长期维护 | 版本升级、兼容、测试、数据迁移与服务结束后的处理 |

开源引擎、商用绘图工具、免费素材与付费音频组件可以出现在同一项目中，分别保留适用条件。购买素材也要确认是否允许把源文件再提供给其他人；用于游戏成品和作为素材包转售是不同的使用方式。

避免把“当前能导出”当成完整成本：还要实际修改一次、在另一台机器打开一次，并确认项目能否脱离某个账号或服务继续维护。

<a id="troubleshooting"></a>
## 常见问题：先检查哪一段

| 现象 | 先查的位置与条件 | 下一步 |
| --- | --- | --- |
| 编辑器有图，游戏没有 | 导出文件、项目引用、资源路径、打包清单 | 检查实际交付目录和加载错误 |
| 图片变糊或边缘出现杂色 | 尺寸、过滤、缩放、压缩、透明边缘 | 用目标显示尺寸比较原图与运行结果 |
| 模型尺寸、朝向不对 | 单位、轴向、对象变换与导入缩放 | 用一个已知尺寸物体统一交接标准 |
| 模型颜色或材质变了 | 支持的材质、纹理路径、色彩空间、法线与光照 | 在简单灯光下逐项对比，确认转换损失 |
| 动画在制作软件里正常，游戏里变形 | 骨架、蒙皮、动画烘焙和运行组件版本 | 从一个最简单动作开始检查 |
| 网页无声 | 用户手势、浏览器策略、音量、加载与编码 | 通过真实首次进入流程启动声音 |
| 本地正常，上线报错 | 路径大小写、部署子路径、缺失文件、缓存与请求限制 | 从公开网址复现并查网络请求 |
| 换网址或浏览器后进度消失 | 存储来源、浏览器、隐私模式和数据清理 | 先保护现有数据，再确认迁移或导入途径 |
| 切场景越来越慢 | 资源重复加载、未释放对象、事件与声音重复注册 | 记录连续操作前后的内存和耗时 |
| 改一段对白后旧存档出错 | 状态结构、文本编号、版本和迁移 | 用旧存档复现，稳定编号与兼容处理 |
| 中文缺字、翻译挤出按钮 | 字体覆盖、字体裁剪、文本长度与容器布局 | 在实际语言、字号和屏幕上逐项检查 |
| 自动测试通过，但玩家卡住 | 测试覆盖、实际版本、起始状态、输入与理解 | 从正常入口重走，并增加针对性的检查 |

排错时每次改变一个主要条件，保留能重现问题的版本和文件。先定位失败发生在制作、导出、导入、运行还是发布，再决定修改哪一个工具或环节。

<a id="confusions"></a>
## 易混名称速查

| 名称 | 区别与关系 |
| --- | --- |
| Unity／C#／Visual Studio | 引擎／语言／开发环境，可以配合使用 |
| VS Code／Visual Studio | 两个不同产品，扩展和工程支持分别确认 |
| Java／JavaScript | 独立语言；名称相似不意味着代码或运行环境相同 |
| Three.js／WebGL、WebGPU／着色器 | 三维库／底层图形接口／用于 GPU 计算的程序 |
| Blender／Cycles、Eevee | 内容制作软件／其中的渲染系统 |
| 引擎／编辑器／运行时 | 基础能力／制作界面／成品执行部分；一套产品可同时包含三者 |
| Git／GitHub／Pages | 版本管理／仓库与协作／静态网站托管 |
| 源工程／导出资源／发布成品 | 继续编辑的文件／进入项目的交换文件／玩家运行的交付物 |
| ink／Inky／Ren’Py | 叙事语言／其编辑器／集成视觉小说常见能力的引擎 |
| Clickteam Fusion／Photon Fusion／Blackmagic Fusion | 游戏制作工具／多人网络产品／视觉合成工具 |
| Unreal／UEFN | 通用游戏引擎／面向 Fortnite 的创作工具 |
| Live2D 或 Spine 编辑器／运行组件 | 制作内容／在游戏中读取和播放，许可与版本分别核对 |
| P4／Helix Core；Unity Version Control／Plastic SCM | 产品在不同阶段的名称，具体能力按版本确认 |
| RealityScan／RealityCapture | 桌面产品名称变化；移动产品另外区分 |
| 游戏 AI／生成式 AI／Illustrator 的 AI 文件 | 角色决策等系统／生成模型／一种绘图工程文件 |

<a id="sources"></a>
## 制作案例与学习入口

工具表中的链接同时作为产品、说明和许可入口。案例的技术采用只覆盖对应资料明确说明的作品、平台或阶段；本文对工作关系的归纳用于帮助比较。

<a id="ref-1"></a>
**[1] Unity / Team Cherry. _Hollow Knight — Made with Unity_.** [制作访谈](https://unity.com/made-with-unity/hollow-knight)。英文，免费。看手绘、PNG 和引擎集成。

<a id="ref-2"></a>
**[2] Unity / Studio MDHR. _Cuphead — Made with Unity_.** [制作访谈](https://unity.com/made-with-unity/cuphead)。英文，免费。看纸上动画、上色与运行资源的交接。

<a id="ref-3"></a>
**[3] GameMaker. _Undertale_.** [官方作品展示](https://gamemaker.io/en/showcase/undertale)。英文，免费。核对 GameMaker 采用关系。

<a id="ref-4"></a>
**[4] Godot Engine. _Brotato_.** [官方作品展示](https://godotengine.org/showcase/brotato/)。英文，免费。核对 Godot 采用关系。

<a id="ref-5"></a>
**[5] ConcernedApe. _Stardew Valley 1.5.5 Released on PC_（2021-11-30）.** [作者公告](https://www.stardewvalley.net/stardew-valley-1-5-5-released-on-pc/)。英文，免费。明确 XNA 到 MonoGame 的迁移版本，也可查本地化与功能修复。

<a id="ref-6"></a>
**[6] Ren’Py. _The Ren’Py Visual Novel Engine_.** [官方介绍](https://www.renpy.org/)。英文，免费。列举初代 DDLC 桌面版，并说明视觉小说引擎的职责。

<a id="ref-7"></a>
**[7] MonoGame. _What Is MonoGame_.** [官方教程](https://docs.monogame.net/articles/tutorials/building_2d_games/01_what_is_monogame/index.html)。英文，免费。看框架职责与《Celeste》等作品实例。

<a id="ref-8"></a>
**[8] Thomas Vasseur. _Using a 3D Pipeline for 2D Animation in Dead Cells_（2018）.** [开发者原文](https://www.gamedeveloper.com/production/art-design-deep-dive-using-a-3d-pipeline-for-2d-animation-in-i-dead-cells-i-)。英文，免费。看三维模型、关键姿态与二维图像帧之间的转换。

<a id="ref-9"></a>
**[9] FMOD / Kevin Regamey. _Celeste_ 教程.** [官方学习入口](https://www.fmod.com/learn/tutorials)。英文，教程可查阅；工程下载的账号要求依官方页面。看声音事件与运行状态怎样连接，示例资源按其学习用途和许可使用。

<a id="ref-10"></a>
**[10] Joseph Humfrey. _Ink: The Narrative Scripting Language Behind 80 Days and Sorcery!_. GDC 2016.** [演讲幻灯片](https://media.gdcvault.com/gdc2016/Presentations/Humfrey_Joseph_Ink_The_Narrative.pdf) · [ink 与 Inky](https://www.inklestudios.com/ink/)。英文，免费。对照语言、编辑器与游戏集成。

<a id="ref-11"></a>
**[11] Yarn Spinner. _About_ / _Showcase_.** [工具来历](https://yarnspinner.dev/about/) · [官方作品目录](https://www.yarnspinner.dev/showcase/)。英文，免费。核对《Night in the Woods》《A Short Hike》《DREDGE》等案例；各组件许可另看所用版本。

<a id="ref-12"></a>
**[12] Maddy Thorson. _Celeste & Forgiveness_.** [作者原文](https://www.mattmakesgames.com/articles/celeste_and_forgiveness/index.html)。英文，免费。把操作容错与程序实现、试玩判断联系起来。

<a id="ref-13"></a>
**[13] Wube Software. _Friday Facts #188 — Bug, Bug, Desync_（2017-04-28）.** [开发记录](https://www.factorio.com/blog/post/fff-188)。英文，免费。理解输入、确定性模拟与不同步。

<a id="ref-14"></a>
**[14] Larian Studios. _Hotfix #4: Redeployed_（2023-08-17）.** [官方新闻](https://baldursgate3.game/news/hotfix-4-redeployed_86) · [Steam 官方公告存档](https://store.steampowered.com/news/posts/?appids=1086940&enddate=1692960041&feed=steam_community_announcements)。英文，免费。看构建、验证与存档恢复。

<a id="ref-15"></a>
**[15] libGDX. _Showcase_ / _Console Support_.** [官方作品目录](https://libgdx.com/showcase/) · [主机支持说明](https://libgdx.com/wiki/articles/console-support)。英文，免费。核对初代《Slay the Spire》的框架采用与移植边界。

<a id="ref-16"></a>
**[16] Audiokinetic / Martin Stig Andersen. _Interview with Playdead_（2010）.** [官方访谈 PDF](https://www.audiokinetic.com/download/documents/customer_profiles/Audiokinetic_Customer_Profile_Playdead_July2010.pdf) · [Playdead 声音演讲目录](https://blog.playdead.com/articles/limbo_presentations/limbo_publications.html)。英文，免费。看《LIMBO》的声音创作与 Wwise 接入。

<a id="ref-17"></a>
**[17] Epic Games. _Unreal Engine 5 Is Now Available in Preview!_（2022）.** [官方文章](https://www.unrealengine.com/blog/unreal-engine-5-is-now-available-in-preview?lang=en)。英文，免费。用于确认《Fortnite》在该阶段的 UE5 采用关系。

### 查操作和原理

| 资料 | 用途与获取方式 |
| --- | --- |
| [Godot Docs](https://docs.godotengine.org/en/stable/)／[Unity Learn](https://learn.unity.com/)／[Unreal Documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine) | 官方免费文档或基础课程；先看场景、资源、脚本与导出，使用匹配版本 |
| [Blender Manual](https://docs.blender.org/manual/en/latest/) | 官方免费手册；按建模、UV、动画、渲染和导出查询 |
| [MDN Games](https://developer.mozilla.org/en-US/docs/Games) | 网页运行、输入、图形和资源的免费资料 |
| [Pro Git](https://git-scm.com/book/en/v2) | 免费在线书；查提交、分支、协作和恢复 |
| [Jason Gregory：Game Engine Architecture](https://www.gameenginebook.com/) | 作者入口与概览免费，书籍购买或借阅；系统理解资源、运行与工具结构 |
| [Xbox Accessibility Guidelines](https://learn.microsoft.com/gaming/accessibility/guidelines) | 官方免费指南；按实际界面、输入与信息通道检查体验 |
| [Steamworks](https://partner.steamgames.com/doc/home)／[itch.io Creator Documentation](https://itch.io/docs/creators/getting-started) | 免费发行文档；查产品页、构建与分发 |

[返回查阅目录](#map) · [理解制作顺序：001](posts-2026-umwelt-game-development-handbook-001.html) · [返回个人笔记目录](../index.html)
