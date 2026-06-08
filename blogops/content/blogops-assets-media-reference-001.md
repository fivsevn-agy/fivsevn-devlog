---
id: blogops-assets-media-reference-001
title: 博客各类内容的保存和引用方式
module: blogops
submodule: assets
topic: media-reference

type: note
status: draft
canonical: false

summary: >
  记录博客图片、视频等内容资源的保存位置与引用方式，
  以及对应平台和路径维护上的优缺点。
parents: []
related: []
tags: [blogops, assets, images, video, cdn, youtube]

audience: [self]
languages: [zh]
maturity: evolving
confidence: 0.80
visibility: public
source_of_truth: devlog

created: 2026-06-07
updated: 2026-06-07
---

# 博客各类内容的保存和引用方式

## 1. 图片

### 1.1 博客图库

```text
https://github.com/fivsevn/fivsevn-assets
```

### 1.2 引用方式

- 把 GitHub 图片路径转换成 CDN 链接。

```text
https://cdn.jsdelivr.net/gh/用户名/仓库名@分支名/文件路径
```

### 1.3 示例

- GitHub 仓库图片：

```text
https://github.com/fivsevn/fivsevn-assets/blob/main/homepage/homepage20251101head.webp
```

- 最终引用链接：

```text
https://cdn.jsdelivr.net/gh/fivsevn/fivsevn-assets@main/homepage/homepage20251101head.webp
```

### 1.4 扩展

#### 1.4.1 批量导入

- 示例页面

``` 
https://fivsevn.com/2026/04/20/kamakura/  
```

- 方法：AI 统一转换、并写成 markdown 图片引用格式，直接批量复制粘帖。

#### 1.4.2 自动更新

- 示例页面

```
https://fivsevn.com/foodie/
```

- 方法：用 GitHub Actions 实现。[详见](https://github.com/fivsevn/fivsevn-assets/blob/main/README.md)


## 2. 视频

### 2.1 博客视频库

```text
https://youtube.com/@fivsevn
```

```text
https://youtube.com/@57store.fivsevn
```

### 2.2 引用方式

- 直接使用视频分享链接。

### 2.3 示例

#### 2.3.1 常规视频

- 直接生成分享链接

```text
https://youtu.be/l1IdOlvnx8U?si=IXnOSa4m6ibdkmMC
```

#### 2.3.2 短视频

- 视频直接生成的分享链接：

```text
https://youtube.com/shorts/64mxEOPAHLc?si=klHgAFeAo7mT-gFJ
```

- 替换成普通视频窗口链接：

```text
https://www.youtube.com/watch?v=64mxEOPAHLc
```

- 这样可以把 Shorts 短视频窗口转成普通 YouTube 视频窗口。

### 2.4 扩展

#### 2.4.1 自动更新

- 示例页面

```
https://fivsevn.com/motion/
```

- 方法：用 GitHub Actions 实现。[详见](https://github.com/fivsevn/fivsevn-assets/blob/main/README.md)


## 3. 特点

### 3.1 优点

- 免费

- 方便维护

  > 资源可以单独管理  
  > 如有需要、也方便迁移博客  

### 3.2 缺点

- CDN 可能有缓存，图片更新后不一定马上生效

- 平台限制

  > GitHub 不适合放太大的文件  
  > YouTube 视频受平台规则影响  

- 资源路径改了以后，博客里的链接也要同步改
