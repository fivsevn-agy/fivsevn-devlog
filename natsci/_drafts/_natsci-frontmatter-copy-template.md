---
id: TEMPLATE-natsci-SUBMODULE-TOPIC-YYYY-slug-001
title: TODO

module: natsci
submodule: TODO # taxonomy / reading / methods / ethnobiology / entomology / marine-ecology / cognitive-science
topic: TODO
type: note # note / article / index / log / spec / dataset / howto / translation
status: hidden # hidden / draft / active / archived
canonical: true # true / false

summary: TODO

parents: []
related: []

tags: [] # example: [natsci, taxonomy, insecta]
audience: self # self / public / tutorial / collaborator
languages: zh # zh / en / jp

maturity: draft # draft / evolving / stable / deprecated
confidence: 0.0 # 0.0 / 0.3 / 0.6 / 0.8 / 1.0
visibility: private # private / public
source_of_truth: devlog # devlog / site / external / mixed

created: YYYY-MM-DD
updated: YYYY-MM-DD

original_title: # for translation
original_source: # for translation
original_publisher: # for translation
original_url: # for translation
translation_note: # for translation
---

# TODO

## 使用说明

这个文件是 `natsci` 模块文章的 frontmatter 复制模板。

新建文章时：

1. 复制上面的 frontmatter。
2. 删除不需要的字段。
3. 把 `TODO` 和枚举注释改成实际值。
4. 正文从 `# TODO` 下面开始写。

## 最少建议保留字段

```yaml
---
id:
title:

module: natsci
submodule:
topic:
type:
status:

summary:

tags:
audience:
languages:

maturity:
confidence:
visibility:
source_of_truth:

created:
updated:
---
```

## 译文建议保留字段

如果文章是译文，建议保留并填写：

```yaml
type: translation
canonical: false
source_of_truth: external

original_title:
original_source:
original_publisher:
original_url:
translation_note:
```

## 和脚本抓取有关的注意事项

`scripts/update_module_indexes.py` 主要读取这些字段：

```yaml
title:
module:
status:
type:
created:
date:
updated:
original_url:
```

注意：

- `title` 必须有实际值；为空会被跳过。
- `module` 在 `natsci` 目录下应写 `natsci`；如果写成别的模块，会被跳过。
- `created` / `date` / `updated` 至少一个要是有效日期。
- 日期建议统一写成 `YYYY-MM-DD`。
- `status: active` 会进入 Recent，并显示为链接。
- `status: draft` 会进入 Recent，但显示为纯文本，并标注“更新中”。
- `status: hidden` / `private` / `archived` / `archive` 不会进入 Recent。
- `type: translation` 会让 Recent 标题后面追加“（译文）”。
- 如果填写 `original_url`，Recent 里的链接会优先指向这个外部 URL，而不是文章在仓库里的路径。
- 如果文章换了文件夹，只要重新运行脚本，站内相对路径会按新位置重新生成；但填了 `original_url` 的文章不会使用站内路径。

## 推荐默认状态

新建文章时建议先用：

```yaml
status: hidden
visibility: private
maturity: draft
confidence: 0.0
```

准备公开时再改成：

```yaml
status: active
visibility: public
maturity: evolving
confidence: 0.6
```


