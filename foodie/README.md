# foodie 板块说明

```text
fivsevn-devlog/foodie/
└── README.md       本说明；不存图片

fivsevn-assets/foodie/
├── README.md
├── eastwindx1/     东风一只bowl
├── byme/           自己做的
└── nothomecooked/  非自制饮食
```

- **[foodie 页面](https://fivsevn.com/foodie/)**：吃喝记录，手机聊天式视觉效果在 WordPress 维护。
- **[图片目录](https://github.com/fivsevn/fivsevn-assets/tree/main/foodie)**：图片留在 assets；选择不同子目录，对应不同标签。devlog 本目录只放说明。

---

## 1. 新建记录

- 手机分享图片 → 运行[图片快捷指令](https://github.com/fivsevn/fivsevn-assets/blob/main/docs/feat%20Add%20image%20asset.shortcut) → 选择下列目录 → Working Copy 提交并推送到 `main`。
- **每张新图片对应一条帖子**；支持 JPG、JPEG、PNG、WebP、GIF。

| 快捷指令选项／保存目录 | WordPress 分类 | 自动标签 |
|---|---|---|
| [`foodie/eastwindx1`](https://github.com/fivsevn/fivsevn-assets/tree/main/foodie/eastwindx1) | `foodie` | `daily`、`东风一只bowl` |
| [`foodie/byme`](https://github.com/fivsevn/fivsevn-assets/tree/main/foodie/byme) | `foodie` | `daily`、`史诗级大厨` |
| [`foodie/nothomecooked`](https://github.com/fivsevn/fivsevn-assets/tree/main/foodie/nothomecooked) | `foodie` | `daily` |

> [图片发布任务](https://github.com/fivsevn/fivsevn-assets/actions/workflows/publish-image-posts.yml)比较本次推送的文件 → [脚本](https://github.com/fivsevn/fivsevn-assets/blob/main/scripts/publish_image_posts.py)按目录选择分类和标签 → 组装引用 CDN 图片的 WordPress 图片区块 → 调用 REST API 新建帖子。  
> 脚本用 Actions Secrets 中的账号与应用密码验证身份，标题取图片的提交时间；图片留在仓库，不上传 WordPress 媒体库。

- **配文**：foodie 当前不读取提交的 extended description；需要文字时，在 WordPress 原帖中添加。
- **方形图片效果**：脚本添加 `foodie-photo-square` 类，WordPress 的附加 CSS 负责显示。

## 2. 修改与撤下

- **改标题、文字、标签或排版**：在 [WordPress 后台](https://fivsevn.com/wp-admin/)更新原帖，保留图片区块。
- **选错标签**：直接修改原帖标签，不靠搬动源图片换标签。
- **替换图片**：先保存好图片，再在 WordPress 原帖更新图片链接；不要把上传另一张图当作修改旧帖。
- **重命名／移动图片**：检查已有图片链接；进入另一发布路径可能新发一条。
- **撤下记录**：在 WordPress 处理原帖。删除仓库图片不会删除帖子，反而可能留下断图。

> 脚本按图片路径生成 slug → 查到已有帖子就跳过；它负责新建，不回写已有帖子的内容或标签。

## 3. 检查与维护

- 打开[图片发布任务](https://github.com/fivsevn/fivsevn-assets/actions/workflows/publish-image-posts.yml) → 查看结果 → 检查 [foodie 页面](https://fivsevn.com/foodie/)的图片、标签与样式。
- 分类和标签映射见[发布脚本](https://github.com/fivsevn/fivsevn-assets/blob/main/scripts/publish_image_posts.py)；通用说明见 [assets 发布说明](https://github.com/fivsevn/fivsevn-assets/blob/main/README.md#image-post-automation)。
- 只改本 README 不会发图；页面视觉样式仍在 WordPress 修改。

---

核对日期：2026-10-13。按当前目录、脚本与工作流记录，后续可调整。
