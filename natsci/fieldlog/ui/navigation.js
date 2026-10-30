/* Return each specimen to the same frame-top position as its detail window. */
(() => {
  "use strict";
  const prefix = "fieldlog:return:";
  const pendingKey = "fieldlog:pending-return";
  const archivePath = /^\/natsci\/fieldlog\/(?:page\/[1-9]\d*\/)?(?:index\.html)?$/;
  let routes = {};
  try { routes = JSON.parse(document.getElementById("fieldlog-archive-map")?.textContent || "{}"); } catch (_) { /* Normal anchors remain available. */ }
  const plainClick = (event) => event.button === 0 && !event.metaKey && !event.ctrlKey && !event.shiftKey && !event.altKey;
  function archiveURL(value) {
    try {
      const url = new URL(value, location.origin);
      if (url.origin !== location.origin || !archivePath.test(url.pathname)) return null;
      const route = routes[decodeURIComponent(url.hash.slice(1))];
      if (!route) return url;
      const mapped = new URL(route, location.origin);
      mapped.search = url.search;
      return mapped;
    } catch (_) { return null; }
  }
  function alignFrame(post, top) {
    let active = true;
    const timers = [];
    const spacerId = "fieldlog-return-space";
    const align = () => {
      if (!active || !post.isConnected) return;
      const scrolling = document.scrollingElement || document.documentElement;
      const destination = Math.max(0, window.scrollY + post.getBoundingClientRect().top - top);
      let spacer = document.getElementById(spacerId);
      const previousHeight = spacer ? parseFloat(spacer.style.height) || 0 : 0;
      const baseHeight = scrolling.scrollHeight - previousHeight;
      const needed = Math.max(0, Math.ceil(destination + window.innerHeight - baseHeight));
      if (needed || spacer) {
        if (!spacer) {
          spacer = document.createElement("div");
          spacer.id = spacerId;
          spacer.setAttribute("aria-hidden", "true");
          spacer.style.pointerEvents = "none";
          spacer.style.overflowAnchor = "none";
          document.body.appendChild(spacer);
        }
        spacer.style.height = needed + "px";
        // Account for any margin-collapsing change when the spacer is first added.
        const remaining = Math.ceil(destination + window.innerHeight - scrolling.scrollHeight);
        if (remaining > 0) spacer.style.height = needed + remaining + "px";
      }
      if (Math.abs(post.getBoundingClientRect().top - top) > 0.5) {
        window.scrollTo(0, destination);
      }
    };
    let queued = false;
    const schedule = () => {
      if (!active || queued) return;
      queued = true;
      window.requestAnimationFrame(() => window.requestAnimationFrame(() => {
        queued = false;
        align();
      }));
    };
    const stop = () => {
      active = false;
      timers.forEach(timer => window.clearTimeout(timer));
      document.removeEventListener("load", schedule, true);
      window.removeEventListener("resize", schedule);
      window.removeEventListener("pagehide", stop);
      ["wheel", "touchstart", "pointerdown", "keydown"].forEach(type => window.removeEventListener(type, stop, true));
      observer?.disconnect();
      // Keep any necessary tail room: removing it here could clamp the user's scroll.
    };
    const observer = window.ResizeObserver ? new window.ResizeObserver(schedule) : null;
    observer?.observe(document.querySelector("main.archive"));
    observer?.observe(post);
    document.addEventListener("load", schedule, true);
    window.addEventListener("resize", schedule);
    window.addEventListener("pagehide", stop);
    ["wheel", "touchstart", "pointerdown", "keydown"].forEach(type => window.addEventListener(type, stop, { capture: true, passive: true }));
    schedule();
    Promise.resolve(document.fonts?.ready).then(() => {
      if (!active) return;
      schedule();
      timers.push(window.setTimeout(stop, 2000));
    });
    timers.push(window.setTimeout(stop, 10000));
  }
  if (document.querySelector("main.archive")) {
    const relocate = () => {
      const target = archiveURL(location.href);
      if (target && target.pathname !== location.pathname) {
        location.replace(target.href);
        return true;
      }
      return false;
    };
    if (relocate()) return;
    addEventListener("hashchange", relocate);
    // Restore the detail frame's top after fonts/images settle, including bfcache returns.
    addEventListener("pageshow", () => {
      try {
        const saved = JSON.parse(sessionStorage.getItem(pendingKey));
        const target = saved && archiveURL(saved.url);
        if (!target || target.pathname !== location.pathname || target.search !== location.search) return;
        const post = document.getElementById(saved.id);
        if (!post || !Number.isFinite(saved.top)) return;
        sessionStorage.removeItem(pendingKey);
        alignFrame(post, saved.top);
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
          id: post.id,
        }));
      } catch (_) { /* The generated return anchor remains usable. */ }
    });
    return;
  }
  const close = document.querySelector("a[data-fieldlog-return]");
  if (!close) return;
  try {
    const saved = JSON.parse(sessionStorage.getItem(prefix + location.pathname));
    const post = close.closest("article[id]");
    if (!post) return;
    const remembered = saved && saved.id === post.id && archiveURL(saved.url);
    const target = remembered || archiveURL(close.href);
    if (!target || decodeURIComponent(target.hash.slice(1)) !== post.id) return;
    close.href = target.href;
    const rememberFrame = () => {
      const top = post.getBoundingClientRect().top;
      if (!Number.isFinite(top)) return;
      try { sessionStorage.setItem(pendingKey, JSON.stringify({ url: target.href, id: post.id, top })); } catch (_) { /* Anchor fallback. */ }
    };
    // Native Back and bfcache returns must use the detail frame too.
    addEventListener("pagehide", rememberFrame);
    const source = document.referrer && archiveURL(document.referrer);
    if (source && source.pathname === target.pathname && history.length > 1) {
      history.replaceState({ ...history.state, fieldlogReturn: target.href }, "");
    }
    close.addEventListener("click", (event) => {
      if (!plainClick(event)) return;
      rememberFrame();
      if (history.length > 1 && history.state?.fieldlogReturn === target.href) {
        event.preventDefault();
        history.back();
      }
    });
  } catch (_) { /* Direct visits and restricted storage use the generated anchor. */ }
})();
