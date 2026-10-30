/* Pure DOM/history mocks: run with Node or macOS JavaScriptCore, without a browser. */
async function runFieldlogNavigationCases(source) {
  const origin = "https://devlog.fivsevn.com";
  const postPath = "/natsci/fieldlog/2026/10/post/";
  const pagePath = "/natsci/fieldlog/page/2/";
  const id = "obs-post";
  const pendingKey = "fieldlog:pending-return";
  const prefix = "fieldlog:return:";
  const completed = [];
  const equal = (actual, expected, message) => {
    if (actual !== expected) throw new Error(message + ": " + JSON.stringify(actual) + " != " + JSON.stringify(expected));
  };
  class TestURL {
    constructor(value, base) {
      value = String(value);
      if (value.startsWith("/")) value = String(base).match(/^https?:\/\/[^/]+/)[0] + value;
      const match = value.match(/^(https?:\/\/[^/]+)([^?#]*)(\?[^#]*)?(#.*)?$/);
      if (!match) throw new Error("Invalid URL");
      this.origin = match[1]; this.pathname = match[2] || "/";
      this.search = match[3] || ""; this.hash = match[4] || "";
    }
    get href() { return this.origin + this.pathname + this.search + this.hash; }
  }
  const URLClass = typeof URL === "function" ? URL : TestURL;
  function hub() {
    const events = new Map();
    return {
      add(type, callback) { if (!events.has(type)) events.set(type, new Set()); events.get(type).add(callback); },
      remove(type, callback) { events.get(type)?.delete(callback); },
      emit(type, event = {}) { [...(events.get(type) || [])].forEach(callback => callback(event)); },
    };
  }
  function environment(mode, storage = new Map(), options = {}) {
    const events = hub(), documentEvents = hub(), closeEvents = hub();
    const frames = [], timers = new Map(), observers = [], nodes = new Map();
    const state = {
      mode, storage, absoluteTop: options.absoluteTop ?? 2300, frameTop: options.frameTop ?? 30,
      baseHeight: options.baseHeight ?? 5000, backCount: 0, replaces: [], scrollCalls: [],
    };
    const location = new URLClass(origin + (options.path || (mode === "archive" ? pagePath : postPath)));
    location.replace = value => state.replaces.push(value);
    const routes = options.routes || { [id]: pagePath + "#" + id };
    nodes.set("fieldlog-archive-map", { textContent: JSON.stringify(routes) });
    let resolveFonts;
    const fonts = { ready: new Promise(resolve => { resolveFonts = resolve; }) };
    const window = {
      scrollY: options.scrollY ?? 200, innerHeight: options.innerHeight ?? 844,
      addEventListener: events.add, removeEventListener: events.remove,
      requestAnimationFrame(callback) { frames.push(callback); },
      setTimeout(callback, delay) { const key = timers.size + 1; timers.set(key, { callback, delay }); return key; },
      clearTimeout(key) { timers.delete(key); },
      ResizeObserver: class {
        constructor(callback) { this.callback = callback; this.active = true; observers.push(this); }
        observe() {}
        disconnect() { this.active = false; }
      },
      scrollTo(left, top) {
        const max = Math.max(0, document.scrollingElement.scrollHeight - window.innerHeight);
        window.scrollY = Math.max(0, Math.min(max, top)); state.scrollCalls.push(window.scrollY);
      },
    };
    const post = { id, isConnected: true, getBoundingClientRect() {
      return { top: mode === "archive" ? state.absoluteTop - window.scrollY : state.frameTop };
    } };
    nodes.set(id, post);
    const main = {};
    const close = {
      href: origin + (options.fallback || pagePath + "#" + id),
      closest() { return post; }, addEventListener: closeEvents.add,
    };
    const document = {
      fonts, referrer: options.referrer || "", documentElement: {},
      querySelector(selector) { return selector === "main.archive" ? (mode === "archive" ? main : null) : close; },
      getElementById(key) { return nodes.get(key) || null; },
      createElement() { return { style: {}, setAttribute() {} }; },
      body: { appendChild(node) { nodes.set(node.id, node); } },
      addEventListener: documentEvents.add, removeEventListener: documentEvents.remove,
      scrollingElement: { get scrollHeight() {
        return state.baseHeight + (parseFloat(nodes.get("fieldlog-return-space")?.style.height) || 0);
      } },
    };
    const history = {
      length: options.historyLength ?? 2, state: options.historyState || null,
      replaceState(value) { this.state = value; }, back() { state.backCount += 1; },
    };
    const sessionStorage = { getItem(key) { return storage.get(key) ?? null; }, setItem(key, value) { storage.set(key, value); }, removeItem(key) { storage.delete(key); } };
    new Function("window", "document", "location", "history", "sessionStorage", "URL", "addEventListener", source)(
      window, document, location, history, sessionStorage, URLClass, events.add);
    const click = () => ({ button: 0, prevented: false, preventDefault() { this.prevented = true; } });
    return Object.assign(state, {
      window, document, close, history, nodes,
      show() { events.emit("pageshow"); },
      hide() { events.emit("pagehide"); },
      userScroll() { events.emit("wheel"); },
      loadImage() { documentEvents.emit("load"); },
      resize() { events.emit("resize"); observers.filter(observer => observer.active).forEach(observer => observer.callback()); },
      fontsReady() { resolveFonts(); },
      open() {
        const event = click(); const link = { href: origin + postPath, closest() { return post; } };
        event.target = { closest() { return link; } }; documentEvents.emit("click", event);
      },
      closeFrame() { const event = click(); closeEvents.emit("click", event); return event; },
      async flush() {
        for (let count = 0; count < 5; count += 1) {
          await Promise.resolve(); const batch = frames.splice(0); batch.forEach(callback => callback());
        }
      },
      top() { return post.getBoundingClientRect().top; },
    });
  }
  {
    const storage = new Map();
    const list = environment("archive", storage, { scrollY: 1720 });
    list.open();
    const remembered = JSON.parse(storage.get(prefix + postPath));
    equal(remembered.id, id, "remember originating post");
    equal(Object.prototype.hasOwnProperty.call(remembered, "offset"), false, "do not save original click offset");
    const detail = environment("detail", storage, { frameTop: 30, referrer: origin + pagePath });
    detail.closeFrame();
    equal(detail.backCount, 1, "same-tab close uses safe history back");
    equal(JSON.parse(storage.get(pendingKey)).top, 30, "capture detail top instead of original list offset");
    const returned = environment("archive", storage, { scrollY: 1720 });
    returned.show(); await returned.flush();
    equal(returned.top(), 30, "returned list frame aligns to detail frame");
    completed.push("same-tab close aligns detail top");
  }
  {
    const storage = new Map();
    const direct = environment("detail", storage, { frameTop: 24, historyLength: 1, fallback: "/natsci/fieldlog/page/4/#" + id,
      routes: { [id]: "/natsci/fieldlog/page/4/#" + id } });
    direct.closeFrame();
    equal(direct.backCount, 0, "direct detail never backs into an unrelated page");
    equal(JSON.parse(storage.get(pendingKey)).top, 24, "direct detail records its frame top");
    const returned = environment("archive", storage, { path: "/natsci/fieldlog/page/4/", routes: { [id]: "/natsci/fieldlog/page/4/#" + id } });
    returned.show(); returned.fontsReady(); await returned.flush();
    equal(returned.top(), 24, "direct fallback returns to page four at mobile frame top");
    completed.push("direct detail and mobile fallback");
  }
  {
    const storage = new Map();
    const detail = environment("detail", storage, { frameTop: 30, referrer: origin + pagePath });
    detail.hide();
    equal(JSON.parse(storage.get(pendingKey)).top, 30, "native Back uses pagehide detail geometry");
    const list = environment("archive", storage);
    list.show(); await list.flush(); equal(list.top(), 30, "native Back aligns");
    list.absoluteTop += 130; list.fontsReady(); await list.flush(); equal(list.top(), 30, "late fonts settle");
    list.absoluteTop += 75; list.loadImage(); await list.flush(); equal(list.top(), 30, "late image settles");
    list.absoluteTop += 50; list.resize(); await list.flush(); equal(list.top(), 30, "layout resize settles");
    list.userScroll(); const before = list.window.scrollY;
    list.absoluteTop += 100; list.loadImage(); list.resize(); await list.flush();
    equal(list.window.scrollY, before, "stop restoring once user interacts");
    completed.push("native Back, fonts, images, and user control");
  }
  {
    const storage = new Map([[pendingKey, JSON.stringify({ url: origin + pagePath + "#" + id, id, top: 24 })]]);
    const list = environment("archive", storage, { absoluteTop: 900, baseHeight: 1300, innerHeight: 844, scrollY: 100 });
    list.show(); list.fontsReady(); await list.flush();
    equal(list.top(), 24, "short last post has enough tail room to align");
    const height = list.nodes.get("fieldlog-return-space").style.height;
    const position = list.window.scrollY;
    list.userScroll(); await list.flush();
    equal(list.nodes.get("fieldlog-return-space").style.height, height, "user interaction retains necessary tail room");
    equal(list.window.scrollY, position, "stopping does not clamp the scroll position");
    completed.push("short final post spacer without scroll jump");
  }
  {
    const storage = new Map([[pendingKey, JSON.stringify({ url: origin + "/natsci/fieldlog/page/3/?preview=yes#" + id, id, top: 30 })]]);
    const routes = { [id]: pagePath + "#" + id };
    const old = environment("archive", storage, { path: "/natsci/fieldlog/page/3/?preview=yes#" + id, routes });
    equal(old.replaces[0], origin + pagePath + "?preview=yes#" + id, "old pagination anchor relocates while retaining query");
    const current = environment("archive", storage, { path: pagePath + "?preview=yes#" + id, routes });
    current.show(); await current.flush(); equal(current.top(), 30, "relocated return aligns correct post");
    completed.push("pagination relocation and query preservation");
  }
  {
    const storage = new Map();
    const first = environment("detail", storage, { frameTop: 30 }); first.hide();
    const refreshed = environment("detail", storage, { frameTop: 24 }); refreshed.hide();
    equal(JSON.parse(storage.get(pendingKey)).top, 24, "refresh recaptures current detail geometry");
    const separate = new Map();
    const other = environment("detail", separate, { frameTop: 42 }); other.hide();
    equal(JSON.parse(storage.get(pendingKey)).top, 24, "another tab cannot replace this tab's target");
    const plain = environment("archive", new Map(), { scrollY: 123 });
    plain.show(); plain.fontsReady(); await plain.flush();
    equal(plain.window.scrollY, 123, "ordinary browsing is untouched");
    equal(plain.nodes.has("fieldlog-return-space"), false, "ordinary browsing has no extra tail room");
    completed.push("refresh, separate tabs, and ordinary browsing");
  }
  {
    const storage = new Map([[pendingKey, JSON.stringify({ url: "https://example.com/natsci/fieldlog/#" + id, id, top: 30 })]]);
    const list = environment("archive", storage, { scrollY: 123 }); list.show(); await list.flush();
    equal(list.window.scrollY, 123, "reject another origin's return location");
    const old = new Map([[pendingKey, JSON.stringify({ url: origin + pagePath + "#" + id, id, offset: 500 })]]);
    const legacy = environment("archive", old, { scrollY: 123 }); legacy.show(); await legacy.flush();
    equal(legacy.window.scrollY, 123, "never restore a stale saved click offset");
    completed.push("reject unsafe or obsolete return state");
  }
  return completed;
}
