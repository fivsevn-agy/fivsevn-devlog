---
id: "motion-readme"
title: "motion 板块说明"

module: "motion"
submodule: "guide"
topic: "guide"

type: "note"
status: "active"
canonical: true

summary: "说明motion 板块说明。"

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

created: "2026-10-13"
updated: "2026-10-13"
metadata_updated: "2026-10-13"
---
# motion 板块说明

```text
fivsevn-devlog/motion/
└── README.md                              本说明；不存视频

fivsevn-assets/
├── scripts/publish_youtube_posts.py        YouTube 发帖脚本
└── .github/workflows/
    └── publish-youtube-posts.yml           定时任务
```

- **[motion 页面](https://fivsevn.com/motion/)**：视频作品与动态影像，展示和视觉效果在 WordPress 维护。
- **[YouTube @fivsevn](https://www.youtube.com/@fivsevn)**：托管视频；GitHub 保存自动发布脚本，本目录只放说明。

---

## 1. 发布新视频

- 视频发布到配置的 YouTube 频道 → 等待[视频发布任务](https://github.com/fivsevn/fivsevn-assets/actions/workflows/publish-youtube-posts.yml)运行 → 检查 WordPress motion。
- **检查频率**：按每小时计划运行，也可在任务页手动点 `Run workflow`；不是即时同步。
- **标题与标签**：如 `夜市记录 #夜市 #日常` → WordPress 标题为“夜市记录”，标签为“夜市”“日常”。每个标签用一个 `#` 分开。

> Actions 启动 → [脚本](https://github.com/fivsevn/fivsevn-assets/blob/main/scripts/publish_youtube_posts.py)读取 Secrets 中的频道 ID → 用 `feedparser` 读取频道 RSS 的**最新一条** → 拆出标题、标签和视频 ID → 生成 WordPress YouTube 嵌入区块 → 调用 REST API 新建 `motion` 分类、`video` 格式的帖子。  
> WordPress 账号与应用密码也来自 Actions Secrets；视频仍在 YouTube，不下载到 GitHub，也不上传 WordPress 媒体库。Shorts 链接统一转为 `watch?v=` 形式。

## 2. 补发与检查

- **最新视频没出现**：查看任务日志；确认视频已进入频道 RSS，再手动运行[视频发布任务](https://github.com/fivsevn/fivsevn-assets/actions/workflows/publish-youtube-posts.yml)。
- **连续发布多条**：逐条检查 WordPress；当前每次只读最新一条，可能漏掉两次检查之间发布的其他视频。
- **补旧视频**：在 [WordPress 后台](https://fivsevn.com/wp-admin/)手动新建帖子 → 插入 YouTube 嵌入区块 → 选择 `motion` 分类与视频格式。任务不会自动遍历全部历史视频。

> 脚本根据视频 ID 生成 `youtube-视频ID` 形式的 slug → 查询 WordPress → 已存在就跳过，不存在才新建。需要手动补发时，对照[脚本规则](https://github.com/fivsevn/fivsevn-assets/blob/main/scripts/publish_youtube_posts.py)保留一致的 slug，避免后续重复创建。

## 3. 修改与撤下

- **改网站标题、标签、文字或排版**：在 WordPress 原帖更新；之后只改 YouTube 标题，不会自动更新已有 WordPress 帖子。
- **同一个视频换链接／另传新版**：在 WordPress 更新原帖嵌入链接；新上传的视频有新 ID，仍可能被任务作为新帖收录。
- **撤下网站帖子**：优先转为草稿并保留 slug；如果直接删除最新视频对应的帖子，任务再次检查时可能重新创建。
- **YouTube 删除或转私密**：WordPress 帖子不会自动撤下，可能留下无法播放的嵌入；同时检查并处理网站原帖。
- **视频原文件**：另行备份；本任务只创建嵌入帖子，不备份视频文件。

> 这条流程是“读取 YouTube → 新建 WordPress 帖子”，不是双向同步，也不是持续覆盖已有帖子。

## 4. 检查与维护

- 查看[视频发布任务](https://github.com/fivsevn/fivsevn-assets/actions/workflows/publish-youtube-posts.yml) → 打开 [motion 页面](https://fivsevn.com/motion/) → 检查标题、标签和实际播放。
- 频道与账号配置由 Actions Secrets 提供；脚本入口见 [publish_youtube_posts.py](https://github.com/fivsevn/fivsevn-assets/blob/main/scripts/publish_youtube_posts.py)，通用说明见 [YouTube 发布说明](https://github.com/fivsevn/fivsevn-assets/blob/main/README.md#youtube-post-automation)。
- 只改本 README 不会启动视频发布任务；不要把视频文件上传到这个说明目录。

---

核对日期：2026-10-13。按当前脚本与工作流记录，后续可调整。
