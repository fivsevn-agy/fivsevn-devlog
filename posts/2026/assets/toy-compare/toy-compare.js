(() => {
  "use strict";
  const root = document.getElementById("toyCompare");
  if (!root) return;
  const db = window.TOY_COMPARE_DATA,
    browse = window.TOY_COMPARE_BROWSE,
    $ = (id) => root.querySelector(`#${id}`);
  if (!db || !browse) {
    $("tc-empty").hidden = false;
    $("tc-empty").querySelector("h3").textContent = "资料未载入";
    $("tc-empty").querySelector("p").textContent =
      "请刷新页面重试，或展开下方“完整资料与记录口径”下载资料表。";
    $("tc-count").textContent = "资料未载入";
    $("tc-empty-reset").hidden = true;
    $("tc-more").hidden = true;
    $("tc-search").disabled = true;
    root.querySelectorAll(".tc-filter-section").forEach((d) => { d.hidden = true; });
    return;
  }
  const PAGE_SIZE = 24;
  const checked = (p) =>
    db.checkDates?.[p.id] || db.previousCheckDate || db.date;
  const byId = new Map(db.products.map((p) => [p.id, p]));
  const cats = db.categories.map((c) => ({
      ...c,
      name: c.id === "role" ? "对象／品类" : c.id === "size" ? "比例／尺寸" : c.name,
    })),
    products = db.products,
    selected = new Set(),
    activeTags = new Set();
  const types = browse.types;
  const memberships = new Map(products.map((p) => [
    p.id, new Set(browse?.products[p.id] || ["human"]),
  ]));
  let activeType = "human",
    activeBrand = "",
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
  const unavailable = (s) =>
    s.availability?.state === "temporarily-unavailable";
  const sourceLink = (s, label = s.title || s.name) =>
    unavailable(s)
      ? `<span class="tc-muted" title="${esc(s.url)}">${esc(label)}（暂不可用）</span>`
      : `<a href="${esc(s.url)}" target="_blank" rel="noopener noreferrer">${esc(label)}</a>`;
  const sourceStatus = (s) =>
    unavailable(s)
      ? `<p class="tc-meta">${esc(s.availability.reason)} 核对：${esc(s.availability.checkedAt)}。</p>`
      : "";
  const primarySource = (p) =>
    p.sources.find((s) => !unavailable(s) && !/研究|学术论文/.test(s.kind)) ||
    p.sources.find((s) => !unavailable(s)) || p.sources[0];
  const eraLabel = (p) => p.chronology?.label || "年代待核实";
  const historyLabel = (p) => p.lifecycle?.historical
    ? (p.lifecycle.discontinued ? "历史型号 · 已停产" : "历史型号") : "";
  const chronologyLine = (p) => `<div class="tc-era">${esc(eraLabel(p))}${historyLabel(p) ? `<span class="tc-history">${esc(historyLabel(p))}</span>` : ""}</div>`;
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
    if (p.icon === "machine")
      return svg(
        '<rect x="13" y="12" width="22" height="14" rx="2"/><circle cx="20" cy="19" r="2"/><path d="M28 17v4M24 26v5M12 32h24v12H12zM16 44v6m16-6v6M8 34v8m32-8v8"/>',
      );
    if (p.icon === "vehicle")
      return svg('<path d="M8 31h32v12H8zM13 31l4-12h14l5 12M21 19v12m-9 0h24"/><circle cx="15" cy="45" r="4"/><circle cx="33" cy="45" r="4"/>');
    if (p.icon === "animal")
      return svg('<path d="M13 18l-3-8 10 5m8 0 10-5-3 8M13 18c0-8 22-8 22 0v8c0 10-22 10-22 0zM17 35l-5 13m19-13 5 13M17 35h14v15H17z"/><circle cx="19" cy="23" r="1"/><circle cx="29" cy="23" r="1"/><path d="M22 29h4"/>');
    if (p.icon === "props")
      return svg('<path d="M9 27h30v6H9zM13 33v18m22-18v18M18 27V12h12v15M18 17h12m-7 0v10"/>');
    const movable = p.tags.joint.some((t) =>
      /可动|拉筋|骨架|球体|球窝|关节/.test(t),
    );
    return svg(
      `<circle cx="24" cy="12" r="5"/><path d="M24 19v18M15 29l9-8 9 8M24 37l-7 14m7-14 7 14"${movable ? ' stroke-width="2.2" stroke-dasharray="5 3.5"' : ""}/>`,
    );
  }
  function scaleLabel(value) {
    const ratio = value?.match(/^(?:比例\s*)?(\d+(?:\.\d+)?)\s*[:：]\s*(\d+(?:\.\d+)?)$/);
    return ratio ? `比例 ${ratio[1]}:${ratio[2]}` : value;
  }
  function sizeTags(p) {
    if (p.sizeNA)
      return [{ cat: "size", text: "尺寸不适用", variant: "unknown" }];
    return [
      {
        cat: "size",
        text: scaleLabel(p.scale) || "比例未披露",
        variant: p.scale ? "scale" : "unknown",
      },
      ...(p.dimensions.length
        ? p.dimensions.map((d) => ({
            cat: "size",
            text: d.label,
            variant: "height",
          }))
        : [{ cat: "size", text: "尺寸未披露", variant: "unknown" }]),
    ];
  }
  function allTags(p) {
    return cats.flatMap((c) =>
      c.id === "size"
        ? sizeTags(p)
        : p.tags[c.id].map((t) => ({ cat: c.id, text: normalizedTag(c.id, t) })),
    );
  }
  function normalizedTag(cat, text) {
    const aliases = cat === "material" ? {
      ABS树脂: "ABS", POM树脂: "POM", PS树脂: "PS",
      塑料: "塑料（未细分）",
    } : {};
    return aliases[text] || text;
  }
  const tagKey = (t) => `${t.cat}:${t.text}`;
  const productTags = new Map(products.map((p) => [p.id, allTags(p)]));
  const productTagKeys = new Map(products.map((p) => [
    p.id, new Set(productTags.get(p.id).map(tagKey)),
  ]));
  const searchable = new Map(products.map((p) => [p.id, [
    p.name, p.brand, p.original, p.country, eraLabel(p), historyLabel(p),
    ...(p.aliases || []), ...(p.credits || []).map((c) => c.name),
    ...productTags.get(p.id).map((t) => t.text),
    ...Object.values(p.tags).flat(),
  ].join(" ").toLocaleLowerCase()]));
  const vocabulary = new Map();
  products.forEach((p) => {
    productTags.get(p.id).forEach((t) => {
      const key = tagKey(t);
      if (!vocabulary.has(key)) vocabulary.set(key, { ...t, count: 0 });
      vocabulary.get(key).count++;
    });
  });
  const matchesType = (p) => activeType === "all" || memberships.get(p.id).has(activeType);
  function chip(t) {
    return `<span class="tc-chip${t.variant === "unknown" ? " tc-unknown" : ""}" data-category="${t.cat}"${t.variant === "scale" ? ' data-variant="scale"' : ""}>${icons[t.cat]}${esc(t.text)}</span>`;
  }
  function matches(p, terms) {
    return matchesType(p) && (!activeBrand || p.brand === activeBrand) &&
      terms.every((t) => searchable.get(p.id).includes(t)) &&
      [...activeTags].every((key) => productTagKeys.get(p.id).has(key));
  }
  function render() {
    const terms = $("tc-search").value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    const shown = products.filter((p) => matches(p, terms));
    $("tc-count").textContent = `${shown.length} / ${products.length} 件产品`;
    $("tc-empty").hidden = shown.length > 0;
    renderTypes();
    renderBrands();
    renderTagFilters();
    const typeIsEmpty = !products.some(matchesType);
    $("tc-empty").querySelector("h3").textContent = typeIsEmpty ? "这个类型尚待整理" : "没有匹配的产品";
    $("tc-empty").querySelector("p").textContent = typeIsEmpty
      ? "已预留分类位置，之后逐步补充。"
      : "试试取消标签、切换厂商，或换一个关键词。";
    $("tc-more").hidden = shown.length <= visibleLimit;
    $("tc-more").textContent = "显示更多";
    $("tc-grid").innerHTML = shown
      .slice(0, visibleLimit)
      .map((p) => {
        const main = [
          ...productTags.get(p.id).filter((t) => t.cat === "joint").slice(0, 1),
          ...productTags.get(p.id).filter((t) => t.variant === "scale"),
          ...p.dimensions
            .slice(0, 1)
            .map((d) => ({ cat: "size", text: d.label, variant: "height" })),
          ...productTags.get(p.id).filter((t) => t.cat === "delivery" && t.text !== "计划商品").slice(0, 1),
        ];
        if (p.tags.dress[0]) main.push({ cat: "dress", text: p.tags.dress[0] });
        const material = productTags.get(p.id).find((t) => t.cat === "material" && !/未披露|未说明/.test(t.text));
        if (material) main.push(material);
        const role = productTags.get(p.id).find((t) => t.cat === "role");
        if (role) main.push(role);
        if (p.tags.delivery.includes("计划商品")) main.push({ cat: "delivery", text: "计划商品" });
        activeTags.forEach((key) => {
          const t = vocabulary.get(key);
          if (!main.some((m) => tagKey(m) === key)) main.push(t);
        });
        return `<article class="tc-card${selected.has(p.id) ? " tc-selected" : ""}"><div class="tc-card-head"><div class="tc-glyph" data-category="${p.icon === "kit" ? "delivery" : p.icon === "outfit" ? "dress" : "joint"}" aria-hidden="true">${glyph(p)}</div><div><div class="tc-brand">${esc(p.brand)}</div><button class="tc-name" data-view="${p.id}">${esc(p.name)}</button>${chronologyLine(p)}</div></div><div class="tc-card-tags">${main.map(chip).join("")}</div><div class="tc-card-actions"><button data-view="${p.id}"><span class="tc-action-arrow tc-site-triangle" aria-hidden="true"></span>详细</button><button data-select="${p.id}" aria-label="${selected.has(p.id) ? "移出" : "加入"}比照：${esc(p.name)}" aria-pressed="${selected.has(p.id)}"><span class="tc-action-arrow tc-action-plus" aria-hidden="true">${selected.has(p.id) ? "−" : "+"}</span>对比</button></div></article>`;
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
    const credits = p.credits?.length
      ? `<div><dt>作者与制作署名</dt><dd>${p.credits.map((c) => `${esc(c.role)}：${esc(c.name)}`).join("<br>")}</dd></div>`
      : "";
    const aliases = p.aliases?.length
      ? `<div><dt>常见叫法</dt><dd>${esc(p.aliases.join("、"))}</dd></div>`
      : "";
    return `<dl class="tc-note-list">${credits}${aliases}${p.notes.map((n) => `<div><dt>${esc(n.title)}</dt><dd>${esc(n.text)}</dd></div>`).join("")}<div><dt>品牌与产地</dt><dd>${esc(p.brand)} · 品牌所在地：${esc(p.country)}；商品标示产地：${esc(p.origin)}。</dd></div><div><dt>记录版本</dt><dd>${esc(p.original)}。${esc(p.version)} 核对日期：${checked(p)}。</dd></div></dl>`;
  }
  function selectLabel(id) {
    return `<span class="tc-action-arrow tc-action-plus" aria-hidden="true">${selected.has(id) ? "−" : "+"}</span>${selected.has(id) ? "取消对比" : "对比"}`;
  }
  function fillDetail(id) {
    const p = byId.get(id);
    activeId = id;
    $("tc-detail-brand").textContent = p.brand;
    $("tc-detail-title").textContent = p.name;
    $("tc-detail-body").innerHTML = `<div class="tc-detail-era">${chronologyLine(p)}<p>${esc(p.lifecycle?.note || p.chronology?.note || "")}</p></div><div class="tc-facts">${cats
      .map((c) => {
        const ts = allTags(p).filter((t) => t.cat === c.id);
        return `<div class="tc-fact"><div class="tc-fact-label" data-category="${c.id}"><i class="tc-dot"></i>${esc(c.name)}</div><div class="tc-tags">${ts.length ? ts.map(chip).join("") : '<span class="tc-muted">未披露</span>'}</div></div>`;
      })
      .join(
        "",
      )}</div><div class="tc-detail-actions"><button class="tc-primary" data-select="${id}" aria-pressed="${selected.has(id)}">${selectLabel(id)}</button>${sourceLink(primarySource(p), primarySource(p).kind)}</div><details><summary>展开说明与适配限制</summary><div>${notes(p)}</div></details><details><summary>产品来源与展会记录 (${p.sources.length})</summary><div>${p.sources.map((s) => `<div class="tc-source">${sourceLink(s)}<p>${esc(s.kind)} · ${esc(s.supports)}</p>${sourceStatus(s)}</div>`).join("")}<p class="tc-meta">${esc(p.event || "尚未取得这件产品对应的展会证据。")}</p></div></details>`;
  }
  function showDetail(id) {
    fillDetail(id);
    const fromCompare = $("tc-compare-dialog").open;
    if (fromCompare) $("tc-compare-dialog").close();
    openDialog("tc-detail", fromCompare ? $("tc-compare-open") : null);
  }
  function compare() {
    const rows = [...selected].map((id) => {
      const product = byId.get(id);
      return { product, tags: allTags(product) };
    });
    const visibleCats = cats.filter((c) => {
      if (!$("tc-diff").checked) return true;
      const sets = rows.map((row) =>
        row.tags
          .filter((t) => t.cat === c.id)
          .map((t) => t.text)
          .sort(),
      );
      return sets.some((ts) => JSON.stringify(ts) !== JSON.stringify(sets[0]));
    });
    $("tc-compare").innerHTML = visibleCats.length
      ? `<table class="tc-compare-table" style="--tc-compare-columns:${visibleCats.length}">
          <caption class="tc-sr-only">所选产品的分类标签比照</caption>
          <colgroup><col class="tc-compare-name-col" /><col span="${visibleCats.length}" /></colgroup>
          <thead><tr><th scope="col">产品</th>${visibleCats.map((c) => `<th scope="col">${esc(c.name)}</th>`).join("")}</tr></thead>
          <tbody>${rows
            .map(
              ({ product: p, tags }) => `<tr>
            <th scope="row"><div class="tc-compare-identity"><div class="tc-glyph">${glyph(p)}</div><div><span class="tc-brand">${esc(p.brand)}</span><h3 class="tc-compare-product-name">${esc(p.name)}</h3>${chronologyLine(p)}</div></div><button class="tc-compare-detail" data-view="${esc(p.id)}">详情与来源</button></th>
            ${visibleCats
              .map((c) => {
                const ts = tags.filter((t) => t.cat === c.id);
                const basis =
                  c.id === "size" && p.heightMm
                    ? `<p class="tc-compare-basis">${esc(p.heightBasis)}</p>`
                    : "";
                return `<td><div class="tc-tags">${ts.length ? ts.map(chip).join("") : '<span class="tc-muted">未披露</span>'}</div>${basis}</td>`;
              })
              .join("")}
          </tr>`,
            )
            .join("")}</tbody>
        </table>`
      : '<p class="tc-muted">这些类别的标签相同。取消“只看不同之处”可查看全部。</p>';
    $("tc-compare-note").textContent = visibleCats.length
      ? "尺寸口径与适配限制见“详情与来源”；“未披露”不等于“没有”。"
      : "";
  }
  function refresh() {
    visibleLimit = PAGE_SIZE;
    render();
  }
  function reset() {
    $("tc-search").value = "";
    activeType = "all";
    activeBrand = "";
    activeTags.clear();
    refresh();
  }
  function renderTypes() {
    $("tc-types").innerHTML = [{ id: "all", name: "全部类型" }, ...types].map((t) => {
      const pending = t.id !== "all" && !products.some((p) => memberships.get(p.id).has(t.id));
      return `<button class="tc-type-choice" data-type="${t.id}" aria-pressed="${activeType === t.id}">${esc(t.name)}${pending ? " · 待整理" : ""}</button>`;
    }).join("");
    $("tc-type-current").textContent = activeType === "all" ? "全部类型" : types.find((t) => t.id === activeType).name;
  }
  function renderBrands() {
    const brands = [...new Set(products.filter(matchesType).map((p) => p.brand))].sort();
    $("tc-brand-current").textContent = activeBrand || "全部厂商";
    $("tc-brands").innerHTML = brands.length ? ["", ...brands]
      .map(
        (b) =>
          `<button class="tc-brand-choice" data-brand="${esc(b)}" aria-pressed="${activeBrand === b}">${esc(b || "全部厂商")}</button>`,
      )
      .join("") : '<p class="tc-filter-empty">尚无厂商记录</p>';
  }
  function filterChip(key, removable = false) {
    const t = vocabulary.get(key);
    return `<button class="tc-chip tc-tag-choice${t.variant === "unknown" ? " tc-unknown" : ""}" data-category="${t.cat}"${t.variant === "scale" ? ' data-variant="scale"' : ""} data-tag-filter="${esc(key)}" aria-pressed="${activeTags.has(key)}" aria-label="${removable ? "取消标签：" : "筛选标签："}${esc(t.text)}">${icons[t.cat]}${esc(t.text)}${removable ? '<span aria-hidden="true"> ×</span>' : ""}</button>`;
  }
  function renderTagFilters() {
    const available = new Set(products.filter((p) => matchesType(p) && (!activeBrand || p.brand === activeBrand))
      .flatMap((p) => [...productTagKeys.get(p.id)]));
    activeTags.forEach((key) => available.add(key));
    $("tc-tag-choices").innerHTML = cats.map((c) => {
      const keys = [...available].filter((key) => vocabulary.get(key).cat === c.id)
        .sort((a, b) => vocabulary.get(b).count - vocabulary.get(a).count || vocabulary.get(a).text.localeCompare(vocabulary.get(b).text, "zh-CN", { numeric: true }));
      return keys.length ? `<div class="tc-tag-filter-group" role="group" aria-label="${esc(c.name)}">${keys.map((key) => filterChip(key)).join("")}</div>` : "";
    }).join("");
    if (!available.size) $("tc-tag-choices").innerHTML = '<p class="tc-filter-empty">尚无标签记录</p>';
    $("tc-tag-filter-count").textContent = activeTags.size ? ` (${activeTags.size})` : "";
    $("tc-active-tags").innerHTML = [...activeTags].map((key) => filterChip(key, true)).join("");
    $("tc-active-filters").hidden = !activeTags.size && !activeBrand && !$("tc-search").value.trim();
  }
  $("tc-resources").innerHTML = [...new Set(db.resources.map((r) => r.group))]
    .map(
      (group) =>
        `<h3 class="tc-resource-group">${esc(group)}</h3>${db.resources
          .filter((r) => r.group === group)
          .map(
            (r) =>
              `<div class="tc-resource">${sourceLink(r)}<p>${esc(r.description)}</p>${sourceStatus(r)}</div>`,
          )
          .join("")}`,
    )
    .join("");
  const tagDefinitions = {
    joint: "拉筋、内部骨架、机械关节、可动部位与固定姿势分别记录。球体关节描述形状，不能仅凭 BJD 称谓判断是否拉筋。插接、粘接等属于连接方法；来源未说明时保留待核实。",
    size: "深红表示厂商标称比例，浅红表示公布的高度等实际尺寸。比例、头身比和尺寸分别记录；1:1、2:1 也可能按作品中的小型人偶为基准。含头、含底座等测量口径保留，不直接换算人体身高。同一比例的不同写法统一筛选，近似比例仍分开。",
    delivery: "涂装、组装、是否附素体或服装分别记录，例如涂装成品、未涂装成品、待拼装、成品含服。计划商品按官方预定日期记录；只有展会资料时，交付与发售状态保留待核实。",
    dress: "布衣穿脱、换假发、换眼、换脸和硬质换件分别记录。附带替换件不代表跨品牌通用，具体适配对象与限制见产品详情。",
    material: "仅记录来源明确的材料，主体与附属部件尽量分开。ABS 与 ABS树脂等同名写法统一筛选；只写“塑料”时记为“塑料（未细分）”。材料标签不代表耐热、耐染或安全评级。",
    role: "“机器人”“拟人动物”描述形象，“素体”“服装配套”描述商品组成，“BJD”“手办”“战棋模型”等是检索称谓。可以交叉标记，不据称谓推定结构、材料或适配。",
  };
  $("tc-tag-defs").innerHTML = `<div class="tc-tag-guide">${cats.map((c) =>
    `<div class="tc-tag-definition"><span class="tc-chip" data-category="${c.id}">${icons[c.id]}${esc(c.name)}</span><p>${esc(tagDefinitions[c.id])}</p></div>`
  ).join("")}</div><div class="tc-tag-rules"><h3>筛选与记录</h3><ul>
    <li>点击标签选中，再点取消；多选标签需要同时满足，可与类型、厂商和关键词组合。选中的标签也会出现在产品卡片上。</li>
    <li>类型为一级，厂商为二级。同一产品可出现在多个类型中，仍使用同一条记录；尚未整理的类型保留入口。</li>
    <li>未披露、待核实和不适用分别保留。来源原文、具体组成与适配限制见详情；卡片图形是结构或商品组成示意图。</li>
  </ul></div>`;
  function chooseType(type) {
    activeType = type;
    if (!products.some((p) => matchesType(p) && p.brand === activeBrand)) activeBrand = "";
    const available = new Set(products.filter((p) => matchesType(p) && (!activeBrand || p.brand === activeBrand))
      .flatMap((p) => [...productTagKeys.get(p.id)]));
    activeTags.forEach((key) => { if (!available.has(key)) activeTags.delete(key); });
    refresh();
    [...$("tc-types").querySelectorAll("button")].find((b) => b.dataset.type === activeType)?.focus({ preventScroll: true });
  }
  root.addEventListener("click", (e) => {
    const b = e.target.closest("button");
    if (!b) return;
    if (b.dataset.type) chooseType(b.dataset.type);
    if (b.dataset.view) showDetail(b.dataset.view);
    if (b.dataset.select) toggle(b.dataset.select);
    if (b.dataset.close) closeDialog(b.dataset.close);
    if (b.hasAttribute("data-tag-filter")) {
      const key = b.dataset.tagFilter;
      const fromChoices = $("tc-tag-choices").contains(b);
      if (activeTags.has(key)) activeTags.delete(key);
      else activeTags.add(key);
      refresh();
      const buttons = (fromChoices ? $("tc-tag-choices") : $("tc-active-tags")).querySelectorAll("button");
      const next = [...buttons].find((x) => x.dataset.tagFilter === key)
        || $("tc-tag-filter").querySelector("summary");
      next.focus({ preventScroll: true });
    }
    if (b.hasAttribute("data-brand")) {
      activeBrand = b.dataset.brand;
      refresh();
      [...$("tc-brands").querySelectorAll("button")]
        .find((x) => x.dataset.brand === activeBrand)
        ?.focus({ preventScroll: true });
    }
  });
  $("tc-filter-reset").addEventListener("click", () => {
    reset();
    $("tc-search").focus({ preventScroll: true });
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
  $("tc-date").textContent = db.date;
  render();
})();
