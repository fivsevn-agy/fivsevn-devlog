# fivsevn system map

本文是 fivsevn 的系统总览，用于说明公开入口、页面板块、内容分类、仓库职责，以及 WordPress、GitHub、assets、YouTube 之间的分工。核心原则是：低成本、可迁移、轻量、长期可维护。

## Quick orientation

- `fivsevn.com` 是主入口，负责视觉展示、页面组织和对外呈现。
- `devlog.fivsevn.com` 是文本 archive / source 入口，负责长文、笔记、资料源和后台日志的公开浏览。
- `posts / natsci / netcom` 是主要知识与笔记分类。
- `foodie` 是生活高频页面；`stills / bygone / motion` 是视觉表达；`intake` 是资料源与每日输入；`57store` 是叙事实验；`blogops` 是后台维护日志。
- GitHub 保存文字、资料源、脚本、规范和静态资源；其中 devlog 偏文字与资料源，assets 偏图片与静态资源。WordPress 负责展示；YouTube 承载视频。

---

## 目录

- [1. 公开入口](#1-公开入口)
- [2. 页面结构](#2-页面结构)
- [3. 视觉与界面风格](#3-视觉与界面风格)
- [4. 知识与笔记](#4-知识与笔记)
- [5. 生活高频页面](#5-生活高频页面)
- [6. 图像与视觉表达](#6-图像与视觉表达)
- [7. 信息源与每日输入](#7-信息源与每日输入)
- [8. 57store](#8-57store)
- [9. blogops](#9-blogops)
- [10. 仓库结构](#10-仓库结构)
- [11. WordPress、GitHub、assets、YouTube](#11-wordpressgithubassetsyoutube)
- [12. 新内容分类规则](#12-新内容分类规则)
- [13. AI 协作规则](#13-ai-协作规则)
- [14. 简述](#14-简述)

---

## 1. 公开入口

### 1.1 主入口：fivsevn.com

```text
https://fivsevn.com/
```

`fivsevn.com` 是 fivsevn 的主要公开入口，也是对外介绍自己时优先使用的链接。它基于 WordPress，用于视觉排版、页面组织、入口展示，以及图像、视频和内容的策展式呈现。WordPress 适合做直观、有设计感的页面，但不作为唯一内容源。

### 1.2 devlog 入口：devlog.fivsevn.com

```text
https://devlog.fivsevn.com/
```

`devlog.fivsevn.com` 是 GitHub 文本内容的公开目录与阅读入口，主要用于长文、笔记、专题内容、资料源、后台日志和仓库文本的浏览。它可以理解为 `fivsevn.com` 主入口之下的文本 archive / source 入口。

---

## 2. 页面结构

页面是读者最直观看到的部分；仓库是内容、资源和结构的保存层。

```text
fivsevn.com / devlog.fivsevn.com
│
├─ 知识与笔记
│  ├─ posts
│  ├─ natsci
│  └─ netcom
│
├─ 生活高频页面
│  └─ foodie
│
├─ 图像与视觉表达
│  ├─ stills
│  │  └─ bygone
│  └─ motion
│
├─ 信息源与每日输入
│  └─ intake
│
├─ 叙事实验
│  └─ 57store
│
└─ 后台日志
   └─ blogops
```

---

## 3. 视觉与界面风格

fivsevn 的页面风格偏暗色、低饱和、monospace / code font、代码 / 终端 / 日志界面感，链接和状态提示常用 `#6becae` 绿色。首页采用 rust-like 的视觉组织方式，并穿插个人物品、家具、器具等 cutout 图像作为模块标识和视觉锚点。整体控制图像密度，主要通过文字、字符、注释、状态行、目录结构和界面语法来建立氛围。页面整体类似一个可浏览的个人系统入口。

页面的展示方式本身也是表达的一部分：`posts` 是 stream，`foodie` 是手机聊天界面，`natsci` 是物种观察窗口，`stills` 是 roll archive，`motion` 是直播界面，`devlog` 是文本目录和仓库 archive。主站 `fivsevn.com` 和 `devlog.fivsevn.com` 在视觉上保持暗色、低饱和、代码界面感的一致性。整个网站接近一组记录装置。

---

## 4. 知识与笔记

### 4.1 posts

```text
https://fivsevn.com/posts/
https://devlog.fivsevn.com/posts/
https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/scripts/publish_wp_text.py
```

`posts` 是默认笔记区，用于随手记录、普通随笔、个人观察、生活想法、杂项和暂时无法归类的内容。

`fivsevn.com/posts/` 偏 stream 形式，用于比较随意的碎片记录、短内容和日常发布，可通过 `publish_wp_text.py` 发布。`devlog.fivsevn.com/posts/` 偏 archive 形式，用于保存长文、正式笔记和按 spec 整理过 frontmatter 的 Markdown 文章。如果 `fivsevn.com/posts/` 需要引用长文，可以链接到 `devlog.fivsevn.com/posts/` 中的文章。

### 4.2 natsci

```text
https://fivsevn.com/natsci/
https://devlog.fivsevn.com/natsci/
```

`natsci` 是自然科学专题，从 `posts` 中分化出来，用于自然科学知识整理、生物与自然观察，以及对自然对象、科学概念和自然现象的记录与理解。

`fivsevn.com/natsci/` 偏视觉展示，页面做成了物种观察窗口一类的展示形式。`devlog.fivsevn.com/natsci/` 偏资料、文章和结构化笔记存档。

### 4.3 netcom

```text
https://devlog.fivsevn.com/netcom/
```

`netcom` 是网络、通信与技术系统专题，从 `posts` 中分化出来，用于整理网络通信、协议、无线电 / RF、计算系统、嵌入式系统、技术基础设施和工程笔记。

由于目前没有强烈的图片展示需求，`netcom` 暂时主要放在 devlog 中，作为资料笔记和技术内容 archive。

---

## 5. 生活高频页面

### 5.1 foodie

```text
https://fivsevn.com/foodie/
```

`foodie` 是饮食页面，属于生活高频内容，不与 `posts / natsci / netcom` 这三个知识与笔记分类平级。它用于食物、饮品、餐厅、日常吃喝、食物照片和饮食相关的轻量记录。

这个页面的重点是视觉展示和日常更新，目前做成类似手机信息界面的形式，适合用 WordPress 进行更自由的视觉设计。同类页面可以按内容量继续扩展，例如以后穿搭内容变多，可以新增一个与 `foodie` 同层级的页面。

---

## 6. 图像与视觉表达

图像、摄影、平面设计和展示方式本身都是 fivsevn 的表达内容。图片本体优先放在 `fivsevn-assets`，页面通过链接引用；WordPress 主要负责展示、排版和策展。

### 6.1 stills

```text
https://fivsevn.com/stills/
```

`stills` 是静态图像展区，用于摄影、静态图像、平面视觉和以视觉为主的内容。当前风格以黑白照片为主，也包含图片组合、编辑和策展式展示。

### 6.2 bygone

```text
https://fivsevn.com/stills/bygone/
```

`bygone` 是 `stills` 中分化出来的旧照片页面，用于整理家里的旧照片、历史图像、家庭记忆和带有时间感的视觉材料。图片本体仍放在 assets，WordPress 负责展示。当前设计是一张图片一个 post，方便浏览和评论。

### 6.3 motion

```text
https://fivsevn.com/motion/
```

`motion` 是动态影像页面，用于收纳视频、motion design、影像实验、AI 生成影像，以及其他以时间和运动为核心的视觉表达。视频本体通常放在 YouTube，并在个人 iCloud 中备份；页面本身采用类似直播界面的策展式结构。

---

## 7. 信息源与每日输入

### 7.1 intake

```text
https://devlog.fivsevn.com/intake/
https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/intake
```

`intake` 是 source 页面，兼具个人资料源保存和每日新闻输入功能。它用于保存和展示个人关注的信息源，并通过 RSS 抓取每日新闻 / 外部信号，作为后续阅读、记录和整理的入口。

`intake` 属于单独板块，不等同于 `posts / natsci / netcom` 的正式笔记，也不等同于 `blogops` 的维护日志。相关脚本和配置保存在 `fivsevn-devlog` 中。

---

## 8. 57store

```text
https://fivsevn.com/57store/
```

`57store` 是叙事实验区，用于叙事实验、世界观片段、fictional archive、故事性文本、设定、角色、场景、物件，以及介于笔记和小说之间的材料。

它与其他内容区保持隔离，因为“五月七日便利店”本身是一个封闭世界观。这个区域需要保持叙事自洽，避免破坏语境。

```text
现实世界 → posts / natsci / netcom / foodie / intake
故事、世界观、叙事氛围 → 57store
```

---

## 9. blogops

```text
https://devlog.fivsevn.com/blogops/
https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/blogops/docs/publish-memo.md
```

`blogops` 是后台日志与维护方法区，用于博客维护记录、页面结构调整、发布流程、自动化脚本说明、WordPress / GitHub / assets 协作方法、CDN 使用说明、系统整理方法，以及写给自己的维护日志。

发布设置、维护流程、具体操作细节和详细的说明文档链接，可优先查阅《博客发布与维护流程备忘》。

---

## 10. 仓库结构

```text
https://github.com/fivsevn
```

页面和仓库分开理解：页面负责展示、入口和视觉组织；仓库负责保存、管理、迁移和规范。

```text
GitHub / repositories
│
├─ fivsevn-devlog
├─ fivsevn-assets
├─ fivsevn-spec
├─ fivsevn-57store
└─ fivsevn-internal
```

### 10.1 fivsevn-devlog

```text
https://github.com/fivsevn-agy/fivsevn-devlog
```

`fivsevn-devlog` 是主要文字仓库，用于保存 `posts`、`natsci`、`netcom`、`intake`、`blogops`、重要 Markdown 文本、长文内容、资料源、自动化脚本和可迁移的正文材料。重要文字和可迁移文本优先保存在 devlog。

### 10.2 fivsevn-assets

```text
https://github.com/fivsevn/fivsevn-assets
```

`fivsevn-assets` 是静态资源仓库，用于保存图片、摄影、图标、平面素材、页面引用资源和可通过 CDN 加速的静态文件。图片优先进入 assets，再由页面引用，以减少 WordPress 空间压力并方便迁移。

### 10.3 fivsevn-spec

```text
https://github.com/fivsevn-agy/fivsevn-spec
```

`fivsevn-spec` 是规范与习惯系统，用于命名规范、metadata 规则、文档格式、分类原则、工作流约定和日常习惯规范。它不只服务博客，也可以服务日常生活中需要结构化和持续维护的部分。

### 10.4 fivsevn-57store

```text
https://github.com/fivsevn/fivsevn-57store
```

`fivsevn-57store` 是 57store 世界观相关内容的专用仓库或子系统，用于保存叙事实验、世界观材料、57store 页面资源、互动页面，以及未来 `57store.fivsevn.com` 相关设计。

### 10.5 fivsevn-internal

```text
https://github.com/fivsevn/fivsevn-internal
```

`fivsevn-internal` 是私有仓库，用于保存私人草稿、临时材料、内部计划、不适合公开的记录，以及暂时无法判断是否公开的内容。不确定是否公开的内容先放 internal，确定可以公开后再整理到公开仓库或页面。

---

## 11. WordPress、GitHub、assets、YouTube

### 11.1 WordPress

WordPress 用于 `fivsevn.com` 的页面编辑和视觉展示，承担入口页、视觉排版、灵活页面、读者浏览体验，以及图片和视频的策展式组织。

### 11.2 GitHub

GitHub 用于长期保存核心内容，包括 Markdown 正文、图片资源、规范文件、系统记录、资料源、自动化脚本和可迁移材料。

### 11.3 assets

`fivsevn-assets` 用于保存图片和静态资源。图片通过 CDN 或直接链接被 WordPress 页面引用。基本原则是：图片本体放 assets，页面展示交给 WordPress。

### 11.4 YouTube

```text
https://www.youtube.com/@fivsevn
https://fivsevn.com/57store/cctv/
```

YouTube 用于承载视频文件。页面中可以引用 YouTube 视频，避免把大体积视频文件放进 GitHub 或 WordPress。57store / CCTV 相关视频作为 57store 叙事系统的一部分。

### 11.5 基本分工

```text
WordPress → 展示与排版
GitHub → 长期保存与迁移
fivsevn-devlog → 文字、长文、资料源、自动化脚本
fivsevn-assets → 图片与静态资源
YouTube → 视频
fivsevn-spec → 规范与习惯
fivsevn-internal → 私有材料
```

---

## 12. 新内容分类规则

新增内容时，优先按公开性和表达形式判断：不确定是否公开的内容先放 `internal`；普通笔记、随想和杂项进入 `posts`；自然科学知识、生物观察和自然记录进入 `natsci`；网络、通信和技术系统进入 `netcom`；饮食和日常吃喝进入 `foodie`；静态图像、摄影和平面视觉进入 `stills`；旧照片和家庭旧影像进入 `bygone`；视频、动态影像和 motion design 进入 `motion`；资料源、RSS 和每日外部信号进入 `intake`；故事、世界观和叙事实验进入 `57store`；博客维护、系统整理和发布方法进入 `blogops`。

---

## 13. AI 协作规则

AI 协作者处理 fivsevn 内容时：

- 先区分页面和仓库。
- `fivsevn.com` 是主入口；`devlog.fivsevn.com` 是长文、仓库文本和资料源的公开目录入口。
- `posts / natsci / netcom` 是主要知识与笔记分类；`foodie` 是生活高频页面；`stills / bygone / motion` 是视觉表达；`intake` 是资料源与每日输入；`57store` 是叙事实验；`blogops` 是后台维护日志。
- 重要文字优先保存到 `fivsevn-devlog`，图片优先保存到 `fivsevn-assets`，视频优先放 YouTube 再由页面引用。
- 不要为了结构完整而新增复杂层级；如果无法判断分类，默认先放 `posts` 或 `internal`。

---

## 14. 简述

fivsevn 是一个以 `fivsevn.com` 为公开主入口、以 GitHub 保存文字、资料源和资源、以 WordPress 做视觉展示、以 YouTube 承载视频、由知识笔记、生活页面、视觉表达、资料输入、叙事实验和后台日志共同组成的轻量个人创作系统。
