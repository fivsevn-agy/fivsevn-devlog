## 博客发布与维护流程备忘


### 发布速查

| 页面 | 内容类型 | 存档位置 | 发布操作 | 触发流程 | 详细说明文档 |
|---|---|---|---|---|---|
| [posts](https://fivsevn.com/posts/) | 单张图片（可附短文） | GitHub Repo [fivsevn-assets](https://github.com/fivsevn/fivsevn-assets) | 上传图片至[`/post/stream`](https://github.com/fivsevn/fivsevn-assets/tree/main/post/stream) | 上传图片 → Actions自动运行 → 检查页面 | [图片发布说明](https://github.com/fivsevn/fivsevn-assets/blob/main/README.md#image-post-automation) |
| [posts](https://fivsevn.com/posts/) | 短文 | Wordpress | 编辑[trigger.md](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/posts/_wordpress/trigger.md)并commit | 编辑短文并commit → Actions自动运行 → 检查页面 | [短文发布触发说明](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/blogops/docs/post-publish-trigger.md) |
| [devlog.posts](https://devlog.fivsevn.com/posts/) | 长文 | GitHub Repo [fivsevn-devlog](https://github.com/fivsevn-agy/fivsevn-devlog) | 在[`/posts/_draft`](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/posts/_drafts)中新建.md文档并commit | 新建长文草稿并commit → Actions 自动补齐 frontmatter → 编辑长文并更改发布状态 → Actions 自动更新索引 → 检查页面 | [草稿自动更新 frontmatter 说明](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/blogops/docs/auto-draft-frontmatter.md) · [自动索引说明](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/blogops/docs/auto-index.md) · [翻译快捷流程](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/blogops/docs/auto-translation-shortcut.md) |
| [foodie](https://fivsevn.com/foodie/) | 单张图片 | GitHub Repo [fivsevn-assets](https://github.com/fivsevn/fivsevn-assets) | 上传图片至[`/foodie`](https://github.com/fivsevn/fivsevn-assets/tree/main/foodie)对应文件夹 | 上传图片 → Actions自动运行 → 检查页面 | [图片发布说明](https://github.com/fivsevn/fivsevn-assets/blob/main/README.md#image-post-automation)  | [foodie](https://fivsevn.com/foodie/) |
| [natsci](https://fivsevn.com/natsci/) | 单张图片（可附短文） | GitHub Repo [fivsevn-assets](https://github.com/fivsevn/fivsevn-assets) |上传图片至[`/natsci/fieldlog`](https://github.com/fivsevn/fivsevn-assets/tree/main/natsci/fieldlog) | 上传图片 → Actions自动运行 → 检查页面 | [图片发布说明](https://github.com/fivsevn/fivsevn-assets/blob/main/README.md#image-post-automation) | [natsci](https://fivsevn.com/natsci/) |
| [devlog.natsci](https://devlog.fivsevn.com/natsci/) | 长文 | GitHub Repo [fivsevn-devlog](https://github.com/fivsevn-agy/fivsevn-devlog) | 在[`/natsci/_draft`](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/natsci/_drafts)中新建.md文档并commit | 新建长文草稿并commit → Actions 自动补齐 frontmatter → 编辑长文并更改发布状态 → Actions 自动更新索引 → 检查页面 | [草稿自动更新 frontmatter 说明](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/blogops/docs/auto-draft-frontmatter.md) · [自动索引说明](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/blogops/docs/auto-index.md) · [翻译快捷流程](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/blogops/docs/auto-translation-shortcut.md) |
| [devlog.netcom](https://devlog.fivsevn.com/netcom/) | 长文 | GitHub Repo [fivsevn-devlog](https://github.com/fivsevn-agy/fivsevn-devlog) | 在[`/netcom/_draft`](https://github.com/fivsevn-agy/fivsevn-devlog/tree/main/netcom/_drafts)中新建.md文档并commit | 新建长文草稿并commit → Actions 自动补齐 frontmatter → 编辑长文并更改发布状态 → Actions 自动更新索引 → 检查页面 | [草稿自动更新 frontmatter 说明](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/blogops/docs/auto-draft-frontmatter.md) · [自动索引说明](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/blogops/docs/auto-index.md) · [翻译快捷流程](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/blogops/docs/auto-translation-shortcut.md) |
| [stills](https://fivsevn.com/stills/) | 多张图片 | GitHub Repo [fivsevn-assets](https://github.com/fivsevn/fivsevn-assets) | 上传图片至[`/stills`](https://github.com/fivsevn/fivsevn-assets/tree/main/stills)对应文件夹 + [WordPress 新建发布]((https://fivsevn.com/wp-admin/)) | 上传图片 → WordPress 新建页面引用图片并发布 → 检查页面 | [图片发布说明](https://github.com/fivsevn/fivsevn-assets/blob/main/README.md#image-post-automation) |
| [stills/bygone](https://fivsevn.com/stills/bygone/) | 单张图片 | GitHub Repo [fivsevn-assets](https://github.com/fivsevn/fivsevn-assets) | 上传图片至[`/stills/bygone`](https://github.com/fivsevn/fivsevn-assets/tree/main/stills/bygone) | 上传图片 → Actions自动运行 → 检查页面 | [图片发布说明](https://github.com/fivsevn/fivsevn-assets/blob/main/README.md#image-post-automation)  |
| [motion](https://fivsevn.com/motion/)  | 单则视频 | YouTube Channel 和 iCloud | 上传视频至 [YouTube @fivsevn](https://www.youtube.com/@fivsevn) | 上传视频 → Actions自动运行 → 检查页面 | [视频自动抓取说明](https://github.com/fivsevn/fivsevn-assets/blob/main/README.md#youtube-post-automation) |

### 日常维护

| 维护项 | 更新位置 | 效果页面 |
|---|---|---|
| [fivsevn.com 主页](https://fivsevn.com) | [WordPress 后台](https://fivsevn.com/wp-admin/) | [fivsevn.com](https://fivsevn.com) |
| [devlog.fivsevn.com 主页](http://devlog.fivsevn.com) | [fivsevn-devlog/README.md](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/README.md) | [devlog 首页](https://devlog.fivsevn.com) |
| [devlog.fivsevn.com/now 页面](http://devlog.fivsevn.com/now/) | [fivsevn-devlog/now/index.md](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/now/index.md) | [now](https://devlog.fivsevn.com/now/) |
| [devlog.fivsevn.com/blogops 页面](https://devlog.fivsevn.com/blogops/) | [fivsevn-devlog/blogops/index.md](https://github.com/fivsevn-agy/fivsevn-devlog/blob/main/blogops/index.md) | [blogops](https://devlog.fivsevn.com/blogops/) |
| 系统维护 | [GitHub Repo](https://github.com/fivsevn) | - |

