---
id: posts-toy-reference-001
title: 玩具资料整理 · Toy Reference
layout: toy-post
module: posts
submodule: reference
topic: toy-reference
type: note
status: active
canonical: true
canonical_url: https://devlog.fivsevn.com/posts/2026/posts-toy-reference.html
lang: zh-CN
summary: >
  按对象类型与厂商浏览玩具资料，以彩色标签筛选和比照结构、比例尺寸、交付、换装与材料；保留具体型号、版本、来源和说明。
description: >
  按对象类型与厂商浏览玩具资料，以彩色标签筛选和比照结构、比例尺寸、交付、换装与材料；保留具体型号、版本、来源和说明。
parents: [posts-index]
related: []
tags: [posts, toys, dolls, comparison, reference]
audience: [public]
languages: [zh]
maturity: evolving
confidence: 0.8
visibility: public
source_of_truth: devlog
created: 2026-10-05
updated: 2026-10-07
---

<link rel="stylesheet" href="{{ '/posts/2026/assets/toy-reference/toy-reference.css' | relative_url }}?v=20261007-dialog-scroll" />
<div id="toyReference">
  <header class="tr-header">
    <div><h2>玩具资料整理</h2><p class="tr-english-title" lang="en">Toy Reference</p></div>
  </header>
  <div class="tr-tools">
    <label class="tr-search"
      ><svg
        viewBox="0 0 16 16"
        fill="currentColor"
        shape-rendering="crispEdges"
        aria-hidden="true"
      >
        <path
          d="M4 2h5v1H4zM2 4h1v5H2zM3 3h1v1H3zM9 3h1v1H9zM10 4h1v5h-1zM3 9h1v1H3zM4 10h5v1H4zM9 9h2v2H9zM11 11h2v2h-2zM13 13h2v2h-2z"
        /></svg
      ><input
        id="tr-search"
        type="search"
        aria-label="搜索产品、厂商、作者、年代或标签"
        placeholder="搜索产品、厂商、年代或标签…"
        autocomplete="off"
    /></label>
  </div>
  <details id="tr-type-filter" class="tr-filter-section" open>
    <summary>类型<span id="tr-type-current" class="tr-filter-current"></span></summary>
    <div id="tr-types" class="tr-types" role="group" aria-label="类型筛选"></div>
  </details>
  <details id="tr-brand-filter" class="tr-filter-section" open>
    <summary>厂商<span id="tr-brand-current" class="tr-filter-current"></span></summary>
    <div id="tr-brands" class="tr-brands" role="group" aria-label="厂商筛选"></div>
  </details>
  <details id="tr-tag-filter" class="tr-filter-section tr-tag-filter">
    <summary>标签<span id="tr-tag-filter-count"></span></summary>
    <div id="tr-tag-choices" class="tr-tag-choices"></div>
  </details>
  <div id="tr-active-filters" class="tr-active-filters" hidden>
    <div id="tr-active-tags" class="tr-active-tags"></div>
    <button id="tr-filter-reset">清空筛选</button>
  </div>
  <div class="tr-results tr-sr-only">
    <span id="tr-count" role="status" aria-live="polite"></span>
  </div>
  <div id="tr-grid" class="tr-grid"></div>
  <div id="tr-empty" class="tr-empty" hidden>
    <h3>没有匹配的产品</h3>
    <p>试试取消标签、切换厂商，或换一个关键词。</p>
    <button id="tr-empty-reset">清空筛选</button>
  </div>
  <div class="tr-more-wrap"><button id="tr-more" hidden>显示更多</button></div>
  <div id="tr-tray" class="tr-tray" hidden>
    <div id="tr-tray-products" class="tr-tray-products"></div>
    <button id="tr-clear">清空</button
    ><button id="tr-compare-open" class="tr-primary" disabled>产品对比</button>
  </div>
  <div class="tr-bottom">
    <details>
      <summary>延伸资料</summary>
      <div class="tr-resources" id="tr-resources"></div>
    </details>
    <details>
      <summary>标签说明</summary>
      <div id="tr-tag-defs" class="tr-tag-defs"></div>
    </details>
    <details>
      <summary>完整资料与记录口径</summary>
      <div>
        <p class="tr-muted">
          以具体型号和交付版本记录。厂商标称比例、实际尺寸、头身比各自保留；“未披露”不等于“没有”。跨品牌适配需有具体对象与限制。
        </p>
        <p class="tr-meta">
          年代按具体版本的发售、受注或生产年份记录；“年代待核实”表示尚缺可靠年份。“历史型号”不等于停产；“已停产”只用于官方明确停售的具体版本。二手与旧库存仍可能流通，复刻另记。
        </p>
        <p class="tr-meta">
          来源优先用官方产品页、厂商旧档案与作家作品页，其次为对应版本的商店或收藏记录；找不到可核对的资料时，才保留研究链接。
        </p>
        <p class="tr-meta">
          本版整理：<span id="tr-date"></span
          >。尚未覆盖历年展会的全部产品；展会关联只在有对应证据时记录，社区链接也不作为热度排名。
        </p>
        <p class="tr-meta">
          <a id="tr-xlsx" href="{{ '/posts/2026/assets/toy-reference/toy-data.xlsx' | relative_url }}" download="玩具资料整理.xlsx"
            >下载完整资料表（Excel）</a
          >
        </p>
      </div>
    </details>
  </div>
  <dialog id="tr-detail" aria-labelledby="tr-detail-title">
    <div class="tr-dialog-head">
      <div>
        <small id="tr-detail-brand"></small>
        <h2 id="tr-detail-title"></h2>
      </div>
      <button class="tr-close" aria-label="关闭产品详情" data-close="tr-detail">
        ×
      </button>
    </div>
    <div class="tr-dialog-body" id="tr-detail-body"></div>
  </dialog>
  <dialog id="tr-compare-dialog" aria-labelledby="tr-compare-title">
    <div class="tr-dialog-head">
      <div>
        <h2 id="tr-compare-title">产品对比</h2>
        <small>六类横向比照，产品向下排列。</small>
      </div>
      <button
        class="tr-close"
        aria-label="关闭产品比照"
        data-close="tr-compare-dialog"
      >
        ×
      </button>
    </div>
    <div class="tr-dialog-body">
      <label class="tr-muted tr-diff-label"
        ><input id="tr-diff" type="checkbox" />只看不同之处</label
      >
      <div
        id="tr-compare-scroll"
        class="tr-compare-scroll"
        tabindex="0"
        aria-label="产品比照表，六类横向排列，产品向下阅读"
      >
        <div id="tr-compare" class="tr-compare"></div>
      </div>
      <p class="tr-meta" id="tr-compare-note"></p>
    </div>
  </dialog>
  <noscript
    ><p>
      开启 JavaScript 后可使用彩色标签与产品比照。完整资料也可从上方 Excel
      链接下载。
    </p></noscript
  >
</div>
<script defer src="{{ '/posts/2026/assets/toy-reference/toy-data.js' | relative_url }}?v=20261007-reference"></script>
<script defer src="{{ '/posts/2026/assets/toy-reference/toy-browse.js' | relative_url }}?v=20261007-reference"></script>
<script defer src="{{ '/posts/2026/assets/toy-reference/toy-reference.js' | relative_url }}?v=20261007-dialog-scroll"></script>
