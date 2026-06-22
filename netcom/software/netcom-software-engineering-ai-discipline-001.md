---
id: netcom-software-engineering-ai-discipline-001
title: AI 需要更多工程纪律，而不是更少

module: netcom
submodule: software-engineering
topic: ai-engineering-discipline

type: translation
status: active
canonical: true

summary: >
  本文讨论 AI 生成代码改变代码生产经济学之后，软件工程应如何把严谨性从手写代码转向规范、验证、可观测性和生产环境反馈。
  作者认为 AI 并不意味着工程纪律减少，反而会迫使团队更认真地编码系统知识、建立短反馈回路，并重新审视代码作为可再生缓存的角色。

parents: []
related: []

tags: [ai, software-engineering, sre, observability, code-review, engineering-discipline, agentic-coding]

audience: [self, public]
languages: [zh]

maturity: stable
confidence: 0.9

visibility: public
source_of_truth: translation

original_title: AI demands more engineering discipline. Not less
original_source: charity.wtf Substack
original_publisher: Charity Majors
original_url: https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline
translation_note: >
  本文为原文内容的中文翻译，仅用于学习与知识整理。
  原文版权归原作者及出版方所有。若权利人认为本文不宜公开保留，请联系后删除或调整。

created: 2026-06-22
updated: 2026-06-22
---

文章翻译

source

* https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline

note

本文为原文内容的中文翻译，仅用于学习与知识整理。原文版权归原作者及出版方所有。若权利人认为本文不宜公开保留，请联系后删除或调整。

⸻

正文

# AI 需要更多工程纪律，而不是更少

几天前，我写了一篇文章，题为“[AI enthusiasts are in a race against time, AI skeptics are in a race against entropy](https://charitydotwtf.substack.com/p/ai-enthusiasts-are-in-a-race-against)”。

我手头记了一大堆 AI 相关主题，本来都想深入写一写：AI 强制令、沟通规范、代码评审、AI 艺术，等等。不幸的是，上一篇文章收到的有意思回应太多了，现在我得先回应这些，才能继续写别的主题。😉

有两类有意思的回应：第一类是技术层面的，第二类是伦理层面的。我会分别回应。先讲技术侧，因为这比较容易。

不知道为什么，有一部分读者读完之后觉得我是在号召所有人抛弃代码评审，把自己最烂的代码不经阅读就直接推到生产环境，_现在立刻_，tout suite。[1](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline#footnote-1)

我不是在做这件事。我也不认为你_应该_这么做。但我选择这个例子并不是随机的，我会告诉你原因。

[![Image 1](https://substackcdn.com/image/fetch/$s_!3g6N!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F87a779c4-2e63-495a-aa1b-b44f1558a24f_903x241.png)](https://substackcdn.com/image/fetch/$s_!3g6N!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F87a779c4-2e63-495a-aa1b-b44f1558a24f_903x241.png)

图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

人们很容易忘记，在 2025 年的大部分时间里，认为 AI 生成的代码是垃圾、而且可能永远都是垃圾，不只是一个合理立场，它还是默认的主流立场。[2](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline#footnote-2)

这个问题在去年 11 月已经被明确回答了。自从 Opus 4.5 发布以来，AI 已经能够生成质量大致相当于软件工程师中位数水平的代码，至少在常见模式上如此，而且速度更快、成本更低。我从一本书的坑里爬出来，在 1 月意识到了这一点；而在 2026 年最初几个月里，似乎我周围的每个人都在经历类似的醒悟。

但很多人更早就看到了这一点。

流行叙事认为，Opus 4.5 才是改变一切的东西。但 Opus 4.5 更像是临界点。Agentic harnesses（把 LLM 包进一个带工具的循环里的代码）在 2025 年中期成为真正的东西，其前身可以追溯到 2024 年末。工具使用、函数调用、MCP……这一整波浪潮在 2025 年逐步积累，并在年底达到真正通用可用的程度。

这就是去年那些热衷者一直想告诉我们的。不只是“这件事要来了”，而是“这件事来得比你想象得更快”。

事实证明，他们是对的。

你可能知道，我来自可靠性这一侧。我愿意给自己和我这类人一个赞美：我们并不难适应新的现实。只要问题是真实的，并且摆在我们面前，我们就会顺滑地、甚至热切地调整自己，这要归功于一种不太健康的热情：我们喜欢舔食恶心的技术烂摊子（以及以后能在篝火旁讲的故事）。

[![Image 2](https://substackcdn.com/image/fetch/$s_!jEKP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F60b0224a-8572-43fa-85d5-0579487ed15f_787x301.png)](https://substackcdn.com/image/fetch/$s_!jEKP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F60b0224a-8572-43fa-85d5-0579487ed15f_787x301.png)

图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

我也愿意给自己和我这类人一个反向赞美：我们有时很难接受_进步是真实存在的_，也很难接受 bug 和边界情况仍然存在，并不会削弱这样一个事实：问题空间中的大片区域确实会随着时间大体被解决，以至于大多数人可以把它们当作理所当然。[3](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline#footnote-3)

当热衷者告诉我们 harness engineering 和 AI validation 是真实的、已经存在、而且正在以惊人的速度变好时，我脑海里一直萦绕着这样一件事：代码从彻底垃圾变成“啊该死，这还不错”的速度。

第一次坚持“我看到才相信”还可以原谅，第二次就没那么可原谅了。事实证明，站在指数变化曲线内部就是这种感觉。[4](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline#footnote-4)

我想在这里暂停一下，非常清楚地说明我认为正在发生什么。然后我会告诉你，我具体对什么感到兴奋，以及为什么。

你没有义务跟我一起走到那里。但现在外面有太多笼统的大话，说什么“它从来不是 X”——“它一直都是 Y”——“未来属于 xyzzy”🤮——我想非常清楚地说明：我的主张有多么有条件、多么具体、多么依赖上下文。

2025 年发生的是：**代码生产的经济学被颠倒了。**过去，生成代码非常困难、耗时、昂贵；而现在，它实际上变成了免费且即时的。几乎在一夜之间，代码行从被珍惜、复用、照料和精心策展的东西，变成了一次性且可再生成的东西。

在计算历史的大部分时间里，人们理解软件的主要方式是编写代码。一旦你达到一定熟练程度，阅读和讨论代码就能让你走完大部分路。（我可能会争辩说，软件工程师一直过度依赖_代码_，而不是通过可观测性来对_系统_进行意义建构。）

[![Image 3](https://substackcdn.com/image/fetch/$s_!3-TF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb45ec2a6-8f65-4ece-af9f-27720fbbaeb2_779x318.png)](https://substackcdn.com/image/fetch/$s_!3-TF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb45ec2a6-8f65-4ece-af9f-27720fbbaeb2_779x318.png)

图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

许多优秀的软件工程师认为，每一个（优秀的）软件工程团队的真正产物，一直都是我们对自己所拥有软件的共同理解。它会作为缓存状态存进我们脆弱的小肉脑里，经常被刷写到磁盘、部署到生产、提交到 GitHub，但意义一直都存在于我们的头脑中。

难怪软件一直都是如此强烈的集体主义事业，对关系动态、礼仪、公平问题和情绪价态极其敏感。当你的大脑有一部分活在别人的大脑里，而你们的集体相互依赖性又高到离谱时，这正是你会预期看到的。

这是我喜欢这个行业的一点。但无法否认的是，对于软件开发模型的某些方面来说，人的头脑一直不是一个好的容器。我们会遗忘、会分心、会不耐烦。我们不擅长发现小细节，会对重复产生习惯化。最糟的是，我们脑中的模型会大幅且持续地偏离用户实际交互的世界。

总之，SRE 从来没有完全买账这个解释。对我们来说，每一个（优秀的）软件工程团队的真正产物显然是生产环境。

只有生产才是生产。在生产中测试，否则就是活在谎言里。

（这些都是背景故事。我保证，我马上讲到重点。）

我们去年 8 月发布了 AI 强制令。[5](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline#footnote-5) 我已经看到了足够多的东西，知道这件事正在发生，而现在是时候做负责任的事了。[Honeycomb](http://honeycomb.io/) 是一家开发者工具公司，人们来找我们，是为了在技术前沿帮他们解决困难问题。我全力投入 AI，但我不能说在内心深处我真的对此非常兴奋。[6](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline#footnote-6)

[![Image 4](https://substackcdn.com/image/fetch/$s_!lHkQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf09736c-8384-4a8b-8055-0e629d3c70f6_786x296.png)](https://substackcdn.com/image/fetch/$s_!lHkQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf09736c-8384-4a8b-8055-0e629d3c70f6_786x296.png)

图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

然后我读到了 Chad Fowler 关于 [Phoenix Architectures](https://aicoding.leaflet.pub/) 的文章。

如果你不知道我在说什么，老实说你现在就应该别再读我这些破东西，直接[去读他的](https://aicoding.leaflet.pub/)。Chad 是 2013 年创造“[immutable infrastructure](https://chadfowler.com/articles/trash-your-servers-and-burn-your-code.html)”这个术语的人。他最知名的文章是“[Relocating Rigor](https://aicoding.leaflet.pub/3mbrvhyye4k2e)”，因为 Martin Fowler[7](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline#footnote-7) 在[回顾一场关于软件未来的 Thoughtworks meetup](https://www.thoughtworks.com/about-us/events/the-future-of-software-development) 时提到了它。我回应了一篇“[Production Is Where the Rigor Goes](https://www.honeycomb.io/blog/production-is-where-the-rigor-goes)”，抱怨他们谈生产环境谈得不够。

我写那篇文章时，想来“Relocating Rigor”是我读过的唯一一篇。但很快我就发现了其余文章；读了两三篇之后，它_就_突然_对上了_。我完全知道他在说什么。我能预测他接下来会说什么。然后，读者啊……然后我_兴奋_起来了。

我会给你摘一小组 Chad 的引文，刚好够你抓住要点。下面这段出自“[The Death and Rebirth of Programming](https://aicoding.leaflet.pub/3malrv6poy22a)”。

> 不可变基础设施。无状态服务。容器。蓝绿部署。基础设施即代码。
> 
> 
> 这些理念都有一个共同前提：永远不要修复正在运行的东西。替换它。
> 
> 
> AI 将这一前提从基础设施推进到了应用代码本身。当重写很便宜时，就地编辑就会变得有风险。变异会累积熵。替换会重置它。

另一个我很喜欢的：“[The Deletion Test](https://aicoding.leaflet.pub/3md5ftetaes2e)”。

[![Image 5](https://substackcdn.com/image/fetch/$s_!WxpU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98d0d940-6230-4da3-8f73-38d275b056bc_779x295.png)](https://substackcdn.com/image/fetch/$s_!WxpU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98d0d940-6230-4da3-8f73-38d275b056bc_779x295.png)

图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

> 这里有一个简单测试，你可以把它应用到自己参与的任何软件系统上：
> 
> 
> 想象删除整个实现。
> 
> 
> 大多数工程师会把删除体验为一种存在性危机。代码感觉像是_那个东西本身_。它是我们编写、评审、版本化、部署和调试的东西。失去它，感觉就像失去了系统本身。
> 
> 
> 当人们说“我们不能就这么把代码扔掉”时，他们通常真正想表达的是更精确的东西：
> 
> 
> *   我们并不确切知道需要什么行为。
> 
> *   我们不知道哪些失败是不可接受的。
> 
> *   我们不知道哪些不变量必须始终成立。
> 
> *   我们不知道如何判断一个新版本是否正确。
> 
> *   我们不知道哪些 bug 是针对被遗忘边界情况的有意修复。
> 
> 
> 
> 这些不是代码问题。它们是评估问题。
> 
> 
> 当代码是知识唯一存在之处时，代码就会变得珍贵。

以及，

[![Image 6](https://substackcdn.com/image/fetch/$s_!TaBS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8910be06-8ab1-4348-a6c2-63c426bc93b6_782x333.png)](https://substackcdn.com/image/fetch/$s_!TaBS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8910be06-8ab1-4348-a6c2-63c426bc93b6_782x333.png)

图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

> 在软件历史的大部分时间里，把代码视为耐久物是合理的。
> 
> 
> 我们把代码视为永久之物，是因为生产它所需的劳动是瓶颈。重写很昂贵。重新验证很冒险。实现会随时间累积意义。结构、测试、注释、bug 修复和部落知识融合成某种你学会不要轻易碰的东西。
> 
> 
> 当生产是约束时，这说得通。
> 
> 
> 当再生成变得容易时，代码就不再是资产，而开始表现得像缓存：一种理解的物化视图，在当前有效时有用，在过时时可丢弃。

“_一种理解的物化视图，在当前有效时有用，在过时时可丢弃_。”我想，让我脑中突然对上的可能就是这句原话。

我刚好年纪够大，我的第一份工作头衔还是“系统管理员”。我那时是个十几岁的孩子，在大学里工作，在他们学会自己绝对_不该这么做_之前，我对每一台机器都有 root 权限。[8](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline#footnote-8)

我亲历了从手工制作的服务器宠物，到不可变基础设施牛群的转变。当时我并不真正理解正在发生什么，但近些年来我思考了很多。我在《Observability Engineering》第二版最后一章里写下了这些内容（截至 6 月 17 日星期三可下载！）：

> 从手工制作服务器到不可变基础设施的转变教会我们：可变性是理解的死敌。任何被就地编辑的 artifact 都会产生漂移。漂移就是让系统无法维护的东西。
> 
> 
> 我们能够杀掉并再生成基础设施组件，正是我们信任它的原因。在 Honeycomb，我们每周二都会通过 cron 杀掉最老的 Kafka 节点。正因如此，我们才对自己的引导和均衡流程有信心：一切都是可重复的，数据可以再生成，承诺存在于别处。
> 
> 
> 我们无法以同样方式再生成代码，这一事实表明我们并不理解它。我们不知道自己做出了哪些承诺，不知道哪些依赖会被打破。大多数时候，我们是通过打破它们才找到它们。

[![Image 7](https://substackcdn.com/image/fetch/$s_!_xw8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3181579b-618e-4ef5-b7da-33756cc15ff8_888x281.png)](https://substackcdn.com/image/fetch/$s_!_xw8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3181579b-618e-4ef5-b7da-33756cc15ff8_888x281.png)

图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

想想你工作生涯中浪费在痛苦迁移和重写上的所有年月。想想替换那些承重的遗留代码。想想所有那些 [strangler figs](https://martinfowler.com/bliki/StranglerFigApplication.html)。

代码行一直承担了_太多_东西。代码一直是开发者意图、用户期望、隐式与显式行为的捆绑仓库，是我们对过往 bug 所拥有的唯一化石化复合记录。太多了！

再看看那些由于维护和修改代码行的巨大、吞噬一切的成本而被忽视的领域。为了理解我们的架构如何演进，我可以评审和讨论哪些 artifact？我们的架构 artifact 到底在哪里？如果我们可以围绕一张架构图讨论并达成一致，而代码可以根据架构变更重新生成，而不是架构只能有点像、差不多地从代码中推断出来，那会怎样？

我_不是_在断言所有代码最终都会由 AI 按规范生成，从而绕开人的理解。整个事业是否可行，取决于一个问题：spec 是什么，或者 spec 可以是什么。任何做过痛苦数据库迁移的人，都本该在我们能否以可重放、可自动化的方式提取并形式化用户期望这件事上，学到一点该死的谦卑。

但我认为，朝这个方向迈出的每一步都会_对我们有益_。

实现这一点的工具还不存在，但许多理念已经存在。大多数来自运维和 QA，而软件工程在历史上一直对这两个领域相当势利。

那些测试和技术并不是为了测试正确性，或者测试_应该_发生什么；它们是在观察并编码_正在_发生什么。行为测试、特征测试、捕获/回放、流量分流器。可观测性（好的那种）。

[![Image 8](https://substackcdn.com/image/fetch/$s_!2r_p!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0156e490-2a09-4246-af73-6d6264cf5324_792x274.png)](https://substackcdn.com/image/fetch/$s_!2r_p!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0156e490-2a09-4246-af73-6d6264cf5324_792x274.png)

图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

生产环境中出现非确定性代码，终于在迫使我们做那些本来一直就该做的事。用 trace 做仪表化。在生产环境中做测试和 eval。生产不是开发结束之后才发生的事情，**生产是开发的一个阶段**。

人脑_并不擅长_验证。那种吹毛求疵、那种重复。这是最不值得我们抱住不放的东西，诸位。在软件的生产和维护中，有太多更好的东西值得我们想要保留，并为自己主张。谈到_验证_，我们永远不可能打败机器——我们字面意义上就是最薄弱的一环！

在创造力、灵感、逻辑跳跃以及很多其他方面，我愿意在相当长一段时间里把赌注押在人类身上，但请千万不要把你关于“软件中仍然需要人类”的杀手级论证，建立在我们是最好的_质量门_之上。天啊。🙈

好了。我差不多说完了。只剩最后一件事。

我认为，过去两年 AI 话语中让许多工程师感到如此疏离和恐惧的，是许多显赫的 AI 声音似乎在兴高采烈地宣称：软件不再是一个工程问题。“[SaaS is dead](https://www.forrester.com/blogs/saas-as-we-know-it-is-dead-how-to-survive-the-saas-pocalypse/)！”“[Making AI great at coding was the strategy that unlocks everything else](https://www.linkedin.com/pulse/something-big-happening-matt-shumer-so5he/)”，等等。甚至 [Adam Jacob](https://www.adamhjk.com/blog/as-we-build-so-we-believe/)——我最亲密的朋友之一，也是一个很少看错技术的人——似乎也预期软件岗位会经历一场血洗。[9](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline#footnote-9)

如果说 2025 年是 vibe coding 之年，AI 生成代码行的能力达到了软件工程师中位数水平，而可能的未来范围常常让人感到不稳定、近乎不可思议地宽阔，那么我觉得 2026 年正在成形为一次**纪律的回归**。

[![Image 9](https://substackcdn.com/image/fetch/$s_!HQKd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F60407b92-d6c2-4436-8f5b-cf9b33fdb42f_860x282.png)](https://substackcdn.com/image/fetch/$s_!HQKd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F60407b92-d6c2-4436-8f5b-cf9b33fdb42f_860x282.png)

图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

毕竟，我们头脑中的知识，在被编码进系统之前，对 AI 来说是不可用的。对这些投入的回报将是巨大的、非线性的。我们也许会争辩说，从长期看它们本来就总会回本。但现在每一位 CEO 都急不可耐地想要尝到那些 AI 小甜饼，所以就给他们吧。纪律在前，甜饼在后。

软件工程团队中在短而快的反馈回路中工作的比例（在我看来，这是纪律的核心标志），一直都小得令人震惊。5%，也许？肯定不到 10%。AI 工具让这件事比以往任何时候都更[触手可及](https://www.honeycomb.io/blog/you-had-one-job-why-twenty-years-of-devops-has-failed-to-do-it)。或者说，它能做到。它有可能做到。对工程纪律的投资所产生的不连续回报是真实存在的，真实到这件事也许真的会发生。

至少在近期，我并不担心 AI 会在缺乏工程纪律的情况下创造巨大、不连续的投资回报。（很多人会尝试，而观看这个过程会很有娱乐性。）

但价值由耐久性支撑，而不是由可丢弃性支撑，我看不到这一点会改变。bit 很便宜、很快，并且受逻辑和语言规则支配；但任何有价值的东西，最终都必须同物理系统相结算：一边是持久性，另一边是用户体验。

人们_不想_每天醒来登录 Slack，发现按钮和菜单都微妙地挪了位置。人们_不想要_大多数时候能完成的金融交易。确定性不会消失，我的朋友们。

AI 不是魔法。这仍然是工程。正如 Adam 所说，“它仍然是技术，而技术需要技术专家。”而我本人很期待学习新的、有趣的工程问题，评审不同类型的 artifact。

并且_再也_不做那种黏糊、挑剔、持续两年的 API 重写或 strangler fig 迁移，永远，_永远_不再做。

_~charity_

P.S. 感谢所有阅读草稿并给我反馈的人：Dave Williams、Chad Fowler、Adam Jacob、Mark Ferlatte、Austin Parker、Erwin van der Koogh、Ankur Bhatt。

[1](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline#footnote-anchor-1)

我上一篇文章并_不是_想做到中立或面面俱到，只是想给每个人一条基本的礼貌底线。但我觉得很能说明问题的是，我被怀疑者指责“对怀疑者过于苛刻”的次数，被热衷者指责“对热衷者过于苛刻”的次数，以及有时仅仅被说“有些人无法接受现实，真可悲”却完全没有说明他们指的是哪一边的次数，都相当多。主啊。

[2](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline#footnote-anchor-2)

Fred Hebert 和我在 2025 年 3 月做了 [SRECon 的闭幕主题演讲](https://www.usenix.org/conference/srecon25americas/presentation/majors)，我们告诉 SRE，他们应该去了解 AI，[也许甚至试试 vibe coding](https://charitydotwtf.substack.com/p/my-hypothetical-srecon26-keynote)（停顿等笑声），因为否则他们的批评不会那么有说服力。

说真的，那就是我们的核心主张。学习 AI，_这样_你才能更有效地抱怨。

[3](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline#footnote-anchor-3)

比如基础设施。顺便说，我觉得很多工程师都是如此。我只是觉得，对那种报名去当 SRE 的工程师来说，这一点真的_非常非常_真实。技术悲观主义和 ADHD，我们最具定义性的两个特征。

[4](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline#footnote-anchor-4)

有一部分 AI 热衷者相信，我们正在进入一个永恒指数增长的时代，在这个时代里，机器会以我们无法理解的方式，开始制造越来越好的机器。

我认为这些人数学不好。关于指数增长，我们唯一确定知道的一点是：_它会结束_。它总会结束。要么以 S 曲线结束，要么以崩溃结束。（想找点乐子的话，去 Google Heinz von Foerster 和“our great-great grandchildren will be squeezed to death”。）

我当然认为我们会用机器来制造机器——废话，我们已经在这么做了——但那关乎递归和专业化。我认为我们现在身处其中的这条指数曲线，是由追逐高回报的泛滥廉价资金、软件作为语言和逻辑函数的属性，以及一个技术繁荣早期总会出现最大发现这些因素共同创造的，因为低垂的果子总会最先被摘走。

我的个人感觉——请记住，我完全不是 AI 专家——是 AI 模型的指数级进步已经在一段时间前趋于平缓，收益变得更难获得，也更偏向增量性质。当然，我可能最终会被证明非常错误。但即使未来不再出现任何 AI 创新，过去一年释放出来的积压力量也已经足以彻底重塑我们所知的软件行业。就像一头卡在蟒蛇肚子里的猪，我们会在很长时间里持续处理其后果。

[5](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline#footnote-anchor-5)

关于这一点，很快会有更多内容。极其快。请关注 [Honeycomb](http://honeycomb.io/blog) 博客！

[6](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline#footnote-anchor-6)

这项技术很酷，但作为一个会思考、有感受、会呼吸，并且关心他人的人，要对一件让这么多人如此不安的东西感到兴奋，可能很难。当许多声音最大的人在外面兴高采烈地谈论让所有人永久失业，而那么多艺术家、作家和发展中国家的人公开谈论它对他们的影响时，也很难对它感到兴奋。

我恳求你，先压住现在想跳进来训斥我的欲望。正如我所说，我会在下一篇文章里处理使用 AI 的伦理和道德问题。说实话，你的注意力跨度并不比我更适合读一篇 10,000 字文章，而我也并不比你更适合写一篇。（这也能怪 AI 吗？）

[7](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline#footnote-anchor-7)

“另一个 Fowler。”我理解他们大概已经开这个玩笑开了……五十年。

[8](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline#footnote-anchor-8)

我在《Observability Engineering》第二版第 32 章里分享了这个故事的更长版本，本周_晚些时候_就可以下载！！

[9](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline#footnote-anchor-9)

Adam 很少看错技术，而且我 100% 确信他正在生活和工作于软件工程的_某一个_未来。我不那么确定的是，这是否就是我们所有人都会生活其中的未来。如果软件中最困难的部分从来都不是写代码——而我相信正是如此——那么逻辑上可以推出，即使代码生产的经济学降为零，困难的部分仍然会困难。
