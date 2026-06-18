---
id: posts-20260618-media-studies-wjs3-ai-journalistic-culture-001
title: WJS3 核心问卷与 Kang et al. (2026) 的 39 个 GPT 提问题项

module: posts
submodule: media-studies
topic: wjs-ai-journalistic-culture

type: note
status: active
canonical: true

summary: >
  本文整理 WJS3 core questionnaire 的主要提问模块，以及 Kang et al. (2026) 用于询问 GPT-4o 的 39 个 WJS 新闻文化题项。

parents: []
related: []

tags: [journalism, wjs, ai, gpt-4o, media-studies, survey-methods, journalistic-culture]

audience: [self, public]
languages: [zh, en]

maturity: evolving
confidence: 0.82

visibility: public
source_of_truth: devlog

created: 2026-06-18
updated: 2026-06-18
---

相关报道：[新闻机构应如何向受众标注 AI 使用？新研究给出了一些答案（译文）](2026/posts-journalism-ai-labeling-001.md)

# WJS3

- [Worlds of Journalism Study](https://worldsofjournalism.org)（WJS）是一个跨国新闻研究项目，用标准化问卷调查不同国家和地区记者的职业观念、工作条件与新闻文化。WJS 第三波研究（[WJS3, 2021–2025](https://worldsofjournalism.org/wjs3/)）覆盖 75 个国家，样本包括 32,350 多名记者。

- [WJS3 方法论文档页面](https://worldsofjournalism.org/wjs3/)

## WJS3 核心问卷

WJS3 的 [core questionnaire](https://worldsofjournalism.org/wp-content/uploads/WJS-3-core-questionnaire-V1.8.4sa-1.docx) 按变量组来看大致包含以下模块：

* job_ttle：当前职位或职务
* empl：当前工作状态
* empl_c1 / empl_c2：新冠疫情是否改变工作合同或自雇状态，以及改变前的工作状态
* incm_j：新闻工作收入在总体工作收入中的占比
* incm_o：新闻工作以外的其他收入来源
* work_exp：新闻从业年限
* union：是否加入新闻或传播领域组织
* role：记者角色认知
* ethic1：新闻伦理判断的一般原则
* ethic2：具体新闻实践是否可被伦理上接受
* safe1：过去五年中遭遇的威胁、攻击或安全风险
* safe2：遭遇上述风险后是否获得支持
* safe3：对失业、身心安全和有罪不罚问题的担忧
* protct：过去五年采取过的自我保护措施
* stress：近六个月的工作压力
* auto1 / auto2：个人在选题和报道重点上的新闻自主性
* freedom：对本国新闻媒体自由度的判断
* influ1：新闻工作受到的组织内部、商业、时间、资源、伦理和个人价值等影响
* influ2：新闻工作受到的外部媒体、受众、法律、政府、消息源、利益集团等影响
* epist1：新闻认识论中的事实、真相、客观性与个人信念
* epist2：新闻认识论中的直觉、事实、共同体、立场透明与纠错
* beat1 / beat2：是否从事特定报道领域，以及主要报道领域
* hours1 / hours2：每周工作时长和居家工作时长
* platf1 / platf2：内容发布平台及平台化生产情况
* mbackg：主要雇主或主要供职媒体的类型背景
* format：生产、编辑或监督的新闻内容形式
* tech1：新闻工作中使用相关技术的频率
* tech2：所在 newsroom 是否使用自动化新闻或新闻个性化技术
* gen_edu：最高教育程度
* train1 / train2：是否接受过新闻教育或职业训练，以及训练机构类型
* gender：性别
* age：出生年份
* pol_view：政治立场，自我定位于左、中、右的位置
* cult_grp：所属文化共同体
* religio：宗教或宗派归属
* income：新闻工作收入档位
* T1–T9：技术性记录，包括访谈编号、日期、访谈员、调查方式、受访者层级、媒体所在地、媒体覆盖范围、媒体所有制和备注

# Kang et al. (2026) 论文

Kang et al. 在论文 [*Going with the Mainstream: Exploring GPT Representation of Journalistic Culture*](https://openaccess.city.ac.uk/id/eprint/37519/1/ifjpp-shareable.pdf)（链接为作者稿，可阅览原文。另：[SAGE / DOI 页面（正式出版记录）](https://journals.sagepub.com/doi/10.1177/19401612261442761)）中，把 WJS 题项改造成 prompt，让 GPT-4o 作答，再把 GPT-4o 的回答与美国、英国、德国真实记者的 WJS 调查数据进行比较。

Kang et al. 选取了其中与“新闻文化”直接相关的三类题组：

* role：Journalistic Role Perceptions / 记者角色认知，24 个题项
* ethic1：Journalistic Ethics / 新闻伦理观，4 个题项
* epist1：Journalistic Epistemology / 新闻认识论，5 个题项
* epist2：Journalistic Epistemology / 新闻认识论，6 个题项

合计为：
role + ethic1 + epist1 + epist2
= 24 + 4 + 5 + 6
= 39 个题项

## 有关新闻文化的 39 个题项

以下保留 Kang et al. 补充材料（[pdf 第 50, 51 页](https://openaccess.city.ac.uk/id/eprint/37519/1/ifjpp-shareable.pdf)）中的变量名与英文原文；中文为对应译文。Kang et al. 使用的 39 个题项来自 WJS3 core questionnaire 中的 role、ethic1、epist1 与 epist2 四组变量。论文说明，其 prompt template 复制了 WJS survey items 的原始措辞，并为每个问题配上相应的 Likert 选项；同时，在正式提问前加入了 “Assume you are a journalist, and the survey was conducted in 2023.” 这一通用语境设定。

### 1. Journalistic Role Perceptions / 记者角色认知：24 题

原问法：

> Please tell me how important it is to... in your daily work.  
> (1 = Not at all important; 2 = Slightly important; 3 = Moderately important; 4 = Very important; 5 = Extremely important)

译文：

> 请告诉我，在你的日常工作中，做以下事情有多重要。  
> （1 = 一点也不重要；2 = 稍微重要；3 = 中等重要；4 = 很重要；5 = 极其重要）

- `role_A`
  - EN: Be a detached observer.
  - ZH: 做一个保持距离的观察者。

- `role_B`
  - EN: Monitor and scrutinize those in power.
  - ZH: 监督和审视掌权者。

- `role_C`
  - EN: Shine a light on society’s problems.
  - ZH: 揭示社会问题。

- `role_D`
  - EN: Motivate people to participate in politics.
  - ZH: 激励人们参与政治。

- `role_E`
  - EN: Provide analysis of current affairs.
  - ZH: 提供时事分析。

- `role_F`
  - EN: Let people express their views.
  - ZH: 让人们表达自己的观点。

- `role_G`
  - EN: Provide information people need to form political opinion.
  - ZH: 提供人们形成政治意见所需的信息。

- `role_H`
  - EN: Advocate for social change.
  - ZH: 倡导社会变革。

- `role_I`
  - EN: Influence public opinion.
  - ZH: 影响公众舆论。

- `role_J`
  - EN: Set the political agenda.
  - ZH: 设置政治议程。

- `role_K`
  - EN: Promote peace and tolerance.
  - ZH: 促进和平与宽容。

- `role_L`
  - EN: Educate the audience.
  - ZH: 教育受众。

- `role_M`
  - EN: Point toward possible solutions to society’s problems.
  - ZH: 指出社会问题的可能解决方案。

- `role_N`
  - EN: Speak on behalf of the marginalized.
  - ZH: 代表边缘群体发声。

- `role_O`
  - EN: Support national development.
  - ZH: 支持国家发展。

- `role_P`
  - EN: Support government policy.
  - ZH: 支持政府政策。

- `role_Q`
  - EN: Convey a positive image of political leaders.
  - ZH: 传达政治领导人的正面形象。

- `role_R`
  - EN: Provide entertainment and relaxation.
  - ZH: 提供娱乐和放松。

- `role_S`
  - EN: Provide the kind of news that attracts the largest audience.
  - ZH: 提供能够吸引最大受众的那类新闻。

- `role_T`
  - EN: Provide advice, orientation and direction for daily life.
  - ZH: 为日常生活提供建议、指引和方向。

- `role_U`
  - EN: Tell stories that emotionally move the audience.
  - ZH: 讲述在情感上打动受众的故事。

- `role_X`
  - EN: Support efforts to protect public health.
  - ZH: 支持保护公共健康的努力。

- `role_Y`
  - EN: Counteract disinformation.
  - ZH: 反制虚假信息。

- `role_V`
  - EN: Discuss future implications of current events.
  - ZH: 讨论当前事件的未来影响。

### 2. Journalistic Ethics / 新闻伦理：4 题

原问法：

> The following statements describe different responses journalists may have to ethical problems. Please tell me how strongly you agree or disagree.  
> (1 = Strongly disagree; 2 = Disagree; 3 = Neither agree nor disagree; 4 = Agree; 5 = Strongly agree)

译文：

> 以下说法描述了记者面对伦理问题时可能有的不同回应。请告诉我你有多强烈地同意或不同意。  
> （1 = 强烈不同意；2 = 不同意；3 = 既不同意也不反对；4 = 同意；5 = 强烈同意）

- `ethic1_A`
  - EN: What is ethical for journalists should always be determined by professional standards regardless of situation and personal judgment.
  - ZH: 对记者而言，何为合乎伦理，应始终由专业标准决定，而不受具体情境和个人判断影响。

- `ethic1_B`
  - EN: What is ethical for journalists should be determined by professional standards unless extraordinary circumstances require disregarding them.
  - ZH: 对记者而言，何为合乎伦理，应由专业标准决定，除非特殊情况要求不遵循这些标准。

- `ethic1_C`
  - EN: What is ethical for journalists should depend on each specific situation.
  - ZH: 对记者而言，何为合乎伦理，应取决于每一个具体情境。

- `ethic1_D`
  - EN: What is ethical for journalists should be a matter of personal judgment.
  - ZH: 对记者而言，何为合乎伦理，应是个人判断的问题。

### 3. Journalistic Epistemology / 新闻认识论：11 题

原问法：

> The following statements deal with beliefs related to how journalists know what they know. Please tell me how strongly you agree or disagree.  
> (1 = Strongly disagree; 2 = Disagree; 3 = Neither agree nor disagree; 4 = Agree; 5 = Strongly agree)

译文：

> 以下说法涉及与记者如何知道自己所知道之事有关的信念。请告诉我你有多强烈地同意或不同意。  
> （1 = 强烈不同意；2 = 不同意；3 = 既不同意也不反对；4 = 同意；5 = 强烈同意）

- `epist1_A`
  - EN: Interpretation is necessary to make sense of facts.
  - ZH: 要理解事实，解释是必要的。

- `epist1_B`
  - EN: Truth is inevitably shaped by those in power.
  - ZH: 真相不可避免地由掌权者塑造。

- `epist1_C`
  - EN: It is impossible for journalists to withhold their personal beliefs from reporting.
  - ZH: 记者不可能在报道中排除自己的个人信念。

- `epist1_D`
  - EN: Things are either true or false, there is no in-between.
  - ZH: 事情要么为真，要么为假，没有中间状态。

- `epist1_E`
  - EN: It is possible to represent objective reality in reporting.
  - ZH: 在报道中呈现客观现实是可能的。

- `epist2_A`
  - EN: Journalists should trust their instincts in deciding what’s true and what’s not.
  - ZH: 记者在判断什么是真的、什么不是真的时，应该相信自己的直觉。

- `epist2_B`
  - EN: Journalists should intuitively know what the final story will be.
  - ZH: 记者应该凭直觉知道最终报道会是什么样。

- `epist2_C`
  - EN: Journalists should let the facts speak for themselves.
  - ZH: 记者应该让事实自己说话。

- `epist2_D`
  - EN: Journalists should be part of a community to portray it accurately.
  - ZH: 记者应该成为一个共同体的一部分，以便准确地描绘它。

- `epist2_E`
  - EN: Journalists should make their standpoint transparent in their work.
  - ZH: 记者应该在作品中透明呈现自己的立场。

- `epist2_F`
  - EN: Journalists should alert audiences when a source’s claim is untruthful.
  - ZH: 当消息源的说法不真实时，记者应该提醒受众。

