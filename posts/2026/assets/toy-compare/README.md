# 玩具资料页的专用文件

## 页面入口

- `../../posts-toy-reference.md`：资料页的 HTML 结构、页面元数据和资源引用。
- `../../posts-toys-cross-category-literature-001.md`：独立的文献文章；不加载资料页脚本。
- `../../posts-toy-compare.html`、`../../posts-humanoid-toys-cross-category-literature-001.html`：旧网址跳转，保留查询参数和页内锚点，不进入文章目录。

## 文件职责

- `toy-data.js`：`window.TOY_COMPARE_DATA`，包括产品记录、六类属性、来源和延伸资料。
- `toy-browse.js`：`window.TOY_COMPARE_BROWSE`，包括浏览类型和产品的类型映射。映射是增补表；未列出的产品默认归入 `human`。新增其他类型的产品时，需要同时补充映射。
- `toy-compare.js`：搜索、筛选、详情与对比。页面内的元素查找限制在 `#toyCompare`，只在两份数据都载入后初始化。
- `toy-compare.css`：资料页的专用样式，选择器以 `#toyCompare` 为范围；字体规则引用同目录的 WOFF2 文件。
- `toy-data.xlsx`：完整资料的下载文件。产品数据更新后，应同步检查下载版本。
- `fusion-pixel-12px-monospaced-zh_hans.woff2`、`LICENSE-OFL.txt`：字体及其许可。

保留 `assets/toy-compare/` 路径，以兼容已发布的资源和下载链接。页面网址、文件名与页面编号使用 `toy-reference`；这个资源目录名不参与文章分类。

## 加载与发布

页面依次引用数据、类型映射、界面脚本，三者都使用 `defer`。保持这个顺序，不改为 `async`。修改资源后，更新页面中对应的版本参数。

目录由 `scripts/update_module_indexes.py` 根据文章元数据和文件路径生成。跳转文件使用 HTML，不作为新的 Markdown 文章收录。发布时应核对实际文章页面、两个旧地址、字体与 Excel 下载，并检查搜索、组合筛选、详情和多产品对比。
