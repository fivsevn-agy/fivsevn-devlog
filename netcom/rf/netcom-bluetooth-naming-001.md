---
id: netcom-bluetooth-naming-001
title: 蓝牙命名的由来

module: netcom
submodule: bluetooth
topic: naming

type: translation
status: active
canonical: false

summary: >
  本文翻译 Jim Kardach 关于 Bluetooth 命名过程的回忆，记录蓝牙从内部代号、商标检索、SIG 成立到最终成为正式名称的关键事件。
  文章同时说明了 Harald Bluetooth、耶灵符文石、产业联盟和营销命名之间的历史关联。

parents: []
related: []

tags: [bluetooth, wireless, naming, sig, intel, ericsson, history]

audience: [self, public]
languages: [zh]

maturity: stable
confidence: 0.90

visibility: public
source_of_truth: external

original_title: Kardach - Naming Bluetooth
original_source: Kardach.com
original_url: https://www.kardach.com/bluetooth/naming-bluetooth
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

![Image 1](https://lh3.googleusercontent.com/sitesv/AA5AbUAaOsXOawYqo3coy3YbDbBGCJIPzgi5OU5uJnPyjXd3wX_oPKO9wQM3V9G0W8s1uWe23IPXj19ebbyRCeHBzQfTJfjZXPixAc7H5lyauJNGFl3OsJnhcL4xzV-Mlx2KoXttUboWDYZ99_molKR-QHm3JvhEMT8MtUzMx84QpEg2f_Y_n9ICgGdYCf2bUUbM4U66l3XY2jh0Hifr=w1280)

> 图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

首先，我想感谢我的朋友 Vince Holton，感谢他允许我更新这篇文章，并把它发表在最后一期 *Incisor* 杂志上（谢谢 Vince）。Vince 从一开始就在现场。大约 20 年前，在 Bluetooth Conference 的休息时间里，我们坐在蒙特卡洛 Hotel de Pari 的一家酒吧里，我讲了这个故事。故事讲完后，Vince 走过来问我是否愿意把这个故事写下来，发表在 *Incisor* 上。我让 Vince 看看桌子，桌上堆满了空啤酒瓶，并表示因为我讲了这个故事，所以我一瓶啤酒都不用买。Vince 说，因为那天是 6 月 8 日（Bluetooth Conference），蒙特卡洛大奖赛刚刚结束，赛道设施还没有拆除。另外，他有一辆蓝色法拉利；如果我愿意写这篇文章，他就带我绕大奖赛赛道跑一圈。Simon Ellis 插了进来，说他必须接管谈判。Simon 重新谈判后的结果是：我会写这篇文章，而 Simon 和我都能绕蒙特卡洛大奖赛赛道跑一圈。

[![Image 2](https://lh3.googleusercontent.com/sitesv/AA5AbUBQZpzv0nJeN2i8lexauDa2M4Pv06_zqiMK0lrOfrx2TdmZGi5qQVgH7FHwOm2nAt3G1duEB1m8ACL6uAPIuzNlg20lOdS2wnChdFAwtXuq4DGd3CEU-aVXWx1RUQDsjlPdyXVPxA9oq0Lo55dl0yvPtAEvEoShtC26lc4monMwzsyhT2BdpMdl6si6GRwNxYI9qWEXSjQ5NLsgizI=w1280)](https://www.youtube.com/watch?v=A1UdtDld-z8&list=PL_fbfFWItJhOAF2HGJ5aLm_pCOpD2T_-d&index=3&t=0s)

> 图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

多年来，我已经把这个故事写过几次，大多数人会指向我的其中一篇文章（最早发表在 *Incisor* 上的三部分文章，以及几年后在 [EE-Times](https://www.eetimes.com/tech-history-how-bluetooth-got-its-name/#) 上发表的较短版本）。不过现在我有了更多认识，也已经从 Intel 退休，所以决定更新最初那篇文章。它很长，但确实是个好故事。

这个名字借自 10 世纪的丹麦国王 Harald Blåtand，英文名为 Harald Bluetooth。在丹麦，他很有名，因为他曾在丹麦旧都耶灵（Jelling）立起一块符文石。符文石是一种斯堪的纳维亚纪念碑，用来纪念某个场合或事件。这是两块符文石中较大的那一块，用来纪念 Harald 的父亲、丹麦第二任国王 “Gorm the Old”，也纪念 Harald 自己的一些功绩。这块石头约 2 米高，底部约 2 米宽，有三个面（像金字塔一样）。其中一面覆盖着文字（用符文书写），概述他的成就；第二面是一条缠绕在藤蔓中的龙（有人告诉我，这象征基督教与旧宗教之间的冲突）；第三面则刻着国王本人的图像。

第二块石头由 Harald 的父亲 Gorm 竖立，用来纪念他的妻子 Thyra。正如我后来才知道的，这几块特定的符文石被视为丹麦的“洗礼石”，因为它们是在丹麦形成的时期附近竖立的。

后来我去耶灵看这些真正的石头时（和我的好朋友 Orjan Johansson 一起，他是 Ericsson 的 Bluetooth 项目经理），有人告诉我们，这块石头曾经失踪了 600 年。显然，Harald 曾因为丹麦的宗教问题与他的儿子 Sweyn Forkbeard 发生争执。Harald 刚刚使王国基督教化（约公元 960 年），而 Sweyn 认为他们应该回去崇拜旧神（Odin、Thor、Frey，等等）。Sweyn 赢得了这场争论（并在此过程中放逐了他的父亲）。由于这块符文石赞颂 Harald 使丹麦人基督教化的功绩，Sweyn 便把它埋了起来。大约 600 年后，一位农民对自己农场上的一个大土丘感到好奇（丹麦是一个非常平坦的地方），于是重新发现了这块石头。

![Image 3](https://lh3.googleusercontent.com/sitesv/AA5AbUAgtTL75w7lfA48o4BGrXoJAdpeOX9ATparAXdkTXp5E8Omh8cay1iNUx-tSj-r7l4F3BwLWh0arEdvWfp0q8wMhT5p4_C-QWCIVWPtIY3r7vBQ5w_EdPbljZ_vvUZ8tPJTtrH62C4fgFBAAkFE3zu0M4riDvt00OxiDPrWROBFUHU7Joibw-DEY82tmASZQrqMr_b0MVVV4ZiDLvY=w1280)

> 图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

Orjan（右）和我（左）在丹麦耶灵看 Bluetooth 石（我身高 6 英尺 2 英寸，最左边是较小的 Thyra 石）。

回到 1997 年，在组建一个短距离无线 Special Interest Group（SIG）时，我并不知道这些。当时我正在与 Ericsson 和 Nokia 合作；它们也有短距离无线项目，我们希望创建一个单一标准。Intel 的项目叫 “Biz-RF”（Business RF），Ericsson 的项目叫 “MC-LINK”，Nokia 的项目叫 “Low Power RF”。那时我们正在决定，是应该成立自己的组织，还是加入一个已有的标准组织，然后在这个现有组织内部开发这项技术。Ericsson 和 Intel 都有成员参与一个现有 SIG，名为 Home-RF。Home-RF 希望开发一种面向消费者的无线技术，我们最初的想法是看看能否利用这个 SIG 来开发我们的技术。

为此，Ericsson 的 Sven Mattisson 和我在加拿大多伦多举行的一次 Home-RF SIG 会议上做了演示。我介绍了 Biz-RF，Sven 介绍了 MC-LINK。我们这些令人困惑的提案得到的反应不冷不热，也正是在那时，我意识到这个项目需要一个所有人都能使用的代号。Home-RF 会议结束后，Sven 和我决定复盘一下，并且在多伦多的酒吧里比较一下瑞典、美国和加拿大啤酒。

喝啤酒时，我最喜欢讨论的话题是历史，所以我很自然地请 Sven 给我讲讲斯堪的纳维亚历史。我说，我对斯堪的纳维亚的了解，只包括那些戴着带角头盔、四处劫掠的维京人，以及他们都是疯狂的首领。

Sven 解释说，虽然他不是历史专家（他对无线电更懂），但他相当确定维京人的头盔上从来没有角，而且《布偶秀》里的 Swedish Chef 是瑞典人长期试图摆脱的一种刻板印象。不过，他读过一本名叫 *The Longships* 的书，那是一本关于维京人的历史小说；他就按照这本书来讲述自己国家的历史。随着夜色渐深（我们也从一家酒吧转到另一家酒吧），Sven 给我讲了一个年轻瑞典小伙 Röde Orm（Red Snake）的故事。他去参加了一次 “Viking”；这个词表示一次为了贸易、发现和/或冒险而进行的远征。这个故事发生的时代，正是 Harald Bluetooth 国王在抵御他的儿子 Sven Tveskäggs（Sven Forkbeard，约公元 940 年），以保卫自己的王国（挪威、丹麦和瑞典的部分地区）。

![Image 4](https://lh3.googleusercontent.com/sitesv/AA5AbUCSzQ7R4f_741niBkZdyIjZdF0TIBwEru38XIG1CiCc2MRs7Lv7QgwGYPKA0XXsZZ7vzSxtbFo4m1stivLsxeJAI6xMd4yZft3dhywo-_JirO9YHQcHLBnYYFyEDvSLl7_hPUwceVtQ2w_X30r8SBkm5ocMjfgVXyoI9-FXm401aQqEE3OD8F878_ogp2eeKLZNMWoGHckWlSxL0j8=w1280)

> 图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

我回到家时，一本我订购的斯堪的纳维亚历史书正在等我。我翻看 Gwyn Jones 的 *The Vikings* 时，看到一张岩石的照片，上面刻着一个人。照片说明写着：“Runic stones from Jelling in Jutland erected by Gorm the Old and Harald Bluetooth”；书中的文字说明，这张图片描绘的是 “Chivalry of Harald”。符文石上有一段铭文，内容是：“King Harald had this memorial made for Gorm his father and Thyri his mother: that Harald who won for himself all Denmark and Norway, and made the Danes Christian”。

![Image 5](https://lh3.googleusercontent.com/sitesv/AA5AbUDq5roQsA9KQi22GTtF1OmEUtKTd9o4Zz8_ZSmvl8Ccz1SH_BZb8VqeKkdEmmrgO-fpSXCpzldj9VTBjPZYdpSsR6jie_oFl-BLhfl6-RNtk13FYBes3LGylSddC7auBd0fAx8A5NskuxtYvGRn_xu2XsqRCONIu-YKg20t1S_816HRUN6B-0_jippkOhM-i2x3HdCOc9Dm20UO=w1280)

> 图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

我其实已经不太记得多伦多那晚的许多细节了，但 Bluetooth 这个名字从我的记忆里浮现了出来。我想到，这个名字与斯堪的纳维亚历史之间的联系（一位统一了挪威和丹麦的 10 世纪丹麦国王）、那块带有 Harald 本人图像的符文石，以及 “Bluetooth” 这个奇特的词，都可能成为这个项目相当不错的代号。

我把这块岩石的图像数字化（此前我用 Sharpie 记号笔把 Harald 标了出来），并制作了一张主题为 “Bluetooth” 的幻灯片，上面有几条要点：

这是他在首都耶灵（Jutland 中部）竖立的两块符文石之一

*   这是石头的正面，描绘 Harald 的骑士风范。

    *   石头上的铭文（“runes”）说：

    *   Harald 使丹麦人基督教化

        *   Harald 控制了丹麦和挪威

        *   Harald 认为笔记本电脑和蜂窝电话应该能够无缝通信。

星期一，我把这个提案拿给 Simon Ellis 试探反应。他当时是 Intel 移动数据业务的市场经理。我告诉 Simon，我想把项目名称从 “Biz-RF”（Business-RF 的缩写，我们总是把它缩成 “Bizarre-F”）改成 Bluetooth。Simon 表示他认为这是个坏主意（也就是说，他发出作呕的声音，并用手指指向自己的喉咙）。然后我给他看了那张符文石的图片。

他从我手里拿过幻灯片，研究了几秒钟，然后说：“你能在他手里画一台笔记本电脑和一部手机吗？”我很快更新了图片，把它交还给 Simon。Simon 随后评论说：“我喜欢它。”但他很快补充说明，这只是一个代号，正式公开宣布之前，市场团队会挑选一个合适的名字。

到那时，Simon 和我已经在不同项目上合作了将近 12 年，我们喜欢在工作中加入一点幽默。Bluetooth 这个名字代表一位 10 世纪的丹麦国王，他把丹麦人、挪威人和瑞典人聚到一起（正如我们的项目把 PC 和电信产业聚到一起），但这个名字听起来也很滑稽。让我们觉得有趣的是，到了某个时刻，Andy Grove 或 Bill Gates 将不得不板着一张严肃的脸，在观众面前说出 “Bluetooth” 这个词。

![Image 6](https://lh3.googleusercontent.com/sitesv/AA5AbUDvJtZgaiWdFx1mD7vcwOUrRzvMz9x2_l88kDw8WKbKhghPmfT0C7cYDT-E2_PvFCvO1ZfqTKD-d7Y0weK7mmP3grL2-kez1xWmDP8eYOwuYFXxm0QlTdqJ3dg-ohUdq4W7S7gSdoXrXOjic_tu0KqVAAQAClf9Zt8tuegtYJ5eOE5Q_ZUyhz3Li5shde4iMIdI4MG8RtDZekiAxjY=w1280)

> 图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

下一步，是让 Intel 批准这个名字作为代号使用。我去找我的老板 Phil Wennblom，并表示我们会把这个新的无线电项目称为 “Bluetooth”。他告诉我，“Bluetooth” 是个糟糕的名字，而且政策要求用北美的一座山或一条河来命名。我把这理解为批准，于是去找 Simon，并阐述说这一定是个绝佳代号，因为 Phil 很讨厌它。Simon 表示同意，但认为我们应该把该做的都做完，去取得我们的总经理 Stephen Nachtsheim（我老板的老板，也是 Simon 老板的老板）的批准。于是我们制作了一张带有那幅漂亮符文石图画的幻灯片，并解释了这个代号的来源。

我们把这张幻灯片打印出来，放在 Stephen 的椅子上，并附了一张便条，说明如果他在本周结束前没有反对，我们就会推进这个代号（Stephen 恰好接下来两周要去欧洲出差）。

要让这个代号获得批准，下一道障碍是让法务做商标检索。我很快给我们的律师发了封邮件，请他对 “Bluetooth” 这个词做一次商标检索。我很快收到回复：

Jim，

你绝不可能把一个项目命名为 “Bluetooth”；我们要求代号必须是一条河、一个湖，或者一座城市！

我试图快速虚张声势一下，声称 Bluetooth 实际上是一个德国村庄名称的英文译名，而且我希望在一周内完成商标检索。他很快回复：

想得挺美，没戏。给我一个河流的名字。

接下来我解释说，这是一个 Special Interest Group 的代号，涉及另外五家公司，其中四家公司没有这些规则，请他在一周内完成检索。

假设商标检索会干净通过，我们随后开始通知 Intel 其他部门：项目名称将发生变化。大家的反应后来变成我们会习以为常的一句话：“你们疯了，我们不能把一个项目叫作 ‘Bluetooth’！”不过，我的经理允许我们继续推进。他的理由是，任何头脑正常的人都不会允许这个项目被称为 “Bluetooth”，所以这个名字会在任何公开宣布之前被改掉（至少他是这么想的）。

一周后，我终于收到了来自法务的关键邮件：

意外，意外，没人把 “Bluetooth” 注册为商标。

我并不意外。

1997 年 12 月，这个“即将成立”的 SIG 的所有主要参与方（Intel、Ericsson、Nokia、IBM 和 Toshiba）第一次在瑞典隆德举行面对面会议。Simon 和我讨论过，怎样才能让其他成员同意一个 SIG 名称（最简单的事情往往最困难），最后我们同意，就在动身参加会议前，发出一套幻灯片，概述 “Bluetooth SIG” 的初始目标和计划。我们制作了一套幻灯片模板，每一页都带有那块“被修改过的符文石”。

在瑞典隆德的会议上，我们刚开始做初始介绍，就立刻有人问：“这个 Bluetooth 是什么？”我们解释说：“每家公司都在使用不同的代号，而作为一个 SIG，我们需要一个单一代号来帮助识别我们的共同努力。我们挑选了一个很难与短距离无线技术直接关联起来的代号；同时，它也象征计算机产业和电信产业的联合，就像 Harald 曾联合丹麦人和瑞典人一样。”

全场一片沉默。

Simon 很快补充说：“而且，这只是一个代号，等市场团队为 SIG 想出一个‘正式’名称后就会替换。”

随后，谈话突然爆发出来，各个小组开始讨论 SIG 的“真正名字”应该是什么。我瞥了一眼 Simon，他也正看着我并咧嘴笑着。我们都知道，SIG 会继续以 “Bluetooth” 这个代号往前推进。

虽然市场团队被赋予了提出正式名称的任务，Program Management（PM）团队还是决定帮他们一把（尽管市场团队反对），进行一次快速的命名头脑风暴。Ericsson 的市场人员已经在努力开发名字，并提出了一个最令人难忘的：

Flirt —— “靠近而不接触”

我至今仍困惑为什么这个名字没有被选中。另一个候选名是 “Conductor”——使用这项技术的设备可以把一整支设备“乐团”“指挥”成一场和谐的生产力交响曲。然而，会议室里某位工程师头脑指出，“conductor” 也是一根电线里的金属部分——而这本来应该是一项无线技术。

另一个提案是 “PAN”，即 “Personal Area Network” 的首字母缩写。有些参与者认为，对于一项最终面向消费者的技术来说，首字母缩写太“工程师化”。此外，PAN 只代表为这项技术开发的三个使用模型类别之一（网络接入、外围设备电缆替代，以及 PAN）；我们不希望过度强调其中一种用途。

隆德的头脑风暴会议没有得出结论；我们必须开展进一步研究来寻找名字。我相信，每个离开那场会议的人都意识到了挑选一个名字会有多难，而我们还必须开发这项技术（这也是另一项困难任务）！

与此同时，技术工作继续推进，Intel 委托制作了第一支 Bluetooth 使用场景视频，该视频是在 1997 年圣诞假期期间开发的。视频讲的是一个笨手笨脚的销售/市场人员，需要做一次重要演示，却被锁在储物间里，最后被 “Wireless-RF” 解救。我不得不向 Simon 抱怨：“一支关于某项技术的视频，不应该提到这项技术的名字或代号吗？”而且 “Wireless-RF sets you free” 这句口号并没有推广这项技术的名字！Simon 表示，虽然代号是 Bluetooth，但正式名称还没有选定，他们希望使用一个通用名称，这样即使正式名称宣布之后，这支视频仍然能继续使用。进一步追查后发现，负责这支视频的市场工程师其实并不喜欢这个代号，并拒绝使用它。不过，我设法拿到了一份视频副本，并把代号重新剪了回去。后来，当显然我们必须以 Bluetooth 这个词发布时，我又拿了一份视频，把标语改成 “Bluetooth SETS YOU FREE”；视频链接如下。

[![Image 7](https://lh3.googleusercontent.com/sitesv/AA5AbUCwntQV0WNnR_JQ5D9FnJDzTP15IpzlvYo-GO4CJG9-nXNfFH6cEITA7suULOSECxaDFPh3lkGVcxDd0Ne1ZkTXTwzUR_Z4dIGxUMFfRKRw09DRhSgataGLqBYNXUGLSE1N-Dvo_ocIeQkFNCkfQTzqQUh2NGQrGERtH3pzzslaRtiJ9Fc2nE5lb98iroSAdK9rTIQOvMkir097llo=w1280)](https://www.youtube.com/watch?v=sZYJFqqa4Lk&list=PL_fbfFWItJhOAF2HGJ5aLm_pCOpD2T_-d)

> 图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

当时市场部门开发的资料中，我最喜欢的一件，是那句著名的 “cutting the cord” 口号（它出现在一份 Bluetooth 宣传资料中）。这份早期资料是为了强调我们的一个主要主题：摆脱线缆。我认为这句口号和图形已经说明了一切（我从来不明白为什么我们只用过一次）。

![Image 8](https://lh3.googleusercontent.com/sitesv/AA5AbUA3R9hRke133q8cEVlszScbpCmxtX29FlZiTkE_x2iVuosIIykUKEJ5qoMCwmAIAZ7GqMzUp90TaQM_fw2W6zEYs7Tk65EY0P0kK2jVFuJQkCZKTg27G33zHxC0N34s9H1UFtWahK4IQ_LT4GTQF03P6ynrdufgYSQoTK9wxXQJOp14hi2w7uE9ERdi0Mp2l3rG2hGkm5kKXuJw=w1280)

> 图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

在这一时期，还发生了另一件与这个故事有关的有趣事件。作为 Intel 移动部门的一名工程师（我们设计笔记本电脑用的处理器和芯片组），我拥有许多专利。我的杰出领导 Stephen Nachtshem（Intel 移动与手持设备部门的副总裁/总经理）请我代他参加一个关于专利的高管会议，因为他无法出席。

我稍微提前到了一间大会议室坐下。会议开始前几分钟，Gordon Moore 和 Andy Grove 走了进来，坐在桌子一端，离我相当近。虽然我过去也参加过有高管在场的会议，但能和 Gordon Moore 同处一个会议，我总是很激动（他帮助 Robert Noyce 发明了平面晶体管/集成电路）；而这次我将和 Gordon 以及 Andy 一起开会。非常酷。

会议讨论的是法务部门提交专利申请的流程。显然，专利数量远多于 Intel 自有律师的人数，因此他们把许多专利申请外包给合同律师。我经历过这个流程很多次，并且对一个我大约 2–3 年前和一位合同律师一起准备的专利感到困扰，因为它从未被提交。事实上，那位律师就像从地球表面消失了一样。大约 2 年后，有人把一份部分完成的专利申请交给我，问我是否还希望提交这项专利。我表示是的，这是一个重要专利，并问到底发生了什么。原来，那位律师已经离开了我们合作的那家律所；两年后，当她的办公桌分配给另一位律师时，他们才在抽屉里发现了这份专利申请。此前我发现，我们的竞争对手正在就某项技术起诉 Intel，而我的这项专利本来可以成为该技术的在先技术。

于是我举起手，正在做演示的律师停下来，认出我，并让我提问。

“既然你们有这些合同律师在处理专利申请，你们有没有一个数据库来跟踪这些专利？”

那位律师看起来有点困惑，让我详细说明。我解释说，既然这些专利申请会交给外部合同律师处理，我们是不是应该记录有哪些专利正在准备、申请是什么时候、以及被发给了谁。这样 Intel 就可以跟踪专利状态，并发现是否有专利丢失或落后于进度。那位律师表示，不，他们没有这样的数据库，然后继续往下讲。

然后发生了一件不寻常的事。Gordon Moore，我见过的最友善、最和蔼的人之一，说：“你说你们没有数据库是什么意思？”事情从这里开始急转直下。Gordon 开始用非常大的声音对那位律师吼起来，并且开始站起身。Andy Grove 很快站起来，把手放在 Gordon 的肩上，说：没事，Gordon，我会处理这件事。

Gordon 坐了下来，然后 Andy 开始对那位律师吼。我坐在那里想着，这也太酷了，我竟然在和 Andy Grove、Gordon Moore 一起开会；庆幸我不是那位律师！突然，Andy Grove 的唾沫落到了我的笔记本上（当时有很多吼叫，而我离 Andy 很近）；我把它圈起来，写上 “Andy Grove’s spittle”。

无论如何，第二天我来上班，正走向办公室时，Stephen Nachtsheim 走过来问我：

“Jim，我昨天派你去的那场会议到底发生了什么？”我告诉 Stephen，那位律师如何介绍专利流程，我提出了什么问题，Gordon 如何开始追问并发火，然后 Andy 如何追问并发火。我还给 Stephen 看了我笔记本上 Andy Grove 的唾沫。Stephen 脸上露出很困惑的表情，回答说：“这件事你不用担心，我会处理。”

1998 年 2 月，在“名称开发”进行的同时，各家公司之间的协议也要签署。自 1997 年 12 月以来，我们一直在与 Ericsson、Nokia、IBM、Toshiba（当然还有 Intel）谈判。除了 IBM 之外，我已经让每家公司都同意签署合同。

问题出在协议中的知识产权条款。它大体上说，如果你拥有任何会覆盖这项技术的 IP，你同意不去起诉 SIG 的其他成员；这被称为 “Open IP” 协议。让 Ericsson 和 Nokia 签署这项协议非常困难，因为在电信世界里，技术通常通过“合理且非歧视性”的许可来授权。

虽然“非歧视性”意味着你不能选择授权给谁、不授权给谁（这是好事），但“合理”这个词并不是很定量化的。对一家公司而言合理的条件，对另一家公司可能就会被视为不合理。此外，以这类协议来运作 SIG，会导致技术因为 IP 位置而被提出（希望获得长期版税收入）。

Open IP 的不同之处在于，你不会从这项技术中获得版税收入，工程师可以根据技术优点来选择方案，而不是根据各自公司的 IP 位置来选择。

在这个案例中，IBM 不想为这项技术采用 Open IP 许可，因为这违反了他们的 IP 政策。此外，IBM 的 IP 归 IBM 内部法务团队所有，而这个法务团队有自己的独立损益（P&L）。因此，IBM 内部出现了裂痕：法务团队表示 IBM 绝不会签署 Open IP 许可，而移动部门（负责设计和制造 IBM 笔记本电脑）则想帮助开发 Bluetooth 技术。更糟的是，我的律师还和我打赌说，IBM 一百万年都不会签署那份合同（Brian Epstein，就是我做商标检索时用的那位律师）。

于是我们在 Ericsson 位于北卡罗来纳州罗利的场地安排了一场会议来签署合同。但我真的不太确定该怎么办，因为 IBM 表示他们不会签署合同，而我们又需要把合同签下来，才能开始技术工作。

我想出了一个聪明（但又愚蠢）的主意：让四家公司先签署协议，然后继续与 IBM 谈判，稍后再把他们作为 promoter 拉进来。为此，我修改了合同，把 IBM 的名字从合同中删掉。由于 SIG 的正式名称当时还没有选定，这些合同是以 “Bluetooth SIG” 的名义拟定的。

Johann Weber 和我一起到达罗利现场。他是 Stephen Nachtsheim 在欧洲的一名技术员工，与欧洲通信业务关系很近。我们到场后，我把合同分发到桌上，让大家审阅并签字。Johann 是 Intel 慕尼黑的员工，一直在帮助 Stephen、Simon 和我把所有公司聚到一起，共同协助建立 SIG。Johann 基本上认识所有这些高管本人，是个非常适合帮你推进事情的好人。

所以 Johann 和我站在那里聊天，大家也陆续就座，这时 IBM 的副总裁 Adalio Sanchez 和律师走了过来。

“嘿 Jim，我刚刚看了合同，它们看起来不错，但我注意到 IBM 被漏掉了，合同上没有签字的位置。”

Johann 有点瞪着我。哇，我也许应该早点告诉他我把名字删掉了。我解释说，我一直在以诚信原则与 IBM 律师（主要谈判人员就站在他旁边）谈判了 2–3 个月，而他们表示他们永远不会签署合同。因此，我需要启动技术工作，所以想先让仍愿意推进的公司签署 promoter 协议，并继续与 IBM 谈判，等达成一致后再把他们作为 promoter 纳入 SIG。

Adalio Sanchez 感谢我的解释，并表示他想和自己的律师私下谈谈。然后他们走进了一间空会议室。我看着 Johann，他冲我笑了笑，说：“你肯定要被炒了。”我心想：“我肯定要被炒了。”接着会议室里传来了非常响亮的吼叫声。Orjan（Ericsson 的 PM）走过来想进入会议室（我们在 Ericsson 的场地），听到吼声后说：“我想我待会儿再回来。”

吼叫又持续了大约五分钟。Johann 和我只是沉默地站在那里。我脑子里唯一的想法就是：“我完了，要被炒了。”最后，吼声停了下来，Adalio 和他的律师走出了会议室。Adalio 满脸笑容，而那位律师脸涨得通红，头发凌乱，心情很差。Adalio 说：“Jim，对这个误会我很抱歉。你能把 IBM 的名字加回合同里吗？我们今天会签署。”然后他走开了。那位律师留在后面，对我说了大意如下的话：“你以为这一回合你赢了，但等你们要批准规范时，IBM 永远不会签。”然后他气冲冲地走了。

Johann 说：“哇。”而我去想办法更新并打印合同。在等合同打印的时候，我给我的律师朋友 Brian 打电话，告诉他：“猜怎么着，IBM 刚刚告诉我他们要签合同。”他完全不敢相信。这真是个好消息。我告诉他我得挂了，然后拿起新的 “Bluetooth” 合同，分发出去，并让各方签署。

![Image 9](https://lh3.googleusercontent.com/sitesv/AA5AbUCngnAMlgpEySby79kXJNK3aT2Q3T1B1qyQQaF5AhO2GqJj8F3oH-T0tyKC2emlwrS1cz2TWqjecepmgmqCXcS_-zNHeE5QAoWlFmKf4Xhi6fan4E0ddCL9ojeCfoQXGt5f--b914Tjy5bRxKejBIFaE543_YPTQO3BBqTNpSQ4zHtqEPhL5CE_g1X4JUzQQMXXUQ1jcqVmq3-hkVE=w1280)

> 图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

那天晚些时候，Brian 回电话告诉我，他去告诉他的老板 Carl Silverman，说 Intel 刚刚让 IBM 签署了一份 Open IP 协议（他们认为这不可能发生）。但 Brian 一提到我的名字，Carl 就开始大喊。我想了想，告诉 Brian 那次高管 IP 会议、我的问题、Gordon Moore 的问题、Andy Grove 生气、Andy 的唾沫落到我笔记本上，以及第二天遇到 Stephen 的事。Carl 可能也在那场会议上……

这组协议提供了条款和条件，使来自不同公司的技术团队能够正式开始共同开发短距离无线技术。此外，它还创建了一个会员框架，让 “Early Adopters” 也能帮助开发技术规范。由于市场团队还没有就 SIG 的正式名称达成一致，它就以代号 “Bluetooth” 成立了。

在名称创建方面，Simon Ellis（Intel 的市场代表，也是 Bluetooth 市场小组主席）与 Intel 命名主管协调了 Intel 内部的头脑风暴，并主动提出，任何提交最终获胜名称的人都可以获得 500 美元奖励。Simon 一直很有竞争心，他希望 Intel 提出的名称能成为正式名称！作为一位极具命名天赋的人，我自己邀请自己参加了这些头脑风暴（毕竟，我想出了这个代号，而且我不想错过任何命名的乐趣）。我遇到了一群有趣的人，他们在过去开发名称方面经验丰富；参会者中有人开发过 PCMCIA、AGP、PCI 和 Pentium 这些名称。

在这样的会议中，开发名称的专业流程大致如下：懂这项技术的人向在场的人概述这项技术，并解释它能为人们做什么。主持人会把这些属性列出来，然后所有人开始对主持人大声喊出名称创意，主持人把它们写下来。几分钟后，提出的名称数量开始放慢……最终停止……然后主持人把这些名称按相似主题分组，并开始淘汰过程。

这个精密流程重复了好几次，最终得出了 “RadioWire” 作为 Intel 的提案。然而，这个流程得出这个名称时，距离预定的名称投票日期只剩一周。Simon 意识到，在投票前只有一周的情况下，很难为 “RadioWire” 赢得支持，于是请求我把投票至少推迟一周。我不得不考虑大局。当时，选择一个名称并不是我们优先事项列表中很高的一项——推迟名称选择只会增加印刷宣传资料的费用。此外，根据各家公司当时的情绪，我不认为推迟会是一个受欢迎的决定（他们基本上已经认定了另一个名字）。我告诉 Simon，他有一周时间准备；我不会推迟投票。

我们决定在一个全球活动上，以 SIG 的正式名称宣布/发布 SIG；活动地点包括英国伦敦、加利福尼亚州圣何塞和日本东京。随着准备工作的推进，关于我们正在做什么的信息开始泄露出来。我的档案里发现了这样一篇文章（注意，它的日期早于 1997 年 5 月 5 日的发布）。

许多文章开始泄露这项技术开发的信息。有些文章在细节上比另一些更准确（例如，上面提到的文章并不完全准确。Microsoft 和 Puma 是后来才参与的）。文章发表后，我确实打电话给 Puma，问他们正在组建的这个名叫 “Blue Tooth” 的新行业联盟是怎么回事；他们是最早加入 SIG 的 Early Adopter 公司之一。不过，所有文章都注意到了这样一个事实：一个代号为 “Bluetooth” 的开发项目正在进行；它的名字来自一位 10 世纪丹麦国王；它代表一种短距离无线技术的发展。事实上，这篇文章中专门用一行解释 “Bluetooth” 这个名字的历史相关性，后来成了后续文章的典型写法。

正如我前面提到的，选择正式名称是全球发布的一个关键里程碑，并会启动发布宣传资料的印刷。为了实现这些目标，“命名会议”大约在实际发布前两个月举行（发布定于 1998 年 5 月 5 日）。这次投票在我们的每周管理会议上进行（称为 “PM（Program Management）meeting”），获胜名称需要获得 5 票中的 3 票才能被接受。

到了预定投票日，五家 promoter 公司都派出了 Program Management 和 Marketing 代表参会。会议形式是由市场人员提出他们的提案，随后由 PM 成员投票。Simon 仍然有些不高兴，因为他没有多少时间预先推销自己的提案，于是先做了第一个陈述；我觉得这额外的 15 秒左右会给他成功所需的优势（你能相信他从来没为此感谢过我吗？）。

Simon 提出了 Intel 的提案 “RadioWire”，并解释为什么这是个很棒的名字：“因为它不是 PAN。PAN 是个糟糕的名字。你们会后悔选择 PAN 这个名字。”随后，另外四家公司分别提出了 PAN。不用说，结果是四比一，SIG 选择了它的第一个正式名称。会议休会，市场团队继续制作所有发布宣传资料。Simon 表示，PAN 被选中是我的错，他不会再和我说话。

大约三周后，Ericsson 召开了一次神秘的紧急电话会议，因为参会者分布在世界各地。Ericsson 的 PM 代表 Orjan Johansson 表示，Ericsson 对 “PAN” 这个名字有严重的法律问题，Jan Ahrenbring 会进一步说明。Jan 接着解释说，“PAN” 这个名字无法注册商标，我们必须使用另一个名字。事实证明，Ericsson（或其他任何公司）在投票前都没有对自己的提案做商标检索。他们震惊地发现，初步商标检索出现了大约 1,700 条命中，使它成为一个注册商标风险极高的名字。

鉴于 Orjan 表示 Ericsson 的法务团队发现了这些问题，我以为 Jan 是 Ericsson 的律师。我把我们的电话静音，问我的团队：“这家伙是 Ericsson 的律师吗？”已经几个星期没怎么和我说话的 Simon 很快宣布：“肯定是。”然后我取消静音，进入我最拿手的“枪打报信人”对话模式。

现在，我必须解释一下，在组建和运营 SIG 的过程中，你不可避免地会与很多律师打交道。这可能是一个非常令人沮丧的过程。现在回头看，当又一位律师在重大活动前最后一刻制造另一个问题时，我想我一定是在释放一些挫败感。Jan 非常抱歉，并表示他们会尽一切努力解决这个问题。

接下来，我总结了我们当前的处境：

*   1.   我们不能继续使用 PAN 这个名字——风险太高。

    2.   我们需要一个发布用名称（大约 3–4 周后），而且现在就需要，这样才能开始重新印刷所有宣传资料。

    3.   我们需要一个低风险的名字，或者一个已经通过商标检索的名字。

结果是，唯一有人做过商标检索的另一个名字就是 Bluetooth（谢谢你，Brian）。所有人很快理解到，我们将以 “Bluetooth” 这个名字发布 SIG。市场团队很快补充了一个后缀说明：他们会在稍后选择并宣布一个正式名称，而这应该成为发布时的关键信息之一。

会议结束后，Simon 让我意外地再次开始和我说话。

“Jim，你不觉得你刚才对 Jan 有点太狠了吗？”

“他是律师，他习惯了。”

“有意思，我以为 Jan 是 Ericsson 的市场副总裁，而且我不确定他习惯被人吼……”

啊，现在我知道 Simon 为什么又和我说话了。Simon 取得了双重胜利。第一，他关于 PAN 是个非常糟糕名字的观点得到了证明（虽然原因完全不同，这似乎并不重要）。第二，Simon 看到我通过痛骂一位 Ericsson 市场副总裁而把自己弄得很难堪。接下来的几周里，我都在紧张地等待自己行为带来的后果。

![Image 10](https://lh3.googleusercontent.com/sitesv/AA5AbUB6VShxCIlzo8bEQH6heYnwTOBfqJ9ibA2g5eezX7YoCa5YCaVURA8neCt7S4Jd0vzo30CMFHEPewezDr4nIDoynFL5ME86fmKhJ6bx9QH7YbbGPfm_4HiG-mXzrw-wqfBEf9d4hvhoWT9J10UjoP_TtMA0MIpk8k1Q8Gd8tSJiJkwWSyXXnq7179O0xLM3hBHImdNCTNHl7b7DfLY=w1280)

> 图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

与此同时，LEGO 到美国与 Intel 进行技术讨论。在这次会议上，有人透露 Intel 正在开发多项无线技术，其中一项代号为 “Bluetooth”。LEGO 的代表相当惊讶，并表示加入并支持任何名为 “Bluetooth” 的开发项目，是他们的爱国义务！LEGO 总部位于丹麦；它们的总部距离耶灵原始 Harald Bluetooth 符文石大约 10 公里。

既然 Simon 又开始和我说话了，我确实指出：Bluetooth 这个名字是我提交的，它也是我们将要公开发布时使用的 SIG 名称，因此我有权获得他承诺的 500 美元奖金。Simon 表示，我们是以代号发布，而不是以正式名称发布；他的奖金是给正式名称的（并且叫我不要抱太大希望）。

这次快速改名带来的一个额外好处，是大量 “PAN” Polo 衫和其他 “PAN” 纪念品。我保存了这样一件纪念品，一件 Ericsson Polo 衫，上面有 PAN 标志。要是那 1,600 个网站没有使用 PAN 这个词就好了……

![Image 11](https://lh3.googleusercontent.com/sitesv/AA5AbUBK77WeIehAWtCSJi8UuBw9eE7I74J28vS5Bfu3jrFnJ-dlzE7Kr7ANEvAOf1kSMvs42ZYRjs8a1t4IwjxfJ-SmfXi98GPlzcMLqQWQC_VIJEcoQQ4P-s81l-kgD9vLbfS0C-1a3-33QwKSfpMi5YzfmIqVWpyDbflHKVBHVDkUi5ozi2YU_EaFt5fA5EyQV9aXyXMugSjOQ3YUaOE=w1280)

> 图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

为了支持发布，市场团队希望给媒体提供一件纪念品，让他们记住这次活动。有人建议，我们应该发放一个迷你 Harald Bluetooth 符文石，也就是我们当时在幻灯片中描绘的那块石头（在上一篇文章中，我们展示了那块著名符文石的增强版，Harald 一手拿着一台笔记本电脑，另一手拿着一部手机）。大家同意了，于是 Anders Edlund（Ericsson Bluetooth Marketing）被交给了制作这些符文石纪念品的任务。我设想的是外面包着塑料的泡沫石块，正面印着 Harald 的图像；然而，Anders 让所有人都感到惊讶，因为他竟然真的把 Harald 的形象刻进了大约 6 英寸高的真花岗岩石头里！拥有一块这样的原始符文石纪念品是一种罕见的荣誉。

![Image 12](https://lh3.googleusercontent.com/sitesv/AA5AbUB8K1Q34goMNoLgKEFX9BDCFfIGNtNuBRL_BX4Yk7BkLi3k0941snoKBi3Ee-3oFqt_aI3xP4E9_dSJzLLRIBWNGcJI1r1KQrQzEN37E8ktwI0TskEbo5D036gYHxnqscWihVpyTL_u2bpaDSGogRmv7bb4YYjmBOrZTj6bmuwalCZ7S4h1zZwWsGSR4XCuU2lu2d1s-CpdaEcKcb0=w1280)

> 图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

5 月初，全球发布举行。Simon Ellis 和我参加了伦敦发布会（不过我在这里也包含了一组来自所有发布会的照片拼贴）。我们聘请来安排活动的公关机构叫 Edelman，活动前一天我们与他们会面。在这些会议上，我们发现 Edelman 的人对这次发布并不太满意。我最初把这归因于“PAN 改名事件”。不过，Edelman 的人非常明确地表达了他们的不满。第一，他们认为 Bluetooth 这个名字令人尴尬，并建议我们完全不要使用它。他们觉得媒体不会认真看待我们，而且它会让人联想到糟糕的牙齿卫生状况，而不是让人联想到酷设备以此前不可能的方式互动。第二，他们讨厌 Bluetooth 石头纪念品；这会让我们难以避免使用 Bluetooth 这个名字，而且他们觉得会出现很多关于 “Bluetooth will drop like a rock” 的标题，并配上那块臭名昭著符文石的图片。Simon 解释说，许多技术媒体已经听说过这个代号，不必太担心这个名字（他可能还提到 Edelman 还没有收到付款，而我们正在开支票）。

后来我们发现，美国的公关团队完全拒绝发放符文石。不过，Simon 和我后来又重新拿回了这些石头，把它们作为纪念品发给加入 Bluetooth 团队的人，或者作为激励发给加入 Bluetooth SIG 的公司。Simon 和我在“伦敦石头叛乱”刚要开始时就阻止了它，但日本发布团队认为它是一件出色的纪念品。在伦敦发布会上，Simon 确实抽时间亲自把我介绍给前面提到的 Jan Ahrenbring，Ericsson 市场副总裁兼兼职律师。

事实证明，这次发布反响很好，产生了大量头条报道，把 Bluetooth 这个名字植入了世界各地人们的脑海。Edelman 做得很好，我们后来发现，他们因为这次发布所产生的宣传量而获得了一个奖项。

[![Image 13](https://lh3.googleusercontent.com/sitesv/AA5AbUBXr4TOLi91t2JfhxzthtDwdOHddUznKNOgH6crE_leqOGWnpgJmVE8PnBduM8b7rNR-Uju2BkFaP5FPH3nnKP1uTxwyuGQXWKW6TNZkvWmYeYhwEkZ8WIDewU1T0fz-Vu4DWPKY6AJdDg2roA7Sq0J9GuRLGgxvcSFAuqZTBLdptjoLWrvYNCLDPFlUX1u7vmQIXpo4aDG0Hu1=w1280)](https://www.youtube.com/watch?v=ivb-Ln6Sm3s&list=PL_fbfFWItJhOAF2HGJ5aLm_pCOpD2T_-d&index=5&t=0s)

> 图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

![Image 14](https://lh3.googleusercontent.com/sitesv/AA5AbUBe8u-CQn5mt2O1MJYN54Ho5N3ZOVDkSwJ-hei5UIOIC_lvIKCz8E7Tha7btRPO_Eq8qfnXX6MM9BR71wIf3b62BiEHHp7AR27dM5hmTU3JRygEwc-lNBQEq8xJaBpCb_iG8Xvv9vrmFxq7FfGx9MnkeLOs6J0ZY0gOxk9rnmfXOh5qbchvBfmXnYSTD0B_FY_gxEH10gVCajjSvn8=w1280)

> 图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

SIG 以新的 Bluetooth 代号发布后，我收到了我的朋友 Sven Matthesson 的一封邮件。他告诉我，Ericsson 的 CEO 打电话给他，问这项技术为什么叫 Bluetooth，而他不知道该怎么回答。我提醒 Sven 多伦多那晚的事，当时他给我讲了《the Longboats》那本书的故事，而书中的丹麦国王名叫 Harald Bluetooth；我还说，当我回到家后，在我买的那本 *The Vikings* 中看到一张 Bluetooth 符文石的图片，我只是觉得它会成为一个很棒的代号。我还提醒他，虽然 IBM 提出了 PAN 这个名字，但他们从未对这个提案做过商标检索（而每个人都以为他们已经做过了商标检索）。

Sven 回复说：

“我不能告诉 Ericsson 的 CEO，说我们是在多伦多一边喝啤酒一边想出这个名字的。”

然后，他整理出一个自己觉得可以接受的故事（我已经没有原始邮件了，所以以下全凭记忆）：

“Jim 和我过去常讨论历史，我给他讲过《The Longboats》的故事，里面 Harald Bluetooth 是国王。Jim 提议把它作为代号，因为 Bluetooth 统一了丹麦、瑞典和挪威，正如我们希望自己的技术能够统一手机和笔记本电脑一样。”

我告诉 Sven，我更喜欢一边喝啤酒一边想出来的版本，但这个版本听起来也不错。然后他给 Ericsson 的 CEO 发了一封邮件（抄送了我，但我把那封邮件弄丢了）。

最近我去了加利福尼亚州山景城的计算机历史博物馆，那里有一个关于 [Nils Rydbeck](https://www.computerhistory.org/revolution/mobile-computing/18/341/2322) 的展览；在 Bluetooth 的开发过程中，我见过他几次，他也是蜂窝电话领域的传奇人物之一（他基本上发明并开发了第一部实用蜂窝电话）。他们采访了 Nils Rydbeck，谈论蜂窝电话和 MC-LINK/Bluetooth 的开发。快到结尾时，他谈到 Bluetooth 技术是如何得名的（3:39）。他说 Ericsson 曾给 Intel 一本非常好的书《the Longboats》，故事中的国王是 Harald Bluetooth。

我想，这很奇怪，Sven 是在发布几个月后才把那本书给我的（我现在还保存着）。然后我想起了和 Sven 的那次邮件往来。我只想着，见鬼，我本来可以让 Nils Rydbeck 在采访里讲我和 Sven 在多伦多喝啤酒的事！那该多酷。

尽管如此，市场团队还有一项未完成的任务，并继续向前推进。他们的下一次尝试会更完整。市场团队一边做同步商标检索，一边针对短距离无线技术的不同名称开展一项全球焦点小组研究。

由于 “Bluetooth” 已经获得大量关注，他们也把这个名字放进研究里，纯粹是为了好玩。我认为，在这个时候，Simon 和 Anders 都已经开始相信，鉴于围绕 Bluetooth 产生的宣传量，改名几乎是不可能的。

这项全球焦点小组研究的结果相当有趣，我真希望自己还保存着一份（我现在讲给你的内容来自记忆）。据我记得，焦点小组研究在伦敦、旧金山、东京和墨西哥城进行（可能还有几个城市被我漏掉了）。我记不住所有测试过的名字，但我认为其中一个热门候选是 CoMeGo（Come、Go 和 Me 的混合体）。

其中一个问题是：“当你听到这个名字时，你会把它和什么联系起来？”对 Bluetooth 的最高频回答是“牙齿卫生问题”（或类似内容）。当被问到会把这个名字与什么行业联系起来时，对 Bluetooth 的最高频回答是“牙科行业”。当被要求按纯粹受欢迎程度给不同名称打分时，Bluetooth 在除墨西哥城外的每个城市都排在最后；在墨西哥城，它被评为第一名（没人知道为什么）。

在这项调查进行的同时，Bluetooth 这个名字继续变得越来越受欢迎。Toshiba 的 PM 代表 Warren Allen 讲到，在一次 *PC Week* 采访结束时，采访者评论说：“无论你们做什么，都不要改这个名字，它是最好的部分。”

事实上，市场团队此时开始严重怀疑改名是否明智。公司通常要花费数亿美元，才能创造出那种围绕 “Bluetooth” 奇迹般出现的名称认知。虽然消费者可能不知道 Bluetooth 是什么，但你几乎可以和任何技术公司交谈，而他们不仅知道 Bluetooth 代表一种短距离无线技术，还知道历史上有一位同名的 10 世纪丹麦国王。

以我自己的个人经验来说，我创建过许多技术标准，但没有哪个是我的家人能够理解或产生关联的。Bluetooth 不同；它不仅是我的母亲或父亲能够理解的东西（替代一根电缆），而且是一项他们会在本地报纸上读到、或在电视上听到的技术。我多次收到电子邮件或信件，里面夹着提到 Bluetooth 的剪报！能参与某个（终于）连我的父母和亲戚都能识别并产生关联的东西，感觉很好。

随着 SIG 的受欢迎程度上升，成员数量迅速飙升，媒体文章数量也持续增加，而这一切都发生在 Bluetooth 这个名字之下。显然，市场团队必须解决正式名称问题。焦点小组研究显示，CoMeGo 在所有市场中测试表现最好，但现实已经摆在眼前：产业界知道 Bluetooth 是什么，却不知道 CoMeGo 是什么。在这个时候改名将是一件风险极高的事情。

于是，市场团队向 PM 小组提出了以下建议：

“焦点小组研究表明，CoMeGo 在我们测试过的不同地区中表现非常好。然而，我们认为创建一个强品牌可能会对我们现有母公司品牌（Intel、IBM、Toshiba、Ericsson 和 Nokia）构成威胁。另一方面，焦点小组研究显示，Bluetooth 完全不会对我们现有品牌构成威胁；此外，Bluetooth 已经在我们的目标行业中与短距离无线技术建立了强关联。因此，我们建议 SIG 保留 ‘Bluetooth’ 作为技术和 SIG 的正式名称。”

于是，Bluetooth 终于成为正式名称。我立刻去找 Simon，要求我的 500 美元奖金。他的第一反应大意是“去死吧”，但大约三个月后，我收到一份奖励通知，我因为提交了获胜技术名称而获得 200 美元。我立刻打电话给 Simon，提醒他奖金是 500 美元！他说我能拿到 200 美元就该庆幸了（我还在等剩下的钱）。

我偶尔会在互联网上搜索 Bluetooth，以衡量它的认知度。刚开始时，我会得到大约十几条结果，全部都指向那位丹麦国王（大多是在家谱网站上）。大约在 Bluetooth 成为正式名称的时候，同样的搜索会得到几百条结果，其中大多数关于这项技术，也有几条关于那位历史上的国王。2002 年，我搜索 “Bluetooth”，得到超过 618,000 条结果（第一条结果直接把我带到 Bluetooth 主页）。今天，我搜索 “Bluetooth”，得到 1,360,000,000 条结果；我看到的第一条专门关于历史人物 Harald Bluetooth（与他的电子对应物无关）的结果出现在搜索结果第 13 页。确实，这个名字已经变得极其流行。

所以，现在你知道了围绕这项技术命名的主要事件。这个过程既不顺利，也不可预测。我相信，任何参与其中的人都不敢预测，这项技术最终会被称为 “Bluetooth”。焦点小组研究证明，这个名字完全不会让人认出我们试图完成的事情。考虑到围绕命名发生的这些事件，我不确定这种现象是否还能被复制。

这个名字为什么成功？也许是因为那个古雅的历史指涉。也许是因为这个奇怪的名字会让人想到牙齿腐坏，然后突然“啊哈”一下，发现它指的是一位历史人物，从而使这个名字难以忘记。也许易于理解的使用模型（替代一根电缆）进一步帮助人们把这个奇怪的名字与这项技术联系起来。我自己也不太确定，不过我认为，如果哈佛能写一篇关于什么造就流行名称的案例研究，并把 Bluetooth 作为其中一个例子，那会很有意思。

关于符文石，还有最后一个故事。1998 年末，我因为一些 SIG 事务去了瑞典隆德，并拜访了 Per Svensson。Per 是我最初开始创建 SIG 框架时合作过的 Ericsson 初始经理之一。Per 和我都对历史很感兴趣，而 Per 对我感兴趣斯堪的纳维亚历史非常高兴。Per 刚刚去过耶灵，也就是原始 Bluetooth 符文石所在的地方，并给我带了一本英文小册子。我非常高兴，因为那本小册子里有一些非常漂亮的符文石照片，也有一段关于 Gorm the Old 和 Harald 的很不错的历史介绍。

回到圣克拉拉后，我打算用这张质量更好的照片制作一个新的石头位图。所以我扫描了照片，并用高分辨率激光打印机把它打印出来。当我走进办公室时，电话响了，我把打印件放到桌上，接起电话。Jeff Schiffer 走进我的办公室；他负责过 SIG 的许多监管工作，处理安全、频谱和模块合规。他拿起照片，开始盯着它看。突然我听到 Jeff 说：“嘿，他的手掌上那些不是洞吗？”这立刻引起了我的注意。我一把抓过照片（一定还把电话掉到了地上），开始更仔细地检查图片。确实，他的手掌上有黑点。

![Image 15](https://lh3.googleusercontent.com/sitesv/AA5AbUDjPjEwuaXKVacVRV33zRbeFy1DOeaK168Z45oVu-yHaCBozNyzGFyDPvgo6HsYpyEa3P5jv4fcgJkd-eil--MSuWdMahS5mSoMjgkMGz3V_-sFR0SPHnnbE3xQwHRY2ESQkDz9Kd0Wq5wVkeOUQJhPJSr5MDPT811JpIyJdgtwJA0jtknc5b46KPkcbZZFfkjcg3xeq5dxO2js=w1280)

> 图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

又做了一点进一步调查后，我找到了新的参考资料，它们把这描述为基督的形象（我们一直对他头部周围的圆圈感到疑惑，现在这个谜团解开了）。后来，一位来自 Compaq computer 的朋友告诉 Simon 和我，哥本哈根博物馆里有一件 Harald Bluetooth 石的复制品，他们确实把这个图像称为基督。

不用说，这非常令人担忧。我生活在一个国家，在 60 年代，当 John Lennon 表示 Beatles 比基督更受欢迎时，人们曾焚烧 Beatles 唱片。而在这里，我竟然无意中把基督用作 Bluetooth 技术的代言人！我不确定该怎么办，于是和 Simon 讨论了这个情况。我们决定低调地停止使用这块石头的图像。我还要说明，我去过耶灵，也看过原始石头；我并没有在他的手掌上看到任何黑点！

不幸的是，我们也收到了来自丹麦人的投诉。他们认为 Harald Bluetooth 符文石是这个国家的“洗礼”石，因为它是在君主制奠基时期竖立的（Harald 的父亲 Gorm the Old 是丹麦第二任国王）。在这个图像上画一台笔记本电脑和一部手机，就像在自由女神像上涂鸦。

自从选择 Bluetooth 作为 SIG 的正式名称以来，SIG 一直试图把 Bluetooth 这个名字注册为商标（我可能会因为在写这个故事时完全无视商标规则而收到 SIG 的正式通知；不过，我写的是商标之前发生的事件）。遗憾的是，我必须报告，我们唯一遭到的驳回来自美国商标局。商标局表示，“Bluetooth” 这个词与短距离无线技术同义，因此不可注册为商标！SIG 确实解释说，正是 Bluetooth SIG 创造了这种关联，最终商标局把 Bluetooth 商标授予了 SIG。
