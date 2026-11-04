---
id: "intake-readme"
title: "Intake"

module: "intake"
submodule: "guide"
topic: "guide"

type: "note"
status: "active"
canonical: true

summary: "说明Intake。"

parents: []
related: []

tags: []

audience: ["self", "internal"]
languages: ["zh"]

maturity: "evolving"
confidence: null

visibility: "public"
source_of_truth: "devlog"

note: "未记录原始写作日期；created 为本路径首次 Git 记录日期，无法合理确定时留空。"
filename_policy: "entrypoint"

created: "2026-06-03"
updated: '2026-11-01'
metadata_updated: '2026-11-01'
---

# Intake

`intake/` 生成[每日阅读页](https://devlog.fivsevn.com/intake/)。

页面是一份信息来源库，包含三部分：

- 每日明信片
- Daily Field Sample／今日野采样本
- **On the shelf／本日上架**：来源目录与 RSS 阅读区

## 结构

```text
intake/sources.md
    -> canonical hand-maintained source registry
    -> controls On the shelf / 本日上架

intake/build.py
    -> parses sources.md
    -> reads config.yml and compiles sources in memory
    -> fetches RSS items
    -> assembles index.html and llm-context.md

intake/scripts/daily_postcard.py
    -> generates the daily postcard fragment

intake/scripts/daily_field_sample.py
    -> generates the Daily Field Sample fragment

intake/config.yml
    -> base site, widget, display-limit and disabled-source configuration

intake/index.html
    -> generated public page

intake/llm-context.md
    -> generated reading context for AI; not hand-maintained
```

## 文件

```text
intake/
├── README.md
├── sources.md
├── config.yml
├── requirements.txt
├── build.py
├── index.html
├── llm-context.md
├── scripts/
│   ├── daily_postcard.py
│   └── daily_field_sample.py
└── data/                         generated during a build, not committed by Actions
    ├── daily_postcard.html
    ├── daily_postcard.json
    ├── daily_field_sample.html
    └── daily_field_sample.json
```

`build.py` 直接写入 [llm-context.md](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/intake/llm-context.md)。`config.yml` 保存基础设置，`sources.md` 提供所选来源与栏目。

## 来源清单

修改 [intake/sources.md](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/intake/sources.md)，即可调整 **On the shelf／本日上架** 的来源、RSS 地址和各来源抓取数量。

每个来源使用下面这种围栏 `source` 块，而不是普通 `yaml` 块；保留 `sources.md` 中已有的分类、展示和栏目定义。

```source
name: Example Source
section: science_news
feed_url: https://example.com/feed.xml
source_cap: 6
site_url: https://example.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

没有可用 feed 时，仍保留网站入口，在原来源块中修改这些字段：

```yaml
feed_url: ''
source_cap: 0
site_url: https://example.com/
```

## 规范引用

字段含义和枚举值在 `fivsevn-spec` 中定义：

- [来源字段](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/source/spec-source-intake-fields-001.md)
- [来源枚举](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/appendix/spec-source-intake-enums-001.md)

`intake/sources.md` 是当前所选来源清单；稳定字段规则和枚举参考由 `fivsevn-spec` 维护。

## 生成文件

以下文件由脚本生成：

```text
intake/index.html
intake/llm-context.md
intake/data/daily_postcard.html
intake/data/daily_postcard.json
intake/data/daily_field_sample.html
intake/data/daily_field_sample.json
```

构建时可能覆盖这些文件，因此修改来源应编辑源文件。当前工作流提交 `index.html` 和 `llm-context.md`；`data/` 保存 Git 忽略的构建片段。基础设置编辑 `config.yml`，来源清单编辑 `sources.md`。

## 手动构建

在仓库根目录运行：

```bash
pip install -r intake/requirements.txt
python intake/scripts/daily_postcard.py
python intake/scripts/daily_field_sample.py
python intake/build.py
```

`build.py` 直接更新 `index.html` 与 `llm-context.md`，与 Actions 的输出一致。

## GitHub Actions

页面由 [Build Intake Page](https://github.com/fivsevn-agy/fivsevn-devlog/actions/workflows/build-news.yml) 生成，配置在 [.github/workflows/build-news.yml](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/.github/workflows/build-news.yml)。

- **定时**：`0 */5 * * *`，计划每天在 UTC 00:00、05:00、10:00、15:00、20:00 运行，实际启动可能延迟。
- **修改来源后**：向 `main` 推送 `sources.md`、`config.yml`、Intake Python 工具、依赖或本工作流的改动，会触发生成；定时和手动运行也保留。只有生成文件变化的提交不会再触发一次 Intake 构建。
- **构建顺序**：离线完整性测试 → 每日明信片 → 今日野采样本 → `build.py` → 提交生成文件。生成中分支发生变化时，任务会停止，避免发布旧结果；在新版本上重跑。
- **存储**：`data/` 是 Git 忽略的临时构建输出，来源列表在内存中编译。
- **核验**：检查构建结果、Pages 部署和实际页面；生成文件已经提交，并不等于网站已经更新。

## 修改位置

```text
Change On the shelf sources, RSS URLs, or per-source fetch counts
-> edit intake/sources.md

Change site/widget titles, display limits, or disabled-feed settings
-> edit intake/config.yml

Change page structure, HTML assembly, header/footer, or rendering logic
-> edit intake/build.py

Change the postcard module
-> edit intake/scripts/daily_postcard.py

Change the Daily Field Sample module
-> edit intake/scripts/daily_field_sample.py
```

`intake/` 是面向当前阅读的生成页，不作为永久存档或独立内容主轴。整理成正式文章的阅读笔记放入 posts、natsci 或 netcom。

核对日期：2026-11-01。计划运行时间未变。

## 来源质量与完整性

有价值的网站即使无法或不宜抓取文章，也保留入口。`manual` 记录代表自有设备文档，继续保留。现有两级目录、网站与文章混排的阅读区、各来源上限、字体、CSS 和导航保持原样。

R 表示特定范围内的事实可靠性，P 表示该栏目中的专业用途；两者都不按来源类型机械赋值。[共享字段规范](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/source/spec-source-intake-fields-001.md)定义证据、范围、限制和可选 `review` 记录。没有复核记录的旧分数仍是历史判断，不代表新近核实。现有 R/P 元数据行通过悬浮提示显示复核信息，LLM 上下文也携带相同依据。

- `item_quality.py`：共享文本／日期规范化和保守的 URL 去重。
- `source_validation.py`：字段、枚举、URL、栏目和复核记录检查。
- `audit_sources.py`：只读审计与具名待复核清单，不修改评分。
- `tests/test_intake.py`：离线 feed 样例、来源保留、去重和完整来源库 HTML／上下文一致性测试。

```bash
python -m unittest discover -s tests -v
python intake/audit_sources.py --output /tmp/intake-audit.json
# Check the source field/enumeration definitions against the shared spec:
python intake/audit_sources.py --spec-root ../fivsevn-spec --output /tmp/intake-audit.json
```

`Check Intake Integrity` 在相关 PR 上运行，并上传审计 JSON。本地 `--spec-root` 检查代码与规范的枚举一致性，字段和枚举应与 spec/main 对齐。审计没有结构错误，不代表每个来源都已完成编辑复核。

发布时间、更新时间、抓取时间和生成时间分别记录。缺少发布时间时显示未知，包括只有更新时间的 Atom 条目。网站入口没有发布日期，仍按观察时间排序。HTML 与上下文使用同一个生成时间；feed 请求有连接／读取超时，失败时仍保留网站入口。

文章身份只忽略已知的跟踪参数；必要或未知 URL 参数、片段、末尾斜线及协议差异均保留。没有更强身份依据时，不合并同标题或跨域转载文章。同一位置内的重复条目会合并，但保留全部来源、分类、地区、原始 URL 和各来源评分；跨分类文章仍在各分类可见。网站卡片不与文章合并。标题和摘要先统一规范，再按输出格式转义；URL 不经过正文清理。

## 复核记录 — 2026-10-30

基线为 devlog `2271cae`、spec `c7e588d`。对全部 680 条已有来源做结构复核，新增 2 个来源，保留全部原记录和 62 个二级栏目；两个 `manual` 来源块未改动。

| 来源／位置 | 决定与证据 | 范围／评分状态 |
|---|---|---|
| Mind | `journal / primary`；[OUP 作者说明](https://academic.oup.com/mind/pages/General_Instructions) | 已确认身份；保留 R4/P4，评分复核为部分完成。 |
| Synthese | `journal / primary`；[出版方范围说明](https://link.springer.com/journal/11229/aims-and-scope) | 已确认身份；保留 R4/P4，评分复核为部分完成。 |
| Noûs | `journal / primary`；[Wiley 期刊页面](https://onlinelibrary.wiley.com/journal/14680068) | 已确认身份；保留 R4/P4，评分复核为部分完成。 |
| Philosophical Studies | `journal / primary`；[出版范围和审稿流程](https://link.springer.com/journal/11098/aims-and-scope) | 已确认身份；保留 R4/P4，评分复核为部分完成。 |
| Kew Science | `institutional / primary`；[研究与资源](https://www.kew.org/science) | 已确认身份；保留 R4/P4，资源层面的质量复核为部分完成。 |
| Business of Fashion — industry_business、fashion_style | 两处均为 `trade_publication / specialist`；[编辑准则](https://www.businessoffashion.com/our-journalism/) | 保留 R4/P4 及各栏目用途，保留不同的 use_role。 |
| Rest of World — civilizational_critique、technology_politics | 两处均为 `specialist_media / specialist`；[使命](https://restofworld.org/about/)、[伦理与更正](https://restofworld.org/about/ethics-editorial-policies/) | 保留 R4/P4，依据限定于科技／社会报道。 |
| iFixit News — hardware_radio_embedded、repair_maintenance | 两处均为 R4；[编辑事实核查与技术复核](https://www.ifixit.com/Info/content-quality) | repair_maintenance 的 R3 → R4；News 编辑范围不包含全部社区回答，P4 和 use_role 保留。 |
| Worlds of Journalism Study | feed_url 中的排版引号 `’‘` 改为实际空字符串 | 仅修正语法，网站、类型和评分保留。 |
| NOWFASHION — fashion_style | 新增网站，`specialist_media / primary`，R4/P4/reference；[档案身份](https://nowfashion.com/about-photo-collection)、[条款](https://nowfashion.com/licensing-agreement-terms-of-service) | 用于秀场照片与展示资料查询；保留 URL，不擅自复制照片或内容。 |
| Pixabay — reference_pool | 新增网站，`reference_tool / community`，R3/P4/tool；[许可](https://pixabay.com/service/license-summary/)、[API](https://pixabay.com/api/docs/) | 用于寻找素材，不作为已核实的事实来源；有条件免费使用，并非普遍免版权，API 需要密钥。 |

当时发现的三处跨栏目身份／R 冲突，已按具体来源证据解决。682 个来源位置中，8 个完成了限定范围的复核，5 个只完成身份核对，669 个没有新增证据复核。审计 JSON 列出全部 674 个待复核位置；这是待处理工作量，不是自动认定为低质量来源。

### 后续来源工作

- 为上表五个部分完成的复核补充文章／资源样本及更正历史检查；不会仅因其为期刊或机构而提高评分。
- 优先检查 academic_reference 中可能的身份不匹配：Britannica、Oxford Reference、Philosophy & Public Affairs、Journal of the History of Ideas、European Journal of Analytic Philosophy、Theory, Culture & Society、Cultural Sociology、Journal of Classical Sociology、Poetics。这些是待核查候选，并非本批次已经修正或核实的结论。
- 针对具体出版物／频道，复核 New Phytologist 和 NVIDIA Technical Blog 等机构技术来源，不直接按整个域名定性。
- 检查其余预印本、视频频道和旧有高 R 记录的领域边界与证据；定义了枚举，不等于逐项验证了旧评分。
- 按来源分别审查允许的 RSS／API／网页获取方式。feed 成功只是技术证据，不代表授权或编辑质量；本批次没有新增通用网页抓取器或 API 凭据。
- 沿用现有栏目和证据记录继续补充有价值的来源。更新设备时核对手册型号、版本和官方 URL，保留仅提供网址的手册。

### 验证与发布

本地离线测试包含完整 682 条记录的构建样例，检查 HTML／上下文中的文章数、URL 和生成时间。Data Is Plural、iFixit News、Guardian World 的线上抽样返回了文章；Data Is Plural 保留原始 2025 年发布日期，没有被改成构建日期。来源审计与共享文档 metadata 检查通过；复核时也对照基线检查了 CSS、JavaScript 块和两级栏目定义。

本次修改前，最后观察到的 Intake 任务和 Pages 部署在 `2271cae` 成功。分支／PR 改动不等于线上部署；合并后依次检查新的 Intake 任务、生成 `index.html`／`llm-context.md` 的提交、对应 Pages 部署，以及包含 NOWFASHION、Pixabay 的公开页面，继续通过生成链路更新输出。
