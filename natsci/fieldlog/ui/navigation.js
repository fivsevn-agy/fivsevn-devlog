/* Keep the archive position when closing a specimen; anchors also work without JS. */
(() => {
  "use strict";
  const prefix = "fieldlog:return:";
  const pendingKey = "fieldlog:pending-return";
  const archivePath = /^\/natsci\/fieldlog\/(?:page\/[1-9]\d*\/)?(?:index\.html)?$/;
  const plainClick = (event) => event.button === 0 && !event.metaKey && !event.ctrlKey && !event.shiftKey && !event.altKey;
  function archiveURL(value) {
    try {
      const url = new URL(value, location.origin);
      return url.origin === location.origin && archivePath.test(url.pathname) ? url : null;
    } catch (_) { return null; }
  }
  if (document.querySelector("main.archive")) {
    // Restore the post's viewport offset after fonts settle, including bfcache returns.
    addEventListener("pageshow", () => {
      try {
        const saved = JSON.parse(sessionStorage.getItem(pendingKey));
        const target = saved && archiveURL(saved.url);
        if (!target || target.pathname !== location.pathname || target.search !== location.search) return;
        const post = document.getElementById(saved.id);
        if (!post || !Number.isFinite(saved.offset)) return;
        sessionStorage.removeItem(pendingKey);
        const restore = () => requestAnimationFrame(() => requestAnimationFrame(() => {
          scrollTo(0, Math.max(0, scrollY + post.getBoundingClientRect().top - saved.offset));
        }));
        if (document.fonts) document.fonts.ready.then(restore);
        else restore();
      } catch (_) { /* Native history or the generated anchor still locates the post. */ }
    });
    document.addEventListener("click", (event) => {
      const link = event.target.closest("a[data-fieldlog-open]");
      if (!link || !plainClick(event)) return;
      const post = link.closest("article[id]");
      if (!post) return;
      try {
        sessionStorage.setItem(prefix + new URL(link.href).pathname, JSON.stringify({
          url: location.pathname + location.search + "#" + post.id,
          id: post.id, offset: post.getBoundingClientRect().top,
        }));
      } catch (_) { /* The generated return anchor remains usable. */ }
    });
    return;
  }
  const close = document.querySelector("a[data-fieldlog-return]");
  if (!close) return;
  try {
    const saved = JSON.parse(sessionStorage.getItem(prefix + location.pathname));
    const target = saved && archiveURL(saved.url);
    const post = close.closest("article[id]");
    if (!target || !post || decodeURIComponent(target.hash.slice(1)) !== post.id) return;
    close.href = target.href;
    const source = document.referrer && archiveURL(document.referrer);
    if (source && source.pathname === target.pathname && history.length > 1) {
      history.replaceState({ ...history.state, fieldlogReturn: target.href }, "");
    }
    close.addEventListener("click", (event) => {
      if (!plainClick(event)) return;
      try { sessionStorage.setItem(pendingKey, JSON.stringify(saved)); } catch (_) { /* Anchor fallback. */ }
      if (history.length > 1 && history.state?.fieldlogReturn === target.href) {
        event.preventDefault();
        history.back();
      }
    });
  } catch (_) { /* Direct visits and restricted storage use the generated anchor. */ }
})();
