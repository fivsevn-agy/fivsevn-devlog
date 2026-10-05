(() => {
  "use strict";
  const root = document.getElementById("toyCompare"),
    db = window.TOY_COMPARE_DATA,
    $ = (id) => document.getElementById(id);
  if (!db) {
    $("tc-empty").hidden = false;
    $("tc-empty").querySelector("h3").textContent = "资料未载入";
    $("tc-empty").querySelector("p").textContent =
      "请检查文章专用资料文件是否上传完整。";
    $("tc-empty-reset").hidden = true;
    $("tc-more").hidden = true;
    $("tc-search").disabled = true;
    $("tc-json").disabled = true;
    return;
  }
  const PAGE_SIZE = 24;
  const checked = (p) =>
    db.checkDates?.[p.id] || db.previousCheckDate || db.date;
  const byId = new Map(db.products.map((p) => [p.id, p]));
  const cats = db.categories,
    products = db.products,
    selected = new Set();
  let activeBrand = "",
    visibleLimit = PAGE_SIZE,
    activeId = null,
    lastFocus;
  const esc = (v) =>
    String(v ?? "").replace(
      /[&<>"']/g,
      (c) =>
        ({
          "&": "&amp;",
          "<": "&lt;",
          ">": "&gt;",
          '"': "&quot;",
          "'": "&#39;",
        })[c],
    );
  // Pixel marks are tag icons; product thumbnails use separate small line drawings.
  const pixel = (rows) =>
    `<svg viewBox="0 0 ${Math.max(...rows.map((r) => r.length))} ${rows.length}" fill="currentColor" shape-rendering="crispEdges" aria-hidden="true">${rows.flatMap((r, y) => [...r].map((c, x) => (c === "." ? "" : `<rect x="${x}" y="${y}" width="1" height="1"${c === "+" ? ' opacity=".35"' : c === "o" ? ' opacity=".6"' : ""}/>`))).join("")}</svg>`;
  const icons = {
    joint: pixel([
      "................",
      "..##............",
      ".####...........",
      "##..##..........",
      "##..##..........",
      ".####...........",
      "..####..........",
      ".....###........",
      "......####......",
      ".......####.....",
      "........#..#....",
      "........#..#....",
      "........####....",
      ".........##.....",
      "................",
      "................",
    ]),
    size: pixel([
      "................",
      "..#....########.",
      ".###...#..#...#.",
      "..#....#..#...#.",
      "..#....#......#.",
      "..#....#..#...#.",
      "..#....#..#...#.",
      "..#....#......#.",
      "..#....#..#...#.",
      "..#....#..#...#.",
      "..#....#......#.",
      "..#....#..#...#.",
      ".###...#..#...#.",
      "..#....########.",
      "................",
      "................",
    ]),
    delivery: pixel([
      "................",
      ".......##.......",
      ".....##oo##.....",
      "...##oooooo##...",
      ".##oooo##oooo##.",
      ".###o##oo##o###.",
      ".#..###++###..#.",
      ".#....####....#.",
      ".#.....##.....#.",
      ".#.....##.....#.",
      ".#.....##.....#.",
      "..##...##...##..",
      "....##.##.##....",
      "......####......",
      ".......##.......",
      "................",
    ]),
    dress: pixel([
      "................",
      "...###....###...",
      "..##o######o##..",
      ".##ooo####ooo##.",
      "##ooooo++ooooo##",
      "##ooo++++++ooo##",
      ".###o++++++o###.",
      "...#o++++++o#...",
      "...#o++++++o#...",
      "...#o++++++o#...",
      "...#o++++++o#...",
      "...#o++++++o#...",
      "...#o++++++o#...",
      "...##########...",
      "................",
      "................",
    ]),
    material: pixel([
      "................",
      ".......##.......",
      ".....######.....",
      "...##########...",
      ".##############.",
      "...##########...",
      ".....######.....",
      ".#.....##.....#.",
      "...##......##...",
      ".....######.....",
      ".......##.......",
      ".#............#.",
      "...##......##...",
      ".....######.....",
      ".......##.......",
      "................",
    ]),
    role: pixel([
      "......####......",
      ".....######.....",
      ".....######.....",
      "......####......",
      ".......##.......",
      "....########....",
      "...##########...",
      "..###.####.###..",
      "..##..####..##..",
      "..##..####..##..",
      "......####......",
      "......####......",
      ".....##..##.....",
      ".....##..##.....",
      "....###..###....",
      "....###..###....",
    ]),
  };
  function glyph(p) {
    const svg = (body) =>
      `<svg viewBox="0 0 48 60" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${body}</svg>`;
    if (p.icon === "outfit")
      return svg(
        '<path d="m15 14-9 5 4 10 5-3v18h18V26l5 3 4-10-9-5c-3 6-15 6-18 0Z"/>',
      );
    if (p.icon === "kit")
      return svg(
        '<rect x="9" y="9" width="30" height="42"/><path d="M24 9v42M9 36h30M17 9v8M28 36v6"/><circle cx="17" cy="21" r="4"/><path d="M28 17h6v13h-6zM15 42h5v4h-5"/>',
      );
    const movable = p.tags.joint.some((t) =>
      /可动|拉筋|骨架|球体|球窝|关节/.test(t),
    );
    return svg(
      `<circle cx="24" cy="12" r="5"/><path d="M24 19v18M15 29l9-8 9 8M24 37l-7 14m7-14 7 14"${movable ? ' stroke-width="2.2" stroke-dasharray="5 3.5"' : ""}/>`,
    );
  }
  function sizeTags(p) {
    if (p.sizeNA)
      return [{ cat: "size", text: "人形尺寸不适用", variant: "unknown" }];
    return [
      {
        cat: "size",
        text: p.scale || "比例未披露",
        variant: p.scale ? "scale" : "unknown",
      },
      ...(p.dimensions.length
        ? p.dimensions.map((d) => ({
            cat: "size",
            text: d.label,
            variant: "height",
          }))
        : [{ cat: "size", text: "高度未披露", variant: "unknown" }]),
    ];
  }
  function allTags(p) {
    return cats.flatMap((c) =>
      c.id === "size"
        ? sizeTags(p)
        : p.tags[c.id].map((t) => ({ cat: c.id, text: t })),
    );
  }
  function chip(t) {
    return `<span class="tc-chip${t.variant === "unknown" ? " tc-unknown" : ""}" data-category="${t.cat}"${t.variant === "scale" ? ' data-variant="scale"' : ""}>${icons[t.cat]}${esc(t.text)}</span>`;
  }
  function matches(p) {
    const q = $("tc-search").value.trim().toLocaleLowerCase(),
      terms = q.split(/\s+/).filter(Boolean),
      all = [
        p.name,
        p.brand,
        p.original,
        p.country,
        ...allTags(p).map((t) => t.text),
      ]
        .join(" ")
        .toLocaleLowerCase();
    return (
      terms.every((t) => all.includes(t)) &&
      (!activeBrand || p.brand === activeBrand)
    );
  }
  function render() {
    const shown = products.filter((p) => matches(p));
    $("tc-count").textContent = `${shown.length} / ${products.length} 件产品`;
    $("tc-empty").hidden = shown.length > 0;
    renderBrands();
    $("tc-more").hidden = shown.length <= visibleLimit;
    $("tc-more").textContent = "显示更多";
    $("tc-grid").innerHTML = shown
      .slice(0, visibleLimit)
      .map((p) => {
        const main = [
          { cat: "joint", text: p.tags.joint[0] || "不适用" },
          { cat: "delivery", text: p.tags.delivery[0] },
          ...(p.tags.delivery.includes("计划商品")
            ? [{ cat: "delivery", text: "计划商品" }]
            : []),
          ...(p.scale
            ? [{ cat: "size", text: p.scale, variant: "scale" }]
            : []),
          ...p.dimensions
            .slice(0, 1)
            .map((d) => ({ cat: "size", text: d.label, variant: "height" })),
        ];
        if (p.tags.dress[0]) main.push({ cat: "dress", text: p.tags.dress[0] });
        return `<article class="tc-card${selected.has(p.id) ? " tc-selected" : ""}"><div class="tc-card-head"><div class="tc-glyph" data-category="${p.icon === "kit" ? "delivery" : p.icon === "outfit" ? "dress" : "joint"}" aria-hidden="true">${glyph(p)}</div><div><div class="tc-brand">${esc(p.brand)}</div><button class="tc-name" data-view="${p.id}">${esc(p.name)}</button></div></div><div class="tc-card-tags">${main.map(chip).join("")}</div><div class="tc-card-actions"><button data-view="${p.id}"><span class="tc-action-arrow tc-site-triangle" aria-hidden="true"></span>详细</button><button data-select="${p.id}" aria-label="${selected.has(p.id) ? "移出" : "加入"}比照：${esc(p.name)}" aria-pressed="${selected.has(p.id)}"><span class="tc-action-arrow tc-action-plus" aria-hidden="true">${selected.has(p.id) ? "−" : "+"}</span>对比</button></div></article>`;
      })
      .join("");
    renderTray();
  }
  function renderTray() {
    $("tc-tray").hidden = selected.size === 0;
    $("tc-tray-products").innerHTML = [...selected]
      .map((id) => {
        const p = byId.get(id);
        return `<button data-select="${id}" aria-label="移出比照：${esc(p.name)}"><span>${esc(p.name)}</span> ×</button>`;
      })
      .join("");
    $("tc-compare-open").disabled = selected.size < 2;
    $("tc-compare-open").textContent = `对比 (${selected.size})`;
  }
  function toggle(id) {
    const inDetail = $("tc-detail").open,
      focus = document.activeElement,
      fromGrid = $("tc-grid").contains(focus),
      fromTray = $("tc-tray").contains(focus);
    if (selected.has(id)) selected.delete(id);
    else {
      selected.add(id);
    }
    render();
    if (inDetail && activeId === id) {
      const b = $("tc-detail-body").querySelector("[data-select]");
      b.innerHTML = selectLabel(id);
      b.setAttribute("aria-pressed", String(selected.has(id)));
    } else if (fromGrid) {
      root
        .querySelector(`#tc-grid [data-select="${id}"]`)
        ?.focus({ preventScroll: true });
    } else if (fromTray) {
      const next =
        $("tc-tray-products").querySelector("button") || $("tc-search");
      next.focus({ preventScroll: true });
    }
  }
  function openDialog(id, returnFocus) {
    lastFocus = returnFocus || document.activeElement;
    $(id).showModal();
    $(id).scrollTop = 0;
    $(id).querySelector(".tc-close").focus({ preventScroll: true });
  }
  function restoreFocus() {
    const f = lastFocus?.isConnected
      ? lastFocus
      : lastFocus?.dataset?.view
        ? root.querySelector(
            `#tc-grid .tc-name[data-view="${lastFocus.dataset.view}"]`,
          )
        : lastFocus?.dataset?.select
          ? root.querySelector(
              `#tc-grid [data-select="${lastFocus.dataset.select}"]`,
            )
          : null;
    f?.focus({ preventScroll: true });
  }
  function closeDialog(id) {
    $(id).close();
    restoreFocus();
  }
  function notes(p) {
    return `<dl class="tc-note-list">${p.notes.map((n) => `<div><dt>${esc(n.title)}</dt><dd>${esc(n.text)}</dd></div>`).join("")}<div><dt>品牌与产地</dt><dd>${esc(p.brand)} · 品牌所在地：${esc(p.country)}；商品标示产地：${esc(p.origin)}。</dd></div><div><dt>记录版本</dt><dd>${esc(p.original)}。${esc(p.version)} 核对日期：${checked(p)}。</dd></div></dl>`;
  }
  function selectLabel(id) {
    return `<span class="tc-action-arrow tc-action-plus" aria-hidden="true">${selected.has(id) ? "−" : "+"}</span>${selected.has(id) ? "取消对比" : "对比"}`;
  }
  function fillDetail(id) {
    const p = byId.get(id);
    activeId = id;
    $("tc-detail-brand").textContent = p.brand;
    $("tc-detail-title").textContent = p.name;
    $("tc-detail-body").innerHTML = `<div class="tc-facts">${cats
      .map((c) => {
        const ts = allTags(p).filter((t) => t.cat === c.id);
        return `<div class="tc-fact"><div class="tc-fact-label" data-category="${c.id}"><i class="tc-dot"></i>${esc(c.name)}</div><div class="tc-tags">${ts.length ? ts.map(chip).join("") : '<span class="tc-muted">未披露</span>'}</div></div>`;
      })
      .join(
        "",
      )}</div><div class="tc-detail-actions"><button class="tc-primary" data-select="${id}" aria-pressed="${selected.has(id)}">${selectLabel(id)}</button><a href="${esc(p.sources[0].url)}" target="_blank" rel="noopener noreferrer">${esc(p.sources[0].kind)}</a></div><details><summary>展开说明与适配限制</summary><div>${notes(p)}</div></details><details><summary>产品来源与展会记录 (${p.sources.length})</summary><div>${p.sources.map((s) => `<div class="tc-source"><a href="${esc(s.url)}" target="_blank" rel="noopener noreferrer">${esc(s.title)}</a><p>${esc(s.kind)} · ${esc(s.supports)}</p></div>`).join("")}<p class="tc-meta">${esc(p.event || "尚未取得这件产品对应的展会证据。")}</p></div></details>`;
  }
  function showDetail(id) {
    fillDetail(id);
    const fromCompare = $("tc-compare-dialog").open;
    if (fromCompare) $("tc-compare-dialog").close();
    openDialog("tc-detail", fromCompare ? $("tc-compare-open") : null);
  }
  function compare() {
    const ps = [...selected].map((id) => byId.get(id));
    const visibleCats = cats.filter((c) => {
      if (!$("tc-diff").checked) return true;
      const sets = ps.map((p) =>
        allTags(p)
          .filter((t) => t.cat === c.id)
          .map((t) => t.text)
          .sort(),
      );
      return sets.some((ts) => JSON.stringify(ts) !== JSON.stringify(sets[0]));
    });
    $("tc-compare").innerHTML = visibleCats.length
      ? ps
          .map(
            (p) =>
              `<article class="tc-compare-product"><div class="tc-compare-product-head"><div class="tc-glyph" data-category="joint">${glyph(p)}</div><div><div class="tc-brand">${esc(p.brand)}</div><h3>${esc(p.name)}</h3></div><button data-view="${p.id}">详情与来源</button></div><div class="tc-facts">${visibleCats
                .map((c) => {
                  const ts = allTags(p).filter((t) => t.cat === c.id);
                  return `<div class="tc-fact"><div class="tc-fact-label" data-category="${c.id}"><i class="tc-dot"></i>${esc(c.name)}</div><div><div class="tc-tags">${ts.length ? ts.map(chip).join("") : '<span class="tc-muted">未披露</span>'}</div>${c.id === "size" && p.heightMm ? `<div class="tc-size-line"><div class="tc-size-bar" style="height:${(p.heightMm / 1000) * 85}px"></div><span>${p.heightMm / 10} cm</span></div><p class="tc-meta">${esc(p.heightBasis)}</p>` : ""}</div></div>`;
                })
                .join("")}</div></article>`,
          )
          .join("")
      : '<p class="tc-muted">这些类别的标签相同。取消“只看不同之处”可查看全部。</p>';
    $("tc-compare-note").textContent = visibleCats.length
      ? "高度图按 100 cm 为同一基准绘制；各产品是否含头或底座，见图下口径。比例按厂商标注保留，不用于推算身高。"
      : "";
  }
  function refresh() {
    visibleLimit = PAGE_SIZE;
    render();
  }
  function reset() {
    $("tc-search").value = "";
    activeBrand = "";
    refresh();
  }
  const brands = [...new Set(products.map((p) => p.brand))].sort();
  function renderBrands() {
    $("tc-brands").innerHTML = ["", ...brands]
      .map(
        (b) =>
          `<button class="tc-brand-choice" data-brand="${esc(b)}" aria-pressed="${activeBrand === b}">${esc(b || "全部厂商")}</button>`,
      )
      .join("");
  }
  $("tc-resources").innerHTML = [
    "综合资料库",
    "评测与资讯",
    "人偶社区",
    "厂商结构与目录",
  ]
    .map(
      (group) =>
        `<h3 class="tc-resource-group">${esc(group)}</h3>${db.resources
          .filter((r) => r.group === group)
          .map(
            (r) =>
              `<div class="tc-resource"><a href="${esc(r.url)}" target="_blank" rel="noopener noreferrer">${esc(r.name)}</a><p>${esc(r.description)}</p></div>`,
          )
          .join("")}`,
    )
    .join("");
  $("tc-tag-defs").innerHTML =
    cats
      .map(
        (c) =>
          `<div><span class="tc-chip" data-category="${c.id}">${icons[c.id]}${esc(c.name)}</span><p>${esc(c.description)}</p></div>`,
      )
      .join("") +
    "<p>卡片上的人形、骨架、板件和衣服图形表示结构或商品组成，不是产品实物照片。</p>";
  $("tc-raw").innerHTML = products
    .map(
      (p) =>
        `<tr><td>${esc(p.brand)}</td><td>${esc(p.name)}</td><td>${esc(p.tags.joint.join("、") || "不适用")}</td><td>${esc(p.sizeNA ? "不适用" : p.dimensions.map((d) => d.label + "（" + d.basis + "）").join("；") || "未披露")}</td><td><a href="${esc(p.sources[0].url)}" target="_blank" rel="noopener noreferrer">${esc(p.sources[0].kind)}</a></td></tr>`,
    )
    .join("");
  root.addEventListener("click", (e) => {
    const b = e.target.closest("button");
    if (!b) return;
    if (b.dataset.view) showDetail(b.dataset.view);
    if (b.dataset.select) toggle(b.dataset.select);
    if (b.dataset.close) closeDialog(b.dataset.close);
    if (b.hasAttribute("data-brand")) {
      activeBrand = b.dataset.brand;
      refresh();
      [...$("tc-brands").querySelectorAll("button")]
        .find((x) => x.dataset.brand === activeBrand)
        ?.focus({ preventScroll: true });
    }
  });
  $("tc-search").addEventListener("input", refresh);
  $("tc-more").addEventListener("click", () => {
    visibleLimit += PAGE_SIZE;
    render();
  });
  $("tc-empty-reset").addEventListener("click", reset);
  $("tc-clear").addEventListener("click", () => {
    selected.clear();
    render();
    $("tc-search").focus({ preventScroll: true });
  });
  $("tc-compare-open").addEventListener("click", () => {
    compare();
    openDialog("tc-compare-dialog");
  });
  $("tc-diff").addEventListener("change", compare);
  root.querySelectorAll("dialog").forEach((d) => {
    d.addEventListener("click", (e) => {
      if (e.target === d) {
        const r = d.getBoundingClientRect();
        if (
          e.clientX < r.left ||
          e.clientX > r.right ||
          e.clientY < r.top ||
          e.clientY > r.bottom
        )
          closeDialog(d.id);
      }
    });
    d.addEventListener("cancel", (e) => {
      e.preventDefault();
      closeDialog(d.id);
    });
  });
  $("tc-json").addEventListener("click", () => {
    const u = URL.createObjectURL(
      new Blob([JSON.stringify(db, null, 2)], { type: "application/json" }),
    );
    const a = document.createElement("a");
    a.href = u;
    a.download = "人形玩具比照-完整记录.json";
    a.hidden = true;
    root.append(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(u), 1000);
  });
  $("tc-date").textContent = db.date;
  render();
})();
