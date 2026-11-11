---
id: netcom-ai-interpretability-capabilities-alignment-001
title: "◇ 可解释性进步的能力加速风险"

module: netcom
submodule: ai
topic: interpretability-capabilities-alignment

type: translation
status: active
canonical: true

summary: >
  作者认为，可解释性方法的进步可能通过提高训练效率、支持模型内部改写与递归自我改进，加速 AI 能力的提升，且这种作用可能超过其对对齐研究的帮助。文章以国际象棋等例子展开论证，并讨论安全开展可解释性研究所需的协调条件。

parents: []
related: []

tags: [interpretability, ai-safety, alignment, ai-capabilities, recursive-self-improvement, neural-networks]

audience: [self, public]
languages: [zh]

maturity: stable
confidence: null

visibility: public
source_of_truth: translation

original_title: "Advances in interpretability would boost capabilities more than alignment"
original_source: "LessWrong"
original_publisher: "LessWrong"
original_url: "https://www.lesswrong.com/posts/hz4kNf8tnowwSrh6R/advances-in-interpretability-would-boost-capabilities-more"
translation_note: >
  根据上述资料形成的中文阅读记录，供个人查阅。相关表述以原始来源为准。

extra:
  original_author: "Alex Amadori"
  original_published: "2026-11-10"

note: >
  未独立评估原文观点的可靠度。

created: "2026-11-11"
updated: "2026-11-11"
---

# ◇ 可解释性进步的能力加速风险

SOURCE

[Advances in interpretability would boost capabilities more than alignment](https://www.lesswrong.com/posts/hz4kNf8tnowwSrh6R/advances-in-interpretability-would-boost-capabilities-more)

作者：Alex Amadori · 来源：LessWrong · 日期：2026.11.10

NOTE

根据上述资料形成的中文阅读记录，供个人查阅。相关表述以原始来源为准。

---

许多人认为，可解释性是对齐研究的一大瓶颈。因此，许多关心 AI 安全，尤其是灭绝风险和其他灾难性风险的人，都在从事可解释性研究。

在这篇文章中，我想论证：更好的可解释性方法很可能会大幅加快能力进步。更糟的是，它们对能力进步的加速作用，会远远超过对对齐进展的加速作用。这既适用于当下的世界，也适用于任何一个在 ASI 开发上尚未达到极高程度的协调与理智的世界。

只要一种世界观认为，能力进步越快，灾难就越可能发生，那么在这种世界观下，我们就应当预期，可解释性的进步会使灾难发生的概率大幅上升。

简而言之，这是因为我们越擅长解释 AI，AI 就越有能力阅读和优化自己的代码。这意味着，可解释性的改进会催化递归自我改进（RSI）。

如果你关心 AI 带来的生存风险，并因此从事可解释性研究，我恳请你想一想这个问题，并考虑停下来。

## 以国际象棋作为 AI 能力的简化示例

作为一个领域，“可解释性”是一组松散相关的研究议程，而不是一个有明确定义的事物，因此我想先明确自己所说的可解释性是什么。

在本文中，凡是有助于理解模型内部及其思考方式的东西，都属于可解释性。我将用国际象棋作为 AI 所执行任务的一个简化示例。这样做是为了说明：在算力和训练数据相同的情况下，帮助我们理解 AI 如何下棋的方法，也会让我们大幅提升 AI 的棋力。[[1]](https://www.lesswrong.com/posts/hz4kNf8tnowwSrh6R/advances-in-interpretability-would-boost-capabilities-more#fn-znH8yEYcxJbekTwxp-1)

具体来说，让我们想一想，现代通用 AI 是如何思考国际象棋的。先说明一下，它们的水平相当不错：Opus 5.5 在高思考强度设置下，[棋力大约为 Elo 2100 分](https://chessbench.org/)（强业余棋手的水平）。在这一设置下，Opus 5.5 平均思考时长只有个位数分钟，远远不足以像专用国际象棋引擎那样搜索庞大的博弈树。因此，它必定是在使用某些有效的启发式方法，而非穷举搜索。

这种 AI 是怎样下棋的？我们可以设想，它在内部所做的一件事，是使用一组启发式方法，在不预先推演后续着法的情况下判断棋盘局面是否“好”。任何下棋的智能体都需要这一点，因为你不可能把每一棵博弈树都模拟到终局。

其中一种简单的启发式方法，就是统计棋盘上还有哪些棋子。对于 AI 可能评估的任何假想局面，这种方法都能告诉它，某一方是否因为剩余棋子更多而占据优势。

稍微复杂一点的启发式方法，可能会沿着某些博弈树向前模拟几步，再将结果交给更简单的启发式方法，例如棋子计数。例如，国际象棋中经常出现多步“兑子序列”，双方会在其中交换许多棋子。由于这一连串着法的每一回合都存在威胁，它们往往具有相当强的强制性。能够评估这些序列的结果，是一项重要的棋艺：这样你才能判断应该引发还是避开它们，甚至判断是否应该提前为它们布局。

既然我们讨论的是通用 AI，它很可能还会用到一些与国际象棋毫无关系的回路。例如，AI 大概对下面这种情况有一种普遍的判断能力：自己已经在解决问题的某种思路上花了太久，应该寻找其他思路了。

它们甚至可能有办法判断，哪些领域值得花更长时间思考，哪些领域更值得多作探索而非利用已有成果，以及在哪些领域，一轮头脑风暴应当能够涵盖所有合理的想法。

## 可解释性会大幅加快能力进步

举过一些可解释性或许能帮助我们解码的“回路”之后，让我们回到核心问题：在算力和训练数据相同的情况下，更好的可解释性方法，能否提升我们把 AI 培养成强大棋手的能力？[[2]](https://www.lesswrong.com/posts/hz4kNf8tnowwSrh6R/advances-in-interpretability-would-boost-capabilities-more#fn-znH8yEYcxJbekTwxp-2)

我的主张是，可解释性方法的任何重大改进，例如我们可能希望用来帮助对齐研究的那种改进，都会使开发者能够以高得多的效率训练 AI，从而大幅加快能力进步。

可解释性越好，神经网络就越像代码。权重不再完全难以理解，而会变得更像可以阅读和修改的源代码。这样，人类和 AI 就能直接看见并优化 AI 的内部算法。

要理解这为什么意义重大，不妨想一想：人类学习国际象棋所需的训练数据，比 AI 少得多。[[3]](https://www.lesswrong.com/posts/hz4kNf8tnowwSrh6R/advances-in-interpretability-would-boost-capabilities-more#fn-znH8yEYcxJbekTwxp-3)

设想你是一个聪明人，正尽力学习国际象棋，但不允许阅读任何国际象棋理论。[[4]](https://www.lesswrong.com/posts/hz4kNf8tnowwSrh6R/advances-in-interpretability-would-boost-capabilities-more#fn-znH8yEYcxJbekTwxp-4) 假设你正在下一盘棋，结果陷入极为不利的局面，或者直接输掉了。你想弄清楚，自己下过的哪些着法对败局负有更直接的责任，以免今后再下出类似的着法。

这极其困难，因为假设空间十分庞大。你下出的每一步棋，都可能通向一棵截然不同的博弈树。你怎么判断，自己的哪些着法明显劣于其他选择？

作为一个聪明人，你可以依靠自己对对抗性、最优性以及受约束的行动空间等概念的理解。即使你从未研究过这些概念，你在这方面的直觉也远远优于一个随机初始化的神经网络。

例如，要赢下国际象棋，就意味着让对手没有任何办法保住自己的王。因此，一听到规则，你就会立刻猜到，自己应该尽可能限制对手的行动空间。

即使一盘棋都还没下，你大概也能猜到：对方棋子越少越好（因为这限制了对方的行动空间），自己的棋子越多越好（因为这让你有更多办法限制对方王的移动）。这样一来，你就已经提出了判断棋局优势最重要的启发式方法，而提出一种启发式方法，几乎已经完成了验证它所需的全部工作。[[5]](https://www.lesswrong.com/posts/hz4kNf8tnowwSrh6R/advances-in-interpretability-would-boost-capabilities-more#fn-znH8yEYcxJbekTwxp-5)[[6]](https://www.lesswrong.com/posts/hz4kNf8tnowwSrh6R/advances-in-interpretability-would-boost-capabilities-more#fn-znH8yEYcxJbekTwxp-6)

随着对局增多，第一性原理会帮助你很快想到保护棋子、强制着法以及强制兑子序列等概念。与之相比，一个对各种假设持均匀先验、起步时毫无领域知识的学习算法，要见过数量极其庞大的对局之后，才可能产生这么好的想法。

反向传播之所以更慢，是因为它并不智能。它无法灵活运用领域知识，也无法运用 AI 设计的第一性原理。人类和通用 AI 能够做到，反向传播却做不到。[[7]](https://www.lesswrong.com/posts/hz4kNf8tnowwSrh6R/advances-in-interpretability-would-boost-capabilities-more#fn-znH8yEYcxJbekTwxp-7)

如果我们能够直接读写 AI 的内部结构，就可以开始运用智能来设计 AI 算法，而不是用反向传播让它们逐渐演化。因此，我预计能力进步会大幅加速。

说清楚一点，我并不认为人类会开始手工重写 AI 的代码。很可能，即使你已经把 AI 的内部结构简化到无法再简化的程度，其中仍然包含过于庞杂的逻辑，人类无法直接理解和编辑。

我的预期是，我们会看到可解释性方法逐步（但很快！）得到采用，以尽可能大规模动用算力的方式加速 AI 训练。在实际操作中，AI 会承担海量繁杂的工作：阅读那些只得到部分解释的内部回路，并判断是否应当修改、增强、重构、清除它们，或作其他处理。[[8]](https://www.lesswrong.com/posts/hz4kNf8tnowwSrh6R/advances-in-interpretability-would-boost-capabilities-more#fn-znH8yEYcxJbekTwxp-8)[[9]](https://www.lesswrong.com/posts/hz4kNf8tnowwSrh6R/advances-in-interpretability-would-boost-capabilities-more#fn-znH8yEYcxJbekTwxp-9)

当然，AI 进步是一个可以验证的领域，这意味着我们可以训练 AI，让它作出更好的修改，以获得更高的性能，然后你就会被拆解成回形针。

## 简化示例之外

当我们走出国际象棋这个简化示例，进入更贴近现实的领域时，我认为，我们有更充分的理由相信，可解释性方法会大幅加快能力进步。

**偏差与噪声。** 现实世界中的奖励可能带有偏差和噪声。训练数据设计不当，会让虚假相关混入其中。在某些领域，单个回合的结果包含很大的随机性，即使数据没有偏差，也可能充满噪声。

在这些情况下，关于哪些回路有用，训练过程可能需要花很长时间，才能把垃圾假设与正确假设区分开。我们越能清楚地理解这些回路，就越容易识别出其中哪些回路捕捉到的是偏差或虚假相关。

**将反思性知识蒸馏为执行技能。** 良好的可解释性，让我们更容易把 AI 的知识蒸馏为它的执行技能。以软件工程为例，AI 可能“知道”某种内存访问模式往往能使软件运行得更快，却仍然倾向于使用另一种访问模式。可解释性会让 AI 的反思性知识与实际执行行为的同步变得容易得多。

**重构与泛化。** 你还可以大规模重构 AI。考虑到 AI 的开发方式，我们应当预期，它们是糟糕的软件。无论充斥着临时特例的意大利面式代码在神经网络中对应着什么，我们都应当预期会在 AI 内部找到它。[[10]](https://www.lesswrong.com/posts/hz4kNf8tnowwSrh6R/advances-in-interpretability-would-boost-capabilities-more#fn-znH8yEYcxJbekTwxp-10)

有了更好的可解释性方法，我们就有可能重构这些代码，大幅简化它们，并把此前零散割裂的智能片段统一起来。对于通用 AI，这可能极其强大：如果有些模式在某个领域（例如系统设计）很容易学会，却能够泛化到许多其他领域（例如操纵人类），便是如此。

即使是最聪明的人，他们的大脑很擅长在不同学科之间建立联系，也从未像今天的 AI 那样，对如此多的学科掌握得如此深入。而当他们确实建立起某种联系时，也无法瞬间更新自己所有的思维模式，将这种联系融入其中。

## 可解释性不等同于对齐

我确实认为，更好的可解释性方法会在一定程度上帮助对齐研究。即便如此，它们仍然会提高这样一种可能性：我们还没有掌握足以防止灾难的对齐科学，就已经获得了足以毁灭世界的能力。

可解释性不等同于对齐。它可以帮助对齐，单是让 AI 行为的静态分析和动态分析容易得多，就已经有帮助了。它可能让我们作出这样的保证：“AI 永远不会做 X”，或“只要 AI 做了 X，我们就能立即检测到并将其关闭”。其中，X 是关于 AI 内部算法的任意逻辑陈述。

这并不等于解决了对齐问题，因为我们想要的对齐性质，极不可能与关于 AI 内部算法的逻辑陈述形成清晰的对应关系。例如，我们可能希望 AI 永远不欺骗我们，但无法保证，所有会导致 AI 欺骗我们的执行路径，都被清楚地标记为某种“欺骗”概念。

事实上，AI 在推理时是图灵完备的，因此，只要有必要，它们就可以从头重新实现欺骗。任何程序员都应当明白：如果你的程序中嵌入了一台图灵机，就没有已知的方法能够保证你的程序永远不会执行某种特定计算，更不用说仅靠关于元层级程序堆栈跟踪的某条简单逻辑陈述来做到这一点。

从人们如何把可解释性介绍为对齐问题的解决方案，就能看出一些迹象。即便假定我们已经获得极其强大的可解释性方法，也没有人提出接下来该做什么的计划。人们只是含糊其辞。含糊的直觉，或许能为“可解释性会*有所帮助*”这一信念增添一点可信度，但也仅此而已，而对齐极其困难。

除此之外，我们甚至还不知道自己究竟想要确保哪些对齐性质。对于顶层概念，例如 CEV 和可纠正性，我们只有极其初步的想法。但据我所知，即使有强大的可解释性方法，也根本没有人知道该如何将这些概念分解成更低层级的保证，再进一步分解，如此反复，直到得到某种能够在 AI 上检验的逻辑谓词。

事实是，要想清楚可解释性方法如何帮助 AI 提升 AI 能力，远比要想清楚这些方法如何帮助人类解决对齐问题容易。

## 可解释性对能力的促进大于对对齐的帮助

**能力比对齐更容易验证。** 对齐不是一个可以验证的领域。我们不知道该怎样定义它，才能加以测量。相比之下，能力要容易验证得多。事实上，你现在就可以问 Opus 5.5，如何衡量 AI 在各类能力上的改进，它会给出不错的想法。

由于能力改进可以验证，任何让 AI 能够尝试提升 AI 能力的方法都极其危险。这是一个可以验证的领域，意味着即使 AI 起初不擅长做这件事，它们也会偶尔成功。即使没有任何可解释性方法，AI 也[已经成功地](https://x.com/rikiyatakehi/status/2117313742891327994)通过直接编辑权重，提升了一个 AI 的性能。

只要它们偶尔能够成功，你就可以把这种成功用作强化学习回合的奖励。

**有了可解释性，AI 会先被 AI 读懂，然后才被人类读懂。** 为了帮助智能体理解 AI 的内部结构，可解释性方法可以把其巨大的复杂性降低到更便于认知处理的程度。但让 AI 能够读懂 AI，远比让人类能够读懂 AI 容易。

设想我们在可解释性上取得了一个惊人的突破：成功把一个权重占用 10TB 的 AI，压缩成了 1GB 极其晦涩的 Rust 代码，外加 1TB 的数据库；这些代码访问数据库的方式受到相当严格的限制。

用这种方式表示 AI，并不会自动让人类理解它。即使有 AI 帮助，理解这样一个代码库也可能花上数十年。至少，我们需要为函数和数据库条目加上标签。其中大部分都不会对应于那种能用一句简短英文描述的概念，而且它们彼此之间会有复杂而出人意料的相互作用。

这个代码库会大到任何一个人都无法理解。我们需要建立分层表示，找到让大群人分工理解代码的方法，以及为没有任何一个人能够完全理解的代码提供形式化与非形式化保证的方法。这就是人类为了对齐而试图确保 AI 的行为性质时所面临的问题。

试图提升 AI 能力的 AI 并不面临这个问题。一方面，AI 的“可塑性”强得多：与人类相比，它们远没有那么在意代码是否标注得清楚，只要大量接触，就会开始理解其中的模式。

此外，一个正在进行递归自我改进的 AI，并不需要像试图解决对齐问题的人类那样，落实严格的保证。对于 RSI，只要它提出的修改利大于弊的次数多于弊大于利的次数，就足以让收益随时间不断复合增长。

在最坏的情况下，对 AI“代码”的任何修改都会未经测试就直接部署。此时，AI 要实现递归自我改进，只需要它所作的干预能够提升能力的概率略高于 50%。

在最好的情况下，基准测试能够可靠地测出性能下降，并筛除任何不良修改；此时，只要改进的概率不为零，收益就会随时间不断复合增长。

## 有例外吗？

是否存在一些可解释性研究议程，它们对帮助我们准备解决对齐问题的作用，大于对帮助我们造出毁灭世界的 AI 的作用？

我不是可解释性研究者，也没有跟进每一个小型可解释性项目。因此，我无法有把握地断言，每一种可解释性研究议程都会以这种方式带来坏处。

我可以想象，也许存在某种研究议程，能有选择地增进我们对安全相关性质的理解，但如果真有，我会感到意外。你怎么可能在不增进对 AI 内部结构的一般性理解的情况下，理解 AI 的安全性质？

## 在什么情况下，从事可解释性研究才是合理的？

在某些世界里，从事可解释性研究是合理的。在那些世界里，你可以确信：一种能够提升能力的技术，只有在非常明确地确定这样做是安全的情况下，才会被用于提升能力。

这需要极强的协调。必须有一种机制，确保世界上没有任何人会使用某种可解释性技术来提升能力。我们需要确保，世界上没有任何一家 AI 公司或任何一个研究项目能够这样做。

现实地说，只有政府能够强制落实这一点：你要么需要国家级的信息安全能力，防止这种方法的知识外泄；要么需要国家的强制力，可靠地阻止各方利用这种方法提升能力。即使如此，你仍然需要建立一些办法，使各国政府能够*相互*信任，确信对方没有使用新的可解释性技术来提升能力。

要让可解释性研究成为合理的工作，还需要在 ASI 研究上保持极高程度的理智。无论由什么机制决定是否将这项技术用于提升能力，该机制都必须拒绝使用它，除非它确信这样做是安全的。

就当前的情况而言，我的看法是：作为一名可解释性研究者，你正在帮助 AI 公司加快能力进步，并毁灭世界。如果你目前正在从事可解释性研究，请考虑停下来。

如果你希望从事可解释性研究能够是安全的，请转而帮助建立所需的协调与理智。

1.   我在这个例子中使用的认知算法，可能并不完全等同于 AI 实际下棋的方式，但愿这不影响一般性。不过，我确实尽力选用了那些有多重理由表明应当存在的思维模式；考虑到 AI 的棋力，它的内部实在应该存在这些模式。 [↩︎](https://www.lesswrong.com/posts/hz4kNf8tnowwSrh6R/advances-in-interpretability-would-boost-capabilities-more#fnref-znH8yEYcxJbekTwxp-1)

2.   请记住，虽然我们很容易生成国际象棋的训练数据，但对于 AI 研究这样的关键领域，我们做不到这一点，因此这是一个非常重要的问题。 [↩︎](https://www.lesswrong.com/posts/hz4kNf8tnowwSrh6R/advances-in-interpretability-would-boost-capabilities-more#fnref-znH8yEYcxJbekTwxp-2)

3.   我们真的知道这一点吗？我做过一个小测试，Fable 5.0 不需要查找我的信息，就能凭记忆知道我在哪里工作。据我估计，在当时的互联网上，我的名字与雇主名称或其他工作相关信息一同出现的次数，还不到大约 10 次。我会假定，即使在记忆方面未必如此，人类在学习技能时的样本效率仍然更高；因为如果 AI 训练的样本效率已经与人类相当，哪怕仅限于计算机任务，我也会预期世界已经呈现出非常不同的面貌。 [↩︎](https://www.lesswrong.com/posts/hz4kNf8tnowwSrh6R/advances-in-interpretability-would-boost-capabilities-more#fnref-znH8yEYcxJbekTwxp-3)

4.   设下这个限制，部分是为了避免去区分哪些知识来自阅读理论、哪些来自实践所带来的复杂性，因为我认为这种复杂性与本文的论点关系不大。另一部分原因，是让它更类似于 AI 学习开展 AI 研究的情形：我们有出色的人类 AI 研究者，却没有一套关于如何开展 AI 研究的成熟理论，不像国际象棋那样有现成的文献。请放心，这个例子是现实的：聪明人确实经常在不阅读任何国际象棋理论的情况下，自己领悟到如此高阶的国际象棋概念。 [↩︎](https://www.lesswrong.com/posts/hz4kNf8tnowwSrh6R/advances-in-interpretability-would-boost-capabilities-more#fnref-znH8yEYcxJbekTwxp-4)

5.   参见[《爱因斯坦的傲慢》](https://www.lesswrong.com/posts/MwQRucYo6BZZwjKE7)[↩︎](https://www.lesswrong.com/posts/hz4kNf8tnowwSrh6R/advances-in-interpretability-would-boost-capabilities-more#fnref-znH8yEYcxJbekTwxp-5)

6.   实际上，人类似乎天生就觉得吃子是好事，但我不认为这是从第一性原理推导出来的。更可能的情况是，这只是人类设计游戏时的一种直觉方式，因此因果关系恰好相反。我想假设这里的主人公没有这种先天直觉，从而展示如何从第一性原理推导出这一点。 [↩︎](https://www.lesswrong.com/posts/hz4kNf8tnowwSrh6R/advances-in-interpretability-would-boost-capabilities-more#fnref-znH8yEYcxJbekTwxp-6)

7.   因为我们还没有完全理解反向传播，所以我无法确定它完全没有运用这些原理。但如果它在设计 AI 时，能够达到一个成熟的现代 AI 所能达到的效率，那会令人意外。我们从未直接优化反向传播，使它作出更好的更新；只有架构层面的一些技巧是例外，而这些技巧无法编码像我在国际象棋例子中所举的那些如此复杂的概念。 [↩︎](https://www.lesswrong.com/posts/hz4kNf8tnowwSrh6R/advances-in-interpretability-would-boost-capabilities-more#fnref-znH8yEYcxJbekTwxp-7)

8.   我不会进一步说明自己认为这会如何实现。这对本文的论点并无必要，而且我不想帮助 AI 公司做到这一点。 [↩︎](https://www.lesswrong.com/posts/hz4kNf8tnowwSrh6R/advances-in-interpretability-would-boost-capabilities-more#fnref-znH8yEYcxJbekTwxp-8)

9.   这是我对“苦涩的教训”的理解。“苦涩的教训”说的是，单凭算力，就能胜过人类手工设计事物的能力。它并没有否认好的先验有助于学习，而且好的先验显然确实有用：人类一直在利用好的先验加快自己的学习。在过去，我们只见过缓慢而聪明的人类，与快速而愚笨的反向传播相竞争。即使人类拥有智能带来的种种优势，反向传播仍然可以借助高出多个数量级的计算量，以快得多的速度让 AI 变得聪明。但我们从未见过：当一个像 AI 这样的智能体，既能利用海量计算，又能聪明地设计 AI 时，会发生什么。 [↩︎](https://www.lesswrong.com/posts/hz4kNf8tnowwSrh6R/advances-in-interpretability-would-boost-capabilities-more#fnref-znH8yEYcxJbekTwxp-9)

10.   这让我想起了一张梗图：一个名为“isEven”的函数，竟是通过为每一个整数分别编写特例来实现的。 [↩︎](https://www.lesswrong.com/posts/hz4kNf8tnowwSrh6R/advances-in-interpretability-would-boost-capabilities-more#fnref-znH8yEYcxJbekTwxp-10)
