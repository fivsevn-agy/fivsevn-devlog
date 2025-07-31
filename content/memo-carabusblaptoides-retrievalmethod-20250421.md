# memo｜マイマイカブリ情報探索メソッド(草案)

> 4月12日开始做的文章，拖到现在还没做完。
> 半成品先放这里。

## Epigraph

以日本食蜗步甲为例，简单而通用的爽玩指南。

<!-- more -->

---

## Essay

本文所涉及到的生物，在物种分类信息中的位置如下：  
https://www.catalogueoflife.org/data/browse?taxonKey=5WYSB  

本博客涉及生物内容的撰写习惯，请参考往期文章：
[锯锯鱼](https://fivsevn.home.blog/2025/03/23/%e9%94%af%e9%94%af%e9%b1%bc/)  

我们在生活当中遇到的问题，有很大一部分都可以归结为“信息检索（information retrieval，IR）”的问题。现实生活中，答案往往不是直接给出（*或者说，“直接给出的答案”要么我们普通人很难直接接触到、要么需要付出一些事先无法明确的代价、要么全凭运气*），而是需要我们从信息当中尝试找出线索、联缀线索并进行推理。在这个过程中，我们需要：  

```text
❓怎么查❓👉 检索策略  
❓该信谁❓👉 筛选能力  
❓该信多少❓👉 评估机制  
❗️下次还要❗️👉 记录系统  
```

对于寻常百姓的衣食住行而言，拥有一定的信息检索能力意味着可以解决不少日常生活当中的问题；而对于持有某种爱好的人来说，“信息检索”更是一种乐在其中的过程。相信我，系统地搭建一套适合自己的信息检索方法，并在实践中不断完善，这一定是人生清单上排名前十的重要的事。  

本文以**昆虫爱好者想要爽玩マイマイカブリ**为例，主要提供我个人的检索思路的分享；本篇当中检索到的具体的网站等信息可能会随着时间的推移而失效，但是，基础的方法论是比较稳固的。我们可以根据各自的领域和需求，以此为基础进行修改和完善，最终形成一套最适合自己的方法和体系。  
  
在“**明确自己的需求**”这一条件下，我建议，可以采用 ChatGPT 等 AI 助理协助进行方法论的优化。  

似乎有必要事先明确的术语定义：
> `检索（Retrieval）`：本文所说“检索”，指的是在搜索引擎、网站或数据库中输入关键词进行查找的操作，简单来说就是“在Google里搜一下”。因为这个词可能对于一部分人来讲不是很直观，但是作为术语来讲经常会用到，在这里明确一下并不是坏事。  
*我想，再简单的事，既然想到了，我们就一起回顾一下！一些概念可能对于一部分人来讲是理所当然，但是对于另一部分人来讲略显陌生；我认为，在日常交流的轻松场合下，不应当把他人的“应该懂”作为一种默认。也许我们确实没有“解释的义务”，但是我们可以主动选择去承担下这份“解释的责任”（限度范围内即可，并非必须，也不用很有压力，适当表达善意就行！）。对于爱好者乃至专业人士而言，基础也是在反复确认基本定义的过程当中逐渐稳固的。本博客的其他文章当中如果有任何不甚明确的内容，也请提醒我进行补充说明。*  

---

### 1. 入手途径【野采 / 线下购买 / 线上购买】
  
想要爽玩——  
  
```text
👉 1.1 野采  
👉 1.2 线下购买  
👉 1.3 线上购买  
```
  
---

#### 1.1 野采（了解物种信息 + 检索野采实绩）

有明确目标的野采，主要问题就是“哪里有？”。大方向分为：

```text
🧐 1.1.1 了解物种信息（不详述）  
🧐 1.1.2 检索野采实绩（Channel A + B + C）
  👉 Channel A：通用搜索引擎检索（Search Engine Pass）
  👉 Channel B：定向网站精查（Site-Specific Search）
  👉 Channel C：间接链路探索（Relational Discovery）
  🧐 一些通用的检索思路：检索词优化（query refinement）+批判性评估（critical evaluation）  
  🧐 实践：以マイマイカブリ野采情报收集为例！
```

---

##### 🧐1.1.1 了解物种信息（不详述）
  
> 了解物种本身的背景信息、习性等。  
> 采用通常的文献检索方式。请注意文献来源，Wiki 等百科请注意查证修改履历等信息。  
  
---

##### 🧐1.1.2 检索野采实绩（Channel A + B + C）
  
> 检索其他人的野采实绩进行分析和研究。这里介绍信息检索的三大主要渠道。  
  
###### 👉 Channel A：通用搜索引擎检索（Search Engine Pass）
> 尝试 Google 或者其他搜索引擎。  

###### 👉 Channel B：定向网站精查（Site-Specific Search）
> 记得个别平台可以单独去搜索！  
> 如果想不到有什么平台可以搜的话，可以按照以下分类去筛查。  
> 示例仅举例帮助理解网站类型，并非我常用的网站。我常用的数据库会在开发日志另外刊载。  

|   编号   | 网站类型              | 示例                                      |  信息特点  |
|----------|---------------------|------------------------------------------|----------|
| **1**    | 官方机构 / 政府站点    | `nature.go.jp`、`env.go.jp`、`usgs.gov` | 权威、可信，但更新慢 |
| **2**    | 学术数据库 / 文献库    | Google Scholar、J-STAGE、CNKI、PubMed   | 准确、有来源，但语言门槛高 |
| **3**    | 博物馆 / 科研单位      | Smithsonian、国立科学博物馆、昆虫标本馆等 | 高质量信息，但网页结构复杂 |
| **4**    | 商业购物网站          | Amazon、Yahoo Japan、淘宝、乐天         | 商品为主，有实用参数、评价，偏重销售导向 |
| **5**    | SNS / 社交媒体平台    | Twitter/X、Instagram、Facebook、微博等 | 快速传播、观点丰富，但偏见强 |
| **6**    | 论坛 / 讨论区         | Reddit、2ch、百度贴吧、insectforum.jp  | 爱好者经验、含实用信息，但真实性不一 |
| **7**    | 匿名板 / 二次元社区    | 4chan、ふたば（ふたば☆ちゃんねる）等     | 更真实/极端的用户经验，但筛选难度高 |
| **8**    | 视频网站              | YouTube、Bilibili、ニコニコ動画、TikTok   | 实物展示、操作演示为主，评论区可能有补充 |
| **9**    | 问答社区 / 众包平台    | Quora、知乎、StackExchange、知識袋       | 聚焦问题解答，通常含争议与多角度观点 |
| **10**   | Wiki / 百科型网站     | Wikipedia、Pixiv百科、百度百科           | 快速了解背景概念，但细节容易过时或有偏 |
| **11**   | 品牌官网 / 制造商网站  | Snow Peak、Evernew、学术出版社官网等     | 参数权威，营销内容多，常用作事实核查 |
| **12**   | 部落格 / 私人网站      | Ameblo、はてなブログ、个人博客、Notion页 | 爱好者记录、失败经验、偏好明显 |
| **13**   | 商品比价 / 数据网站    | Kakaku.com、Keepa、camelcamelcamel、価格.com | 客观价格变动数据，有助购买决策 |
| **14**   | 下载类资源站          | Archive.org、Open Science Framework 等   | 获取文献、历史资料、图鉴等文档原始版本 |

###### 👉 Channel C：间接链路探索（Relational Discovery）
> 看引用、点链接、追踪同类发帖、看标签页等等等等，通过这些结构化关联路径发掘隐藏资料。  
> 简而言之，一篇内容看完先不要把网页关掉，留意一些关联信息。  

---

###### 🧐 一些通用的检索思路（检索词优化+批判性评估）

```text
👉 【检索词优化（Query Refinement）】  
  ➡️ 增加限定词（Query Expansion）  
  ➡️ 同义词切换（Synonym Substitution）  
  ➡️ 关键词组合调整（Boolean Query Adjustment，布尔查询调整）  
  ➡️ 去除歧义词（Disambiguation）  
  ➡️ 多语言切换（Multilingual Retrieval）  
  ➡️ 可尝试切换代理网络（Proxy Switching / Geolocation-based Retrieval）  
  ➡️ 其他（Other Techniques）  
    
👉 【批判性评估（Critical Evaluation）】  
  ➡️ 可靠性（Credibility Assessment）  
  ➡️ 偏见（Bias Detection）  
  ➡️ 逻辑性（Information Validation）  
```

👉 【检索词优化（Query Refinement）】  
  
假设我们一开始检索的是【[Google搜索：マイマイカブリ](https://www.google.com/search?q=マイマイカブリ)】  
我们可以尝试变换各种关键词进行搜索（query refinement），例如：  
  
- `增加限定词（Query Expansion）`  
    - 【[Google搜索：マイマイカブリ どこにいる](https://www.google.com/search?q=マイマイカブリ+どこにいる)】
- `同义词切换（Synonym Substitution）`  
上述【どこにいる】可以换成其他说法，例如但不限于：  
    - 【[Google搜索：マイマイカブリ 採集](https://www.google.com/search?q=マイマイカブリ+採集)】
    - 【[Google搜索：マイマイカブリ 誘い](https://www.google.com/search?q=マイマイカブリ+誘い)】
    - 【[Google搜索：マイマイカブリ 探す](https://www.google.com/search?q=マイマイカブリ+探す)】
    - 可尝试把汉字切换成假名。
- `关键词组合调整（Boolean Query Adjustment）`  
    - 例如，把【採集】放在具体采集对象关键词的前面，尝试【[採集 マイマイカブリ](https://www.google.com/search?q=採集+マイマイカブリ)】等等。
- `去除歧义词（Disambiguation）`  
    - 如果搜索语句当中存在歧义的话，删掉再试试。  
- `多语言切换（Multilingual Retrieval）`  
    - 切换中文、日文、英语或者拉丁语等等。
    - 不论是以某种语言为主的网站（例如以简体中文用户为主的 [bilibili](https://search.bilibili.com/all?keyword=日本食蜗步甲&from_source=webtop_search&spm_id_from=333.1007&search_source=5)等）、还是全球性的网站（例如 Youtube 等），都可以切换语言试一试。
- `可尝试切换代理网络（Proxy Switching / Geolocation-based Retrieval）`  
    - 同样搜索引擎不同语言版本的结果存在差异。 插入[一则新闻](https://9to5google.com/2025/04/15/google-com-search/)，Google 搜索将停止使用 ccTLD（国家和地区顶级域名）（例如 google.com.br（巴西）、google.fr（法国）等），统一改为全球使用 google.com。因此还是尝试直接切换代理网络，网页会自动切换到对应国家。
- `更多请尝试灵机一动！`  
  
以上方法当然也有可能没啥用，但是建议都尝试一下。这是一个不断试错的过程，一开始便过于功利地追求一个结果的话，很可能会“欲速则不达”。别急就对了。
  
  
👉 【批判性评估（Critical Evaluation）】  
  
重点关注检索到的内容的背景信息。以搜索到的昆虫采集内容为例，这篇内容的创作背景可能是：

```text
【父母写的亲子活动记录】【学校组织的昆虫采集活动】【昆虫爱好者组织的自费活动】  
【喜欢昆虫的个人爱好者】【喜欢步甲的个人爱好者】【喜欢参加社交活动的人的日记】  
【涉及到该物种的研究笔记】【NPO 的宣传稿】【营利性机构的收费活动宣传】  
```

等等。  
  
判断方法：  
  
- 初步评估作者、平台、内容等是否可靠（credibility assessment）：  
> 特别要注意有没有交易活动在里面，关注点是这件事的性质是否是“交易”，而不是单纯的钱多还是钱少。  
 >  - 作者是否有相关领域的经验、学术资历、行业影响力等？（关注“圈内大佬”自身的教育背景）  
 >  - 内容看起来更像是某个营利性活动的宣传？（很多，请注意甄别）  

- 判断信息是否带有偏见或者选择性描述（bias detection）：  
> 这些当然也可以作为博主的个人特色去理解，我认为并不完全是负面的。只是有时候需要根据偏见尝试进行反向修正，以得出自己想要的信息；但并非否定原作者。  
 >  - 作者的常住地或文化背景是否影响判断？  
 >  - 是否存在个人喜好、倾向性或隐性偏见？  

- 判断作者自身的发言是否具有逻辑性（information validation）：  
> 容易忽视但非常重要；另外，过程存在逻辑性的问题并不意味着结论一定错误，针对这类结论，建议当成赌博。  
 >  - 有没有提供一些具体的细节，还是说，在没有合理说明的情况下选择避而不提？  
 >  - 这些细节是否能够验证？  
 >  - 前后有没有自相矛盾的地方？  

---

### Source 1  

作为示例，这里给一些有关【マイマイカブリ野采情报】的收集过程。  

#### Step1 
总之先随意 Google 一下试试看。
[Google 搜索：マイマイカブリ 採集](https://www.google.com/search?q=マイマイカブリ+採集)

#### Step2
如果一开始检索内容较少，那么我们的重点就放在“尽量多多挖掘”，这一点毋庸置疑。  
如果一开始检索内容较多，那么我们的重点就可以调整为“一边搜索一边整理”。如果只是挨个儿去阅览一条一条的结果，会变成内容的无序堆叠；就好比，我们只是不停地走，走过了很多地方，但是始终没有画出一个地图，把我们走过的这些地方标记到地图当中去。内容的无序堆叠会带来一些问题——看到后面忘记前面、重复的内容可能会占据过多的记忆空间、越看越疲劳、想知道更多更深入的内容但是不知道要看到什么时候才能找到，等等。我们的算力始终是有限的，这时候，我们就需要提高数据的利用效率。针对一些高频出现的要素，不论是网站、作者、团体机构等等具体的要素，还是某种模式、语言风格、视觉效果等等抽象的要素，都可以作为某种集合的标准，简而言之，就是先粗略地去分类；类目逐渐增多之后，就可以考虑“把类目进行分类”，也就是进行目录的整理；再往后，就是对目录进行优化，调整出合适的架构。说到这里，我们可能已经意识到，成长过程中我们都多少接受过类似的方法教育；问题在于，我们实际上对这个方法的理解程度和运用程度是多还是少。  
  
##### Ameba アメーバブログ
[Ameba 搜索：マイマイカブリ](https://search.ameba.jp/search/マイマイカブリ.html)  
  
- 一些反复高频出现的作者。  
- 这些作者可以进入主页专门去看他们发布的内容。  
- 存在关系网的可能。可以采用 Channe C 进行探索。  
- 作者可能在其他媒体平台有同步更新，例如 Youtube 等，记得检索。  
> [昆虫イベント企画　ルリハムシ昆虫教室（小林隆人）](https://profile.ameba.jp/ameba/takato1770/)  
> [クロクロフネ](https://profile.ameba.jp/ameba/shun-shun-1120/)  
> [非常ボタン乱れ押し](https://profile.ameba.jp/ameba/midareoshi1987/)  
> [奇虫ガスキー](https://profile.ameba.jp/ameba/aki--channel/)  
> [瓢箪坊主](https://profile.ameba.jp/ameba/witchcraft444/)  

- 一些近期的野采记录。  
- 时效性也很重要。关注一些比较新的情报，即使并非出自于深度爱好者。  
> [2025年初採集](https://ameblo.jp/ryou-ei/entry-12887566191.html)  
> [ミヤマウズラ斑入り探し](https://ameblo.jp/fc-3srx7/entry-12891737012.html)  
> [河川敷の採集](https://ameblo.jp/witchcraft444/entry-12890419373.html)  
> [CⅢ92の商品化作業　2](https://ameblo.jp/autorestoreyk/entry-12891467486.html) 注：这位博主在库房整备的时候遇到冬眠苏醒的マイマイカブリ了，挺好玩儿。  
> [あなどるなかれマイマイカブリ](https://ameblo.jp/manakaga/entry-12884713591.html)  
> [怪異！](https://ameblo.jp/obomatu/entry-12878450930.html) 注：这是装潢驱虫有关的文章，似乎提到发现了比较多的マイマイカブリ。哎呀真便宜他啦。  
  
*请以这样的思路作为参考，进行进一步的探索！*  
  
##### FC2 Blog
[用 Google 的“site:”命令搜索：site:blog.fc2.com マイマイカブリ](https://www.google.com/search?client=safari&rls=en&q=site%3Ablog.fc2.com+マイマイカブリ&ie=UTF-8&oe=UTF-8&sei=XTn7Z-mgC8jC1e8P0t2CkAg)

- 同样，先关注高频出现的作者。   
- 注意一下这个作者目前是否有在更新。  
- 不论博客是否有停更，对于具体的博客内容，都可以做一下`时效性`和`通用性`方面的判断。时刻把`时间戳`（另开文章讨论）的概念放在心上。  
> [吉丁虫色の日々](https://kontyuki.blog.fc2.com)  
> [ホペイフリークの自己満足日記](http://hopeif.blog.fc2.com/) 注：有在更新 Youtube 频道。  
> [クワガタ狂カシオペアの採集＆飼育日記【改】](http://cassiopeia19770720.blog.fc2.com/ "クワガタ狂カシオペアの採集＆飼育日記【改】")  
> [takoの昆虫メモ](http://yotubosi5364sp.blog.fc2.com/)  
> [虫けら屋の「ちょっと虫採り行ってくる！」](http://lucanidae.blog.fc2.com/ "虫けら屋の「ちょっと虫採り行ってくる！」") 注：这个人搬到 Ameba 了：[虫けら屋の「ちょっと虫採り行ってくる！」](https://profile.ameba.jp/ameba/64kera8/)，但是 FC2 这边的帖文存档也可以看一下。  
> [干物虫屋の採集記](http://golgimaimai.blog.fc2.com/)  
> [へっぽこ昆虫採集記](http://siaymito.blog.fc2.com/ "へっぽこ昆虫採集記")  
> [東京23区内の虫 2](http://tokyoinsects2.blog.fc2.com/)  
> [気ままにマイクワ日誌](http://buranko42.blog.fc2.com/)  
> [ふわもち昆虫日記](http://sayurizevodsk21464.blog.fc2.com/ "ふわもち昆虫日記")  
> [甲虫三昧](http://soda62.blog.fc2.com/)  
> [ギリギリダークサイド](http://toasanoumi.blog.fc2.com/ "ギリギリダークサイド")  
> [何有荘ｶﾕｳｿｳのブログ](http://ismkayusou.blog.fc2.com/) 注：这个人比较综合，挺有意思的。  
> [100円でできる昆虫採集](http://garnetplanet0512.blog.fc2.com)  
> [きままのTOEIC満点990&クワガタ](http://toeic990kuwagata.blog.fc2.com/ "きままのTOEIC満点990&クワガタ") 注：教托业顺便玩虫是吧，虫圈托业哥！  
> [Slapp Happy!!](http://vaultthatborderline.blog.fc2.com) 注：如果是有农业大学背景的作者，记得关注一下他们方法论相关的内容。  
> [生きとし生けるもの何でも観る記](http://futagoyamazushi.blog.fc2.com/ "生きとし生けるもの何でも観る記")  
> [いない虫はとれない。](http://inatore.blog.fc2.com/ "いない虫はとれない。")  
> [マイマイカブリの東MAXブログ](http://ryjhencetvmaadl2fmco.blog.fc2.com/ "マイマイカブリの東MAXブログ")  

- 其他相关。  
> [たがや](http://tagayajp.blog.fc2.com/) 注：这个人似乎是自己制作金属虫模。  
> [日本固有種の昆虫「マイマイカブリ」](http://angeyamagata.blog.fc2.com/blog-entry-1167.html) 注：不是爱好者，但是可以看一下捉到マイマイカブリ时候的环境等条件。这种都是值得纳入マイマイカブリ生息地的数据库的资料。之前我在收集[锯鳐资料](https://fivsevn.home.blog/2025/03/23/锯锯鱼/#more-650)的时候搜到 [ISED（国际锯鳐目击数据库）](https://www.floridamuseum.ufl.edu/sawfish/map/)这样的数据库，对于濒危物种或者地方特有物种，这方面可以多多关注。  
> [マイマイカブリ。](https://ginsuke02.blog.fc2.com/blog-entry-1575.html) 注：这个采集到マイマイカブリ时候的气温似乎是蛮高的。另还有遭遇幼虫一篇：[マイマイカブリの幼虫。](https://ginsuke02.blog.fc2.com/blog-entry-1654.html)。真不错啊！  
> [トラフトンボ 。。。（マイマイカブリ・コサナエなども）](https://chankochan.blog.fc2.com/blog-entry-5627.html)  
> [エゾマイマイカブリ他](https://f2ex.blog.fc2.com/blog-entry-4535.html?sp) 注：看主页是个胶佬。  
> [マイマイカブリ（蝸牛被）](https://kangensui2017.blog.fc2.com/blog-entry-2046.html)  
> [オサムシ幼虫か](http://chisaito.blog.fc2.com/blog-entry-287.html)  

*资料收集的第一要义是耐心。如果是学术研究的话，理论上讲，不论多寡，所有相关的先行文献都应该彻查一遍。从操作上讲，“探索未知”很大一部分其实是在“探索已知”。*  

##### Hatena はてなブログ
 [用 Google 的“site:”命令搜索：site:hatena.blog マイマイカブリ](https://www.google.com/search?client=safari&rls=en&q=site%3Ahatena.blog+マイマイカブリ&ie=UTF-8&oe=UTF-8&sei=mT37Z_TUK52Gvr0Pso31gAQ)  
   
 - 检索到的主要都是这位作者。  
> [虫村の日記](https://musimura.hatenablog.com/)   

- 另外有一篇研究向的文章。一般写得出这种内容的作者都非常值得关注一下。  
> [マイマイカブリの地理的変異：首が細いか太いか](https://naturalist2008.hatenablog.com/entry/20101231/1293778424)  

*可以推测虫佬的博客大致集中在 Ameba 和 FC2 上面。*  

##### Note ノート
 [Note 搜索：マイマイカブリ](https://note.com/search?q=マイマイカブリ&context=note&mode=search)  
   
 - 一些爱好者的主页。 
> [トモロウ](https://note.com/tomorrows_nest)  
> [ぴ。](https://note.com/witty_clover434)  
> [かんずく](https://note.com/lofty_whale2048)  
> [オサム](https://note.com/kitakaburi)  
> [mofuuu/オオキベリアオ](https://note.com/mofuuu294)  
> [JLS](https://note.com/papilio_asotus)  
> [魁‼︎奇蟲天国❤️](https://note.com/cute_marten840) 注：这哥们之前 Ameba 上面[也有看到](https://ameblo.jp/aki--channel/)。Ameba 那边更新比较新。  
> [キヨタミ](https://note.com/kiyotami_note)  
> [虫田](https://note.com/eager_clam6156)  
> [Hinata](https://note.com/hinatatsu)  
> [姫アサギ](https://note.com/amabilis)  
> [あつすぎ](https://note.com/gifted_elk812)  
> [Project WILD JAPAN](https://note.com/projectwild) 注：关联主页的[图鉴](https://www.projectwild-museum.jp)感觉很有用。  

- 还有一些主页不是虫为主，但是有更新一些相关的文章。  
> [トガミ昆虫記③ アオオサムシ](https://note.com/togami10/n/nc4f3e353b1ba)  
> [壁の虫](https://note.com/mamimujina/n/ne8314b1dd600)  
> [マイマイカブリ](https://note.com/butsuzou1046/n/n815a5d2ef817)  
> [今世紀最大のニュース！オサムシの新種、福島で発見される！](https://note.com/syoudagokurou/n/nbc0ec08440bf)  
  
##### Livedoor
- 用 Google 的“site:”命令搜索没爬得出，可能有爬虫限制。
- 可能需要登录才能使用网站内部的检索系统？也有可能我看漏了。
- 不过一般的 Google 搜索[Google搜索：マイマイカブリ 採集](https://www.google.com/search?q=マイマイカブリ+採集)会出现一些相关内容，我搜到的是[鬼怒川&那珂川マイマイカブリ採集記](https://agrobio.livedoor.blog/archives/17608684.html)，还是个漫画。
- 可以在 Livedoor 网站的[昆虫类目](https://blog.livedoor.com/category/157/)下去找找文章。这种反爬虫的网站可能内部建有自己的分类系统。

##### 楽天ブログ
 - [楽天ブログ搜索：マイマイカブリ](https://cse.google.com/cse?ie=UTF-8&q=マイマイカブリ&cx=002636997843861491696%3Adqgmv6ghta0&sa=&siteurl=plaza.rakuten.co.jp%2F&ref=&ss=)   

- 一些爱好者的主页。
> [昆虫採集と飼育の毎日](https://plaza.rakuten.co.jp/pryeri/)   
> [bayashi](https://plaza.rakuten.co.jp/syou0806/)   

- 自然观察综合。因为主页内容比较综合，这里就只放通过マイマイカブリ检索看到的文章。  
> [マイマイカブリを見つけた。](https://plaza.rakuten.co.jp/ootakuwildlife/diary/201905090000/)  
> [マイマイカブリ](https://plaza.rakuten.co.jp/siroharu/diary/201003250000/)   
> [マイマイカブリ](https://plaza.rakuten.co.jp/jijiran/diary/200604180000/)   
> [猪名川河川敷マイマイカブリ採集](https://plaza.rakuten.co.jp/gokki/diary/200712200000/)  
> [マイマイカブリ](https://plaza.rakuten.co.jp/kitchinkato/diary/201305020000/)  
> [トンボ；ミヤマアカネ♂、マユタテアカネ♂。様；ベニシジミ。昆虫；マイマイカブリ。](https://plaza.rakuten.co.jp/mae717da/diary/202412060001/)  
> [て、づっか　オサムシ](https://plaza.rakuten.co.jp/bnvn06/diary/202007150000/)  
> [我が家に迷い込んだゲスト](https://plaza.rakuten.co.jp/udoku369/diary/200610280000/)  
> [この虫はなんなんでしょうか、、、、、。](https://plaza.rakuten.co.jp/silverheltz/diary/200711130000/) 注：作者看起来不是虫虫爱好者，但是拍到的照片是マイマイカブリ的幼虫在嗦蜗牛！！  
> [室生の旅のアルバム](https://plaza.rakuten.co.jp/madaranov/diary/201206120001/)  
> [アゲハの幼虫が成長](https://plaza.rakuten.co.jp/mabo400dc/diary/201207240001/)  
> [松くい虫の殺虫剤空中散布](https://plaza.rakuten.co.jp/udoku369/diary/200606300000/) 注：本文反对无差别直升机喷洒杀虫剂。  

##### 一些博客收集平台
- 类似博客的黄页（Yellow Pages），一般是个人主动申请登录的。  
- 可以按照收录类别去检索。  
- 顺带一提，以下两个网站是我从 [吉丁虫色の日々](https://kontyuki.blog.fc2.com)  的页面上看到的。  
> [にほんブログ村](https://blogmura.com)  
> [人気ブログランキング](https://blog.with2.net)  

*请以此为思路继续探索！*

##### 其他媒体平台
 - Daily Portal Z（デイリーポータルZ）比较有意思的媒体平台。
[Daily Portal Z搜索：マイマイカブリ](https://cse.google.com/cse?cx=partner-pub-7606411586889028%3A8688168104&q=マイマイカブリ&sa.x=0&sa.y=0#gsc.tab=0&gsc.q=マイマイカブリ&gsc.page=1)  

- マイマイカブリ为主的内容。
> [長崎県・福江島で巨大マイマイカブリを探す](https://dailyportalz.jp/kiji/kyodai-maimaikaburi) 
> [真冬の昆虫採集 ｢オサ掘り｣](https://dailyportalz.jp/kiji/120309154113)

- 不是マイマイカブリ为主，但是也很有意思的内容。
> [｢木に甘いものを塗っておくと虫が集まる｣説は本当か](https://dailyportalz.jp/kiji/130805161341)
> [鳥の群れを一瞬で数え、虫に油性ペンで印を書く～環境調査というお仕事](https://dailyportalz.jp/kiji/kankyo-chosa-oshigoto)
> [漆黒のヘビを探して](https://dailyportalz.jp/kiji/120727156635)
> [新種のカエル、サドガエルを捕まえた](https://dailyportalz.jp/kiji/130913161762)
> [海水浴場の黒いダイヤ、オオヒョウタンゴミムシを求めて](https://dailyportalz.jp/kiji/scarites_sulcatus)
> [三葉虫に寿司を運ばせたい](https://dailyportalz.jp/kiji/sanyochu-sushi) 注：三叶虫回转寿司好好玩。

*更多媒体平台靠持续积累！*

#### Step3
- 除了博客这类长内容以外，可以再去 Twitter 这种短消息比较多的地方[检索补充一下](https://www.google.com/search?client=safari&rls=en&q=site%3Ax.com+マイマイカブリ&ie=UTF-8&oe=UTF-8)。其他类似平台以此类推。不想注册的话，可以试着用 Google 的“site:”命令搜索；爬虫爬不到的话，可以打开 App 在站内搜索。
- 检索一些专门的兴趣爱好论坛。
- Reddit 上面可以顺便搜一下看看老外虫佬对マイマイカブリ[怎么讲的](https://www.reddit.com/search/?q=blaptoides&cId=31127f4a-2081-4749-bdef-6e448e21f511&iId=456e77dd-a8cb-4a9d-a9d7-dbcc645fd2bf)。用学名检索出来内容少的话，同样采用【检索词优化（Query Refinement）】的方法，比方说试试 [Japanese ground beetle](https://www.reddit.com/search/?q=Japanese+ground+beetle&cId=14c38c41-050e-4061-ac73-bc63773fa747&iId=4d9bb83e-141f-4a1b-8e88-4586b20dd889) 之类的，仅举例。
- 以此类推，发掘更多信息源。这次检索到的比较有用的网站可以收藏整理起来。提示一下，不仅是收藏，还要整理！好的整理方式可以提升资源的利用程度。

#### Step4
- 图文为主的网站搜完之后，可以检索视频网站 Youtube 等。Step 2 的时候我们已经可以顺藤摸瓜到一些博主的 Youtube 频道了，这边可以进入 Youtube 再[集中检索](https://www.youtube.com/results?search_query=マイマイカブリ)一下。其他视频网站也同理。
- 没有一个绝对的的检索顺序我们必须去遵循；先从自己习惯的、平时经常获取信息的渠道开始尝试就可以。
- 当我们还想要挖掘更多资源的情况下，为了避免遗漏，我们可以按照网站分类逐一排查。

---

#### 1.2 线下购买
  
线下情况比较综合，这里不限于购买环节，简单介绍一些我在出行时候的个人习惯，可能无法涵盖大多数人的需求，仅作观点的分享。  
  
- 总之还是先各类检索一下。切换搜索主题，过程参考前文。  

- 一般先去博物馆、档案馆、图书馆、书店等等地方。  
> 这些地方信息浓度比较高，存在大量间接经验（Mediated experience，或【认知论 epistemology】常用：Testimonial knowledge），有时候可以省去不少自己从零开始收集整理资料的时间。    
> 我个人由于时间、金钱、精力有限，平时大量依靠间接经验学习（【社会学习理论 Social Learning Theory】常用：Vicarious learning）。    
> 想要“行万里路”，不“读万卷书”会后劲不足。可以理解成：行路是考验算力，读书可以增强算法。  

- 关注场馆或者机构之间的合作项目。   
> 这是出于我专业研究的需求。  
> 不论我们是不是研究人员，都可以锚定一个我们自己的视角。可以是在校的时候选择的专业、可以是工作所属的领域、也可以是我们的兴趣爱好，等等，作为对世界的纵深挖掘点。  

- Google Map（或者其他常用地图软件）上搜索并标记地点，简单点击保存即可。不论实际上是否会去，都先做标记备用。  

- 全部标记完成之后，再根据标记集中程度、交通状况等等，大致安排当日行程。    
> 简单来讲：标记充足、行程自由。    
> 我可以标记很多地方，但是如果最后全都没去，也完全可以。    
> 想要去什么地方转一转的时候，不会没有地方可去。    

- 是否重点依赖地图资讯，要看当地的实际状况。有些地方的具体情况并非公开透明，要注意。一套方法一用到底的情况并不多见，各类工具和信息源搭配使用。  

- 出现状况先自己思考、自己尝试解决。依赖他人帮助的时候，要**附上自己已经尝试过的方法**作为他人帮助我们的参考。  

#### 1.3 线上购物

##### 综合性购物平台

- 楽天
- eBay
- アマゾン
- ヤフオク
- 其他

##### 专门网站
搜虫屋的线上网站
重点：配送方式、付款方式、邮费等等


### 2. 玩家交流

#### 昆虫论坛

个人博客除外

#### Line 公开群组

Line直接搜

#### 其他文化圈的玩家群

中国的外国的

---
