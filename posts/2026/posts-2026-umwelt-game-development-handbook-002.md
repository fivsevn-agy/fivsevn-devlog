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
  按用途认识游戏开发中的软件、引擎、编程语言、程序库与在线服务。用白话解释它们分别做什么、怎样搭配，覆盖个人、小团队与大型制作中的主要环节，并附工具官网、易混名称和示例组合。
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

 **从“这个游戏用什么做的？”开始认识工具 · 撰写：ChatGPT · 2026-10-13**

“Unity 做的”“C# 写的”“Blender 建的模”“放在 Steam 上”，可以同时是在说同一个游戏。因为它们分别回答： **拿什么组织游戏、拿什么写规则、拿什么做素材、到哪里发布。**

[上一篇手册](https://devlog.fivsevn.com/posts/2026/posts-2026-umwelt-game-development-handbook-001.html)讲制作流程。这一篇把流程里会遇到的名字放回各自的位置：先知道它负责什么，再决定是否需要学。

这里覆盖个人、小团队和大型制作中的主要软件类别与代表工具，也包括容易被叫成“软件”的语言、程序库和在线服务。 **它是一张查名字的地图，不是必须安装的清单，也不声称收尽全球每个插件和公司内部工具。** 同一软件可能跨好几个类别，表中只挑最有辨识度的用途；不按价格、名气或团队大小排高低。

工具名称的链接指向官网、官方文档或作者项目页，既是来源，也方便继续查。产品会改名、调整授权和导出平台；本文不列易过期的精确价格和版本号。 **功能定位按 2026-10-13 查阅的资料整理；实际采用前，核对目标版本、授权与平台支持。**

<a id="start"></a>
## 先认清：这些名字不是同一种东西

| 名词 | 它是什么 | 再白话一点 |
| --- | --- | --- |
| 游戏引擎 | 提供游戏运行所需的一批基础系统，通常配有制作工具 | 别人先做好显示画面、播放声音、接收操作等基础功能，你再放进自己的内容与规则 |
| 编辑器 | 供人编辑内容的操作界面 | 摆角色、改代码、调动画的工作台；“编辑器”不一定是游戏引擎 |
| 编程语言 | 编写程序时遵循的表达规则 | 告诉电脑“什么情况下做什么”的写法 |
| 库／程序库 | 可被程序调用的一组现成功能 | 这块功能别人写过了，我拿来用；这里不是图片素材库 |
| 框架 | 在现成功能之外，还给出组织程序的方式 | 工具给你，基本架子也搭好，你往里填具体内容 |
| 插件 | 扩展现有软件功能的部件 | 给现有工具加一个功能，不一定能单独运行 |
| SDK，软件开发工具包 | 接入某个平台或功能的一套程序、接口说明和工具 | 厂商给你的“接线套件”；例如让游戏接入成就或某种动画 |
| API，应用程序接口 | 软件之间调用功能的约定 | 你按规定发出请求，对方按规定回应；不是一个必须另装的软件 |
| 运行时／Runtime | 游戏或功能实际执行时需要的程序部分 | 制作时在编辑器里操作，玩家游玩时由这部分真正工作 |
| 中间件／Middleware | 接进项目、负责某类专门任务的技术 | 不整套重做游戏，而是买或接一套声音、物理、联机等专门功能 |
| 资源／素材／Asset | 游戏使用的图像、模型、音频、字体等内容 | 玩家看到、听到，以及程序要读取的那些东西 |
| 工具链／制作管线 | 内容从制作、加工到进入游戏的一连串步骤与工具 | “在这里做，交到那里处理，最后放进游戏”的路线 |
| 技术栈 | 一个项目组合使用的技术 | 我这次选用的这一套东西，不是某个软件名称 |

这些分类会交叉，并非严格等级。例如 [Phaser 官方](https://docs.phaser.io/phaser/getting-started/what-is-phaser)称它为游戏框架，同时说明它以 JavaScript 库的形式提供。不要纠结谁比谁“高级”，先看它替你负责了多少工作。

 **引擎与编辑器的区别尤其值得记住。** 你在 Unity 的编辑器里摆放一条蛇；玩家打开成品时，不需要跟着打开你的制作工作台，而是运行导出的游戏及其所需程序。Unity 提供场景、脚本、渲染等能力，蛇具体说什么、点击后怎样回应，仍然是你的设计。[Unity 官方介绍](https://unity.com/products/unity-engine)

<a id="map"></a>
## 按用途跳转

| 你正在问什么 | 去看哪里 |
| --- | --- |
| 做之前，拿什么记想法、查资料、算数值？ | [01 规划与资料](#tools-01) |
| 游戏主体用什么做？ | [02 通用引擎](#tools-02) · [03 专用工具与平台](#tools-03) · [04 框架与图形库](#tools-04) |
| 规则怎么写，代码在哪里写？ | [05 语言与技术名词](#tools-05) · [06 编程工作台](#tools-06) |
| 图像、模型、场景怎么做？ | [07 二维绘图](#tools-07) · [08 三维建模](#tools-08) · [09 材质与贴图](#tools-09) · [10 场景与关卡](#tools-10) |
| 角色怎么动，特效怎么来？ | [11 角色与动画](#tools-11) · [12 扫描、渲染与特效](#tools-12) |
| 声音、剧情、菜单和多语言怎么做？ | [13 音频](#tools-13) · [14 交互叙事](#tools-14) · [15 界面与本地化](#tools-15) |
| 多个人怎样不把项目改乱？ | [16 版本管理](#tools-16) · [17 制作协作](#tools-17) |
| 怎样查错、查卡顿、处理专门功能？ | [18 测试与性能](#tools-18) · [19 物理等中间件](#tools-19) |
| 联机和账号后台是什么？ | [20 网络与后台](#tools-20) |
| 怎样交给玩家，出问题怎么知道？ | [21 构建与发布](#tools-21) · [22 维护与运营](#tools-22) |
| 宣传片、现成素材、AI 呢？ | [23 宣传制作](#tools-23) · [24 素材与加工](#tools-24) · [25 AI 辅助](#tools-25) |
| 免费与开源什么区别？哪些工具一起用？ | [授权怎么读](#licensing) · [搭配实例](#combinations) · [易混名称](#confusions) |

不必从头背到尾。第一次先看开头、02—06 和最后的搭配实例；以后遇到某个名字，用浏览器“在页面中查找”。

<a id="tools-01"></a>
## 01｜规划、资料与数值：先弄清楚要做什么

 **这一类用来记录和组织设计，不直接负责让游戏运行。** 白话说：写设定、排任务、放参考图、计算“这个数值合不合理”。

| 工具 | 主要用途 | 放到游戏开发中怎么理解 |
| --- | --- | --- |
| [Word](https://www.microsoft.com/microsoft-365/word)、[Google Docs](https://workspace.google.com/products/docs/) | 写文档、评论与修改 | 写企划、需求、剧情初稿和验收说明 |
| [Notion](https://www.notion.com/product)、[Obsidian](https://obsidian.md/) | 整理知识、关联笔记 | 把角色、世界观、调查笔记和设计决策连接起来 |
| [Excel](https://www.microsoft.com/microsoft-365/excel)、[Google Sheets](https://workspace.google.com/products/sheets/)、[LibreOffice Calc](https://www.libreoffice.org/) | 表格、公式和数据整理 | 列道具数值、算成长曲线、记录资源清单；表格不是只给财务用的 |
| [Miro](https://miro.com/)、[FigJam](https://www.figma.com/figjam/)、[draw.io／diagrams.net](https://www.drawio.com/) | 白板、流程图和关系图 | 画剧情分支、页面跳转、玩家流程 |
| [PureRef](https://www.pureref.com/) | 把参考图片摆在一块画布上 | 画蛇时，把姿态、鳞片和配色参考放在旁边 |
| [Zotero](https://www.zotero.org/) | 文献、来源和引用管理 | 记住设定来自哪篇论文，而不只存一张无出处截图 |

 **这一环节的产物通常是文档和数据。** 以后能否直接导入游戏，要看项目是否做了对应的读取或转换功能；“写在表格里”不等于游戏自动认识它。

<a id="tools-02"></a>
## 02｜通用游戏引擎：把素材和规则组织成游戏

 **游戏引擎提供一组可重复使用的基础能力。** 白话说：你不必从零研究怎么在屏幕上画图、怎么播放声音，再开始写自己的玩法。但引擎不会替你自动设计出好玩的内容。

| 引擎 | 主要定位 | 先这样认识 |
| --- | --- | --- |
| [Unity](https://unity.com/products/unity-engine) | 通用二维／三维引擎 | 把场景、角色、界面和规则放在一起；脚本主要使用 C# |
| [Unreal Engine／虚幻引擎／UE](https://www.unrealengine.com/) | 通用实时三维引擎及制作工具 | 提供场景、动画、物理等完整工具；规则可用 C++、蓝图等方式制作，不只服务于写实画面 |
| [Godot](https://godotengine.org/features/) | 通用二维／三维引擎 | 用场景和节点组织游戏；常见脚本语言是 GDScript、C# |
| [GameMaker](https://gamemaker.io/en) | 以二维制作为核心 | 有对象、房间、事件等制作方式；会遇到 GML 代码和图形化逻辑 |
| [GDevelop](https://gdevelop.io/) | 以事件系统为核心的可视化制作 | 用“满足条件 → 执行动作”组织行为，也能扩展功能 |
| [Construct](https://www.construct.net/en) | 浏览器中的游戏制作工具，偏二维 | 用事件表安排逻辑；“在浏览器里制作”不等于只能做静态网页 |
| [Clickteam Fusion](https://www.clickteam.com/clickteam-fusion-2-5) | 事件式游戏与交互应用制作 | 用可视化事件安排规则；不是后面讲的视频合成软件 Fusion |
| [Defold](https://defold.com/) | 跨平台游戏引擎 | 提供编辑器、资源处理和运行系统，脚本使用 Lua |
| [Cocos Creator](https://www.cocos.com/en/creator) | 二维／三维游戏制作 | 通过可视化编辑器和脚本组织项目；注意区分 Creator 与旧教程里的 Cocos2d-x |
| [LayaAir](https://www.layaair.com/) | 面向跨平台与网页等场景的引擎 | 国内网页、小游戏开发讨论中会遇到的另一条引擎路线 |
| [O3DE](https://o3de.org/) | 可扩展的三维引擎 | 关注模块组合、实时内容和底层扩展能力 |
| [Stride](https://www.stride3d.net/) | C#／.NET 路线的引擎 | 用另一套编辑器与引擎系统做二维、三维项目 |
| [Flax](https://flaxengine.com/) | 三维游戏引擎 | 提供编辑器、渲染和脚本工具，不是 Unity 的一个插件 |
| [Frostbite／寒霜](https://www.ea.com/frostbite)等公司自有引擎 | 针对公司项目和制作流程维护的引擎 | 认识这个类别即可：不应默认它和公开下载的通用工具一样，能直接供个人使用 |

 **大公司不等于一定自研，个人也不等于只能用“简易引擎”。** 选择应看项目需求、现有资产、人员能力、目标平台和维护成本，而不是把团队规模当成软件等级。

“蓝图”“可视化编程”“事件表”意味着部分规则可以通过节点或界面设置， **不意味着不需要逻辑** 。你仍然要想清楚条件、顺序和结果。

<a id="tools-03"></a>
## 03｜专用制作工具与创作平台：为某类作品少搭一点架子

 **这一类预先安排了某种作品特别需要的结构。** 白话说：做视觉小说时，现成的对话、选择和存档，比从空白场景开始更贴近任务。专用不等于低级，也不等于不能扩展。

| 工具／平台 | 主要用途 | 与通用引擎的区别 |
| --- | --- | --- |
| [Ren’Py](https://www.renpy.org/) | 视觉小说、对话叙事 | 提供对白、选项等机制；用专用脚本写内容，必要时用 Python 扩展 |
| [RPG Maker／RPG 制作大师](https://www.rpgmakerweb.com/products/rpg-maker-mz) | 以地图、事件、角色等系统制作 RPG | 很多内容在界面里设定；不同代产品的脚本和插件体系不应混用 |
| [TyranoScript／TyranoBuilder](https://tyranoscript.com/) | 视觉小说制作 | 前者采用脚本方式，后者提供图形化制作界面；是同一生态中的不同操作路线 |
| [Twine](https://twinery.org/) | 非线性文本和互动故事 | 把文本段落连起来，能发布成网页；复杂功能取决于选用的故事格式及扩展 |
| [GB Studio](https://www.gbstudio.dev/) | 制作 Game Boy 风格及相应平台作品 | 围绕特定显示和运行限制安排制作流程 |
| [Bitsy](https://bitsy.org/) | 小型像素探索与叙事 | 用有限的房间、角色和对白表达一个小故事 |
| [PICO-8](https://www.lexaloffle.com/pico-8.php) | “幻想主机”：人为限定规格的创作环境 | 把代码、画图、音效等装在一起，用限制帮助完成小作品 |
| [TIC-80](https://tic80.com/) | 另一套幻想电脑式制作环境 | 也是整合式小型游戏创作工具，但规格和生态不同 |
| [Roblox Studio](https://create.roblox.com/docs/studio) | 为 Roblox 平台制作体验 | 工具与平台的运行、发布规则相连；脚本会遇到 Luau |
| [UEFN](https://dev.epicgames.com/documentation/en-us/fortnite/unreal-editor-for-fortnite) | 为 Fortnite 制作内容 | 是面向特定平台的编辑器与工作流，不等于把一个独立 UE 项目随意发到所有平台 |

 **引擎、作品风格、发布平台是三件事。** 像素画面不代表用了 PICO-8；有文字选项也不代表一定用了 Ren’Py。

<a id="tools-04"></a>
## 04｜框架、图形库与代码型引擎：不一定打开一套大型编辑器

 **这里的工具主要通过代码调用。** 白话说：你可以把现成的画面、输入、声音功能接进程序，再自己组织游戏。提供范围有大有小，厂商对“库／框架／引擎”的命名也会交叉。

| 工具 | 主要职责 | 别混淆成什么 |
| --- | --- | --- |
| [Three.js](https://threejs.org/) | JavaScript 三维图形库：场景、相机、模型、灯光等 | 不是语言，也不是自带所有玩法系统的另一套 Unity |
| [Babylon.js](https://www.babylonjs.com/) | 网页三维引擎及相关工具 | 与 Three.js 处在相近技术领域，但提供的系统和工作方式不同 |
| [PlayCanvas](https://playcanvas.com/) | 网页三维引擎及在线编辑器工作流 | 不只是一个三维模型查看网站；引擎和托管编辑服务也要分开认识 |
| [Phaser](https://docs.phaser.io/phaser/getting-started/what-is-phaser) | 二维网页游戏框架 | 提供场景、输入等游戏能力，不是做模型的软件 |
| [PixiJS](https://pixijs.com/) | 高性能二维绘制与显示 | 重点是把画面高效画出来；完整玩法仍需要你组织 |
| [raylib](https://www.raylib.com/) | 用代码处理图形、输入、音频等 | 是开发库，不是一套拖拽式大型编辑器 |
| [SDL](https://www.libsdl.org/)、[SFML](https://www.sfml-dev.org/) | 跨平台窗口、输入、图形／音频等基础功能 | 提供基础部件，通常还要自己搭更多游戏结构 |
| [LÖVE](https://love2d.org/) | 用 Lua 编写二维游戏 | Lua 是语言，LÖVE 是提供游戏功能的框架 |
| [Solar2D](https://solar2d.com/) | Lua 路线的二维游戏引擎 | 通过代码使用引擎能力，是另一种跨平台制作路线 |
| [MonoGame](https://monogame.net/) | .NET 游戏框架 | 偏代码组织，不要因为名字里有 Game 就默认带完整场景编辑器 |
| [libGDX](https://libgdx.com/) | Java 路线的跨平台游戏框架 | 是框架，不是 Java 语言本身 |
| [Bevy](https://bevy.org/) | Rust 路线的游戏引擎 | 是代码驱动的一条路线；是否需要某种编辑工作流应另行确认 |
| [HaxeFlixel](https://haxeflixel.com/) | Haxe 路线的二维游戏框架 | Haxe 是语言，HaxeFlixel 提供二维游戏结构 |
| [React](https://react.dev/)、[Vue](https://vuejs.org/)、[Svelte](https://svelte.dev/) | 构建网页界面 | 可用于菜单、对话界面或工具页面，但不是专门的游戏引擎 |

例如，“React + Three.js”可以表示：一部分界面用 React 组织，三维内容交给 Three.js。这不是“同时选了两个互相打架的引擎”，而是分工；怎样连接仍需项目代码。

 **简单的网页互动甚至可以不加这些库** ，直接用 HTML、CSS 和 JavaScript。增加依赖应是因为它解决了具体问题，而不是因为软件名越多越专业。[MDN 对网页技术的说明](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/What_is_JavaScript)

<a id="tools-05"></a>
## 05｜编程语言与技术名词：规则用什么写

 **语言不是安装后就能制作整款游戏的工作台。** 白话说：语言规定写法，引擎或库提供能调用的功能，编辑器让你方便地把它们写出来。

| 名字 | 它是什么 | 在哪里可能遇到 |
| --- | --- | --- |
| [JavaScript／JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript) | 编程语言 | 网页交互、Phaser、Three.js，以及部分工具和服务器 |
| [TypeScript／TS](https://www.typescriptlang.org/) | 在 JavaScript 基础上增加类型等开发能力的语言 | “这里应该是数字，不该是文字”这类问题可更早检查；通常处理为 JavaScript 后运行 |
| [C#](https://learn.microsoft.com/en-us/dotnet/csharp/) | 编程语言，读作 C sharp | Unity，以及支持它的 Godot、Stride、MonoGame 项目 |
| [C++](https://isocpp.org/) | 编程语言 | UE、引擎底层、高性能系统和原生工具 |
| [C](https://www.iso.org/standard/82075.html) | 编程语言 | 系统与基础库、raylib 等路线；不是 C++ 的简称 |
| [GDScript](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html) | Godot 的脚本语言 | 写 Godot 游戏行为；看起来像 Python，但不是 Python |
| [GML](https://manual.gamemaker.io/monthly/en/GameMaker_Language/GameMaker_Language_Index.htm) | GameMaker Language | 编写 GameMaker 项目逻辑 |
| [Lua](https://www.lua.org/about.html) | 便于嵌入其他程序的脚本语言 | LÖVE、Defold，以及一些游戏或工具的脚本 |
| [Luau](https://luau.org/) | 从 Lua 发展来的语言 | Roblox 开发；不要把两者的所有语法和库当成完全相同 |
| [Python](https://www.python.org/about/) | 通用编程语言 | Ren’Py 扩展、Blender 自动化、批量整理资源、测试和后台工具 |
| [Rust](https://www.rust-lang.org/)、[Haxe](https://haxe.org/) | 不同的通用编程语言 | 分别会在 Bevy、HaxeFlixel 等路线中遇到 |
| [Java](https://dev.java/)、[Kotlin](https://kotlinlang.org/)、[Swift](https://www.swift.org/) | 通用及平台开发相关语言 | 游戏框架、Android／Apple 平台接入和原生应用开发 |
| [Verse](https://dev.epicgames.com/documentation/en-us/fortnite/verse-language-reference) | Epic 的编程语言 | UEFN 等相关创作环境 |
| [HTML 与 CSS](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/What_is_JavaScript) | 网页结构的标记语言与外观的样式语言 | HTML 说“有一个按钮”，CSS 说“它摆哪里、长什么样”；不是两个游戏引擎 |
| [SQL](https://www.postgresql.org/docs/current/tutorial-sql.html) | 操作关系数据库的语言 | 查询玩家记录、道具数据等；数据库软件与 SQL 是两个层次 |
| [HLSL](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl)、[GLSL](https://www.khronos.org/opengl/wiki/Core_Language_(GLSL))、[WGSL](https://www.w3.org/TR/WGSL/) | 编写着色器的语言 | 告诉图形处理器怎样计算画面中的一部分，例如颜色、光照和变形 |

再认三个经常夹在软件名里的东西：

| 名字 | 白话说明 |
| --- | --- |
| JSON、CSV、YAML、TOML | 保存数据或配置的不同格式。例如对白表、设置文件；通常不是编写整套玩法的语言 |
| Markdown／`.md` | 用简单符号写标题、链接、列表的文档格式；这份博客源文就属于这种形式 |
| WebGL、WebGPU、OpenGL、Vulkan、Direct3D、Metal | 与图形处理器打交道的接口或标准。它们不是和 Unity 并列的完整游戏编辑器；有时由引擎替你处理 |
| WebAssembly／Wasm | 一种可作为编译目标的执行格式；可让其他语言编写的程序在支持它的环境中运行。不是“三维引擎”，也不是只服务游戏 |

图形相关的关系可以这样记： **Three.js 是你使用的三维工具，WebGL／WebGPU 是它可能借助的底层接口；GLSL／WGSL 则是相关着色器写法。** 不同版本和渲染后端的支持并不完全相同。[Three.js](https://threejs.org/) · [WebGL](https://www.khronos.org/webgl/) · [WebGPU](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API)

<a id="tools-06"></a>
## 06｜代码编辑、编译与依赖：程序员的工作台和加工工具

 **这些工具负责写、检查、处理和运行代码。** 白话说：不是设计一条蛇，而是让你方便地写出“点击蛇之后发生什么”，并把这些文件处理成能执行的程序。

| 工具／类别 | 主要用途 | 白话说明 |
| --- | --- | --- |
| [VS Code](https://code.visualstudio.com/docs) | 代码编辑器 | 写代码、找文件、装扩展；它不是 Visual Studio 的简称 |
| [Visual Studio](https://visualstudio.microsoft.com/)、[Rider](https://www.jetbrains.com/rider/) | 集成开发环境，简称 IDE | 把写代码、运行、检查错误等工作集中起来 |
| [Xcode](https://developer.apple.com/xcode/)、[Android Studio](https://developer.android.com/studio) | 平台开发工具 | 处理 Apple／Android 应用的开发、构建和调试；即使用其他引擎，也可能在导出时遇到 |
| 浏览器、[Node.js](https://nodejs.org/en/about)、[.NET](https://dotnet.microsoft.com/learn/dotnet/what-is-dotnet) | 不同的运行环境或开发平台 | 代码必须在能执行它的环境里工作；Node.js 让 JS 能在浏览器之外运行 |
| [npm](https://docs.npmjs.com/about-npm/)、[pnpm](https://pnpm.io/)、[Yarn](https://yarnpkg.com/) | JavaScript 生态的包管理工具 | 帮你安装和管理项目依赖；同类选择，不是每个都要装 |
| [pip](https://pip.pypa.io/en/stable/)、[NuGet](https://learn.microsoft.com/en-us/nuget/what-is-nuget)、[Cargo](https://doc.rust-lang.org/cargo/) | 其他语言生态的包／项目工具 | 分别会在 Python、.NET、Rust 路线里遇到 |
| [Vite](https://vite.dev/guide/)、[webpack](https://webpack.js.org/) | 网页开发与构建工具 | 开发时预览，发布前整理程序和资源；不是网页游戏引擎 |
| [GCC](https://gcc.gnu.org/)、[Clang](https://clang.llvm.org/)、[MSVC](https://learn.microsoft.com/en-us/cpp/overview/visual-cpp-in-visual-studio) | 编译工具 | 把相应语言写成的源代码转换为后续可链接、执行的程序形式 |
| [CMake](https://cmake.org/)、[Gradle](https://gradle.org/)、[MSBuild](https://learn.microsoft.com/en-us/visualstudio/msbuild/msbuild) | 组织软件构建 | 安排哪些文件怎样编译、依赖什么、按什么顺序处理 |
| [Emscripten](https://emscripten.org/docs/introducing_emscripten/about_emscripten.html) | 面向网页等目标的编译工具链 | 可把 C／C++ 项目编译到 WebAssembly 等目标；并不保证所有桌面功能原样搬到网页 |
| 终端、PowerShell、Bash 等命令行工具 | 输入和执行命令 | 不是神秘的黑色编程语言窗口；只是另一种操作电脑的方式 |

“ **依赖** ”就是项目借用了哪些外部程序包。“ **构建／Build** ”就是按规定处理代码与资源，生成可运行或可交付结果。编辑器里的“运行”按钮，有时已经替你调用了其中好几样工具。

 **通常先确定路线，再安装它需要的工具。** 只做一个普通 JS 页面，没有必要先把所有语言的编译器装齐。

<a id="tools-07"></a>
## 07｜二维绘图与像素画：做立绘、背景、图标

 **二维绘图软件制作的是平面图像。** 白话说：把角色、背景、按钮和道具画出来；它们不会仅仅因为画好了，就自动具有游戏行为。

| 工具 | 主要用途 | 先这样区分 |
| --- | --- | --- |
| [Photoshop／PS](https://www.adobe.com/products/photoshop.html) | 图像编辑、绘画、合成 | 修图、背景、贴图、界面素材等；不是只能处理照片 |
| [Clip Studio Paint／CSP](https://www.clipstudio.net/en/) | 插画、漫画和二维动画 | 角色立绘、线稿、表情差分等 |
| [Krita](https://krita.org/en/)、[GIMP](https://www.gimp.org/) | 绘画和图像编辑 | 前者突出数字绘画，后者是综合图像编辑；用途有交叉 |
| [Procreate](https://procreate.com/procreate) | 平板绘画 | 在 iPad 上绘制角色与场景，再导出资源 |
| [Illustrator／AI](https://www.adobe.com/products/illustrator.html)、[Inkscape](https://inkscape.org/) | 矢量绘图 | 用曲线和形状画标志、图标等；这里的 AI 是 Illustrator 的简称，不是生成式 AI |
| [Affinity](https://www.affinity.studio/) | 矢量、像素图像与版面设计 | 当前统一应用整合这些工作；旧教程中的 Designer、Photo、Publisher 是此前分别命名的应用 |
| [Aseprite](https://www.aseprite.org/) | 像素绘图和逐帧动画 | 一格一格地画像素角色、道具和动作 |
| [LibreSprite](https://libresprite.github.io/)、[Piskel](https://www.piskelapp.com/)、[Pixelorama](https://orama-interactive.itch.io/pixelorama) | 其他像素绘图与动画工具 | 是同一工作类别的不同选择，不需要全部会用 |

 **DCC，数字内容创作工具** ，是绘图、建模、动画等软件的一个总称，不是另一个必须下载的软件。

 **位图** 可以先理解成由小色块组成的图片； **矢量图** 记录的是曲线和形状。放大、编辑和导出方式不同，但不必因此把游戏画面分成“高低级”。

“ **差分** ”就是同一角色的不同版本，例如闭眼、微笑、换衣服。“ **逐帧动画** ”是连续播放一张张画面。画出三种表情，与让游戏根据对白切换表情，是两个环节。

<a id="tools-08"></a>
## 08｜三维建模与雕刻：制作物体的立体形状

 **建模是建立三维形状，雕刻则像捏黏土一样推拉表面。** 白话说：先做出一条能从不同角度看的蛇，再决定给它什么颜色、动作和灯光。

| 工具 | 主要用途 | 放到游戏开发中怎么理解 |
| --- | --- | --- |
| [Blender](https://www.blender.org/) | 建模、雕刻、动画、渲染等综合三维制作 | 一套工具能覆盖多种资源制作任务，不只是“做模型” |
| [Maya](https://www.autodesk.com/products/maya/overview) | 三维建模、绑定、动画和特效制作 | 可制作角色、动作，也可通过脚本融入团队流程 |
| [3ds Max](https://www.autodesk.com/products/3ds-max/overview) | 三维建模、动画和渲染 | 另一套综合三维制作工作台 |
| [Cinema 4D](https://www.maxon.net/en/cinema-4d) | 三维设计、动画和动态图形 | 可用于资源、视觉演示与宣传内容，不等于运行游戏的引擎 |
| [ZBrush](https://www.maxon.net/en/zbrush)、[Nomad Sculpt](https://nomadsculpt.com/) | 数字雕刻 | 做皮肤、褶皱等形体细节；高细节模型未必适合直接放进游戏 |
| [3DCoat](https://3dcoat.com/) | 雕刻、拓扑、贴图等 | 既处理形体，也处理把形体整理为可用资源的步骤 |
| [Blockbench](https://blockbench.net/) | 低多边形和方块风格建模、贴图、动画 | 适合认识由简单形体构成的角色与物件制作 |
| [MagicaVoxel](https://ephtracy.github.io/) | 体素建模 | 像堆立体小方块；“体素”可先理解成三维空间中的小格子 |

经常一起出现的三个词： **网格／Mesh** 是由点、边、面组成的模型结构； **拓扑** 是这些点和面怎么连接； **重拓扑** 是重新整理这张“网”，例如让雕刻模型更适合变形或运行。

 **三维软件不是三维游戏的证明。** 你可以在 Blender 中做立体场景，最后只导出图片；游戏端仍然播放二维图像。这正是《体温调节》讨论过的一种制作思路，而不是要求额外加入一个实时三维引擎。

<a id="tools-09"></a>
## 09｜贴图、材质、UV 与烘焙：让模型不再像灰色石膏

先把几个词翻成人话： **贴图** 是给表面提供颜色、粗糙程度等信息的图像； **材质** 规定表面怎样表现； **UV** 像把物体表皮摊开，告诉软件图片应该贴到哪里； **烘焙** 是把某些计算结果提前存下来，供后续使用，而不是每次都重新计算。

| 工具 | 主要用途 | 白话说明 |
| --- | --- | --- |
| [Substance 3D Painter](https://www.adobe.com/products/substance3d/apps/painter.html) | 在三维模型上绘制与制作贴图 | 像直接给模型上色、做磨损，再导出引擎要用的贴图 |
| [Substance 3D Designer](https://www.adobe.com/products/substance3d/apps/designer.html) | 用节点和参数构建材质 | 不是逐笔画每个裂缝，而是搭规则生成可调整的表面 |
| [Substance 3D Sampler](https://www.adobe.com/products/substance3d/apps/sampler.html) | 从图像等输入制作材质 | 把素材处理为可用于三维表面的资源 |
| [ArmorPaint](https://armorpaint.org/)、[Mari](https://www.foundry.com/products/mari) | 三维贴图绘制 | 与 Painter 同属模型表面制作方向，流程和侧重点不同 |
| [Material Maker](https://www.materialmaker.org/) | 节点式材质生成 | 搭积木般组合图像处理与生成规则 |
| [RizomUV](https://www.rizomuv.com/) | UV 展开与排布 | 把模型表皮摊开，并合理安排到图片空间里 |
| [Marmoset Toolbag](https://marmoset.co/) | 模型展示、渲染、烘焙与材质相关工作 | 检查模型效果，也可把细节计算结果输出为资源 |

 **节点** 就是一个代表操作或数据的小方块；连接节点表示数据或执行顺序怎样流动。材质节点、动画节点和蓝图都可能长得像“连线图”，但处理的对象不同。

例如，高细节雕刻模型可以把一部分表面细节烘焙到低面数模型的贴图里。 **不是让模型真正拥有全部几何细节，而是用更合适的方式表现其中一部分。**

<a id="tools-10"></a>
## 10｜场景、地形与关卡：安排“在哪里玩”

 **场景制作偏向环境内容，关卡设计还要安排路线、障碍、触发点和节奏。** 白话说：不只画一片森林，还要决定玩家从哪走、在哪里遇到什么。

| 工具 | 主要用途 | 它交出的是什么 |
| --- | --- | --- |
| 引擎自带场景／关卡编辑器 | 摆放物体、灯光、触发器和玩法对象 | 可以直接与项目规则连接的场景内容 |
| [Houdini](https://www.sidefx.com/products/houdini/) | 程序化三维制作 | 用规则生成或处理建筑、地形等资源；“程序化”不等于生成式 AI |
| [Gaea](https://quadspinner.com/)、[World Machine](https://www.world-machine.com/)、[World Creator](https://www.world-creator.com/en/index.phtml) | 地形制作 | 山脉形状、地形高度图及相关表面信息 |
| [SpeedTree](https://unity.com/products/speedtree) | 树木与植被制作 | 树木模型及相关资源；不是整片游戏世界的完整引擎 |
| [Tiled](https://www.mapeditor.org/) | 二维瓦片与对象地图编辑 | 地图图块、对象位置等数据，游戏程序再读取它们 |
| [LDtk](https://ldtk.io/) | 二维关卡编辑 | 地图、实体和字段等数据，需通过相应方式接入游戏 |
| [TrenchBroom](https://trenchbroom.github.io/) | 面向 Quake 系等工作流的关卡编辑 | 特定格式的三维关卡，不是通用模型雕刻软件 |

 **瓦片／Tile** 就是反复拼接的小图块； **高度图** 可以理解为用图片中的数值记录地面高低； **触发器** 是“进入某处或满足条件，就执行动作”的安排。

做了一张 Tiled 地图，还需要游戏知道地图怎样显示、哪些地方不能走。 **地图编辑器负责制作地图数据，不会自动替所有游戏完成玩法。**

<a id="tools-11"></a>
## 11｜角色、绑定、动画与动作捕捉：让它动起来

 **绑定／Rigging** 是给角色安装控制结构； **骨骼动画** 通过控制骨架带动形体； **动作捕捉／Mocap** 记录真实动作，再用于数字角色。白话说：做形状、装控制器、编排动作，是相连但不同的工作。

| 工具 | 主要用途 | 先这样认识 |
| --- | --- | --- |
| [Live2D Cubism](https://www.live2d.com/en/cubism/about/) | 把二维绘图制作成可变形、可控制的角色 | 能做转头、眨眼等表现；并不是把原图自动变成真正的三维模型 |
| [Spine](https://esotericsoftware.com/) | 二维骨骼动画 | 把头、手臂等图片部件交给骨架控制，并制作动画 |
| [Rive](https://rive.app/) | 可交互的动画与界面 | 不只播放一段固定动画，也可根据状态和输入切换表现 |
| [Moho](https://moho.lostmarble.com/)、[Toon Boom Harmony](https://www.toonboom.com/products/harmony)、[OpenToonz](https://opentoonz.github.io/e/) | 二维动画制作 | 制作逐帧或绑定类动画；导入游戏的方式要另行安排 |
| Blender、Maya、[Cascadeur](https://cascadeur.com/) | 三维角色动作制作 | 摆关键姿势、调动作和身体运动；Cascadeur 侧重角色动画辅助 |
| [Character Creator](https://www.reallusion.com/character-creator/)、[VRoid Studio](https://vroid.com/en/studio)、[MetaHuman](https://www.metahuman.com/) | 数字角色制作 | 分别提供不同风格和流程的角色工具；导出、授权、运行成本应按具体产品确认 |
| [iClone](https://www.reallusion.com/iclone/) | 实时角色动画与场景演出 | 安排人物表演、动作和镜头，再按项目路线输出 |
| [Marvelous Designer](https://www.marvelousdesigner.com/) | 三维服装设计与布料模拟 | 做衣服及褶皱；游戏中怎样实时显示和运动是后续问题 |
| [Mixamo](https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html) | 人形角色自动绑定和动作资源 | 主要针对双足人形，不应默认能给蛇或任意动物自动绑定 |
| [Rokoko Studio](https://www.rokoko.com/products/studio)、[Vicon Shogun](https://www.vicon.com/software/shogun/)、[OptiTrack Motive](https://www.optitrack.com/software/motive) | 捕捉、处理与输出动作数据 | 常与特定设备和拍摄流程配合；不能把软件和硬件系统混为一谈 |

 **关键帧** 是你指定的重要时间点和姿势；软件可以计算中间变化。 **重定向／Retargeting** 是把一套动作映射给另一个骨架，骨架比例和命名不同可能需要调整。

以 Live2D 为例： **Cubism Editor 制作角色，Cubism SDK 等运行组件负责让它在游戏里被控制。** 买了制作软件、导出了资源，与目标项目能否正确播放，是不同问题；相关授权也应分别查看。[Live2D 官方说明](https://www.live2d.com/en/cubism/about/)

<a id="tools-12"></a>
## 12｜扫描、渲染与特效：把资源变成最终画面

 **渲染** 就是根据形状、材质、灯光和相机计算画面。白话说：模型像舞台上的物件，渲染负责计算“从这个位置拍出来是什么样”。 **实时渲染** 要跟得上玩家操作； **离线渲染** 可以先花时间算好，再把成品图像或视频交出去。

| 工具／模块 | 主要用途 | 白话说明 |
| --- | --- | --- |
| [RealityScan](https://www.realityscan.com/uses) | 从照片等输入重建三维资源 | 旧资料中的 RealityCapture 已更名；另有 RealityScan Mobile，不要混淆桌面与手机产品 |
| [Agisoft Metashape](https://www.agisoft.com/)、[Meshroom／AliceVision](https://alicevision.org/) | 摄影测量与三维重建 | 根据多个角度的照片计算物体形状；成品往往仍需清理、减面、贴图处理 |
| [Cycles](https://docs.blender.org/manual/en/latest/render/cycles/index.html)、[Eevee](https://docs.blender.org/manual/en/latest/render/eevee/index.html) | Blender 的不同渲染系统 | 同一制作软件里可以有不同的画面计算路线；不是两个另做玩法的引擎 |
| [Arnold](https://www.autodesk.com/products/arnold/overview)、[V-Ray](https://www.chaos.com/vray)、[Redshift](https://www.maxon.net/en/redshift) | 三维渲染工具 | 可用于资源效果、预渲染画面和宣传内容；不应默认会直接成为游戏运行时 |
| [Niagara](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine)、[Unity Visual Effect Graph](https://unity.com/features/visual-effect-graph) | 引擎中的视觉特效制作 | 做火花、烟雾、能量等动态表现；分别属于对应引擎工具体系 |
| [Effekseer](https://effekseer.github.io/en/)、[PopcornFX](https://www.popcornfx.com/) | 特效制作及运行集成 | 在专门工具里做效果，再通过对应运行组件接入项目 |

 **粒子系统** 可以先理解为管理许多小元素的生成和运动，例如火星、雨点、烟尘。不是所有特效都是粒子，也不是每个粒子都必须是一颗真实立体小球。

<a id="tools-13"></a>
## 13｜录音、作曲、音效与交互音频：制作声音，安排声音

 **DAW，数字音频工作站** 是录音、编曲、剪辑、混音的综合工作台。白话说：把对白、乐器和音效放在不同轨道上制作。 **音频中间件** 则进一步处理游戏运行时“何时响、怎样变化”。

| 工具 | 主要用途 | 先这样区分 |
| --- | --- | --- |
| [Audacity](https://www.audacityteam.org/)、[Adobe Audition](https://www.adobe.com/products/audition.html) | 录音、剪辑、修复和音频处理 | 剪掉多余声音、处理对白、整理音效 |
| [REAPER](https://www.reaper.fm/)、[Pro Tools](https://www.avid.com/pro-tools)、[Cubase](https://www.steinberg.net/cubase/)、[Nuendo](https://www.steinberg.net/nuendo/) | 综合音频制作 | 多轨录音、音乐与声音设计；功能和流程各有侧重 |
| [Logic Pro](https://www.apple.com/logic-pro/)、[Ableton Live](https://www.ableton.com/en/live/)、[FL Studio](https://www.image-line.com/fl-studio) | 编曲、音乐制作与音频处理 | 写背景音乐、组织乐器与节奏，不是专门的游戏引擎 |
| [Ardour](https://ardour.org/) | 多轨音频工作站 | 同一工作类别的另一条路线 |
| [ChipTone](https://sfbgames.itch.io/chiptone)、[FamiStudio](https://famistudio.org/) | 合成复古音效、芯片音乐制作 | 前者偏短音效生成，后者偏特定复古音源风格的音乐 |
| [Soundly](https://getsoundly.com/) | 音效检索、管理和相关制作工作 | 帮你从大量声音中找到需要的素材 |
| [FMOD Studio](https://www.fmod.com/studio)、[Wwise](https://www.audiokinetic.com/en/) | 交互音频制作与中间件 | 根据场景、距离、状态等控制声音；不是只把 MP3 播放出来 |

举一个设计例子： **REAPER 制作三层背景音乐；FMOD 或 Wwise 根据战斗紧张度控制哪些层加入；游戏程序把紧张度告诉音频系统。** 不是三个软件在重复干同一件事。

对一个只有背景音乐和几种点击音效的小作品，引擎自带音频功能也可能足够。专门中间件是按复杂度增加的选择，不是“做游戏必须有”。

<a id="tools-14"></a>
## 14｜对白与分支叙事：不是所有文字都直接写死在程序里

 **交互叙事工具管理的是文字、选择、条件和状态之间的关系。** 白话说：不只写台词，还要写“玩家做过什么，才会听到这句”。

| 工具 | 主要用途 | 先这样认识 |
| --- | --- | --- |
| [Twine](https://twinery.org/) | 把故事段落连接成可选择的结构 | 可以直接制作网页互动故事，也适合检查分支关系 |
| [ink／Inky](https://www.inklestudios.com/ink/) | ink 是叙事脚本语言；Inky 是相应编辑器 | 把文本、选择和逻辑一起编写，再直接测试或接入游戏 |
| [Yarn Spinner](https://www.yarnspinner.dev/) | 对话编写与运行集成 | 管理对白、选择和程序调用，不等于游戏所有画面与操作都由它负责 |
| [articy:draft](https://www.articy.com/en/) | 可视化叙事、流程与内容数据设计 | 把角色、分支和条件组织起来，再导出或接入项目 |

 **Ren’Py 和 ink 不是同一层级的替代品。** Ren’Py 提供视觉小说制作与运行系统；ink 重点提供叙事语言及相关工具。选择谁，应看你需要一套完整作品框架，还是只需要其中的叙事部分。

“脚本”也可能有两种意思：编剧说的是剧情文本，程序员说的可能是行为代码。讨论需求时，直接说“剧情脚本”或“程序脚本”，更不容易误会。

<a id="tools-15"></a>
## 15｜界面、字体与本地化：让人看懂，也用得顺

 **UI 是界面，UX 是使用体验；本地化是让内容适合目标语言与地区。** 白话说：按钮放哪里、文字能否读清、翻译后会不会挤出对话框，都属于这一环节。

| 工具／模块 | 主要用途 | 白话说明 |
| --- | --- | --- |
| [Figma](https://www.figma.com/)、[Penpot](https://penpot.app/) | 界面设计与交互原型 | 先设计菜单、对话框和页面流转；画得能点的原型不自动等于游戏代码 |
| 引擎自带 UI 系统，例如 [Unity UI Toolkit](https://docs.unity3d.com/Manual/UIElements.html)、[Unreal UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/umg-ui-designer-for-unreal-engine) | 制作游戏实际运行的界面 | 把视觉设计变成能响应玩家操作的控件 |
| [FontForge](https://fontforge.org/en-US/)、[Glyphs](https://glyphsapp.com/)、[FontLab](https://www.fontlab.com/) | 字体制作与编辑 | 设计字形、字距等；使用字体文件也有单独授权问题 |
| [Crowdin](https://crowdin.com/)、[Weblate](https://weblate.org/en/) | 管理多语言翻译流程 | 把同一句文字的不同语言版本、翻译进度和上下文放在一起 |
| [Poedit](https://poedit.com/)、[OmegaT](https://www.omegat.org/) | 翻译文件编辑与辅助翻译 | 利用术语、历史译文等帮助翻译；不是游戏引擎 |

 **本地化不只是把中文替换为英文。** 还要检查换行、字体缺字、日期和数字格式，以及选项文字变长后的布局。工具能协助管理，最后仍要在游戏里查看结果。

<a id="tools-16"></a>
## 16｜版本管理：记住改了什么，必要时能退回去

 **版本管理记录文件的变动与历史。** 白话说：别只留下“最终版、最终版2、真的最终版”，而要知道谁改了哪里，并能找回之前的版本。

| 工具／平台 | 主要用途 | 不要混成一件事 |
| --- | --- | --- |
| [Git](https://git-scm.com/about) | 版本控制 | 记录代码和文件历史；不需要把 Git 本身理解成网站 |
| [Git LFS](https://git-lfs.com/) | Git 的大文件扩展 | 让模型、音频等大资源采用专门的存储方式；不是不限容量的免费网盘 |
| [GitHub](https://github.com/features)、[GitLab](https://about.gitlab.com/platform/)、[Bitbucket](https://bitbucket.org/product) | 托管仓库、协作与审查等 | 围绕版本管理提供网上协作；并不是 Git 的三个版本 |
| [GitHub Desktop](https://desktop.github.com/)、[Sourcetree](https://www.sourcetreeapp.com/) | Git 图形客户端 | 用按钮和图形操作版本历史，少敲一些命令 |
| [Perforce P4](https://www.perforce.com/products/p4) | 源码与数字资源版本管理 | 适用于需要管理大量代码、二进制资源和权限的流程；旧资料常见 Helix Core 名称 |
| [Unity Version Control](https://docs.unity.com/en-us/unity-version-control) | 面向代码与内容的版本管理 | 旧资料常见 Plastic SCM 名称；不要与引擎运行时混淆 |
| [Subversion／SVN](https://subversion.apache.org/) | 集中式版本管理 | 在旧项目或既有团队流程中可能遇到的另一套系统 |

 **仓库／Repository** 是项目文件及其版本历史； **提交／Commit** 是一笔保存的修改记录； **分支／Branch** 让某条修改路线暂时与其他工作分开； **合并／Merge** 把变动整合回来。

代码文本常能逐行比较，但模型、音频等文件不一定适合自动合并。 **文件锁定** 的意思是先约定某份资源由谁编辑，减少多人同时改坏的机会。是否采用锁定，取决于文件格式和协作工具，不是所有东西都应锁住。

 **版本管理也不等于完整备份方案。** 仍应确认原始素材、大文件存储和重要凭据是否有独立、安全的备份。

<a id="tools-17"></a>
## 17｜任务、审片与制作追踪：让多人接得上工作

 **这一类管理的是谁做什么、做到哪一步、哪份内容已被批准。** 白话说：模型师交出的角色，动画师应该接哪一版？谁负责检查？哪里还欠修改？

| 工具 | 主要用途 | 先这样认识 |
| --- | --- | --- |
| [Jira](https://www.atlassian.com/software/jira)、[Trello](https://trello.com/)、[GitHub Projects](https://github.com/features) | 任务、问题和进度管理 | 把工作拆成条目，安排负责人和状态；不是自动完成工作 |
| [Codecks](https://www.codecks.io/) | 面向游戏团队的项目管理 | 用卡片等方式组织开发任务与反馈 |
| [Flow Production Tracking](https://www.autodesk.com/products/flow-production-tracking/overview) | 资源、镜头、任务和审阅流程管理 | 旧称 ShotGrid，更早也见 Shotgun；不是三维建模软件 |
| [ftrack](https://www.ftrack.com/en/)、[Kitsu](https://www.cg-wire.com/kitsu/) | 创意制作的追踪与审阅 | 把制作进度、版本和反馈关联起来 |
| [AYON](https://docs.ayon.dev/) | 跨制作软件的管线组织与集成 | 协调资源怎样从一个工具进入下一个工具；不是又一套画图软件 |
| [Slack](https://slack.com/)、[Microsoft Teams](https://www.microsoft.com/microsoft-teams/group-chat-software)、[Discord](https://discord.com/) | 沟通、会议和协作频道 | 用来讨论和联络；关键决定仍应落回可查的任务或文档 |

个人项目可以把这些工作合并到一个简单看板。大型项目可能把资源审阅、任务管理和工具集成拆开。 **增加软件的理由应是解决交接问题，而不是模仿大公司的软件数量。**

<a id="tools-18"></a>
## 18｜调试、测试与性能分析：为什么出错，为什么卡

 **调试** 是找出错误原因； **测试** 是检查是否符合要求； **性能分析／Profiling** 是测量时间、内存等花在哪里。白话说：“能打开”“没发现报错”“运行流畅”，是三种不同结论。

| 工具／类别 | 主要用途 | 白话说明 |
| --- | --- | --- |
| [浏览器开发者工具／DevTools](https://developer.chrome.com/docs/devtools) | 看报错、网络请求、页面和性能 | 网页游戏图片没加载、按钮没反应时，查看实际发生了什么 |
| [Unity Profiler](https://docs.unity3d.com/Manual/Profiler.html)、[Unreal Insights](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine) | 引擎性能分析 | 看哪些程序步骤花时间、占内存，不要只凭感觉优化 |
| [RenderDoc](https://github.com/baldurk/renderdoc)、[PIX](https://devblogs.microsoft.com/pix/)、[Nsight Graphics](https://developer.nvidia.com/nsight-graphics) | 图形调试和分析 | 检查一帧画面如何绘制；支持的系统、接口和硬件各有不同 |
| Xcode／Android Studio 中的性能与调试工具 | 移动平台分析 | 检查手机上的程序、内存等情况，不能只看电脑预览 |
| [Jest](https://jestjs.io/)、[Vitest](https://vitest.dev/)、[pytest](https://docs.pytest.org/)、[NUnit](https://nunit.org/) | 自动化代码测试 | 自动验证一小段规则是否仍符合预期；分别对应不同技术生态 |
| [Playwright](https://playwright.dev/)、[Appium](https://appium.io/) | 模拟操作的自动化测试 | 前者主要控制浏览器，后者用于应用自动化等场景；不等于真人试玩 |
| [BrowserStack](https://www.browserstack.com/) | 浏览器和设备测试服务 | 提供不同环境进行测试；设备覆盖与具体服务范围要看所选方案 |
| [NVDA](https://www.nvaccess.org/about-nvda/)、[VoiceOver](https://www.apple.com/accessibility/vision/)、[TalkBack](https://support.google.com/accessibility/android/answer/6283677) | 屏幕阅读器 | 辅助检查界面能否被读取；不能只安装读屏软件就声称游戏已无障碍 |

 **日志／Log** 像程序留下的工作记录； **断点／Breakpoint** 让程序暂时停在指定位置，便于查看当时的值。它们是查原因的手段，不是只要删除报错文字就修好了问题。

自动化测试擅长重复执行已定义的检查，试玩则能发现“读不懂”“节奏不对”“操作不舒服”。 **工具通过检查，不等于游戏已经好玩或全面兼容。**

<a id="tools-19"></a>
## 19｜物理、寻路与其他中间件：只接入一块专门能力

 **物理引擎主要处理运动、碰撞等模拟；寻路系统帮助对象找到路线。** 白话说：箱子会不会掉下去、角色怎样绕开墙，可以由专门技术处理，不必每个项目从数学细节重写。

| 工具／技术 | 主要用途 | 它不等于什么 |
| --- | --- | --- |
| [Box2D](https://box2d.org/) | 二维刚体物理 | 不是完整二维游戏编辑器 |
| [Jolt Physics](https://jrouwe.github.io/JoltPhysics/)、[Bullet](https://pybullet.org/wordpress/) | 三维物理等模拟 | 不负责你的剧情、界面和全部游戏系统 |
| [PhysX](https://developer.nvidia.com/physx-sdk) | 物理模拟 SDK | 不是必须单独再买一套画面渲染软件 |
| [Rapier](https://rapier.rs/) | 二维／三维物理 | 可以作为其他程序的一部分接入，不替代整套游戏结构 |
| [Havok](https://www.havok.com/) | 物理、导航、布料等中间件产品 | 是一组专门能力，不是所有项目都必须采购的标准配置 |
| [Recast／Detour](https://recastnav.com/) | 导航网格生成与寻路 | 帮角色知道哪些地方可走、怎样找路；不等于具有完整“智能” |
| [Bink、Oodle](https://www.radgametools.com/) | 视频播放、数据压缩等中间件 | 解决游戏中的特定运行和资源处理问题 |

引擎可能已经集成其中某种技术，或自带其他实现。 **看到某游戏同时提到 UE 和某个物理系统，并不一定是用了两个完整游戏引擎。**

另外，游戏开发里说的“AI”也可能只是角色决策、行为树或寻路， **不一定是聊天大模型或生成式 AI** 。

<a id="tools-20"></a>
## 20｜联机、服务器与数据库：多个人怎样进入同一个世界

 **客户端** 是玩家设备上运行的部分； **服务器** 是提供远端功能的程序或机器； **数据库** 负责有组织地保存与查询数据。白话说：玩家手机显示画面，远端可能协调房间、保存账号、判定结果。

| 工具／服务 | 主要用途 | 先这样区分 |
| --- | --- | --- |
| [Photon Fusion／Quantum](https://www.photonengine.com/fusion) | 多人游戏的网络与同步技术 | 帮不同设备协调游戏状态；产品采用的同步方式不同 |
| [Mirror](https://mirror-networking.com/)、[FishNet](https://fish-networking.gitbook.io/docs) | Unity 多人网络框架 | 为项目增加网络层，不会自动解决全部账号和运营需求 |
| [Colyseus](https://colyseus.io/) | 多人游戏服务器框架 | 组织房间和状态同步等；需要与客户端配合 |
| [Nakama](https://heroiclabs.com/nakama/) | 游戏后台与多人社交功能 | 提供账号、社交、排行榜、多人等相关能力 |
| [PlayFab](https://learn.microsoft.com/en-us/xbox/playfab/get-started/what-is-playfab)、[Unity Gaming Services](https://unity.com/solutions/gaming-services) | 游戏在线服务 | 按产品选用账号、数据、联机、运营等服务；不是一个必须全部接入的大包 |
| [Epic Online Services／EOS](https://onlineservices.epicgames.com/)、[Steamworks](https://partner.steamgames.com/doc/home) | 平台与在线功能的接口、工具或服务 | 可能涉及好友、成就、联机等；EOS 不等于 UE，Steamworks 不等于 Steam 商店客户端 |
| [Firebase](https://firebase.google.com/products-build)、[Supabase](https://supabase.com/) | 通用应用后台服务 | 可用来做认证、存储、数据库等，但不是完整游戏引擎 |
| [SQLite](https://www.sqlite.org/about.html) | 可嵌入程序的数据库 | 能用于本地数据；使用数据库不代表一定要开远程服务器 |
| [PostgreSQL](https://www.postgresql.org/about/)、[Redis](https://redis.io/) | 数据库／数据存储系统 | 前者是关系数据库，后者常用于快速数据访问等任务；职责不能简单互换 |
| [Docker](https://www.docker.com/resources/what-container/) | 容器化运行环境 | 把程序及运行所需环境按规则打包，减少“换台机器就坏了” |
| [Kubernetes](https://kubernetes.io/docs/concepts/overview/) | 管理容器化应用 | 当有许多程序实例时，协调它们运行；不是小型单机游戏的必需品 |
| [Amazon GameLift Servers](https://aws.amazon.com/gamelift/servers/)、[Agones](https://agones.dev/) | 游戏服务器托管或编排 | 前者提供托管服务路线，后者帮助在 Kubernetes 上管理专用游戏服务器 |

 **“游戏在网页上”不代表“必须有账号后台”。** 一个纯单机网页游戏可以由浏览器运行规则，把进度保存在本地；提供网页文件的托管服务，与负责账号或对战的应用服务器，是不同职责。

“ **网络同步** ”也不是把两个玩家的屏幕视频互相发送，而通常是交换输入、位置、状态等数据。具体由谁判定结果，需要按玩法设计，不能因为接入了某个库就省略这一步。

<a id="tools-21"></a>
## 21｜自动构建、打包与发布：交给玩家的到底是哪一份

 **构建** 处理项目文件， **打包** 整理可交付内容， **部署／发布** 把它放到目标设备或服务上。白话说：你电脑里能玩的开发项目，需要变成别人也能正确打开的成品。

| 工具／平台 | 主要用途 | 白话说明 |
| --- | --- | --- |
| 引擎自带导出工具，以及 Xcode、Android Studio 等 | 生成目标平台程序 | 生成网页文件、桌面程序或移动平台工程／应用等 |
| [GitHub Actions](https://github.com/features/actions)、[GitLab CI/CD](https://docs.gitlab.com/ci/)、[Jenkins](https://www.jenkins.io/)、[TeamCity](https://www.jetbrains.com/teamcity/) | 自动执行构建、测试和发布流程 | 提交修改后，让机器按既定步骤检查和产出版本；这类流程常称 CI/CD |
| [Electron](https://www.electronjs.org/)、[Tauri](https://tauri.app/) | 使用网页界面等技术制作应用 | 可作为网页项目的桌面应用路线；不是把网页改名为 `.exe` |
| [Capacitor](https://capacitorjs.com/) | 网页技术与移动应用平台之间的桥接 | 在原生应用环境中使用网页内容并接入设备能力 |
| [Steamworks](https://partner.steamgames.com/doc/home) | Steam 开发者工具、构建分发与平台接入 | 管理上架、测试版本及相关功能，不是用来画角色的 |
| [itch.io](https://itch.io/docs/creators/) | 发布网页或可下载作品等 | 给作品一个页面，并管理文件；也可结合 butler 上传工具 |
| [App Store Connect](https://developer.apple.com/app-store-connect/)、[TestFlight](https://developer.apple.com/testflight/) | Apple 平台发布管理与测试分发 | TestFlight 主要用于测试，不是正式 App Store 上架的同义词 |
| [Google Play Console](https://play.google.com/console/about/) | Android 商店发布与管理 | 管理应用、测试轨道和发布等工作 |
| [微信开发者工具](https://developers.weixin.qq.com/minigame/dev/devtools/download.html)、[抖音开发者工具](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/developer-instrument/development-assistant) | 对应平台的小游戏开发与调试 | 平台容器、接口和发布要求各有差异，不是把任意网页直接上传就一定能运行 |
| [GitHub Pages](https://pages.github.com/)、[Cloudflare Pages](https://developers.cloudflare.com/pages/)、[Netlify](https://www.netlify.com/)、[Vercel](https://vercel.com/) | 网站托管与部署 | 可承载相应网页项目；后端能力和限制按具体服务区分 |

 **“支持导出某平台”不等于“保证直接通过该平台发布要求”。** 还要核对开发者资格、所需 SDK、性能、输入、签名及审核等事项；主机平台尤其不能仅凭引擎下载页就推断全部开发条件。

CI/CD 可先理解为“让固定检查与交付步骤自动执行”。是否自动发布到正式环境，是团队配置决定的，不是打开自动化工具就必须直接上线。

<a id="tools-22"></a>
## 22｜崩溃、数据与玩家反馈：上线之后仍然要维护

 **监控关注运行状况，分析关注使用数据，社区与客服承接反馈。** 白话说：出错时能知道，玩家卡在哪里能调查，而不是发布以后只看评论猜原因。

| 工具／服务 | 主要用途 | 白话说明 |
| --- | --- | --- |
| [Sentry](https://sentry.io/) | 错误、崩溃与性能观测 | 接入后收集相应问题信息；不是自动修好每个错误 |
| [GameAnalytics](https://www.gameanalytics.com/) | 游戏行为与运营数据分析 | 统计定义好的事件，帮助观察玩家流程和变化 |
| [Firebase Crashlytics](https://firebase.google.com/products/crashlytics) | 应用崩溃报告 | 聚合崩溃，辅助定位受影响版本和问题 |
| [Prometheus](https://prometheus.io/)、[Grafana](https://grafana.com/grafana/) | 指标采集与可视化 | 观察服务器负载、错误率等运行指标，而不是制作游戏画面 |
| [Discord](https://discord.com/)、[Discourse](https://www.discourse.org/)、[Zendesk](https://www.zendesk.com/) | 社区交流、论坛或客服工单 | 分别侧重不同反馈渠道，不是同一种聊天软件的三个皮肤 |

收集数据前先决定“为了回答什么问题，确实需要哪些数据”，避免顺手上传不必要的个人信息。工具接得越多，隐私、费用和维护责任也越需要明确。 **没有接统计工具，不等于作品不专业；也可以通过主动反馈与试玩记录改进。**

<a id="tools-23"></a>
## 23｜录屏、剪辑与宣传：让别人看见游戏

 **这一类制作的是演示视频、预告片、商店图和宣传内容。** 白话说：游戏已经能玩，还要把值得看的部分清楚地展示出来。

| 工具 | 主要用途 | 先这样区分 |
| --- | --- | --- |
| [OBS Studio](https://obsproject.com/) | 录屏、直播和画面组合 | 录制实机操作、窗口和声音；不是剪辑时间线的同义词 |
| [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve) | 剪辑、调色、合成、音频后期 | 把实机片段组织成视频，也能进行较完整的后期制作 |
| [Adobe Premiere](https://www.adobe.com/products/premiere.html)、[Final Cut Pro](https://www.apple.com/final-cut-pro/)、[Kdenlive](https://kdenlive.org/) | 视频剪辑 | 选择镜头、调整时长、加入字幕和音轨 |
| [After Effects／AE](https://www.adobe.com/products/aftereffects.html)、[Fusion](https://www.blackmagicdesign.com/products/fusion) | 动态图形与合成 | 制作标题动画、叠加视觉效果；不等于游戏里的实时特效系统 |
| [FFmpeg](https://ffmpeg.org/)、[HandBrake](https://handbrake.fr/) | 音视频转换与压缩等处理 | FFmpeg 可按命令批量处理，HandBrake 提供视频转码工作流 |
| [Canva](https://www.canva.com/)及二维设计软件 | 海报、商店图、社交媒体内容 | 把画面和文字排版成宣传材料 |

 **预渲染宣传片与实机画面应区分。** 同一套模型可以用于两者，但制作方式、运行成本和能否让玩家操作，并不相同。

<a id="tools-24"></a>
## 24｜现成素材与批量加工：不必每一块砖都自己做

 **素材平台提供内容，资源加工工具把内容整理成项目需要的形式。** 白话说：可以找现成树木和音效，但还要挑选、整理、检查授权和运行效果。

| 平台／工具 | 主要用途 | 要注意什么 |
| --- | --- | --- |
| [Fab](https://www.fab.com/)、[Unity Asset Store](https://assetstore.unity.com/) | 模型、材质、工具包等资源市场 | 同一市场里可能既卖素材又卖插件；资源授权和兼容性需逐项确认 |
| [itch.io Game Assets](https://itch.io/game-assets)、[Kenney](https://kenney.nl/assets) | 二维、三维、界面等游戏资源 | 先看资源说明与许可，不要只看能不能下载 |
| [Poly Haven](https://polyhaven.com/) | 模型、纹理、环境照明图等 | 看清资源类型和分辨率；下载最大文件不一定最合适 |
| [Freesound](https://freesound.org/help/faq/) | 声音资源分享 | 不同声音可能使用不同许可，不能一概称为“无版权音效” |
| [TexturePacker](https://www.codeandweb.com/texturepacker) | 精灵图集打包 | 把多张小图放进大图，并输出位置数据，供程序正确取用 |
| [ImageMagick](https://imagemagick.org/) | 图片批量处理 | 批量缩放、转换等；不是必须手工打开几百张图逐一处理 |

 **图集／Atlas** 是一张或一组装了多张小图的资源；程序靠附带的位置数据知道每张图在哪里。图集只是某种资源组织方式，是否有益要结合实际渲染和加载方式判断。

也会看到 `.blend`、`.psd` 等源工程，以及 `.png`、`.webp`、`.glb`、`.gltf`、`.fbx`、`.wav`、`.ogg` 等交换或运行资源。 **文件扩展名不是软件名称，也不保证其中所有功能都能被目标引擎读懂。** 例如 glTF 定义了三维资源交付格式，实际支持还取决于导出器、导入器与扩展。[glTF 官方说明](https://www.khronos.org/gltf/)

<a id="tools-25"></a>
## 25｜AI 辅助：帮你完成任务，但仍要知道成果是什么

 **AI 工具可以辅助设计、编程和资源制作，但它不是一种统一的游戏引擎。** 白话说：“AI 做的”只说明某个环节用了 AI，还没说明成品依靠什么运行。

| 工具／类别 | 可以参与什么工作 | 不要误会 |
| --- | --- | --- |
| [ChatGPT](https://openai.com/chatgpt/overview/) | 讨论设计、解释技术、整理资料和辅助编程 | 对话中的解释不是自动经过验证的项目实现 |
| [Codex](https://openai.com/codex/)、[GitHub Copilot](https://github.com/features/copilot) | 阅读、编写和修改代码，辅助开发流程 | 实际能读取、运行或提交什么，取决于当前接入的环境和权限 |
| [Cursor](https://cursor.com/) | 带 AI 开发能力的代码工作环境 | 是开发工具，不是项目玩家端使用的游戏引擎 |
| [Adobe Firefly](https://www.adobe.com/products/firefly.html)等视觉生成工具 | 制作概念图、视觉草稿或相应素材 | 需要检查风格一致性、可编辑性、授权和是否适合运行资源 |
| [ComfyUI](https://comfy.org/) | 组织视觉生成模型与节点工作流 | 它是把模型和处理步骤连起来的工具；软件、模型与输出的许可不能自动视为同一件事 |

给 AI 的任务也应按环节说清楚。例如：“把这段对白整理成 JSON”“给现有按钮增加一次点击保护”“将图片导出为统一尺寸”，都比“帮我把游戏做好”更容易检查。

 **验收对象仍然是文件和实际运行结果。** 代码有没有执行、图片有没有透明边缘、存档能否恢复、授权是否合适，都不能只凭一句“已完成”。

<a id="licensing"></a>
## 免费、开源、付费：这是另一条分类轴

 **用途回答“它干什么”，授权回答“我在什么条件下能用”。** 不要拿“免费”代替授权说明，也不要以为“商业软件”就是大公司专用。

| 说法 | 白话意思 | 不能据此直接推断 |
| --- | --- | --- |
| 免费使用 | 某些条件下不收使用费 | 不一定开源，也不一定所有功能、平台和商业场景都免费 |
| 开源 | 按相应开源许可证开放源码并授予使用、修改、再分发等权利 | 不是没有版权、没有条件，也不排斥收费服务 |
| 源码可见／Source-available | 允许在规定条件下查看源码 | 不自动等于符合开源定义；实际可做什么仍看许可 |
| 买断／永久许可 | 某个产品或版本的许可按所购条款持续有效 | 不一定包含未来所有大版本和服务 |
| 订阅 | 按期限付费取得相应使用权或服务 | 不同产品停订后的使用、导出与访问条件可能不同 |
| 分成／Royalty | 达到相应条件时按规则支付费用 | 不一定所有收入都按同一规则计算 |
| 教育／个人／独立开发者版 | 面向特定资格提供的方案 | 不一定能直接用于任意公司、项目或收入规模 |

这里“开源”的含义参照 [Open Source Initiative 的定义](https://opensource.org/osd)，不是把“网上能找到源码”都叫开源。选软件时分别查看 **编辑器许可、运行组件许可、素材许可、平台服务条款** ；它们可能不是同一份文件。

采用前做一个最小检查：目标操作系统能否使用，能否导出项目需要的格式和平台，许可是否符合用途，后续成本能否承受。对已停更或维护不明的工具，再确认是否有可用版本、依赖环境与迁移办法。 **不要仅凭几年前的教程决定今天的授权和平台支持。**

<a id="combinations"></a>
## 把名字串起来：几套完整搭配，看看它们怎么分工

下面是 **示意组合，不是唯一推荐，不是已验证的现有项目配置，也不是要求把每一格装齐。** 同一职责可以换工具，简单项目也可以省掉某些环节。

### A．图片与对白为主的竖屏网页游戏

 **Blender 或二维绘图工具 → 图片资源 → HTML／CSS／JavaScript → 浏览器 → GitHub Pages 等托管服务。**

Blender 负责制作画面；HTML 放入图片、对话框和按钮；CSS 安排外观；JavaScript 处理选择与状态；浏览器运行；托管服务把文件交给访问者。VS Code 用来编辑，Git 用来记录修改，它们不需要跟着成品出现在玩家屏幕上。

这一组合可用来理解《体温调节》讨论过的“制作时用三维，运行时用二维画面”的方案。 **仅因为用了 Blender，并不推出必须加入 Three.js。** 只有需要实时三维能力时，才继续比较相应路线。

### B．以人物对白与分支为核心的视觉小说

 **绘图软件制作立绘 → 音频工具制作声音 → Ren’Py 组织对白、选项与运行 → 导出目标平台版本。**

现成视觉小说系统负责部分通用功能，你仍要写故事、安排条件、制作美术并验证存档。增加 Live2D 或其他动画前，还要确认对应的集成与许可，而不是假设随便拖进去就能动。

### C．二维动作或探索游戏

 **Aseprite 制作角色 → Tiled／LDtk 或引擎编辑器安排关卡 → Godot／GameMaker／Phaser 等其中一条路线组织玩法 → 对应平台发布。**

这里的斜线表示备选路线，不是三套引擎同时安装。选择地图编辑器时，还要确认游戏怎样读取地图。音效可以由 Audacity 等工具处理，复杂音乐由所选音频工作站制作。

### D．可自由转动视角的网页三维互动

 **Blender 制作模型 → 导出适合目标的三维资源 → Three.js／Babylon.js／PlayCanvas 等路线加载和显示 → JS／TS 处理交互 → 网页发布。**

这次玩家运行时仍要改变三维视角或物体，所以需要相应实时图形能力；这和预先渲染好一张背景图不是同一个需求。是否加 React 之类的界面工具，要看界面复杂度。

### E．多人协作的三维制作项目

 **Maya／Blender 等制作形体 → ZBrush 等补细节 → 材质工具处理表面 → 动画工具制作动作 → Unity／UE 或自有引擎整合 → 专门工具测试和发布。**

同时用版本管理保存变动，用制作追踪安排审阅，用自动构建持续生成可测试版本。需要在线功能时再加入联机和后台服务。 **大型流程的关键不是名字多，而是每一步的产物、负责人和检查标准能接起来。**

<a id="confusions"></a>
## 最容易混淆的名字与说法

| 听到的说法 | 正确放回哪一层 |
| --- | --- |
| “Unity，C#，Visual Studio” | 引擎、语言、开发工作台，可以一起用 |
| “Java 和 JavaScript” | 两种不同语言，不是完整版与简化版的关系 |
| “Three.js 和 TypeScript” | 三维库与语言，可以配合，不是二选一 |
| “VS Code 和 Visual Studio” | 不同产品，不是一个名字的长短写法 |
| “Clickteam Fusion、Photon Fusion、Blackmagic Fusion” | 分别是游戏制作、多人网络、视觉合成方向的产品；不能只凭 Fusion 一个词判断 |
| “Blender 和 Cycles” | 综合制作软件与它其中的渲染系统 |
| “Unreal 和 UEFN” | 通用引擎与面向 Fortnite 创作的特定编辑工作流 |
| “Git、GitHub、GitHub Pages” | 版本控制、仓库协作平台、网页托管服务 |
| “ink 和 Inky” | 叙事语言与相应编辑器 |
| “Live2D Editor 和 SDK” | 制作内容的工具与把内容接入项目的开发／运行组件 |
| “AI 文件、游戏 AI、生成式 AI” | 可能分别指 Illustrator 文件、角色行为系统、生成内容的人工智能 |
| “Unity Version Control／Plastic SCM” | 当前产品名与旧资料常见名称，查文档时注意版本 |
| “P4／Helix Core” | 当前 Perforce 产品名与旧资料常见名称 |
| “Flow Production Tracking／ShotGrid” | 当前制作追踪产品名与旧称 |
| “RealityScan／RealityCapture” | 当前桌面产品名与旧称；RealityScan Mobile 还需单独区分 |
| “Affinity Designer／Photo／Publisher” | 旧资料中的分别命名应用；当前 Affinity 统一应用整合多类功能 |
| “Shader／着色器” | 处理图形计算的程序，不是固定指某个品牌的软件 |
| “插件／插件包／素材包” | 插件通常加功能，素材包提供内容；一个商品也可能包含两者 |
| “开源引擎做的游戏” | 不足以单独判断游戏本身或其素材的授权，要看具体许可与使用方式 |
| “HTML5 游戏” | 常是对网页游戏技术路线的宽泛称呼，不是在报一个具体引擎名 |
| “3A／AAA” | 项目制作规模等语境中的称呼，不是引擎、语言或软件质量等级 |

改名对照可直接参看 [Perforce P4](https://www.perforce.com/products/p4)、[Unity Version Control 文档](https://docs.unity.com/en-us/unity-version-control)、[Flow Production Tracking](https://www.autodesk.com/products/flow-production-tracking/overview)、[RealityScan](https://www.realityscan.com/uses)和 [Affinity](https://www.affinity.studio/)的官方说明。旧名有助于搜索历史教程，但不能假设旧版操作、许可和兼容条件仍然完全适用。

<a id="finish"></a>
## 最后，怎样回答“你用什么做的？”

回答完整，不是把知道的软件全报一遍，而是说明分工。比如一个假设中的网页项目可以这样说：

> “是用 HTML、CSS 和 JavaScript 做的网页互动，没有用 Unity 这类完整引擎。画面在 Blender 里制作后导出成图片，代码用 VS Code 编辑，通过 Git 管理，再发布到网页托管服务。”

或是：

> “游戏主体用 Unity，脚本用 C#，模型在 Blender 里做，贴图在 Painter 里做，角色动作由动画工具制作后导入。”

以后遇到新名字，先问三个问题： **它负责哪一步？它输出什么？下一步由谁接着用？**

只要能回答这三个问题，即使没有用过那个软件，也已经能把它放在游戏开发流程中的正确位置。

<a id="sources"></a>
## 来源与查阅方式

本文的工具定位优先依据各产品官网、官方文档和作者项目页，来源直接放在对应软件名称上，不另复制一份数百项的链接名单。关系解释与搭配实例是为初学者组织的说明，不代表厂商对任意跨软件组合的兼容承诺。

概念的主要核对入口包括 [Unity 的引擎介绍](https://unity.com/products/unity-engine)、[Godot 的功能说明](https://godotengine.org/features/)、[Phaser 的自我定义](https://docs.phaser.io/phaser/getting-started/what-is-phaser)、[MDN 的网页技术说明](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/What_is_JavaScript)、[Git 文档](https://git-scm.com/about)、[Git LFS](https://git-lfs.com/)、[glTF 规范入口](https://www.khronos.org/gltf/)和 [OSI 开源定义](https://opensource.org/osd)。

查阅时间为  **2026-10-13** 。本文不提供下载镜像、破解资源、价格保证或平台授权保证。采用工具时，从对应官方入口继续核对当前版本与具体许可；这份手册首先帮助理解“它是什么”，而不是代替最终技术选型和实际测试。
