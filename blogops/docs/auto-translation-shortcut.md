---
id: blogops-docs-auto-translation-shortcut-001
title: 自动翻译快捷流程说明

module: blogops
submodule: docs
topic: auto-translation-shortcut

type: note
status: active
canonical: true

summary: >
  说明 自动翻译快捷流程说明 的使用场景、操作流程与维护规则。

parents: []
related: [spec-content-translation-001, spec-content-frontmatter-001]

tags: [blogops, docs, translation, shortcuts, automation]

audience: [self, internal]
languages: [zh]

maturity: stable
confidence: 0.9

visibility: public
source_of_truth: devlog

created: 2026-06-15
updated: 2026-06-15
---

# Auto Translation Shortcut Workflow
# 自动翻译快捷流程说明

本文记录 fivsevn-devlog 中用于生成翻译稿的自动化工作流。

本文件属于 `blogops/docs` 操作说明，不属于 fivsevn-spec。  
它说明的是实际操作流程、工具组合和提示词使用方式。

翻译内容本身的规范，以 fivsevn-spec 中的翻译规范为准：

```text
https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/spec-content-translation-001.md
```

---

## 1. 目的

本流程用于把外部网页、PDF、截图或其他材料整理成可发布的 Markdown 中文翻译稿。

最终目标是生成一份可以直接保存到 fivsevn-devlog / site 内容仓库的 `.md` 文件。

流程重点不是绑定某一个工具，而是把以下模块组合起来：

```text
材料输入
→ 正文抓取
→ 提示词组装
→ AI 翻译整理
→ 生成 Markdown 文件
→ 人工检查与发布
```

当前使用的 iOS Shortcuts 只是其中一种实现方式。  
后续也可以替换为其他自动化工具、网页服务、脚本或人工复制流程。

---

## 2. 工作流边界

本文件说明：

- 如何获取待翻译材料；
- 如何把网页或文件内容转换成可处理文本；
- 如何组装发送给 AI 的提示词；
- 如何让 AI 按 fivsevn-spec 输出可发布 Markdown；
- 如何保存和检查生成结果。

本文件不重新定义：

- 翻译内容的 frontmatter 字段；
- 翻译正文的通用要求；
- 图片远程资源处理规则；
- 版权与公开发布说明；
- `status`、`visibility`、`source_of_truth` 等字段语义。

这些规则以 fivsevn-spec 为准。

---

## 3. 总体流程

推荐流程如下：

```text
1. 获取原始材料
2. 抓取或整理正文文本
3. 将原文 URL 和正文文本填入提示词
4. 把提示词发送给 AI
5. AI 生成可发布 Markdown 文件
6. 人工检查 frontmatter、正文、链接和版权说明
7. 保存到对应内容目录
```

当前快捷指令流程为：

```text
Share Sheet 输入 URL
→ 生成 r.jina.ai 读取地址
→ Get Contents of URL 获取网页 Markdown
→ 拼接固定提示词
→ 生成日期命名的 .md prompt 文件
→ 打开分享菜单
→ 手动发送给 ChatGPT 或其他 AI
→ AI 输出最终翻译稿文件
```

---

## 4. 材料输入方式

输入材料可以来自多种来源。

常见输入包括：

- 普通网页 URL；
- 新闻、博客、技术文章 URL；
- GitHub 文档页面；
- PDF 文件；
- 网页截图；
- 应用内分享出的文本；
- 手动复制的网页正文；
- 其他 AI 或工具已经整理出的 Markdown。

优先使用 URL 输入。  
如果 URL 抓取失败，再使用 PDF、截图、复制文本或人工整理结果。

---

## 5. 正文抓取方式

正文抓取的目标不是保留网页完整外壳，而是获得可翻译的正文内容。

可使用以下方式。

### 5.1 自动网页抓取

当前快捷指令使用：

```text
https://r.jina.ai/<原文 URL>
```

例如：

```text
https://r.jina.ai/https://example.com/article
```

作用：

- 将网页转换成适合 AI 处理的 Markdown 或纯文本；
- 尽量保留标题、正文、链接、图片 Markdown、列表和段落；
- 减少网页菜单、脚本和样式干扰。

在 iOS Shortcuts 中，对应结构为：

```text
Receive URLs from Share Sheet

Text
https://r.jina.ai/[Shortcut Input]

Get Contents of URL
输入：上一步 Text
```

其中：

```text
Shortcut Input
= 原始网页 URL

Contents of URL
= 抓取到的网页 Markdown 内容
```

### 5.2 手动复制正文

如果自动抓取失败，可以直接从网页中复制正文。

适用场景：

- 网页禁止抓取；
- r.jina.ai 返回内容不完整；
- 页面需要登录；
- 网页正文结构复杂；
- 自动抓取混入过多导航和广告。

手动复制时，应尽量保留：

- 标题；
- 小标题；
- 段落顺序；
- 列表；
- 表格；
- 引用；
- 链接；
- 图片位置和图片 URL；
- 作者、发布时间、来源信息。

### 5.3 PDF 输入

如果原文是 PDF，或网页无法稳定抓取，可使用 PDF 作为输入材料。

处理方式：

- 直接把 PDF 交给 AI；
- 或先提取 PDF 文本；
- 或把关键页面截图后交给 AI；
- 或人工复制 PDF 中的正文。

PDF 场景下，应额外注意：

- 保留原文标题和发布方；
- 如果 PDF 有 DOI、报告编号、出版社或机构信息，应保留；
- 如果 PDF 分栏、脚注、图注较复杂，生成结果后需要人工检查段落顺序；
- 图表内容不应随意改写或扩写。

### 5.4 截图输入

如果网页、PDF 或应用内容无法复制，可以使用截图。

适用场景：

- App 内文章；
- 图片型网页；
- 扫描版 PDF；
- 页面禁止复制；
- 只需要翻译局部内容。

截图处理要求：

- 尽量截完整段落；
- 多张截图应按阅读顺序排列；
- 如果截图中含有图片、表格或图注，应提醒 AI 保留其位置和含义；
- OCR 结果需要人工检查，避免识别错误导致译文失真。

### 5.5 人工整理输入

在抓取结果不可靠时，可以先人工整理一版输入文本。

最低要求是保留：

```text
原文标题
原文 URL 或来源说明
正文内容
重要链接
图片位置或图片 URL
作者 / 发布方 / 发布时间
```

只要能提供完整可读的原文正文，就可以进入后续 AI 翻译步骤。

---

## 6. 当前快捷指令模块

当前 iOS Shortcuts 的核心模块如下。

### 6.1 接收 URL

```text
Receive URLs from Share Sheet
```

作用：

- 从 Safari、浏览器、阅读器或其他 App 分享网页 URL；
- 如果没有输入，可以退回到剪贴板。

### 6.2 生成抓取 URL

```text
Text
https://r.jina.ai/[Shortcut Input]
```

作用：

- 将原始 URL 转换为 r.jina.ai 读取地址。

### 6.3 获取网页 Markdown

```text
Get Contents of URL
输入：上一步 Text
```

作用：

- 获取转换后的网页 Markdown；
- 输出结果作为后续提示词中的“网页 Markdown 内容”。

### 6.4 组装提示词

```text
Text
固定提示词 + Shortcut Input + Contents of URL
```

作用：

- 把规则、原文 URL 和网页 Markdown 拼成一个完整 prompt；
- 该 prompt 后续会发送给 AI。

### 6.5 生成 prompt 文件

```text
Set Name of Text to Current Date.md
```

建议日期格式：

```text
yyyy-MM-dd
```

作用：

- 将完整 prompt 保存成一个日期命名的 Markdown 文件；
- 文件名只是 prompt 文件名，不是最终译文文件名。

### 6.6 打开分享菜单

```text
Open Renamed Item
Show Open In Menu: On
```

作用：

- 打开 iOS 分享菜单；
- 手动选择 ChatGPT 或其他 AI；
- 由 AI 生成最终翻译稿文件。

---

## 7. 提示词

以下提示词用于发送给 AI。  
使用时，把最后的两个占位符替换成实际变量。

```text
你是 fivsevn 内容系统的翻译整理助手。请根据以下输入，生成一份可以直接保存到 fivsevn devlog / site 内容仓库的 Markdown 中文翻译稿。

你的目标是生成一份完整、可发布的 `.md` 文件。不要输出解释过程，不要输出规则说明，不要输出“我将如何处理”。

## 任务

将下方网页 Markdown 内容完整翻译成中文，并按照 fivsevn-spec 自动填写 frontmatter。

最终生成的 Markdown 应当可以直接保存、提交和发布。

## 必须遵守的规范来源

请按照以下规范理解并填写元数据：

- fivsevn-spec 总入口：
  https://github.com/fivsevn-agy/fivsevn-spec

- Content Frontmatter 说明：
  https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/spec-content-frontmatter-001.md

- Content Frontmatter 枚举表：
  https://github.com/fivsevn-agy/fivsevn-spec/blob/main/appendix/spec-content-frontmatter-enums-001.md

- Content Frontmatter 枚举速查：
  https://github.com/fivsevn-agy/fivsevn-spec/blob/main/appendix/spec-content-frontmatter-enums-quickref-001.md

- Content Translation Specification：
  https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/spec-content-translation-001.md

## 最终输出方式

优先生成一个可下载的 Markdown 文件附件。

文件名必须使用 frontmatter 中的 `id`，格式为：

id.md

例如：

netcom-bluetooth-naming-001.md

如果当前环境无法生成文件附件，才退化为直接输出完整 Markdown 文件内容。

不要输出：

- 解释过程
- 规则说明
- “我将如何处理”
- Markdown 代码块围栏
- 英文原文全文
- 文件内容之外的附加说明

## 最终文件结构

最终 Markdown 文件必须使用以下结构：

---
填写好的 YAML frontmatter
---

## 文章翻译

### source

- [原文链接](原文链接)

### note

本文为原文内容的中文翻译，仅用于学习与知识整理。原文版权归原作者及出版方所有。若权利人认为本文不宜公开保留，请联系后删除或调整。

---

## 正文

完整中文翻译正文

## frontmatter 字段结构

必须输出 YAML frontmatter，字段如下，并且必须保留字段组之间的空行：

---
id:
title:

module:
submodule:
topic:

type:
status:
canonical:

summary: >

parents: []
related: []

tags: []

audience: []
languages: []

maturity:
confidence:

visibility:
source_of_truth:

original_title:
original_source:
original_publisher:
original_url:
translation_note: >

created:
updated:
---

## frontmatter 填写规则

请不要照抄占位符。必须根据文章内容自动填写。

1. `id` 必须是稳定主键，不随文件名变化。

   格式尽量为：

   module-submodule-topic-001

   例如：

   netcom-bluetooth-naming-001

2. `title` 使用中文标题，清楚表达文章主题。

3. `module / submodule / topic` 必须根据文章内容填写。

   如果文章属于通信、网络、无线技术、蓝牙、射频、协议、计算机科学、AI、数学、硬件、嵌入式等，优先考虑：

   module: netcom

   如果文章属于自然科学、生物、分类学、古生物、生态、动物、植物、演化等，优先考虑：

   module: natsci

   如果无法确定，请选择最合理的分类，不要留空。

4. `type` 对翻译文章必须填写：

   translation

5. `status` 默认填写：

   active

6. `canonical` 默认填写：

   true

7. `summary` 写 1–2 句中文摘要，说明本文解决什么问题、讲了什么。

   必须使用 YAML block scalar：

   summary: >
     这里写中文摘要。

8. `parents` 如果无法确定，填写空数组：

   parents: []

9. `related` 如果无法确定，填写空数组：

   related: []

10. `tags` 填 3–8 个英文小写标签。

    使用短横线，不使用中文标签，不使用空格。

11. `audience` 默认填写：

    [self, public]

12. `languages` 填写：

    [zh]

13. `maturity` 默认填写：

    stable

    如果内容明显只是暂存或未检查，才填写：

    draft

14. `confidence` 使用 0–1 小数，推荐保留一位小数。

    对完整抓取并忠实翻译的文章，默认填写：

    0.9

15. `visibility` 默认填写：

    public

16. `source_of_truth` 对翻译稿必须填写：

    translation

17. `original_title` 使用原文标题。

18. `original_source` 使用原文来源名称，例如栏目名、站点名、项目名。

    不要把 URL 填到这里。

19. `original_publisher` 写原作者、网站名、机构名或发布方。

    如果无法判断，写原网站名。

20. `original_url` 填写原文 URL。

21. `translation_note` 必须使用以下文字：

    本文为原文内容的中文翻译，仅用于学习与知识整理。
    原文版权归原作者及出版方所有。若权利人认为本文不宜公开保留，请联系后删除或调整。

22. `created` 和 `updated` 使用今天日期，格式为：

    YYYY-MM-DD

## frontmatter 排版要求

最终 YAML frontmatter 必须保留分组空行，方便人工编辑和检查。

排版结构必须类似：

---
id: module-submodule-topic-001
title: 中文标题

module: module-name
submodule: submodule-name
topic: specific-topic

type: translation
status: active
canonical: true

summary: >
  一到两句中文摘要。

parents: []
related: []

tags: []

audience: [self, public]
languages: [zh]

maturity: stable
confidence: 0.9

visibility: public
source_of_truth: translation

original_title:
original_source:
original_publisher:
original_url:
translation_note: >
  本文为原文内容的中文翻译，仅用于学习与知识整理。
  原文版权归原作者及出版方所有。若权利人认为本文不宜公开保留，请联系后删除或调整。

created: YYYY-MM-DD
updated: YYYY-MM-DD
---

要求：

- 字段分组之间必须保留空行。
- YAML 中不要保留任何 `# 注释`。
- 不要保留“标题”“原文链接”“module-name”“specific-topic”等占位符。
- `summary: >` 和 `translation_note: >` 的正文必须换行并缩进两个空格。
- frontmatter 结束后空一行，再进入正文。

## 正文结构要求

frontmatter 之后必须使用以下结构：

## 文章翻译

### source

- [原文链接](原文链接)

### note

本文为原文内容的中文翻译，仅用于学习与知识整理。原文版权归原作者及出版方所有。若权利人认为本文不宜公开保留，请联系后删除或调整。

---

## 正文

完整中文翻译正文

## 翻译要求

必须严格遵守以下翻译规则：

1. 忠实传达原意，不删减、不扩写。
2. 不用总结替代翻译。
3. 不改写为评论、解读或二次创作。
4. 保留原文段落顺序，尽量逐段翻译，方便对照。
5. 保留 Markdown 标题、列表、表格、引用块、代码块和链接结构。
6. 链接目标 URL 不得修改。
7. 原文中的图片链接、YouTube 链接、普通链接、代码块、表格、引用块和特殊符号必须保留。
8. 专有名词、技术术语、人名、机构名、产品名应准确处理。
9. 常见技术术语使用自然中文译法；必要时保留英文原词。
10. 语言应自然流畅，符合中文阅读习惯，保持良好的中文水平。
11. 不改变事实、时间、数量、因果关系或语气。
12. 原文中的幽默、口语、引号和括号说明，应尽量保留表达效果。
13. 原文中的明显拼写、语法或标点问题，翻译时可自然化处理，但不得改变含义。
14. 不遗漏标题、图片说明、列表、引用、括号内容或脚注式信息。
15. 如果原文中有无法确定的含义，采用保守译法，不自行发挥。
16. 不要把英文原文整段附在译文后面，除非它是链接、代码、专有名词或必须保留的格式内容。

## 网页内容清理要求

只保留文章主体和与正文直接相关的扩展阅读内容。

应删除以下非正文网页元素：

- 网页导航
- Cookie 提示
- 菜单
- 搜索框
- 作者页脚
- 分类列表
- 归档列表
- 评论区
- 分享按钮
- 广告
- 站点说明
- 与正文无关的推荐内容

可酌情保留：

- 与正文直接相关的参考链接
- 原文中的相关阅读
- 文章内部的脚注、注释和来源说明
- 对理解正文有必要的附录材料

## 图片与远程资源要求

必须严格遵守以下图片规则：

1. 保留原文中的图片 Markdown。
2. 不下载、不转存、不替换图片 URL。
3. 不把图片保存到 fivsevn-assets、GitHub、jsDelivr、本地路径或任何其他仓库 / CDN。
4. 图片 alt 文本保持原样，不翻译、不改写。
5. 每一个图片 Markdown 块下方，都必须增加固定提示：

   > 图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

6. 对普通图片结构：

   ![...](...)

   输出时必须变成：

   ![...](...)

   > 图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

7. 对图片缩略图包裹链接的结构：

   [![...](...)](...)

   输出时必须变成：

   [![...](...)](...)

   > 图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

8. 原文自带的图片说明文字仍然需要保留并翻译。

9. 如果图片后面原本紧跟图片说明，则最终顺序必须是：

   图片 Markdown

   > 图片为原文远程资源引用；若无法显示，或需查看原图与上下文，请访问原文。

   翻译后的原文图片说明文字

10. 不要在没有图片 Markdown 的地方添加图片提示。
11. 不要把所有图片提示集中放到文章末尾，必须逐张图片就地添加。

## 版权与公开发布说明要求

每篇译文必须在正文 `source` 之后加入：

### note

本文为原文内容的中文翻译，仅用于学习与知识整理。原文版权归原作者及出版方所有。若权利人认为本文不宜公开保留，请联系后删除或调整。

公开发布时必须遵守：

- 必须保留原文链接。
- 必须记录原文标题、来源和发布方。
- 不删除原文自带的作者、来源、版权或许可说明。
- 不声称译文为原创文章。
- 不将译文包装为商业发布内容。
- 如果原文明确禁止转载、复制或翻译，应优先不公开发布。
- 如果原文来自付费墙、会员区、未公开材料或受限访问内容，不应公开发布完整译文。

如果原文明确禁止转载、复制或翻译，或者明显来自付费墙、会员区、未公开材料，请不要生成公开发布稿；改为在 frontmatter 中使用：

status: hidden
audience: [self]
maturity: draft
confidence: 0.0
visibility: private

并在正文 note 中说明该译文仅作私人学习暂存。

## 输入信息

原文 URL：

[Shortcut Input]

网页 Markdown 内容：

[Contents of URL]
```

---

## 8. 提示词变量

在 iOS Shortcuts 中，提示词末尾使用两个变量。

```text
原文 URL：

[Shortcut Input]

网页 Markdown 内容：

[Contents of URL]
```

变量含义：

| 变量 | 含义 |
|---|---|
| `Shortcut Input` | 从分享菜单传入的原始 URL |
| `Contents of URL` | 通过 r.jina.ai 或其他抓取方式得到的正文 Markdown |

如果输入材料不是 URL，而是 PDF、截图或人工整理文本，可以把：

```text
网页 Markdown 内容：
```

改成：

```text
材料正文内容：
```

并放入对应的 OCR、复制文本或人工整理结果。

---

## 9. AI 处理模块

提示词可以发送给不同 AI 工具。

可选方式包括：

- ChatGPT；
- 其他能够读取长文本或 Markdown 文件的 AI；
- 支持上传 PDF、截图或文本文件的 AI；
- 本地模型或脚本化处理工具。

当前做法是：

```text
Open Renamed Item
Show Open In Menu: On
```

然后在分享菜单中手动选择 AI。

这样做的好处是：

- 不绑定某一个 AI；
- 可以根据材料复杂度选择工具；
- 可以让 AI 直接生成下载文件；
- 如果某个 AI 对长文本处理不好，可以换另一个。

---

## 10. 生成结果检查

AI 生成最终译文后，应人工检查以下内容：

- 文件名是否使用 frontmatter 中的 `id`；
- frontmatter 是否完整；
- 字段组之间是否保留空行；
- `type` 是否为 `translation`；
- `status`、`visibility` 是否符合公开发布状态；
- `original_url` 是否为原文链接；
- 正文是否包含 `source` 和 `note`；
- 图片后是否逐张添加远程资源提示；
- 原文链接、图片链接和 YouTube 链接是否保留；
- 是否误删了正文段落、表格、图注或引用；
- 是否混入网页导航、评论区、广告等非正文内容；
- 是否错误声明原创或删除原文版权信息。

---

## 11. 保存位置

最终生成的翻译稿应保存到 fivsevn-devlog / site 内容仓库中对应模块目录。

模块由 frontmatter 中的：

```yaml
module:
submodule:
topic:
```

决定。

常见情况：

```text
netcom/
natsci/
posts/
```

具体目录结构以当前内容仓库实际结构为准。

---

## 12. 维护说明

本文件记录的是实际操作流程，可以随工具变化调整。

如果后续更换抓取工具、AI 工具或 Shortcuts 结构，只需要更新本文对应模块，不需要修改 fivsevn-spec 中的翻译规范。

fivsevn-spec 只维护翻译内容本身的通用规则。  
本文件维护具体自动化流程和工具组合。
