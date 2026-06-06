---
id: netcom-bluetooth-naming-001
title: 蓝牙名称的由来

module: netcom
submodule: bluetooth
topic: naming

type: translation
status: active
canonical: true

summary: >
  本文翻译 Jim Kardach 对 “Bluetooth” 命名过程的长篇回忆，说明这个名称如何从临时代号变成蓝牙 SIG 与短距离无线技术的正式名称，并串联了 Harald Bluetooth、Jelling 符文石、商标检索和产业联盟谈判等背景。

parents: []
related: []

tags: [bluetooth, wireless, naming, sig, intel, ericsson, technology-history]

audience: [self, public]
languages: [zh]

maturity: stable
confidence: 0.92

visibility: public
source_of_truth: translation

original_title: Kardach - Naming Bluetooth
original_source: https://www.kardach.com/bluetooth/naming-bluetooth
original_publisher: Jim Kardach / Kardach.com
translation_note: >
  本文为原文内容的中文翻译，仅用于学习与知识整理。
  所有版权归原作者及出版方所有。

created: 2026-06-07
updated: 2026-06-07
---

## 文章翻译

### source

- [原文链接](https://www.kardach.com/bluetooth/naming-bluetooth)

---

## 正文

![Image 1](https://lh3.googleusercontent.com/sitesv/AA5AbUDLZYW8pQbxZNHpPU11I9f7WpdRUMiTR7EyrfvY64na8hp-29bfeMywSkPiC4aHe2r4uGwyxeuRAdQIQeWv8mKtn7B-dt8bblyFP4yA4G275nsP3xagfX_4115HzxyHgT5fqk0s5e9ethLWJGlCmAWpLcWUSkdY5FX1vvER35v0i3Rm0Lq-V2VqRQfD3nceQbnYwYWUWlL8G09n=w1280)

首先，我想感谢我的朋友 Vince Holton，感谢他允许我更新这篇文章，并把它刊登在最后一期《Incisor》杂志上（谢谢 Vince）。Vince 从一开始就在场。大约 20 年前，在一次 Bluetooth Conference 的休息时间里，我们坐在蒙特卡洛 Hotel de Pari 的酒吧里，我讲了这个故事。讲完之后，Vince 走过来问我是否愿意把这个故事写下来，发表在《Incisor》上。我让 Vince 看看桌子，桌上摆满了空啤酒瓶，然后我表示，既然是我讲了这个故事，我就一瓶啤酒都不用买。Vince 说，因为当天是 6 月 8 日（Bluetooth Conference），蒙特卡洛大奖赛刚刚结束，赛道布置还没撤掉。而且他有一辆蓝色法拉利，只要我写这篇文章，他就带我绕大奖赛赛道跑一圈。Simon Ellis 介入进来，说谈判必须由他接手，于是 Simon 重新谈判，结果变成：我写这篇文章，而 Simon 和我都能在蒙特卡洛大奖赛赛道上跑一圈。

[![Image 2](https://lh3.googleusercontent.com/sitesv/AA5AbUDsnY88yCnwHMwmmyLT1AWinTkZdEtpb92kMYXAGy8scaX0JReLQd1OR_kuOIKf1Ayk4X6piJCl8XpIEK2cWB-EanibyeGLARFyx526aQkjWZACl7MmfHJCCBblCr5XehdNvwn5Xo08Jq0emqOvq68NIzLgac9HnLt3WFoJ1z5VpR1bE8Q-cpsjqHcoQn_r1p22bZOntB_Sx5rHy2U=w1280)](https://www.youtube.com/watch?v=A1UdtDld-z8&list=PL_fbfFWItJhOAF2HGJ5aLm_pCOpD2T_-d&index=3&t=0s)

这些年来，我把这个故事写下来过几次，多数人会指向我的某篇文章（最早是《Incisor》上的三篇连载文章，几年后又在 [EE-Times](https://www.eetimes.com/tech-history-how-bluetooth-got-its-name/#) 上发表过一个较短版本）。不过现在我有了更多见解，也已经从 Intel 退休，所以决定更新最初那篇文章。它很长，但确实是个好故事。

这个名字借自 10 世纪的一位丹麦国王 Harald Blåtand，英文即 Harald Bluetooth。在丹麦，他很有名，因为他曾在丹麦旧都 Jelling 立起一块符文石。符文石是斯堪的纳维亚的一种纪念碑，用来纪念某个场合或事件。这是两块符文石中较大的一块，用来纪念 Harald 的父亲（丹麦第二任国王）“Gorm the Old”，同时也纪念 Harald 的若干成就。这块石头大约 2 米高，底部约 2 米宽，有三个面（像金字塔一样）。其中一面覆盖着文字（符文），概述他的成就；第二面展示一条缠绕在藤蔓中的龙（有人告诉我，这象征着基督教与旧宗教之间的冲突）；第三面则显示国王本人的图像。

第二块石头由 Harald 的父亲（Gorm）竖立，用来纪念他的妻子 Thyra。后来我才知道，这几块特定的符文石被认为是丹麦的“洗礼石”，因为它们是在丹麦形成的时间点附近竖立的。

后来，当我和我的好友 Orjan Johansson（来自 Ericsson 的 Bluetooth 项目经理）去 Jelling 看真正的石头时，我们被告知这块石头曾经失踪了 600 年。显然，Harald 曾经和他的儿子 Sweyn Forkbeard 因丹麦的宗教问题发生争执。Harald 刚刚让王国基督教化（约公元 960 年），而 Sweyn 认为他们应该回去崇拜旧神（Odin、Thor、Frey……）。Sweyn 赢得了这场争论（过程中还放逐了他的父亲）。由于这块符文石颂扬的是 Harald 使丹麦人基督教化的功绩，Sweyn 便把它埋了起来。大约 600 年后，一位农民对自家农田里的一座大土丘感到好奇（丹麦是个非常平坦的地方），于是重新发现了这块石头。

![Image 3](https://lh3.googleusercontent.com/sitesv/AA5AbUAgwRiRhJIFseEnq-TrvV3pLnFqAgwUZWVhyhlOu9wX54tEKWH_JoXuUYBhFcPm7N1W2Xieq9iI3iGfha0ISgy6sQTFJ5IXyFo_dhDy9xK8B2Zulb4-ziax_MFFC6-pshbDWmWFS6ID-BgukeUdgdbAOiHezJiSqxxklLlHtnK8d8_yWXFnOvTEkb_SNnkZRdUoPGsD_wyXDnyj6KY=w1280)

Orjan（右）和我（左）在丹麦 Jelling 看 Bluetooth 石（我身高 6 英尺 2 英寸，最左边是较小的 Thyra 石）。

1997 年，当我们组建一个短距离无线 Special Interest Group（SIG）时，我并不知道这些。当时我正在与 Ericsson 和 Nokia 合作——它们也有短距离无线项目——目标是创建一个单一标准。Intel 的项目叫 “Biz-RF”（Business RF），Ericsson 的项目叫 “MC-LINK”，Nokia 的项目叫 “Low Power RF”。当时我们正在决定，是应该成立自己的组织，还是加入一个现有标准组织，然后在这个既有组织内部开发这项技术。Ericsson 和 Intel 都有成员参与一个名为 Home-RF 的现有 SIG；Home-RF 想做一种面向消费者的无线技术，而我们最初的想法是看看能否利用这个 SIG 来开发我们的技术。

为此，Ericsson 的 Sven Mattisson 和我在加拿大多伦多举行的一次 Home-RF SIG 会议上做了演示。我介绍了 Biz-RF，Sven 介绍了 MC-LINK。我们这些令人困惑的提案得到的反应很冷淡，也正是在这个时候，我意识到我们需要一个项目代号，供所有人共同使用。Home-RF 会议结束后，Sven 和我决定做一次复盘，并在多伦多的酒吧里比较一下瑞典、美国和加拿大啤酒。

喝啤酒时，我最喜欢讨论的话题是历史，所以我很自然地请 Sven 给我补一补斯堪的纳维亚历史。我表示，我对斯堪的纳维亚的了解只限于：维京人戴着带角头盔四处奔跑、袭击和掠夺各地，而且他们都是疯狂的酋长。

Sven 解释说，虽然他不是历史专家（他更懂无线电），但他相当确信维京人的头盔上从来没有角，而且《布偶秀》里的 Swedish Chef 是瑞典人长期以来一直试图摆脱的刻板印象。不过，他读过一本叫《The Longships》的历史小说，讲的是维京人，他愿意按这本书来讲述自己国家的历史。随着夜晚推进（我们也从一家酒吧转到另一家酒吧），Sven 给我讲了一个故事：一个年轻的瑞典小伙 Röde Orm（Red Snake）去参加一次 “Viking”。这个词表示一次贸易、发现和/或冒险性质的远征。故事发生在 Harald Bluetooth 国王防御其王国（包括挪威、丹麦和瑞典的部分地区）免受其子 Sven Tveskäggs（Sven Forkbeard，约公元 940 年）攻击的时代。

![Image 4](https://lh3.googleusercontent.com/sitesv/AA5AbUBD-rOsxUNXY__MDKf9qYR2-69KJ48CxzbJhAC4SLNRFVb791NT6EvETKhEl7mZW-qN0YoJcvdfXjW5E9IukHWoyG-ao4OpUmDGZ_yVwduzGvALuX6WtpnLJdYtufSRshApRU1sXg8q2dvFWe8GR0bqKCqeHGS0cGm9G52iOY9CPysbR2DaH_8vWIy6DL9zmvftgxi3bTCO0Ux-0w4=w1280)

我回到家时，之前订购的一本关于斯堪的纳维亚历史的书正在等着我。我翻阅这本 Gwyn Jones 所著的《The Vikings》时，看到一张岩石照片，上面刻着一个人。图片说明写着：“由 Gorm the Old 和 Harald Bluetooth 在日德兰 Jelling 立起的符文石”，书中的文字还说明，这张图片描绘的是 “Harald 的骑士风范”。符文石上的铭文写道：“Harald 国王为其父 Gorm、其母 Thyri 立此纪念碑：这个 Harald 为自己赢得了整个丹麦和挪威，并使丹麦人成为基督徒。”

![Image 5](https://lh3.googleusercontent.com/sitesv/AA5AbUC_YO8evon9tFTG-GXOhQtwRg9NcWcXOmAqnNAs8uCeezctYiwxT737Ro-E4Vkxq6acgeLSfwxNpDTuDi_y_1AKuxFXxqVnfYmAh7ocWhBlUWA2s3VfSXFOAKX6EThTJ-YISFn5J8O1w5IyHIO59ZiJO1LAcXltW4bIXSHGt-FPK0Ef2hA4bduQFhmAQK5wWMmE33u3RYIXvkFD=w1280)

我其实不太记得多伦多那晚的很多细节了，但 Bluetooth 这个名字在我的记忆里浮现出来。我想到，这个名字和斯堪的纳维亚历史有关（一位统一了挪威和丹麦的 10 世纪丹麦国王）、符文石上有 Harald 本人的图像，再加上 “Bluetooth” 这个奇怪的词，或许会成为这个项目的一个相当不错的代号。

我把那块石头的图像数字化了（先用 Sharpie 记号笔把 Harald 标出来），并做了一张投影片，主题是 “Bluetooth”，下面列了一些要点：

这是他在首都 Jelling（中日德兰）竖立的两块符文石之一

*   这是石头正面，描绘 Harald 的骑士风范。

    *   石头上的铭文（“runes”）写道：

    *   Harald 使丹麦人基督教化

        *   Harald 控制了丹麦和挪威

        *   Harald 认为笔记本电脑和蜂窝电话应该能无缝通信。

周一，我把这个提案拿给 Simon Ellis 看。他当时是 Intel 移动数据业务的市场经理。我告诉 Simon，我想把项目名称从 “Biz-RF”（Business-RF 的缩写，我们总是把它简称为 “Bizarre-F”）改成 Bluetooth。Simon 表示，他认为这是个糟糕的主意（也就是说，他发出作呕的声音，还指着自己的喉咙）。然后我给他看了符文石的图片。

他从我手里拿过投影片，看了几秒钟，然后说：“你能不能在他手里画一台笔记本电脑和一部手机？”我很快更新了图片，把它递回给 Simon。Simon 接着评价说：“我喜欢。”但他马上补充说明，这只是一个代号，在公开发布之前，市场部门会选择一个合适的正式名称。

到那个时候，Simon 和我已经在不同项目上合作了将近 12 年，也都喜欢把一点幽默带进工作里。Bluetooth 这个名字代表一位 10 世纪丹麦国王，他把丹麦人、挪威人和瑞典人联合起来（正如我们的项目把 PC 行业和电信行业联合起来一样），但这个名字听起来很滑稽。我们想到，总有一天 Andy Grove 或 Bill Gates 必须在观众面前一本正经地说出 “Bluetooth” 这个词，这让我们觉得很有趣。

![Image 6](https://lh3.googleusercontent.com/sitesv/AA5AbUC6vB68iY1wXD9oUxpiSJ8Z5gZoS92qle2tHNe0JdXnZGviLEbkDiJuU6YHJV3umd1E5HoGLo7N1hEJvyGFOTWxSlggCtfzU-eWNAezvZ5xZfk0ZarSStaVPu5UR82RiLt1_rDPP_EYK_S2CXDilfjBMWfA8qjmdMEOH_5xvN3pgtHZq9vFDfXIsdwoYipJRsyTv-ku11fLLqcgdtE=w1280)

下一步，是让 Intel 批准把这个名字作为代号使用。我去找我的老板 Phil Wennblom，告诉他我们会把这个新的无线电项目称为 “Bluetooth”。他告诉我，“Bluetooth” 是个糟糕透顶的名字，而且公司的政策是用北美的山或河来命名。我把这当成了批准，于是去找 Simon，向他阐述：这一定是一个很棒的代号，因为 Phil 讨厌它。Simon 表示同意，但认为我们应该把各方面都照顾到，去取得我们的总经理（我的老板的老板，也是 Simon 的老板的老板）Stephen Nachtsheim 的批准。于是我们做了一张投影片，上面有那张整洁的符文石图，并解释这个代号从何而来。

我们把这张投影片打印出来，放在 Stephen 的椅子上，并附上一张纸条，写明如果他在本周结束前没有反对意见，我们就会继续使用这个代号（碰巧 Stephen 接下来两周要去欧洲出差）。

要让这个代号获得批准，下一道障碍是让法律部门做一次商标检索。我很快给我们的律师发了一封邮件，请他对 “Bluetooth” 这个词进行商标检索。我很快收到回复：

Jim，

你绝不可能把一个项目命名为 “Bluetooth”。我们要求代号必须是一条河、一个湖或一座城市！

我试着快速虚张声势一下，声称 Bluetooth 实际上是一个德国村庄名称的英文翻译，并且我希望一周内完成商标检索。他很快回复：

想得美，不行。给我一个河名。

接着我解释说，这是一个涉及另外五家公司的 Special Interest Group 的代号，其中四家公司没有这些规则，所以请他在一周内完成检索。

在假定商标检索会顺利通过的情况下，我们接着开始通知 Intel 内部其他人，说明项目名称将要变更；反应变成了我们后来会习惯的一种反应：“你们疯了，我们不能把一个项目叫作 ‘Bluetooth’！”不过我的经理允许我们继续推进。他的推理是，没有任何心智正常的人会允许这个项目被称为 “Bluetooth”，所以这个名字在任何公开发布之前都会被改掉（至少他是这么想的）。

一周后，我终于收到了来自法律部门的关键邮件：

意外吧，意外吧，没人把 “Bluetooth” 注册成商标。

我并不意外。

1997 年 12 月，即将成立的 SIG 的所有主要成员（Intel、Ericsson、Nokia、IBM 和 Toshiba）第一次在瑞典 Lund 举行面对面会议。Simon 和我讨论过，怎样才能让其他成员同意一个 SIG 名称（最简单的事情往往最难），最后我们决定，在动身去开会之前，直接发出一套投影片，概述 “Bluetooth SIG” 的初始目标和项目。我们做了一套投影片模板，每一页都有那块“被改过的符文石”。

在瑞典 Lund 的会议上，我们开始介绍最初的演示内容，很快就被问到：“这个 Bluetooth 是什么？”我们解释说：“每家公司都在用不同的代号，而作为一个 SIG，我们需要一个统一代号来帮助识别我们的联合努力。我们选择了一个很难让人联想到短距离无线技术的代号，同时它也象征着计算机行业和电信行业的联合，就像 Harald 曾经联合丹麦人和瑞典人一样。”

一片完全的沉默。

Simon 迅速补充说：“而且，这只是一个代号，等到市场小组为 SIG 想出一个‘正式’名称为止。”

谈话声突然爆发出来，不同小组开始讨论 SIG 的“真正名称”应该是什么。我瞥了 Simon 一眼，他也正看着我并咧嘴笑。我们俩都知道，SIG 会带着 “Bluetooth” 这个代号继续推进。

虽然市场小组被赋予了交付正式名称的任务，Program Management（PM）小组还是决定帮他们一把（尽管市场部门表示抗议），进行一次快速命名头脑风暴。Ericsson 的市场人员已经努力开发了一些名称，并提出了其中一个最令人难忘的：

Flirt —— “靠近而不接触”

我至今仍然困惑，为什么这个名字没有被选中。另一个候选名称是 “Conductor”——使用这项技术的设备可以把一支设备“管弦乐队”指挥成一曲和谐的生产力交响乐。不过，房间里某位工程头脑指出，“conductor” 也是一根电线中的金属部分——而这本应是一种无线技术。

另一个提案是 “PAN”，是 “Personal Area Network” 的首字母缩略词。参与其中的一些人认为，对于一项最终面向消费者的技术而言，缩略词过于“工程化”。此外，PAN 只代表这项技术所开发的三类使用模型之一（网络接入、外设线缆替代，以及 PAN）；我们不希望过度强调某一种用途。

Lund 的头脑风暴没有得出结论；我们还必须做进一步研究，寻找一个名称。我相信，每个人离开那次会议时都意识到，选一个名字会有多难，而我们还必须开发这项技术（这也是另一个困难任务）！

与此同时，技术工作继续推进，Intel 委托制作了第一支 Bluetooth 使用场景视频，这支视频是在 1997 年圣诞假期期间开发的。视频讲的是一个笨手笨脚的销售/市场人员，他需要做一次重要演示，结果却被锁在衣柜里，最后被 “Wireless-RF” 解救。我不得不向 Simon 抱怨：“一支关于某项技术的视频，难道不应该提到这项技术的名称或代号吗？”而且口号 “Wireless-RF sets you free” 并没有推广这项技术的名称！Simon 表示，虽然代号是 Bluetooth，但正式名称尚未选定，他们想要一个通用名称，这样即使正式名称宣布之后，视频仍然可以使用。进一步追问后才发现，负责这支视频的市场工程师其实并不喜欢这个代号，并拒绝使用它。不过，我拿到了一份视频副本，并把代号重新剪了进去。后来，当情况变得很明显——我们不得不用 Bluetooth 这个词发布时，我拿了一份视频，把标语改成了 “Bluetooth SETS YOU FREE”；下面是这支视频的链接。

[![Image 7](https://lh3.googleusercontent.com/sitesv/AA5AbUD6TeLH7ZK_TrVAiz-rNM0Z1ks9Rgldz3hcmtYQVsEmwHhOmlzpuC7XVVn5Bxwnv0VYGCnIG7FCH1SVCpWNXE098HNlbHDkfWQBon2Lot1zFpcClzghdfCgBZ2eISLyHto0cJ2gL5BK8Y0SbU2S34ZYT_BpvFjuRMSTKyRLZD0QxAOmdFmsbjJxj6cg3WwH9fo49MhAZC5NePA2chM=w1280)](https://www.youtube.com/watch?v=sZYJFqqa4Lk&list=PL_fbfFWItJhOAF2HGJ5aLm_pCOpD2T_-d)

这个时期由市场部门开发的宣传材料中，我最喜欢的之一是著名的 “cutting the cord”（剪断线缆）口号（它出现在一份 Bluetooth 宣传材料中）。这份早期宣传材料的开发，是为了强调我们的一个主要主题：摆脱线缆。我认为这个口号和图形不言自明（我从来不明白为什么我们只用过一次）。

![Image 8](https://lh3.googleusercontent.com/sitesv/AA5AbUDvIMNj43gb9XSC5RQed2SRrSI7EKeyV1EI0_xjX3JUkB1YGf1X6kfvlNFYIHejGqQPgAmGPtHG52HVG436g04Iu9PNtihzuVrBIyOdpO4ypXvsQZy1p7bwlNqLK6mCEijopDeIY-PW-mk3oGA_LLMMV840qrfWedT_a_JpA2782ZyOIVJUCaba7cZehX2KXgONukrH3KvFHIoF=w1280)

在这一时期，还发生了另一个与这个故事有关的有趣事件。作为 Intel 移动部门的一名工程师（我们设计笔记本电脑所用的处理器和芯片组），我拥有许多专利。我的杰出领导 Stephen Nachtshem（Intel 移动与手持设备部门副总裁/总经理）让我代他参加一次关于专利的高管会议，他本人无法出席。

我提前一点到了一个大会议室并坐了下来。开始前几分钟，Gordon Moore 和 Andy Grove 走了进来，坐在桌子尽头，离我很近。虽然我过去也参加过一些有高管出席的会议，但能和 Gordon Moore 开会总是让我很振奋（他帮助 Robert Noyce 发明了平面晶体管/集成电路），而这次我会和 Gordon、Andy 一起开会；非常酷。

会议内容是法律部门提交专利申请的流程。显然，Intel 的专利数量远多于律师数量，所以他们把许多专利申请外包给合同律师。我经历过这个流程很多次，而且有一项我大约 2–3 年前和一位合同律师一起处理的专利让我很困扰，因为它一直没有提交。事实上，那位律师就像从地球上消失了一样。大约 2 年后，有人把那份半成品专利申请拿给我，问我是否还想提交这项专利。我说是的，这是一项重要专利，并问发生了什么。结果发现，那位律师已经离开了我们合作的律师事务所；2 年后，她的办公桌交给另一位律师时，他们在抽屉里发现了这份专利申请。早些时候，我发现我们的竞争对手正在就一项技术起诉 Intel，而我的专利本可以构成这项技术的在先技术。

于是我举手，正在做演示的律师停下来，点了我，我问了一个问题。

“既然你们有这么多合同律师在处理专利申请，你们有没有一个数据库来跟踪这些专利？”

律师看起来有点困惑，要求我进一步说明。我解释说，既然这些专利申请会发给外部合同律师，我们难道不应该记录哪些专利正在准备、何时以及发给了谁吗？这样 Intel 就能跟踪专利状态，并发现是否有任何专利丢失或进度落后。律师表示不，他们没有这样的数据库，然后继续往下讲。

接着发生了一件不自然的事。Gordon Moore——我见过的最友善、最和蔼的人之一——说：“你说没有数据库是什么意思？”然后事情就急转直下。Gordon 开始对那位律师大声吼叫，并开始站起来。Andy Grove 迅速站起来，把手放在 Gordon 肩上，说，没事 Gordon，我来处理。

Gordon 坐下，Andy 开始对那位律师吼叫。我坐在那里想，这也太酷了，我正在和 Andy Grove、Gordon Moore 开会；幸好我不是那个律师！突然，Andy Grove 的唾沫落在了我的笔记本上（当时有很多喊叫，而我离 Andy 很近）；我把它圈了起来，并写上 “Andy Grove 的唾沫”。

不管怎样，第二天我来上班，正走向自己的办公室时，Stephen Nachtsheim 走过来问我。

“Jim，我昨天让你去参加的那场会议到底发生了什么？”我告诉 Stephen，那位律师讲解专利流程，我提了问题，然后 Gordon 开始追问，并生气了，接着 Andy 也开始追问，并生气了。我还给 Stephen 看了笔记本上 Andy Grove 的唾沫。Stephen 脸上露出非常困惑的表情，然后回答说：“别担心这些，我来处理。”

1998 年 2 月，在“名称开发”进行期间，不同公司之间的协议签署也要进行。我们从 1997 年 12 月起就一直在与 Ericsson、Nokia、IBM、Toshiba（当然还有 Intel）谈判；除 IBM 外，我已经让每家公司都同意签署合同。

问题出在协议中的知识产权条款上。它在高层面上基本意思是：如果你拥有任何会覆盖这项技术的 IP，你同意不因其起诉 SIG 的其他成员；这被称为 “Open IP” 协议。对 Ericsson 和 Nokia 来说，签署这份协议非常困难，因为在电信世界里，技术通常通过“合理且非歧视性”的许可来授权。

“非歧视性”意味着你不能选择许可给谁或不许可给谁（这是一件好事），但“合理”这个词并不十分量化。对一家公司来说合理的东西，对另一家公司来说可能被认为不合理。此外，在这种协议下运行一个 SIG，会导致技术因为 IP 地位而被提出（希望获得长期的版税收入流）。

Open IP 则不同，因为你不会从这项技术中获得版税收入，工程师可以基于技术本身的优劣来选择方案，而不是基于他们公司的 IP 地位。

在这个案例中，IBM 不愿为这项技术采用 Open IP 许可，这违反了他们的 IP 政策。此外，IBM 的 IP 由 IBM 内部法律部门拥有，而这个法律部门有自己独立的损益（P&L）。所以 IBM 内部出现了裂痕：法律部门表示 IBM 永远不会签署 Open IP 许可，而移动部门（设计和制造 IBM 笔记本电脑的部门）则希望帮助开发 Bluetooth 技术。更糟的是，我的律师和我打赌，说 IBM 一百万年也不会签那份合同（Brian Epstein，就是我做商标检索时用的同一位律师）。

于是我们安排在北卡罗来纳州 Raleigh 的 Ericsson 场地开会签合同，但我真的不确定该怎么办，因为 IBM 表示他们不会签合同，而我们又需要签署合同，才能启动技术工作。

我想出了一个聪明（但也很蠢）的主意：先让四家公司签署协议，然后继续与 IBM 谈判，之后再把他们作为 promoter 拉进来。为此，我修改了合同，把 IBM 的名字从合同中删除。由于正式 SIG 名称尚未选定，这些合同使用 “Bluetooth SIG” 这个名称起草。

Johann Weber 是 Stephen Nachtsheim 手下的一名欧洲技术员工，非常接近欧洲通信业务。他和我到达 Raleigh 场地后，我把合同分发到桌上，供大家审阅和签署。Johann 常驻 Intel 慕尼黑，一直在帮助 Stephen、Simon 和我把所有公司聚集到一起，支持这个 SIG。Johann 基本上私下认识所有高管，是一个在这类事情上非常有帮助的人。

于是，大家陆续落座时，Johann 和我站在一旁聊天，这时 IBM 的副总裁（Adalio Sanchez）和律师走了过来。

“嘿 Jim，我刚刚看了合同，看起来不错，但我注意到合同里没有 IBM，没有签署的位置。”

Johann 有点瞪着我。哇，我也许应该早点告诉他我把名字删掉了。我解释说，我已经真诚地和 IBM 的律师（主要谈判人就站在他旁边）谈判了 2–3 个月，而他们表示永远不会签署合同。因此，我需要启动技术工作，所以想先与仍愿意继续推进的公司签署 promoter 协议，同时继续与 IBM 谈判，等达成协议后再把他们作为 promoter 带进 SIG。

Adalio Sanchez 感谢我的解释，并表示他想和自己的律师私下谈谈。然后他们走进了一间空会议室。我看着 Johann，他对我笑了笑，说：“你肯定要被开除了。”我想：“我肯定要被开除了。”随后那间会议室里传出非常响亮的吼叫声。Orjan（Ericsson 的 PM）走过来想进入会议室（我们在 Ericsson 的设施里），听到吼叫后说：“我想我待会儿再来。”

吼叫声又持续了大约五分钟。Johann 和我只是沉默地站在那里。我脑子里唯一的想法就是：“我肯定要被开除了。”最后，吼叫停止了，Adalio 和他的律师从会议室出来。Adalio 满脸笑容，而那位律师脸色通红，头发凌乱，情绪很差。Adalio 说：“Jim，抱歉造成混乱，你能不能把 IBM 的名字加回合同里？我们今天会签。”然后他走开了。那位律师留在后面，对我说了大意是这样的话：“你以为这一轮你赢了，但等你们要批准规范时，IBM 永远不会签。”然后怒气冲冲地走了。

Johann 说：“哇。”我则去想办法更新并打印合同。所以，在等合同打印时，我给我的律师朋友 Brian 打电话，告诉他：“猜怎么着，IBM 刚刚告诉我他们要签合同。”他完全不敢相信，这真是好消息。我告诉他我得走了，然后拿起新的 “Bluetooth” 合同，分发出去，并让大家签署。

![Image 9](https://lh3.googleusercontent.com/sitesv/AA5AbUB3-v9Ely1FiWOpJCvY2O6MAKLAAMlSi6Nzb2e-oFcBwD2OUtLtCFSq7sxI7iGyX8YECbqvnfN2GJMWoe-jXgttZC5-lgSESjrXjBFXjix5UvQZhSVkiASIDCioU-JawPQ8V5SEyq-5CTg70mRjqH9bBzxyXMZnp1ePKwKxtZgM1IHtBgnoqqao4kSC1W9-y3MCLKpU1Jo-d5-bvA0=w1280)

当天晚些时候，Brian 给我回电话，说他去告诉他的老板 Carl Silverman，Intel 刚刚让 IBM 签署了一份 Open IP 协议（他们原以为这是不可能的）。但 Brian 一提到我的名字，Carl 就开始大吼。我想了想，把那次高管 IP 会议的事告诉了 Brian：我的问题、Gordon Moore 的问题、Andy Grove 发火、Andy 的唾沫落在我的笔记本上，以及第二天我见 Stephen 的事。Carl 很可能也在那次会议上……

这一组协议提供了条款和条件，使各家公司技术团队能够正式开始共同开发这项短距离无线技术。此外，它创建了会员框架，使 “Early Adopters” 也能够帮助开发技术规范。由于市场小组尚未就 SIG 的正式名称达成一致，这个组织便以其代号 “Bluetooth” 成立。

在名称创建方面，Simon Ellis（Intel 的市场代表，也是 Bluetooth 市场小组主席）与 Intel 的命名主管们协调了 Intel 内部的头脑风暴会议，并主动提出：任何提交最终获胜名称的人可以获得 500 美元奖励。Simon 一直是个很有竞争心的人，他希望 Intel 提出的名字能成为正式名称！作为一个天赋极高的命名人物，我主动把自己邀请进了这些头脑风暴会议（毕竟，我提出了代号，而且我不想错过任何命名乐趣）。我遇到了一群很有意思的人，他们在过去开发名称方面经验丰富；参会者中有人开发过 PCMCIA、AGP、PCI 和 Pentium 这些名称。

在这样一次会议中，开发名称的专业流程大致如下：了解技术的人先向在场人员概述这项技术，并解释它能为人们做什么。主持人把这些属性列出来，然后每个人开始向主持人大声喊出命名想法，主持人把它们写下来。几分钟后，被提出的名称数量开始减少……最终停止……随后主持人把名称按相似主题分组，并开始淘汰流程。

这个精密流程重复了几次，最后产生了 “RadioWire” 作为 Intel 的提案。不过，这个流程是在预定名称投票日期前一周才得到这个名字。Simon 意识到，在投票前只剩一周的情况下，很难为 “RadioWire” 争取支持，于是恳求我至少把投票推迟一周。我必须考虑大局。选择名称在当时其实并不是我们的高优先级事项——推迟选名只会增加印刷宣传材料的成本。此外，根据不同公司的情绪来看，我不认为推迟会是一个受欢迎的决定（他们基本已经认定了另一个名字）。我告诉 Simon，他有一周时间准备；我不会推迟投票。

我们决定在一次全球发布活动上，以正式名称宣布/发布 SIG。活动地点包括英国伦敦、加利福尼亚州圣何塞和日本东京。准备工作进行时，关于我们正在做什么的信息开始泄露出来。我的档案中发现了这样一篇文章（注意，它的日期早于 1997 年 5 月 5 日的发布）。

许多关于这项技术开发的文章开始泄露出来。有些在细节上比另一些更准确（例如，上面那篇文章并不完全准确。Microsoft 和 Puma 是后来才参与进来的）。那篇文章发表后，我确实给 Puma 打过电话，问他们关于这个名叫 “Blue Tooth” 的新产业联盟的事；他们是最早加入 SIG 的 Early Adopter 公司之一。不过，所有文章都提到了这样一个事实：有一个代号为 “Bluetooth” 的开发项目正在进行；这个名字源自一位 10 世纪的丹麦国王；它代表一种短距离无线技术的发展。事实上，这篇文章中专门用一行解释 “Bluetooth” 名称历史相关性的做法，后来也成为相关文章的典型写法。

正如我前面提到的，正式名称的选择是全球发布的关键里程碑，也会启动发布宣传材料的印刷。为满足这些目标，“命名会议”大约在实际发布前两个月举行（发布计划定于 1998 年 5 月 5 日）。这次投票发生在我们的每周管理会议上（称为 “PM（Program Management）meeting”），获胜名称需要获得 5 票中的 3 票才能通过。

在预定投票当天，来自五家 promoter 公司的 Program Management 和 Marketing 人员都参加了会议。会议形式是由市场人员介绍各自提案，随后由 PM 成员投票。Simon 仍然有点不高兴，因为他没有多少时间预先推销自己的提案；他第一个发言。我想，多给他这 15 秒左右的时间，应该能给他成功所需的优势（你相信吗，他从来没有为此感谢过我）。

Simon 介绍了 Intel 的提案 “RadioWire”，并解释为什么这是个好名字：“因为它不是 PAN。PAN 是个糟糕的名字。你们会后悔选 PAN 这个名字。”随后，其他四家公司分别提出了 PAN。不用说，结果是四比一，SIG 选出了它的第一个正式名称。会议休会，市场团队继续制作发布所需的所有宣传材料。Simon 表示，PAN 被选中是我的错，而且他不会再跟我说话。

大约三周后，Ericsson 召集了一次神秘的紧急会议。会议通过电话举行，因为参与者分布在世界各地。Ericsson 的 PM 代表 Orjan Johansson 表示，Ericsson 在 “PAN” 这个名称上遇到了严重法律问题，Jan Ahrenbring 会进一步说明。Jan 随即开始解释，“PAN” 这个名字不能注册商标，我们必须使用另一个名字。事实证明，Ericsson（以及其他任何公司）在投票之后才对自己的提案做商标检索。他们震惊地发现，初步商标检索返回了大约 1,700 条命中结果，使它成为一个商标风险极高的名称。

由于 Orjan 表示是 Ericsson 的法律部门发现了这些问题，我以为 Jan 是 Ericsson 的律师。我把我们的电话静音，问我的小组：“这家伙是 Ericsson 的律师吗？”Simon 已经好几周没怎么跟我说话了，这时迅速宣布：“肯定是。”然后我取消静音，进入了我最擅长的“杀信使”式对话。

现在，我必须解释，在组建和运行一个 SIG 时，你不可避免会和许多律师打交道。这可能是一个非常令人沮丧的过程。现在回想起来，我一定是释放了一点挫败感，因为又一位“在重大活动前最后一分钟出现的律师”制造了另一个问题。Jan 非常抱歉，并表示他们会尽一切可能解决问题。

接着我总结了我们当前的处境：

*       1.   我们不能继续使用 PAN 这个名字——风险太高

    2.   我们需要一个发布用名称（大约 3–4 周后），而且为了开始重新印刷所有宣传材料，我们现在就需要它。

    3.   我们需要一个低风险名称，或者某个已经通过商标检索的名称

结果，唯一另一个有人做过商标检索的名字就是 Bluetooth（谢谢你 Brian），于是所有人很快都明白，我们将以 “Bluetooth” 这个名称发布 SIG。市场部门很快补充了一个后缀：他们会在稍后选择并宣布一个正式名称，而且这应该成为发布时的关键信息之一。

会后，Simon 让我很意外地再次开始和我说话。

“Jim，你不觉得你刚才对 Jan 有点太凶了吗？”

“他是律师，他习惯了。”

“有意思，我还以为 Jan 是 Ericsson 的市场副总裁，而且我不确定他习惯被人吼……”

啊，现在我知道为什么 Simon 又跟我说话了。Simon 获得了双重胜利。第一，他关于 PAN 是个非常糟糕的名称的观点得到了证明（理由完全不同似乎并不重要）。第二，Simon 看到我通过痛骂一位 Ericsson 市场副总裁，把自己弄得很丢脸。接下来的几周，我紧张地等待自己行为带来的后果。

![Image 10](https://lh3.googleusercontent.com/sitesv/AA5AbUDMWJVctsTKAH0eHAgRosQ-zhTE8AnX_TDaUgCT3yf39wn25JsrHX5_xqk1D9gh6gbQdMRxEfWLi4QvvRl6Zu8tJnEZh1A-X7_Fxn2ohI8hfzjjmZxJYRyeS6vPxxTm0WWqgbwzo6mAPRiS3BxSTSSOYHEpgbKeBcdr3kO9AuXEfK8z3Je3ZT8pdNn1H09UPucGakj0daiXf3yA4vw=w1280)

与此同时，LEGO 来到美国与 Intel 进行技术讨论。在这次会议上，有人透露 Intel 正在研究多项无线技术，其中一项代号为 “Bluetooth”。LEGO 的代表非常惊讶，并表示加入和支持任何名为 “Bluetooth” 的开发项目，是他们的爱国义务！LEGO 总部位于丹麦；他们的总部距离 Jelling 原始 Harald Bluetooth 符文石大约 10 公里。

由于 Simon 又开始跟我说话，我确实指出：我提交了 Bluetooth 这个名字，而这也是我们将要公开发布的 SIG 名称，因此我有权获得他提出的 500 美元奖金。Simon 表示，我们是用代号发布，而不是用正式名称发布；他的奖金是给正式名称的（并让我不要抱希望）。

这次快速改名带来的一个额外好处，是留下了大量 “PAN” Polo 衫和其他 “PAN” 纪念品。我保存了这样一件纪念品，一件 Ericsson Polo 衫，上面有 PAN 标志。要是没有那 1,600 个网站已经用过 PAN 这个词就好了……

![Image 11](https://lh3.googleusercontent.com/sitesv/AA5AbUBpTIgtOTfGZNr2YPyKSq7vb3JaVeLN6ykt3wSdArjToF0cWPjBMpMp_kWDd-7H19YrwVDl8NeL_GAmGxTWCpjQZf24Wdv8b3e4--M_zG_MOuhW_LEqr3UxZyl-9rxLdxJsZS3kN2wvIMXLgo8FAYuNeTtjXNw2Z_lWhcQpYFiHSk2UaTV5B7HvQHfvW0XpSquQKjfnasdxTWGwU08=w1280)

为了支持发布，市场部门希望给媒体提供一件纪念品，让他们记住这次活动。有人建议，我们应该发放一块 Harald Bluetooth 符文石的微缩版，也就是我们当时在投影片中展示的那块（在上一篇文章中，我们展示过那块著名的符文石，并做了增强处理，让 Harald 一手拿笔记本电脑，另一手拿手机）。大家同意了，Anders Edlund（Ericsson Bluetooth Marketing）被赋予了制作这些符文石纪念品的任务。我想象的是包着塑料的泡沫石头，正面印着 Harald 的图片。然而，Anders 让所有人大吃一惊：他真的把 Harald 的图像刻进了大约 6 英寸高的真花岗岩石头里！拥有一块这样的原始符文石纪念品，是一种罕见的荣誉。

![Image 12](https://lh3.googleusercontent.com/sitesv/AA5AbUALL-3c8vwkQcTV0es83oNnbkx6ndlZ1UPY4JvtleK82tTiD44CQ36wCcr9YvNqP0m8n2oJkXOqOaGbypDDyOvqLjTWq-ozUuTSEyOuWGO6domEXHZNOyvN1y4z23k87V3Y4q4exNAmIeNwuMKYy5TWGx_oM1lNADrLZzAZfhAzpbFteYc_xbkgwn6B7VKo6ABjWbiLNy7IJc7nz0Y=w1280)

5 月初，全球发布举行。Simon Ellis 和我参加了伦敦发布会（不过我也收录了一组所有发布会的拼贴照片）。我们聘请来安排活动的公关公司叫 Edelman，活动前一天我们与他们会面。在这些会议上，我们发现 Edelman 的人对发布会并不满意，我最初把这归因于 “PAN 改名事件”。不过，Edelman 的人非常明确地表达了他们的不满。首先，他们认为 Bluetooth 这个名字很丢脸，并建议我们完全不要使用。他们觉得媒体不会认真对待我们，而且它唤起的是牙齿卫生差的形象，而不是酷炫设备以前所未有的方式互动的形象。第二，他们讨厌 Bluetooth 石头纪念品；这让我们很难避免使用 Bluetooth 这个名字，而且他们觉得会出现大量关于 “Bluetooth will drop like a rock” 的标题，配上那块臭名昭著的符文石图片。Simon 解释说，许多技术媒体已经听过这个代号，不必太担心这个名字（他可能还提到 Edelman 尚未收到付款，而我们正在开支票）。

后来我们发现，美国的公关团队干脆拒绝发放符文石。不过，Simon 和我后来重新拿回了这些石头，并把它们作为纪念品送给加入 Bluetooth 团队的人，或者作为激励送给加入 Bluetooth SIG 的公司。Simon 和我在“伦敦石头叛乱”刚开始时就制止了它，但日本发布团队认为这是一件出色的纪念品。在伦敦发布会上，Simon 确实抽时间亲自把我介绍给前面提到的 Jan Ahrenbring——Ericsson 市场副总裁兼兼职律师。

结果，发布会反响很好，并产生了大量标题新闻，把 Bluetooth 这个名字嵌入了各地人们的脑海。Edelman 做得很好，我们后来发现，他们还因为这次发布所产生的宣传量而获奖。

[![Image 13](https://lh3.googleusercontent.com/sitesv/AA5AbUAXD9rmhYJ7mLTvhVOhgvk_wnYL7fqn_Y-_78l7Uw4WzGGY3VbmXHb3NVAzDYLGeFmvfWX0DymUCvI6CTR5guUyL0kercnbKB5uYsa6r3ttZy5hSicIaRg_-jzvGaBjn5qqUHePyD-uKPZS2wtKh4fd0LmXl4T77HDGCy5NB21s01QUzzoVet5Yc5SpbihnL9RggyeqHmhs4aLo=w1280)](https://www.youtube.com/watch?v=ivb-Ln6Sm3s&list=PL_fbfFWItJhOAF2HGJ5aLm_pCOpD2T_-d&index=5&t=0s)

![Image 14](https://lh3.googleusercontent.com/sitesv/AA5AbUBpz934mosUZZ2vEmz5NcakjWrGQ9mbcD5l3q6oeIdLI1eCak_WZ48xCWmd2UK5lF3YGSPtkNj8sV6XGBoYMSL063U0CDGEwUSclhGDDluxuA_wmR29Ie2CZZVErNvceruu7yX4uzaB6beDzpUiSeweCbKRmqYnNhaoOpyPfPvoRhb3XLkUETEyd0NxN1Z8dmAgG-dtrz9Mndhok-Y=w1280)

SIG 以新的 Bluetooth 代号发布后，我收到了我的朋友 Sven Matthesson 发来的邮件。他告诉我，Ericsson 的 CEO 给他打电话，问这项技术是怎么得到 Bluetooth 这个名字的，而他不知道该怎么回答。我提醒 Sven，多伦多那晚他给我讲了《The Longboats》这本书的故事，书中那位丹麦国王叫 Harald Bluetooth；我也提醒他，当我回家后，在我买的那本《The Vikings》中看到了 Bluetooth 的符文石图片，我只是觉得这会是个很棒的代号。我还提醒他，尽管 IBM 提出了 PAN 这个名字，但他们从未对该提案做过商标检索（而所有人都以为他们已经做过商标检索）。

Sven 回复说：

“我不能告诉 Ericsson 的 CEO，我们是在多伦多一边灌啤酒一边想出这个名字的。”

然后他组织了一个他觉得说得出口的故事（我现在已经没有原邮件了，所以全凭记忆）：

“Jim 和我过去常常讨论历史，我给他讲过《The Longboats》的故事，里面 Harald Bluetooth 是国王。Jim 提议把它作为代号，因为 Bluetooth 联合了丹麦、瑞典和挪威，正如我们希望这项技术能够联合手机和笔记本电脑一样。”

我告诉 Sven，我更喜欢那个灌啤酒版本，但这个听起来也不错。然后他给 Ericsson 的 CEO 发了一封邮件（抄送给了我，但我把那封邮件弄丢了）。

最近我去了加利福尼亚州 Mountain View 的计算机历史博物馆，他们在那里有一个关于 [Nils Rydbeck](https://www.computerhistory.org/revolution/mobile-computing/18/341/2322) 的展览；我在 Bluetooth 开发过程中见过他几次，他是手机领域的传奇人物之一（他基本上发明并开发了第一部实用手机）。他们采访了 Nils Rydbeck，谈到手机和 MC-LINK/Bluetooth 的开发。在接近结尾处，他谈到 Bluetooth 技术是如何得名的（3:39）。他说 Ericsson 给了 Intel 一本非常好的书《The Longboats》，书里的国王就是 Harald Bluetooth。

我心想，这很奇怪，Sven 是在发布几个月后才把那本书给我的（我现在还留着）。然后我想起了和 Sven 的邮件往来。我只能想，见鬼，要是能让 Nils Rydbeck 讲到我和 Sven 在多伦多灌啤酒，那该多酷啊！

尽管如此，市场小组仍有一项未完成的任务，于是继续前进。他们下一次尝试会更完整。市场部门在开展一项面向短距离无线技术不同名称的全球焦点小组研究时，同时进行了商标检索。

由于 “Bluetooth” 已经获得了大量关注，他们也半开玩笑地把这个名字纳入研究。我认为在这个时候，Simon 和 Anders 都开始相信，考虑到围绕 Bluetooth 产生的宣传量，改变这个名字几乎已经不可能了。

全球焦点小组研究的结果相当有趣，我希望自己现在还留着一份（我接下来讲的都是凭记忆）。我记得焦点小组研究在伦敦、旧金山、东京和墨西哥城进行（也许还有其他几座城市，我漏掉了）。我已经不记得所有被测试的名称了，但我认为最受青睐的名称之一是 CoMeGo（Come、Go 和 Me 的组合词）。

其中一个问题是：“当你听到这个名字时，你会把它和什么联系起来？”Bluetooth 的最高频回答是“牙齿卫生问题”（或类似说法）。当被问到会把这个名字和什么行业联系起来时，Bluetooth 的最高频回答是“牙科行业”。当被要求仅从受欢迎程度对不同名称打分时，Bluetooth 在除墨西哥城外的每座城市都排在最后；在墨西哥城，它被评为第一（没人知道为什么）。

这项调查进行期间，Bluetooth 这个名字继续越来越受欢迎。Toshiba 的 PM 代表 Warren Allen 提到，在一次 PC Week 采访结束时，采访者评论说：“不管你们做什么，都不要改这个名字，它是最好的部分。”

事实上，市场小组此时开始认真怀疑改名是否明智。公司通常要花费数亿美元，才能创造出刚刚围绕 “Bluetooth” 神奇出现的那种名称认知度。虽然消费者也许不知道 Bluetooth 是什么，但你几乎可以和任何技术公司交谈，而他们不仅知道 Bluetooth 代表一种短距离无线技术，还知道历史上存在一位同名的 10 世纪丹麦国王。

就我个人经验而言，我创建过许多技术标准，但没有一个是我的家人能够理解或关联起来的。Bluetooth 不同，它不仅是我的母亲或父亲能够理解的东西（替代一根线缆），也是一种他们能在本地报纸上读到、或在电视上听到的技术。很多时候，我会收到邮件或信件，里面夹着提到 Bluetooth 的剪报！能参与某个（终于）连我的父母和亲戚都能识别并关联起来的项目，感觉很好。

随着 SIG 的知名度增长，会员数量迅速上升，媒体文章数量也持续增加，而这一切都在 Bluetooth 这个名字之下进行。显然，市场小组必须解决正式名称问题。焦点小组研究显示，CoMeGo 在所有市场中的测试表现最好，但现实已经摆在眼前：行业知道 Bluetooth 是什么，却不知道 CoMeGo 是什么。此时改名会是一件风险极高的事。

于是，市场小组向 PM 小组提出了如下建议：

“焦点小组研究显示，CoMeGo 在我们测试的不同地理区域中表现极佳。然而，我们认为创建一个强品牌可能会对我们现有母公司品牌（Intel、IBM、Toshiba、Ericsson 和 Nokia）构成威胁。另一方面，焦点小组研究显示，Bluetooth 完全不会对我们现有品牌构成威胁；此外，Bluetooth 已经在我们的目标行业中与短距离无线技术建立了强关联。因此，我们建议 SIG 保留 ‘Bluetooth’ 作为该技术和 SIG 的正式名称。”

于是，Bluetooth 终于成了正式名称。我立刻去找 Simon，要我的 500 美元奖金。他的第一反应大意是“去死吧”，但大约三个月后，我收到了一份奖励通知，因为提交获胜技术名称而获得了 200 美元。我立刻打电话给 Simon，提醒他奖金是 500 美元！他说我能拿到 200 美元已经很幸运了（我还在等剩下的）。

偶尔，我会在互联网上搜索 Bluetooth，衡量它的认知度。一开始，我会得到大约十几个命中结果，全部都指向那位丹麦国王（多半出现在族谱网站上）。大约在 Bluetooth 成为正式名称的时候，同样的搜索会返回数百个结果，其中大多数关于这项技术，另有几个关于历史上的国王。2002 年，我搜索 “Bluetooth”，得到超过 618,000 个结果（第一条结果直接带我到 Bluetooth 主页）。今天我搜索 “Bluetooth”，得到 1,360,000,000 个结果；我看到第一个专门关于历史上的 Harald Bluetooth（而非他的电子对应物）的结果出现在搜索结果第 13 页。这个名字确实已经变得极为流行。

所以，现在你知道了围绕这项技术命名的主要事件。这个过程既不顺利，也不可预测；我相信，参与其中的人没有谁敢预测这项技术最终会被称为 “Bluetooth”。焦点小组研究表明，这个名字完全不能让人联想到我们试图完成的事情。考虑到命名过程中发生的这些事件，我不确定这种现象是否还能再复制一次。

为什么这个名字会成功？也许是因为那个古雅的历史典故。也许是因为这个奇怪的名字会让人想到蛀牙，然后突然出现一个“啊哈”时刻：它原来指的是一个历史人物，而这让这个名字很难忘记。也许那个容易理解的使用模型（替代一根线缆）进一步帮助人们把这个奇怪的名字和这项技术联系起来。我自己也不太确定，不过我觉得，如果有一篇哈佛案例研究用 Bluetooth 作为案例之一，分析什么造就一个流行名称，那会很有趣。

最后再讲一个关于符文石的故事。1998 年末，我因一些 SIG 事务去了瑞典 Lund，并拜访了 Per Svensson。Per 是我们最初开始创建 SIG 框架时，我合作过的 Ericsson 早期经理之一。Per 和我都对历史非常感兴趣，而 Per 对我也感兴趣于斯堪的纳维亚历史感到非常高兴。Per 刚刚去过 Jelling——原始 Bluetooth 符文石所在的地方——并给我带了一本英文小册子。我很高兴，因为这本小册子里有一些非常漂亮的符文石照片，也有一段关于 Gorm the Old 和 Harald 的不错历史介绍。

我回到 Santa Clara 后，本来打算用这张质量更好的照片，为那块石头制作一个新的位图。于是我扫描了照片，并用高分辨率激光打印机打印出来。当我走进办公室时，电话响了，我把打印件放在桌上，拿起电话。Jeff Schiffer（他做了很多 SIG 的监管工作，涉及安全、频谱和模块合规）走进我的办公室，拿起那张图片开始盯着看。突然，我听到 Jeff 说：“嘿，他手掌上的那些不是洞吗？”这立即引起了我的注意。我一把拿过照片（一定是把电话掉在了地上），开始更仔细地检查图片。确实，他的手掌上有暗点。

![Image 15](https://lh3.googleusercontent.com/sitesv/AA5AbUBoEzeAnd5qrXZH9GsT4ptrroCo4CuxRy2xHl2wkk39OxFLzn7uOn_t-FRBcmsIBm0SRWA2nQwkFtIJNaLYkRy6SPaDUTmRjyZeX-hUbc7Dl-qK2EowpzACcNM7Ir8GbQke6l5R5i9x3VI5_7dG2Hxh5jwyZE1d4jWoX2cHafOX3qt8k_2k8mDEjpl5KyE88CQG8KO7K3jztwQu=w1280)

又做了一点进一步调查后，我发现有新的资料把这幅图描述为基督像（我们一直想知道他头周围的那些圆圈是什么，这下谜团解开了）。后来，一位来自 Compaq computer 的朋友告诉 Simon 和我，哥本哈根博物馆里有一件 Harald Bluetooth 石的复制品，并且确实把这个图像称为基督。

不用说，这非常令人担忧。我生活在这样一个国家：在 60 年代，当 John Lennon 表示 Beatles 比基督更受欢迎时，人们曾焚烧 Beatles 唱片。而现在，我竟然无意中把基督用作 Bluetooth 技术的代言人！我不确定该怎么做，于是和 Simon 讨论了这个情况，我们决定低调停止使用这块石头的图像。我还要说明，我去过 Jelling，也看过原石；我没有看到他手掌上有任何暗点！

不幸的是，我们还收到了丹麦人的投诉。他们认为 Harald Bluetooth 符文石是这个国家的“洗礼”石，因为它是在君主制建立之时竖立的（Gorm the Old，Harald 的父亲，是丹麦第二任国王）。在这幅图像上画一台笔记本电脑和一部电话，就像在自由女神像上涂鸦。

自从选择 Bluetooth 作为 SIG 的正式名称以来，SIG 一直试图把 Bluetooth 这个名字注册为商标（我可能会因为在写这个故事时完全无视商标规则而收到 SIG 的正式通知，不过我写的是发生在商标注册之前的事件）。很遗憾，我们唯一遇到的驳回来自美国商标局。商标局表示，“Bluetooth” 这个词已经等同于短距离无线技术，因此不能注册为商标！SIG 确实解释说，是 Bluetooth SIG 创造了这种关联，最终 SIG 获得了 Bluetooth 商标。
