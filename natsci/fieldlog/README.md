---
id: natsci-fieldlog-readme
title: Fieldlog 发布与维护
module: natsci
submodule: fieldlog
topic: guide
type: note
status: active
canonical: true
summary: 自然观察影像记录的内容结构、发布方法与迁移说明。
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
updated: '2026-10-30'
---
# Fieldlog

[展示页面](https://devlog.fivsevn.com/natsci/fieldlog/) · [发布任务](https://github.com/fivsevn-agy/fivsevn-devlog/actions/workflows/publish-fieldlog.yml)

[图片入口说明](trigger_imgs/README.md) · [直接上传图片](https://github.com/fivsevn-agy/fivsevn-devlog/upload/main/natsci/fieldlog/trigger_imgs)

延续 [flux](https://github.com/fivsevn/fivsevn-flux) 和 [savour](https://github.com/fivsevn/fivsevn-savour) 的做法：内容留在 Git，每则帖子一个文件夹，由 Python 生成静态页面，在现有 devlog GitHub Pages 发布。图片、字体和首页图片都保存在本目录；展示不依赖 WordPress 或原 assets 仓库。

## 发一张图片

1. 把图片放进 `natsci/fieldlog/trigger_imgs/`，可用 Working Copy，也可把原图片快捷指令的目标仓库和路径改到这里。
2. 提交并推送到 `main`。提交标题写简短说明；**extended description（提交正文）写公开配文**，可用 Markdown。同一次提交多张图，会分别成帖，并使用相同配文。
3. 等待 **Publish fieldlog** 完成，再等 GitHub Pages 部署完成；拉取自动生成的帖子后继续编辑。

支持 JPG/JPEG、PNG、WebP、GIF、HEIC/HEIF。新上传图片按 savour 的处理方式生成 WebP；入口原图保留，不自动删除。每次有效的“提交 + 图片路径”都是一个独立发布事件：重试不重复发帖，后续提交覆盖同名图片会另发一则。直接在网页上传时，可将配文写进提交的 extended description。

日期取提交时间，转换为北京时间（Asia/Shanghai）。如需记录拍摄日期，发布后修改帖子 `date` 和 `observation_id`；保留 `id` 和目录名，地址不变。

**删除入口图片不会撤回已提交的发布事件。** 修改或隐藏旧帖应编辑已生成文件夹内的 `index.md`，不要通过重传入口图片更新原帖。配文只在详情页显示；列表中点击绿色时间码进入详情页。

## 每则帖子

```text
natsci/fieldlog/
├── 2026/07/260715090824/
│   ├── index.md          内容源：图片引用、日期和配文
│   ├── index.html        自动生成的详情页
│   └── assets/IMG_8302.jpg
├── trigger_imgs/         新图片入口（保留上传原图）
├── index.html            自动生成的列表首页
├── page/2/index.html     自动生成的分页，每页 17 则
├── ui/                   样式、字体和首页图片
├── migration/manifest.json
└── .publishing/state.json  上传游标与去重记录
```

手动新建时，创建 `YYYY/MM/唯一id/index.md`，把图片放在同目录 `assets/`。例如：

```yaml
---
id: '261030174000'
observation_id: '261030174000'
title: '30 Oct, 2026 17:40'
date: '2026-10-30T17:40:00+08:00'
archive_status: Archived
status: published
published: false
image: assets/photo.webp
alt: 自然观察影像
---

这里写发布时附带的文字。支持段落、链接、列表等 Markdown。
```

`id` 必须与文件夹名一致且唯一；`observation_id` 是页面显示的 12 位时间码，可重复。`date` 决定列表排序，必须带时区。`title` 是 Annotation Log 旁显示的标题；留空或不填时，使用 `date` 转换成北京时间的日期时间。迁移记录中的 `annotation_date` 仅保留原始信息，修改标题直接改 `title`。详情页右上角绿色 `X` 返回原分页与帖子位置；窗口内部仅在内容超出视口时滚动。

`status: published` 生成展示页面；改成 `draft`、`hidden` 或 `archived` 后，下一次构建会移除该则已生成的 HTML。这里的 `archive_status: Archived` 只是原窗口中的显示标签。**`published: false` 必须保留**：它用于阻止 Jekyll 再把内容源生成一个页面，不影响本项目的发布状态。公开 Git 仓库中的草稿、历史和原图仍可被访问，这些状态不提供隐私保护。

## 修改与构建

改配文、日期、标题或图片引用，编辑原 `index.md`；替换图片可直接改原帖 `assets/` 中的文件。提交到 `main` 后自动重建，不改变原帖地址。布局由 `scripts/fieldlog_templates/` 与 `ui/fieldlog.css` 管理，勿直接修改生成的 HTML。`natsci` 普通笔记目录不收录这些单图帖子。

本地检查：

```sh
python3 -m pip install -r scripts/requirements-fieldlog.txt
python3 scripts/build_fieldlog.py
python3 scripts/build_fieldlog.py --check
python3 -m unittest discover -s scripts -p 'test_fieldlog_triggers.py' -v
python3 -m unittest discover -s tests -p 'test_fieldlog.py' -v
```

发布任务读取 Git 提交历史，先保存帖子与游标，再生成并提交 HTML，最后请求现有 GitHub Pages 分支构建。构建中若 `main` 有新的提交，任务会停止以免覆盖；在 Actions 重新运行即可。失败时入口图保留，游标仅随成功保存的帖子一起提交，不要手动清空或重置它。

## 本次迁移

2026-10-30 从 [WordPress natsci](https://fivsevn.com/natsci/) 的 fieldlog 分类复制全部 **43 则、43 张原图**。保留原始图片字节、OBS 日期、原标题（Annotation Log）、来源链接；迁移清单记有每张图片的 SHA-256、字节数及对应帖子。原帖均无配文、无评论，因此详情页留空附文位置，不显示虚构的占位内容。

两则观察时间相同的记录，文件夹和 `id` 分别加原 WordPress ID `-3522`、`-3543`，显示时间码保持原样。列表维持原来每页 17 则，共 3 页；同时间记录按原站顺序排列。

**旧 assets、旧发布任务和 WordPress 内容尚未删除或修改。** 等新页面验收后再单独处理旧内容及旧发布入口。
