# AI Posts Boot Protocol
# AI文章生成引导协议

Purpose:
Generate a Markdown post skeleton for a `posts` column.

AI outputs only:
- filename
- frontmatter
- minimal body skeleton

User will paste real content manually.

> 只生成骨架，正文我来贴。

---

## 0) Load Metadata Spec
You MUST follow:
[spec-gov-meta-frontmatter-001](https://raw.githubusercontent.com/fivsevn-agy/fivsevn-spec/main/gov/spec-gov-meta-frontmatter-001.md)

Hard rules:
- all fields present
- field order identical
- no extra fields
- date format YYYY-MM-DD

> frontmatter 字段齐全、顺序一致、不加字段

---

## 1) Read Posts Index
Read:
[posts/index.md](https://raw.githubusercontent.com/fivsevn-agy/fivsevn-devlog/main/posts/index.md）

Goal:
Locate the target column path.

Example reference:
 [oai_citation:1‡index.md](sediment://file_00000000977871fdb749c8cb2d8c70d3)

> 先从 posts 主索引找到专栏入口

---

## 2) Read Column Index
Read column index:
[posts/ai-discourse-analysis/index.md](https://raw.githubusercontent.com/fivsevn-agy/fivsevn-devlog/main/posts/ai-discourse-analysis/index.md)

Goal:
- understand column purpose (for tags/summary tone only)
- parse Case List
- compute next article number

Auto-number rule:
- Extract all leading numbers from Case List items (e.g. 001, 002, 003)
- next_number = max_number + 1
- Format as 3 digits with zero-padding (e.g. 004)

If Case List is empty:
- next_number = 001

Example reference:
 [oai_citation:2‡index.md](sediment://file_00000000cf7c71fd9f44af4dce289524)

> 从 Case List 自动算下一篇：最大值+1，补零三位

---

## 3) Learn Existing Article Format
Read latest 1–3 articles in the column.

Goal:
- naming style `NNN-topic-slug.md`
- typical body sections
- common tags and maturity/confidence defaults
- keep style consistent

Do NOT reuse content, only learn format.

---

## 4) User Inputs
User provides:
- column name
- title (must be used verbatim)

Optional:
- topic slug (if missing, AI generates)
- materials links (optional)

User does NOT need to provide the number.

> 用户只给：专栏 + 标题。编号自动算

---

## 5) Topic Slug Generation
If user does not provide topic slug:
Generate a short english slug from the title:

Rules:
- lowercase
- letters/numbers/hyphen only
- 2–6 words max
- remove stopwords
- avoid dates in slug unless meaningful

> topic slug 自动英文化，短，稳定

---

## 6) File Naming
Filename:
{NNN}-{topic-slug}.md

NNN is auto-numbered from Step 2.

---

## 7) Frontmatter Rules
Required fixed values:
module: posts
submodule: (from column index; do not invent)
type: article
status: active

Other fields:
- id: must follow repo id convention; keep consistent with existing articles in this column
- topic: use topic slug
- summary/tags/maturity/confidence/audience/languages/visibility/source_of_truth:
  infer from column + existing articles (keep consistent)

Dates:
created = today
updated = today

> 保持仓库统一 metadata 语法；其余字段按专栏既有风格推断

---

## 8) Body Skeleton (minimal)
Generate minimal placeholders only:

# 本期材料
(placeholder)

---
# 提示词
(placeholder)

---
# 正文
(placeholder)

No actual content.

---

## 9) Also Output: Index Update Line (Optional helper)
Additionally output ONE suggested line for updating the column Case List:

- [NNN｜{title}](content/{NNN}-{topic-slug}.md)

User will paste it into the column index manually.

> 额外给一行：我手动贴回专栏 index 的 Case List

---

## 10) Output Format (strict)
Output ONLY:

1) Filename
2) Full markdown (frontmatter + skeleton)
3) Suggested Case List line (single line)

No explanations.
No extra text.