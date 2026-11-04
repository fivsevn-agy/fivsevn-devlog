---
id: "blogops-docs-auto-translation-shortcut-001"
title: "自动翻译快捷流程说明"

module: "blogops"
submodule: "docs"
topic: "auto-translation-shortcut"

type: "note"
status: "active"
canonical: true

summary: |
  说明 自动翻译快捷流程说明 的使用场景、操作流程与维护规则。

parents: []
related: ["spec-content-translation-001", "spec-content-frontmatter-001"]

tags: ["blogops", "docs", "translation", "shortcuts", "automation"]

audience: ["self", "internal"]
languages: ["zh"]

maturity: "stable"
confidence: 0.9

visibility: "public"
source_of_truth: "devlog"

note: "保留现有文件名：展示目录或已发布链接使用该路径，本次不修改展示页；metadata id 继续作为内容身份。"
filename_policy: "stable-link"

created: "2026-06-15"
updated: '2026-11-04'
metadata_updated: '2026-11-01'
---

# Auto Translation Shortcut Workflow
# 自动翻译快捷流程说明

本文记录 fivsevn-devlog 的翻译与发布流程。实际执行规则以用户自行保存的 `translate and post.md` 为准。

本文件属于 `blogops/docs` 操作说明，不属于 fivsevn-spec。  
它说明的是实际操作流程、工具组合和提示词使用方式。

相关规范：

```text
https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/spec-content-translation-001.md
```

---

## 1. 目的

本流程用于把外部网页、PDF、截图或其他材料整理成可发布的 Markdown 中文翻译稿。

默认由具备相应能力的 AI 完成翻译、校验、入库、提交与线上核验；用户指定仅生成文件或发布受阻时，交付完整 Markdown 文件并说明实际停点。

流程重点不是绑定某一个工具，而是把以下模块组合起来：

```text
材料输入
→ 正文抓取
→ 提示词组装
→ AI 翻译整理
→ 生成 Markdown 文件
→ 校验、自动提交与发布
→ 核对 Actions 和实际页面
```

当前使用的 iOS Shortcuts 只是其中一种实现方式。  
后续也可以替换为其他自动化工具、网页服务、脚本或人工复制流程。

---

## 2. 工作流边界

本文件说明：

- 如何获取待翻译材料；
- 如何把网页或文件内容转换成可处理文本；
- 如何组装发送给 AI 的提示词；
- 如何连接 AI 处理与文章入库；
- 如何保存和检查生成结果。

metadata 字段语义与类型遵循共用 frontmatter 规范和 schema。页面开头统一使用“◇ 概括性中文标题 → SOURCE → NOTE”，目录由现有脚本生成。具体执行方式以用户保存的提示词为准。

---

## 3. 总体流程

推荐流程如下：

```text
1. 获取原始材料
2. 抓取或整理正文文本
3. 将原文 URL 和正文文本填入提示词
4. 把提示词发送给 AI
5. AI 生成可发布 Markdown 文件
6. AI 检查 frontmatter、正文、来源、链接和实际发布条件
7. 按现行仓库规则保存、提交、推送，并核验部署与实际页面
8. 未完成发布时交付完整译稿和准确停点
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
→ AI 按用户保存的提示词完成处理与自动发布，受阻时交付文件
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

<a id="7-提示词"></a>

## 7. 实际发布提示词

快捷指令使用的 `translate and post.md` 由用户自行保管，不收录在本仓库或网站中。快捷指令的 Text 动作使用用户保存的版本，并接入下一节所列变量。

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

AI 在保存与发布前检查以下内容；用户也可据此复核：

- 生成的下载文件是否使用 frontmatter 中的 `id`；Posts 正式发布时保存为对应发布包的 `index.md`；
- frontmatter 是否完整；
- 字段组之间是否保留空行；
- `type` 是否为 `translation`；
- `status`、`visibility` 是否符合公开发布状态；
- `original_url` 是否为原文链接；
- 页面主标题与 metadata、目录是否同为 `◇ 概括性中文标题`，且无重复主标题；
- 页面是否包含普通文本标签 `SOURCE` 和 `NOTE`；
- 来源和资源链接是否有效；
- 提交中是否混入提示词、私人材料或临时文件。

---

## 11. 保存位置

符合实际提示词发布条件的译稿保存到 fivsevn-devlog 对应模块目录；待审核稿按提示词保存在本地或已确认权限的私人位置。

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

Posts 正式发布保存为 `posts/YYYY/MM/文章编号/index.md`；配图和附件放在同一发布包的 `assets/`。生成的下载文件可先使用 `id.md`，整理进发布包时改为 `index.md`，保留原 `id`。

natsci、netcom 仍按各自主题目录保存。具体目录结构以当前内容仓库实际结构为准。

---

## 12. 维护说明

本文件记录的是实际操作流程，可以随工具变化调整。

如果后续更换抓取工具、AI 工具或 Shortcuts 结构，只需要更新本文对应模块，不需要修改 fivsevn-spec 中的翻译规范。

本文只维护快捷指令接线方式和仓库操作说明。`translate and post.md` 由用户自行更新和存档，不在仓库内同步提示词正文。
