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

[每日阅读页](https://devlog.fivsevn.com/intake/)包含明信片、今日野采样本、来源目录和 RSS 条目。

| 文件 | 用途 |
|---|---|
| `sources.md` | 手动维护来源、分类和抓取数量 |
| `config.yml` | 页面标题、展示上限与禁用源配置 |
| `build.py` | 从来源清单生成页面与 AI 阅读上下文 |
| `scripts/daily_postcard.py`、`scripts/daily_field_sample.py` | 生成每日卡片 |
| `index.html`、`llm-context.md` | 自动生成并提交的公开输出 |
| `data/` | 本地构建片段，不提交 |

`Build Intake Page` 每日 UTC 00、05、10、15、20 时运行；来源、配置或脚本变化也会触发。生成成功后自动部署网站。

```sh
python -m pip install -r intake/requirements.txt
python intake/scripts/daily_postcard.py
python intake/scripts/daily_field_sample.py
python intake/build.py
```

检查：`python -m unittest discover -s tests -p 'test_intake.py'`。只读来源审计：`python intake/audit_sources.py`。

来源保留网站入口，即使暂时抓不到文章。R/P 评分及其依据按[来源规范](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/source/spec-source-intake-fields-001.md)维护。
