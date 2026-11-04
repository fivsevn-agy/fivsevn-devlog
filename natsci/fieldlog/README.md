---
id: natsci-fieldlog-readme
title: Fieldlog 发布与维护
module: natsci
submodule: fieldlog
topic: guide
type: note
status: active
canonical: true
summary: 自然观察档案的发布包、发布、校验与维护说明。
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
updated: '2026-11-05'
metadata_updated: '2026-11-05'
---

# Fieldlog

Fieldlog 是[自然观察照片档案](https://devlog.fivsevn.com/natsci/fieldlog/)。本目录保存可编辑的发布包、共用界面素材和发布状态；相关笔记放在 [natsci 自然科学档案](https://devlog.fivsevn.com/natsci/)。

照片上传到 [`trigger_imgs/`](trigger_imgs/)，每张图片生成一篇独立帖子，可附 Markdown 配文。发布步骤见[图片入口说明](trigger_imgs/README.md)。

## 仓库结构

```text
natsci/fieldlog/
  YYYY/MM/{id}/
    index.md                       Canonical metadata and editable Markdown caption
    assets/                        This post's archived image
  trigger_imgs/                    Temporary image-upload inbox
    README.md                      upload guide
  ui/                              Shared image, fonts, CSS, and navigation behavior
  site-data/
    history.json                   Stable order for posts sharing an exact timestamp
  .publishing/
    state.json                     Upload cursor and immutable image-event records
    deployed.json                  File hashes from the last verified public build
scripts/
  site_post_metadata.py            Shared metadata normalization and validation
  fieldlog_image_codec.py          Shared image validation and WebP conversion
  normalize_fieldlog_images.py     Normalize saved package images without changing post IDs
  import_fieldlog_triggers.py      Import committed inbox snapshots into post packages
  build_fieldlog.py                Build listings, details, assets, and a build receipt
  verify_fieldlog_live.py          Verify the public build before clearing originals
  fieldlog_image_inbox.py          Clear only matching, publicly verified inbox files
  fieldlog_templates/              Page and opening-window templates
  requirements-fieldlog.txt        Pinned dependencies
schemas/                           Local shared core and site-post schema copies
_site/natsci/fieldlog/              Generated deployment artifact
```

修改源发布包和模板。HTML 在 `_site/` 中由源文件重新构建。Fieldlog 自己提供照片、字体和界面素材。

## 发布图片

1. 推荐网页或直接调用 GitHub 的快捷指令上传；网页可使用[图片上传页](https://github.com/fivsevn-agy/fivsevn-devlog/upload/main/natsci/fieldlog/trigger_imgs)。
2. 把一张或多张照片保存到 `natsci/fieldlog/trigger_imgs/`，保留原文件名。
3. 提交摘要用作操作名称；需要公开的 Markdown 配文写在摘要下方的 **详细说明（extended description）** 中。留空则只发图片。
4. 提交并推送到 `main`，等待[发布任务](https://github.com/fivsevn-agy/fivsevn-devlog/actions)成功，再检查[列表页](https://devlog.fivsevn.com/natsci/fieldlog/)和单帖页面。

快捷指令使用 **fivsevn-agy/fivsevn-devlog**、上述图片入口及 GitHub 当前的 `main`。历史清理会更新版本编号；旧 Working Copy 副本请重新克隆，不要合并旧历史。GitHub 的只读 PR 引用和服务端对象保留由平台管理。

每张图片独立成帖，同一次提交的图片共用详细说明中的配文。上传时只需照片和可选配文，共享 metadata 由导入脚本自动补齐。

### 日期、命名与重试

- 发布时间取上传提交的 **committer 时间戳**，转换为 `Asia/Shanghai`，保存时带时区偏移。
- 发布包 ID 由时间戳、上传提交和文件路径的摘要组合而成，目录为 `YYYY/MM/{id}/`。
- 每张上传图片各有一个发布包，归档文件命名为 `YYYYMMDD-HHMMSS-fieldlog-<package-key>-001.webp`。
- 同一提交及路径只处理一次。任务重跑会保留发布包以及后续编辑的配文。
- 在**新提交**中上传同名文件或相同内容，会生成新帖；修改旧帖应编辑已保存的发布包。
- 删除入口文件不会撤回此前已经提交的上传事件；需要撤下时，隐藏或删除对应的发布包。

精确时间戳、界面显示的 12 位观察编号和稳定的发布包 ID 相互独立。更正观察时间时修改 `extra.published_at` 和 `extra.observation_id`，保留 ID 与目录；帖子网址保持不变。

## 图片

支持 JPG/JPEG、PNG、WebP、GIF、HEIC、HEIF，也支持大写扩展名、Unicode 文件名和入口中的嵌套文件夹。

| 输入 | 归档方式 |
| --- | --- |
| JPEG、HEIC/HEIF 照片 | 质量 95、method 6 的 WebP；不缩放，保留原显示尺寸，校正方向，保留 ICC 色彩配置和适用的 EXIF 资料 |
| PNG 图形 | 无损 WebP，保留透明度和动画时间 |
| GIF 动画 | 无损动画 WebP，保留帧、时间、透明度和循环方式 |
| 已有 WebP | 校验后逐字节保留 |

MPO、HEIF 使用主显示照片，手机的辅助帧不会变成动画帧。归档图片统一为 WebP；已有的有效 WebP 保留原字节和文件名拼写，构建时直接复制到发布产物。

`normalize_fieldlog_images.py` 也会处理直接存入发布包的图片，包括隐藏帖、草稿和帖子当前未选用的图片。脚本先校验整批文件，暂存 WebP，更新 `extra.image` 及相应上传记录，再统一替换旧格式文件。整批失败时恢复原文件和 metadata；归档已经全部为 WebP 时，重跑不会改文件。

当前内容树只保存 WebP 归档。线上核验并清理入口后，流程会清理 Fieldlog 旧格式图片的 `main` 历史并同步发布游标；有待处理输入或并发提交时延后。原件请另存仓库外，上传前先拉取最新 `main`。转换不改变帖子 ID、网址、观察日期或配文。

界面中的 `OBS-…_raw.tif` 是虚拟标本文件名，实际显示的图片由 `extra.image` 指定，格式为 WebP。

## 配文与已保存的帖子

每个发布包包含 `index.md` 和自己的 `assets/`：

```yaml
---
id: 2026-10-30-174000-example
title: 30 Oct, 2026 17:40
module: natsci
submodule: fieldlog
topic: null
type: log
status: published
canonical: true
summary: null
parents: []
related: []
tags: []
audience: [public]
languages: [zh]
maturity: evolving
confidence: null
visibility: public
source_of_truth: devlog
filename_policy: entrypoint
created: '2026-10-30'
updated: '2026-10-30'
metadata_updated: '2026-10-30'
extra:
  profile: site-post-v1
  published_at: '2026-10-30T17:40:00+08:00'
  author: 五月七日
  image: assets/20261030-174000-01.webp
  alt: A specimen observed in the field
  observation_id: '261030174000'
  display_status: Archived
---

Write the accompanying observation here. **Markdown** and [named links](https://example.com/) are supported.
```

已保存帖子与 Flux、Savour 使用同一套[共享核心 metadata](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/content-metadata.schema.json)和 [site-post profile](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/site-post.schema.json)。共享 helper 和 schema 副本保存在仓库中，规范化、校验和构建可以离线运行；采用新规范版本时一并更新这些副本。

| 字段 | 含义 |
| --- | --- |
| `id` | 唯一且稳定的身份，与已有目录名一致 |
| `title` | Annotation Log 旁的标签，与发布时间独立 |
| `module`、`submodule`、`type` | 分别为 `natsci`、`fieldlog`、`log` |
| `status`、`visibility` | 仅在 `visibility: public`，且状态为 `active`、`publish` 或 `published` 时公开列出 |
| `created`、`updated` | 内容日期，与精确发布时间独立 |
| `metadata_updated` | metadata 维护日期；无变化的规范化不会刷新它 |
| `extra.profile` | `site-post-v1` |
| `extra.published_at` | 带时区偏移的精确观察／发布时间，控制排序 |
| `extra.image`、`extra.alt` | `assets/` 下的包内相对图片路径及替代文字 |
| `extra.observation_id` | 界面显示的 12 位 OBS 时间编号，不同帖子可以相同 |
| `extra.display_status` | 窗口显示标签，通常为 `Archived`，与发布状态独立 |

配文写在第二个 `---` 后面，只显示在单帖页面；列表显示照片和 metadata。手动保存的发布包会在校验前补齐缺失字段，已有状态与可见性保留，无法识别的旧 metadata 保存到 `legacy.metadata`。

修改 `index.md` 可以更新配文、标签和可见性。将 `status` 设为 `hidden`、`draft`，或将 `visibility` 设为 `private`、`internal`，可从生成网站中移除。公开 Git 仓库中的文件仍然可访问。删除整包可移除帖子，旧版本仍在 Git 历史中。

## 界面与网址

每个列表页最多显示 **11 篇已发布帖子**，开头的工作区窗口和结尾的 Root Directory 链接不计入帖子数；最后一页显示剩余帖子。

单帖网址为 `/natsci/fieldlog/YYYY/MM/{id}/`，后续列表页使用 `/natsci/fieldlog/page/N/`。OBS 锚点会映射到当前列表页，页数变化后，旧分页书签仍能找到原帖。绿色 `X` 返回来源列表页及帖子位置；直接访问详情页时，使用当前列表锚点。详情窗口内容超过视口时在窗口内滚动。

开场图片、窗口居中、字体和配色由 `ui/fieldlog.css` 与 `scripts/fieldlog_templates/` 控制。Root Directory 指向 [fivsevn.com](https://fivsevn.com/)。

## 构建与发布

整个 devlog 共用一次 Pages 部署。工作流依次规范化 metadata 和照片、测试发布行为、导入已提交的入口图片、校验发布包、构建主站并叠加 Fieldlog 产物；部署前一起保存源发布包和上传游标。

部署后，`verify_fieldlog_live.py` 将公开构建回执及相关页面／素材的字节与本地发布产物比较。校验范围包含改动文件、首尾列表页和待清理入口所对应的发布包；归档未变时，不重复下载全部旧照片。清理时分别核对上传原件和归档图片的摘要，只删除匹配的入口原图。任务失败、有更新的上传、帖子未公开或归档图片已变化时，原件保留。

提交清理前，工作流还会确认远端分支仍与本次运行一致。失败可重跑；新的上传提交会产生新帖。日常维护保留发布游标和事件记录。

### 本地开发

```sh
python3 -m pip install -r scripts/requirements-fieldlog.txt
python3 scripts/site_post_metadata.py normalize --site fieldlog --root natsci/fieldlog --schema-dir schemas
python3 scripts/normalize_fieldlog_images.py
python3 scripts/site_post_metadata.py check --site fieldlog --root natsci/fieldlog --schema-dir schemas
python3 -m unittest discover -s scripts -p 'test_fieldlog_*.py'
python3 -m unittest discover -s tests -p 'test_fieldlog.py'
python3 scripts/build_fieldlog.py
python3 scripts/build_fieldlog.py --check
python3 -m http.server 8000 --directory _site
```

打开 `http://localhost:8000/natsci/fieldlog/`。`build_fieldlog.py` 默认输出到 `_site/natsci/fieldlog`；`--output /absolute/path` 指定其他模块产物目录，`--root` 指定仓库位置。`--check` 只读检查 metadata、生成链接及产物是否为最新。

线上核验和入口清理需要使用实际部署的同一份产物：

```sh
python3 scripts/verify_fieldlog_live.py
python3 scripts/fieldlog_image_inbox.py
```

两者都支持 `--root` 和 `--output`；公开校验另支持 `--url`。清理需要相符的公开校验和部署记录，普通本地构建不会获得删除入口原图的凭证。

### 维护与恢复

- `.publishing/state.json` 保存不可变上传事件、原件与归档图片摘要、发布包路径；修改配文或模板时保留它。
- `.publishing/deployed.json` 保存最后一次通过线上校验的产物摘要；产物中的 `build-receipt.json` 标识本次构建，`.verified.json` 是本地校验标记。
- `site-data/history.json` 固定相同时间戳的排序。替换照片时更新包内图片并提交；文件名变化时同步修改 `extra.image`。工作流会转为 WebP，记录并校验当前字节，历史摘要不会阻止主动换图。
- 上传图片损坏或格式不支持时，替换或移除相应入口文件后推送。后续修复会取代无效事件；当前无效上传会阻止整批安装，避免同批帖子只保存一部分。
- 有更新提交或线上字节不符时，等待最新排队任务继续，或在最新 `main` 上重跑。下一次手机上传前先拉取机器人提交。
- 游标丢失，或不在当前分支的第一父提交历史中时，先检查或恢复 Git 历史再修复状态；直接重置可能重放已处理的上传。

## 发布素材命名

包内图片使用 `YYYYMMDD-HHMMSS-<board>-<package-key>-NNN.ext`。其中 key 是 `board:id` 的 SHA-256 前 12 个小写十六进制字符，时间使用 Asia/Shanghai；显示顺序变化时，图片序号保持不变。上传时自动规范命名，共享素材和未编排草稿保留现有位置。详见[共享命名规范](https://github.com/fivsevn-agy/fivsevn-spec/blob/main/content/spec-content-media-naming-001.md)。
