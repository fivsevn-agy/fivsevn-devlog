---
id: blogops-docs-auto-draft-frontmatter-001
title: 自动草稿 frontmatter 维护手册

module: blogops
submodule: docs
topic: auto-draft-frontmatter

type: howto
status: active
canonical: true

summary: >
  说明 fivsevn-devlog 中 posts、natsci、netcom 三个板块的 _drafts 草稿自动 frontmatter 规则，
  包括抓取范围、占位命名、字段生成、GitHub Actions 自动提交与日常使用流程。

parents: []
related:
  - system-docs-auto-index-manual-001

tags: [blogops, docs, automation, draft, frontmatter]
audience: [self, collaborator]
languages: [zh]

maturity: stable
confidence: 0.95

visibility: public
source_of_truth: devlog

created: 2026-06-12
updated: 2026-06-12
---

# 自动草稿 frontmatter 维护手册

本仓库使用 `_drafts/` 作为随手草稿缓冲区。

目标是：

```text
随手写 md
↓
commit / push
↓
GitHub Actions 自动补 frontmatter
↓
自动生成占位文件名与 id
↓
自动 commit 回仓库
```

这套流程只服务草稿收纳，不负责正式发布。

正式发布仍然需要人工移动文件、改正式文件名、改正式 `id`，并设置：

```yaml
status: active
visibility: public
```

---

## 1. 适用范围

脚本只处理三个板块下 `_drafts/` 目录第一层中的 Markdown 文件：

```text
posts/_drafts/*.md
natsci/_drafts/*.md
netcom/_drafts/*.md
```

只处理 `.md` 文件。

不会处理：

```text
.jpg
.png
.txt
.pdf
.zip
.webloc
.canvas
```

也不会处理正式内容目录中的文章。

例如以下文件不会被这个脚本处理：

```text
posts/2026/example.md
natsci/taxonomy/example.md
netcom/rf/example.md
```

---

## 2. 不处理的文件

以下情况会跳过：

```text
已有 frontmatter 的 md
模板文件 TEMPLATE-*.md
非 md 文件
不在 _drafts/ 第一层的文件
```

判断已有 frontmatter 的规则：

```text
文件开头是 ---
```

如果一个草稿已经手动写了 frontmatter，脚本不会覆盖。

---

## 3. 草稿占位命名规则

### posts

`posts` 草稿带日期：

```text
posts-YYYYMMDD-draft-001.md
```

示例：

```text
posts-20260612-draft-001.md
posts-20260612-draft-002.md
posts-20260612-draft-003.md
```

### natsci

`natsci` 草稿不带日期：

```text
natsci-draft-001.md
```

示例：

```text
natsci-draft-001.md
natsci-draft-002.md
natsci-draft-003.md
```

### netcom

`netcom` 草稿不带日期：

```text
netcom-draft-001.md
```

示例：

```text
netcom-draft-001.md
netcom-draft-002.md
netcom-draft-003.md
```

---

## 4. id 规则

草稿文件名和 frontmatter `id` 必须保持一致。

规则：

```text
id = 文件名去掉 .md
```

示例：

```text
posts/_drafts/posts-20260612-draft-001.md
```

对应：

```yaml
id: posts-20260612-draft-001
```

示例：

```text
natsci/_drafts/natsci-draft-001.md
```

对应：

```yaml
id: natsci-draft-001
```

示例：

```text
netcom/_drafts/netcom-draft-001.md
```

对应：

```yaml
id: netcom-draft-001
```

---

## 5. title 规则

`title` 从正文第一个一级标题提取。

例如草稿正文：

```md
# 今天随手记

这里随便写一点。
```

生成：

```yaml
title: 今天随手记
```

标题可以是中文。

如果正文没有一级标题，脚本生成：

```yaml
title: TODO
```

---

## 6. 自动生成的 frontmatter

脚本会生成以下 frontmatter：

```yaml
---
id: posts-20260612-draft-001
title: 今天随手记

module: posts
submodule: drafts
topic: draft

type: note
status: hidden
canonical: true

summary: TODO

parents: []
related: []

tags: [posts]
audience: [self]
languages: [zh]

maturity: draft
confidence: 0.0

visibility: private
source_of_truth: devlog

created: 2026-06-12
updated: 2026-06-12
---
```

其中：

```yaml
status: hidden
visibility: private
```

表示草稿不会进入首页目录，也不会被视为公开文章。

---

## 7. 日常使用流程

### 新建草稿

在对应板块的 `_drafts/` 里随便新建一个 `.md` 文件。

例如：

```text
posts/_drafts/tmp.md
```

内容：

```md
# 今天随手记

这里随便写一点。
```

然后正常 commit / push。

### 自动处理后

GitHub Actions 会自动将文件改名为：

```text
posts/_drafts/posts-20260612-draft-001.md
```

并补上 frontmatter。

### 自动提交

脚本会自动生成一个 commit：

```text
chore: apply draft frontmatter
```

---

## 8. 正式发布流程

草稿成熟后，人工执行以下操作：

1. 将文件移出 `_drafts/`；
2. 改成正式文件名；
3. 修改 frontmatter 中的 `id`，使其与正式文件名一致；
4. 修改 `submodule`、`topic`；
5. 修改状态：

```yaml
status: active
visibility: public
maturity: evolving
```

例如：

```text
netcom/_drafts/netcom-draft-001.md
```

正式发布时可以改为：

```text
netcom/rf/netcom-rf-antenna-test-001.md
```

frontmatter 同步改为：

```yaml
id: netcom-rf-antenna-test-001
module: netcom
submodule: rf
topic: antenna-test
status: active
visibility: public
```

---

## 9. 脚本文件

脚本路径：

```text
scripts/apply_draft_frontmatter.py
```

脚本内容：

```python
from __future__ import annotations

from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MODULES = {
    "posts": {
        "draft_id_pattern": "posts-{yyyymmdd}-draft-{seq:03d}",
    },
    "natsci": {
        "draft_id_pattern": "natsci-draft-{seq:03d}",
    },
    "netcom": {
        "draft_id_pattern": "netcom-draft-{seq:03d}",
    },
}


def has_frontmatter(text: str) -> bool:
    return text.startswith("---\n") or text.startswith("---\r\n")


def extract_title(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            if title:
                return title
    return "TODO"


def next_draft_id(module: str, draft_dir: Path, today: str) -> str:
    yyyymmdd = today.replace("-", "")
    pattern = MODULES[module]["draft_id_pattern"]

    existing_stems = {p.stem for p in draft_dir.glob("*.md")}
    seq = 1

    while True:
        candidate = pattern.format(yyyymmdd=yyyymmdd, seq=seq)
        if candidate not in existing_stems:
            return candidate
        seq += 1


def make_frontmatter(module: str, doc_id: str, title: str, today: str) -> str:
    return f"""---
id: {doc_id}
title: {title}

module: {module}
submodule: drafts
topic: draft

type: note
status: hidden
canonical: true

summary: TODO

parents: []
related: []

tags: [{module}]
audience: [self]
languages: [zh]

maturity: draft
confidence: 0.0

visibility: private
source_of_truth: devlog

created: {today}
updated: {today}
---

"""


def should_skip(path: Path, text: str) -> bool:
    if path.name.startswith("TEMPLATE-"):
        return True

    if has_frontmatter(text):
        return True

    return False


def process_file(module: str, path: Path) -> bool:
    text = path.read_text(encoding="utf-8")

    if should_skip(path, text):
        print(f"SKIP: {path}")
        return False

    today = date.today().isoformat()
    draft_dir = path.parent
    doc_id = next_draft_id(module, draft_dir, today)
    new_path = draft_dir / f"{doc_id}.md"

    if new_path.exists():
        raise FileExistsError(f"Target already exists: {new_path}")

    title = extract_title(text)
    frontmatter = make_frontmatter(module, doc_id, title, today)
    new_text = frontmatter + text

    new_path.write_text(new_text, encoding="utf-8")

    if new_path != path:
        path.unlink()

    print(f"UPDATED: {path} -> {new_path}")
    return True


def main() -> int:
    changed = False

    for module in MODULES:
        draft_dir = ROOT / module / "_drafts"

        if not draft_dir.exists():
            continue

        for path in sorted(draft_dir.glob("*.md")):
            if process_file(module, path):
                changed = True

    if not changed:
        print("No draft files needed frontmatter.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

---

## 10. GitHub Actions 文件

Workflow 路径：

```text
.github/workflows/apply-draft-frontmatter.yml
```

内容：

```yaml
name: Apply Draft Frontmatter

on:
  push:
    branches: [main]
    paths:
      - "posts/_drafts/*.md"
      - "natsci/_drafts/*.md"
      - "netcom/_drafts/*.md"
      - "scripts/apply_draft_frontmatter.py"
      - ".github/workflows/apply-draft-frontmatter.yml"
  workflow_dispatch:

permissions:
  contents: write

jobs:
  apply-draft-frontmatter:
    runs-on: ubuntu-latest

    if: github.actor != 'github-actions[bot]'

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.x"

      - name: Apply draft frontmatter
        run: python scripts/apply_draft_frontmatter.py

      - name: Commit changes
        run: |
          if [[ -n "$(git status --porcelain)" ]]; then
            git config user.name "github-actions[bot]"
            git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
            git add posts/_drafts natsci/_drafts netcom/_drafts
            git commit -m "chore: apply draft frontmatter"
            git push
          else
            echo "No draft frontmatter changes."
          fi
```

---

## 11. 本地测试

在仓库根目录运行：

```bash
python scripts/apply_draft_frontmatter.py
```

查看改动：

```bash
git status
git diff
```

确认无误后提交：

```bash
git add scripts/apply_draft_frontmatter.py .github/workflows/apply-draft-frontmatter.yml
git commit -m "Add draft frontmatter automation"
git push
```

---

## 12. 快速规则表

| 项目 | 规则 |
|---|---|
| 抓取目录 | `posts/_drafts/*.md`、`natsci/_drafts/*.md`、`netcom/_drafts/*.md` |
| 是否抓子目录 | 否 |
| 是否抓非 md | 否 |
| 是否处理已有 frontmatter | 否 |
| 是否处理模板文件 | 否 |
| 是否改正文 | 否 |
| 是否自动改文件名 | 是 |
| 文件名和 id 是否一致 | 是 |
| posts 草稿格式 | `posts-YYYYMMDD-draft-001.md` |
| natsci 草稿格式 | `natsci-draft-001.md` |
| netcom 草稿格式 | `netcom-draft-001.md` |
| title 来源 | 正文第一个 `# 一级标题` |
| 默认 status | `hidden` |
| 默认 visibility | `private` |
| 是否进入首页目录 | 否 |
| 自动 commit message | `chore: apply draft frontmatter` |

---

## 13. 维护原则

1. `_drafts/` 是随手草稿缓冲区，不进入首页目录。
2. 草稿阶段使用占位文件名，不强行生成正式语义 slug。
3. 文件名和 `id` 必须一致。
4. `posts` 草稿带日期。
5. `natsci` 和 `netcom` 草稿不带日期。
6. 正式发布时再人工改正式文件名、正式 `id`、`submodule` 和 `topic`。
7. 脚本只负责草稿初始化，不负责文章发布。
