---
id: "blogops-docs-post-publish-trigger-001"
title: "发布入口说明"

module: "blogops"
submodule: "docs"
topic: "post-publish-trigger"

type: "note"
status: "active"
canonical: false

summary: |
  保留旧发布说明地址，区分 WordPress 文字发布与长文目录刷新；操作统一指向板块 README。

parents: []
related: ["system-docs-auto-index-manual-001", "blogops-docs-auto-draft-frontmatter-001"]

tags: ["blogops", "docs", "automation", "publish", "trigger"]

audience: ["self", "internal"]
languages: ["zh"]

maturity: "stable"
confidence: 0.9

visibility: "public"
source_of_truth: "devlog"

note: "保留现有文件名：展示目录或已发布链接使用该路径，本次不修改展示页；metadata id 继续作为内容身份。"
filename_policy: "stable-link"

created: "2026-06-13"
updated: "2026-10-13"
metadata_updated: "2026-10-13"
---

# 发布入口说明

> 旧文把“长文目录刷新”也称为 post trigger，容易和 WordPress 短文发布混淆。本页保留地址，具体步骤不再重复维护。

- **发 WordPress 短文**：[posts README｜新建文字](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/posts/README.md#新建文字)。
- **发布或修改长文**：[posts](../../posts/README.md) · [natsci](../../natsci/README.md) · [netcom](../../netcom/README.md)。
- **目录刷新**：[自动目录入口](auto-index.md)，不是 WordPress 发文。
- **草稿处理**：[自动草稿入口](auto-draft-frontmatter.md)，不负责把草稿正式发布。

## 脚本维护与验证

- [文字发布脚本](../../scripts/publish_wp_text.py) · [工作流](../../.github/workflows/publish-wp-trigger.yml) · [回归测试](../../tests/test_publish_wp_text.py)。
- 测试和预览不读取 WordPress 凭据、不发送 WordPress 请求；工作流判断可以发文后，才进入单独的发文步骤。
- 从仓库根目录运行：

```bash
python -m pip install requests markdown pyyaml
python -m unittest discover -s tests -p 'test_publish_wp_text.py' -v
python scripts/publish_wp_text.py --dry-run
```

完整预览需要 Git 历史；`--dry-run` 仅校验和转换，不发送帖子。**不要把不带参数的发布命令当作测试命令。**
