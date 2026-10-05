---
id: posts-toy-compare-001
title: 人形玩具比照
module: posts
submodule: reference
topic: humanoid-toy-comparison
type: note
status: active
canonical: true
summary: >
  以彩色标签比照具体人偶与人形玩具的连接方式、比例高度、交付形态、换装和材料；保留型号来源与展开说明。
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
updated: 2026-10-06
---

<link rel="stylesheet" href="{{ '/posts/2026/assets/toy-compare/toy-compare.css' | relative_url }}" />
<div id="toyCompare">
  <header class="tc-header">
    <div><h2>人形玩具比照</h2></div>
  </header>
  <div class="tc-tools">
    <label class="tc-search"
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
        id="tc-search"
        type="search"
        aria-label="搜索产品、厂商、作者或标签"
        placeholder="搜索产品、厂商、作者或标签…"
        autocomplete="off"
    /></label>
  </div>
  <div
    id="tc-brands"
    class="tc-brands"
    role="group"
    aria-label="厂商筛选"
  ></div>
  <div class="tc-results tc-sr-only">
    <span id="tc-count" role="status" aria-live="polite"></span>
  </div>
  <div id="tc-grid" class="tc-grid"></div>
  <div id="tc-empty" class="tc-empty" hidden>
    <h3>没有匹配的产品</h3>
    <p>试试切换厂商，或换一个关键词。</p>
    <button id="tc-empty-reset">清空筛选</button>
  </div>
  <div class="tc-more-wrap"><button id="tc-more" hidden>显示更多</button></div>
  <div id="tc-tray" class="tc-tray" hidden>
    <div id="tc-tray-products" class="tc-tray-products"></div>
    <button id="tc-clear">清空</button
    ><button id="tc-compare-open" class="tc-primary" disabled>产品对比</button>
  </div>
  <div class="tc-bottom">
    <details>
      <summary>玩具资源整理</summary>
      <div class="tc-resources" id="tc-resources"></div>
    </details>
    <details>
      <summary>标签怎么读</summary>
      <div id="tc-tag-defs" class="tc-tag-defs"></div>
    </details>
    <details>
      <summary>完整资料与记录口径</summary>
      <div>
        <p class="tc-muted">
          以具体型号和交付版本记录。厂商标称比例、实际高度、头身比各自保留；“未披露”不等于“没有”。跨品牌适配需有具体对象与限制。
        </p>
        <p class="tc-meta">
          本版整理：<span id="tc-date"></span
          >。尚未覆盖历年展会的全部产品；展会关联只在有对应证据时记录，社区链接也不作为热度排名。
        </p>
        <p class="tc-meta">
          <a id="tc-xlsx" href="{{ '/posts/2026/assets/toy-compare/toy-data.xlsx' | relative_url }}" download
            >下载完整资料表（Excel）</a
          >
          · <button id="tc-json">导出完整记录</button>
        </p>
        <div class="tc-raw-scroll">
          <table class="tc-raw-table">
            <thead>
              <tr>
                <th>品牌</th>
                <th>产品</th>
                <th>连接／可动</th>
                <th>尺寸口径</th>
                <th>产品来源</th>
              </tr>
            </thead>
            <tbody id="tc-raw"></tbody>
          </table>
        </div>
      </div>
    </details>
  </div>
  <dialog id="tc-detail" aria-labelledby="tc-detail-title">
    <div class="tc-dialog-head">
      <div>
        <small id="tc-detail-brand"></small>
        <h2 id="tc-detail-title"></h2>
      </div>
      <button class="tc-close" aria-label="关闭产品详情" data-close="tc-detail">
        ×
      </button>
    </div>
    <div class="tc-dialog-body" id="tc-detail-body"></div>
  </dialog>
  <dialog id="tc-compare-dialog" aria-labelledby="tc-compare-title">
    <div class="tc-dialog-head">
      <div>
        <h2 id="tc-compare-title">产品对比</h2>
        <small>六类横向比照，产品向下排列。</small>
      </div>
      <button
        class="tc-close"
        aria-label="关闭产品比照"
        data-close="tc-compare-dialog"
      >
        ×
      </button>
    </div>
    <div class="tc-dialog-body">
      <label class="tc-muted tc-diff-label"
        ><input id="tc-diff" type="checkbox" />只看不同之处</label
      >
      <div
        id="tc-compare-scroll"
        class="tc-compare-scroll"
        tabindex="0"
        aria-label="产品比照表，六类横向排列，产品向下阅读"
      >
        <div id="tc-compare" class="tc-compare"></div>
      </div>
      <p class="tc-meta" id="tc-compare-note"></p>
    </div>
  </dialog>
  <noscript
    ><p>
      开启 JavaScript 后可使用彩色标签与产品比照。完整资料也可从上方 Excel
      链接下载。
    </p></noscript
  >
</div>
<script src="{{ '/posts/2026/assets/toy-compare/toy-data.js' | relative_url }}"></script>
<script src="{{ '/posts/2026/assets/toy-compare/toy-compare.js' | relative_url }}"></script>
