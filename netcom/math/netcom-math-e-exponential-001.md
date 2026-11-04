---
id: "netcom-math-e-exponential-001"
title: "指数微分方程 dy/dt = ky 的推导与 e 的意义"

module: "netcom"
submodule: "math"
topic: "exponential-growth"

type: "article"
status: "active"
canonical: true

summary: |
  推导 dy/dt = ky 的解形式， 解释自然对数 ln 与常数 e 的数学来源， 建立指数增长模型的基础。

parents: ["netcom-index"]
related: ["netcom-math-dynamical-system-prototypes-001"]

tags: ["netcom", "math", "exponential", "e"]

audience: ["public"]
languages: ["zh"]

maturity: "stable"
confidence: 0.98

visibility: "public"
source_of_truth: "devlog"

legacy:
  metadata:
    parents:
    - netcom-module-map

created: "2025-12-12"
updated: "2026-11-04"
metadata_updated: "2026-11-04"
---
## 解dy/dt=ky

```
一种是假设我是个古人，我算极限的时候怎么逼近出这么个神奇的数值。  
另一种就是ln独立定义之后可以用现代的方法积分求出来。
```

- ln：logarithmus naturalis（拉丁语），自然对数。
- e：好像说是数学家Euler随便起的，说这个e还没被用过就用e吧。

> **手绘笔记勘误（2026-11-04）**：第一张图中，`n = 10000` 时 `(1 + 1/n)^n ≈ 2.7181459268`；约 `2.71828…` 是继续趋近的极限 e，不能提前填在这一行。这里想说明的仍是有限次复利逐渐逼近连续增长。对照 [OpenStax 的 e 与连续复利说明](https://openstax.org/books/precalculus-2e/pages/4-1-exponential-functions)和[Pearson 的极限定义](https://www.pearson.com/content/dam/one-dot-com/one-dot-com/us/en/higher-ed/en/products-services/course-products/sullivan-10e-info/pdf/Guided-Lecture-Notes-Sample.pdf)，并分别用高精度幂运算与对数形式复算。下方保留原图，该行数值以此为准。

![mathe1](../assets/20251212mathe1.png)
![mathe2](../assets/20251212mathe2.png)  


