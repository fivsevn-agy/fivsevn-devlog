# 玩具资料页的专用文件

## 页面入口

- `../../../../_layouts/toy-post.html`：仅供下面两篇文章使用的页面模板。沿用主题的容器、样式、页脚和标题锚点，并读取文章自己的 `lang`。全站默认模板保持不变。
- `../../posts-toy-reference.md`：资料页的 HTML 结构、页面元数据和资源引用。
- `../../posts-toys-cross-category-literature-001.md`：独立的文献文章；不加载资料页脚本。

## 文件职责

- `toy-data.js`：`window.TOY_REFERENCE_DATA`，包括产品记录、六类属性、来源和延伸资料。
- `toy-browse.js`：`window.TOY_REFERENCE_BROWSE`，包括浏览类型和产品的类型映射。映射是增补表；未列出的产品默认归入 `human`。新增其他类型的产品时，需要同时补充映射。
- `toy-reference.js`：搜索、筛选、详情与对比。页面内的元素查找限制在 `#toyReference`，只在两份数据都载入后初始化。
- `toy-reference.css`：资料页的专用样式，选择器以 `#toyReference` 为范围；字体规则引用同目录的 WOFF2 文件。
- `toy-data.xlsx`：完整资料的下载文件。产品数据更新后，应同步检查下载版本。
- `fusion-pixel-12px-monospaced-zh_hans.woff2`、`LICENSE-OFL.txt`：字体及其许可。

资料页的资源统一位于 `assets/toy-reference/`。页面网址、文件名、页面编号和资源目录都使用 `toy-reference`。

## 加载与发布

页面依次引用数据、类型映射、界面脚本，三者都使用 `defer`。保持这个顺序，不改为 `async`。修改资源后，更新页面中对应的版本参数。

目录由 `scripts/update_module_indexes.py` 根据文章元数据和文件路径生成。两篇文章用 Markdown 收录，资源目录不进入文章目录。发布时应核对实际文章页面、字体与 Excel 下载，并检查搜索、组合筛选、详情和多产品对比。
