---
id: netcom-lora-meshtastic-device-ecosystem-001
title: Meshtastic 设备生态与支持级别划分

module: netcom
submodule: lora
topic: device-ecosystem

type: article
status: active
canonical: true

summary: >
  梳理 Meshtastic 官方支持与社区支持设备结构，
  并补充未列入官方名单的第三类设备。

parents: [netcom-module-map]
related: [netcom-lora-meshtastic-structure-001]

tags: [netcom, lora, meshtastic, device]
audience: [public]
languages: [zh]

maturity: evolving
confidence: 0.95

visibility: public
source_of_truth: devlog

created: 2025-11-23
updated: 2026-03-01
---
## meshtastic设备

```
我根据Meshtastic官网给出的信息进行的二次总结。
表述未必精准，主要方便梳理。
```

① 按照Meshtastic官网所述，硬件设备分为两种：

- A：【Officially Supported】官方支持设备  
  - `厂商掏钱？参加官方 Backer/Partner 计划`  
   
- B：【Community Supported】社区支持设备  
  - `官方团队不负责售后和测试了`  

② 除了Meshtastic官方给的这两类之外，再补充一类：  

- C：完全不在以上列表里的  

③ 综上，我自己定义一下：

> 官方支持设备：A  
> 非官方支持设备：B+C  

④ 买之前留意一下。

---

### Meshtastic官方支持设备A

> A类设备会随Meshtastic主线同步更新，有长期兼容性保证。

- A类直接去官方网页看，列表会更新：
  - [官网页面：Devices Supported Hardware Overview](https://meshtastic.org/docs/hardware/devices/)
- 经常会搜到的比方说：
  - LilyGO（T-Beam/T-Echo/T-Deck等）
    - [LilyGO官网](https://lilygo.cc)
  - Heltec（LoRa 32 V3/Mesh Node T114）
    - [Heltec官网](https://heltec.org)
  - RAKwireless
    - [RAKwireless官网](https://www.rakwireless.com/zh-cn)
  - Seeed Studio
    - [Seeed Studio官网](https://www.seeedstudio.com)
  - 等等

---

### 非Meshtastic官方支持设备B

> B类能跑但不保证未来也能跑，主要看社区热度。

- B类也直接看官网整理的：
  - [官网页面：Community Supported](https://meshtastic.org/docs/hardware/devices/community-supported/?utm_source=chatgpt.com)
- 一些实现性的好玩的东西，或者是功能未必完整的、更新节奏不稳定的、老型号的设备等等等等。

---

### 非Meshtastic官方支持设备C（待补充）

> 部分C类设备虽然未被列入官方列表，但有长期维护团队。

- `M5Stack（明栈信息科技）`
- 🔗 [X：M5Stack](https://x.com/m5stack?s=21)

  - 卡片电脑+扩展：[M5Stack官方介绍：Cardputer-Adv + Cap LoRa868](https://docs.m5stack.com/zh_CN/guide/lora/meshtastic/cardputer_adv)

  - 另一个：[M5Stack官方介绍：Unit C6L](https://docs.m5stack.com/zh_CN/unit/Unit_C6L)
 
 
- `GAT562（加特物联GAT-IOT）`
- 🔗 [抖音：加特物联](https://v.douyin.com/pKHz1IdP0mA/ 3@8.com :0pm)

  - MeshCN圈比较火：[MeshCN网站介绍：GAT562](https://meshcn.net/gat-iot-handheld-review/)

---

### 其他

- 购买渠道：淘宝、亚马逊、闲鱼、ebay等
- 各大平台都搜一搜、收集资料。
- 关注厂商参展动态。




 