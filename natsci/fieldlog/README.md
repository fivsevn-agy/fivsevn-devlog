---
id: natsci-fieldlog-readme
title: Fieldlog publishing and maintenance
module: natsci
submodule: fieldlog
topic: guide
type: note
status: active
canonical: true
summary: Content packages, publishing, validation, and maintenance for the natural observation archive.
parents: [natsci-readme]
related: []
tags: [natsci, fieldlog]
audience: [self, internal]
languages: [zh]
maturity: evolving
confidence: null
visibility: public
source_of_truth: devlog
filename_policy: entrypoint
created: '2026-10-30'
updated: '2026-11-01'
metadata_updated: '2026-11-01'
---

# Fieldlog

[Fieldlog](https://devlog.fivsevn.com/natsci/fieldlog/)保存自然观察照片与配文，每张照片一帖。

## 发布与修改

1. 拉取最新 `main`，将照片放进 [`trigger_imgs/`](trigger_imgs/README.md)。
2. 配文写在提交的详细说明中；提交并推送。
3. 等待 [Actions](https://github.com/fivsevn-agy/fivsevn-devlog/actions/workflows/publish-pages.yml)完成，检查页面。

支持 JPG/JPEG、PNG、WebP、GIF、HEIC/HEIF；系统归档为 WebP，线上核验后删除上传原图。同次提交重跑不重复发帖；重新上传会另建一帖。

旧帖位于 `YYYY/MM/帖子编号/`：正文和资料在 `index.md`，图片在 `assets/`。修改原文件，保留 `id` 与文件夹名。撤下设为 `status: hidden`；换图时同步更新 `extra.image`。

## 维护

- `ui/` 与 `scripts/fieldlog_templates/`：界面和模板。
- `site-data/history.json`：相同时间戳的稳定排序。
- `.publishing/`：上传游标、事件和已验证发布记录，需保留。
- `_site/natsci/fieldlog/`：构建产物。

```sh
python -m pip install -r scripts/requirements-fieldlog.txt
python -m unittest discover -s scripts -p 'test_fieldlog*.py'
python scripts/build_fieldlog.py
python scripts/build_fieldlog.py --check
```

图片命名和资料格式使用[共享规范](https://github.com/fivsevn-agy/fivsevn-spec)。上传失败时修复入口文件后重跑；继续手动修改前先拉取机器人提交。
