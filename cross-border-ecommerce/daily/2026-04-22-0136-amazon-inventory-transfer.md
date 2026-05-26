# 主题153：亚马逊仓储跨境转移与库存重组

> 学习时间：2026-04-22 01:36

## 学习内容摘要

### 一、亚马逊库存转移（Inventory Transfer）的核心场景

**什么时候需要移仓/转移库存？**
- 将库存从美国站 FBA 仓库转移到欧洲站 FBA 仓库（支持泛欧计划内部调配）
- FBA 库存需要移至第三方海外仓（换标/处理滞销）
- 多渠道配送（Multi-Channel Fulfillment）：用 FBA 库存履独立站订单
- 旺季前在库容紧张前将货物转移至海外仓，分散存储

**亚马逊提供的标准转移选项：**
1. **Create a removal order（移除订单）**：将 FBA 库存退回或销毁
2. **FBA Inventory Placement Service（库存配置服务）**：让亚马逊帮你将库存发往靠近消费者的运营中心（亚马逊自动分仓）
3. **FBA Cross-Border Inventory Transfer（跨境库存转移）**：FBA 库存从一个国家的仓库转移到另一个国家（如美国→加拿大/墨西哥），需单独开通权限并缴纳跨境调配费

---

### 二、FBA 移仓移除（FBA Liquidations）详解

**什么是 FBA Liquidations？**
- 亚马逊将你的冗余库存批量出售给清算商（liquidation company），以原价的约 5%~20% 回收价值
- 比直接弃置（create a removal order）回收更多钱，减少损失
- 适用场景：滞销库存、旺季积压、断款后冗余库存

**Liquidations 操作流程：**
1. 在卖家中心 → Inventory → Manage FBA Inventory → Actions → "Create a liquidation order"
2. 选择要清算的 ASIN 和数量
3. 亚马逊扣除 liquidation fee（约 $0.25~$0.50/unit + 配送费），将订单分配给清算商
4. 约 30~60 天内收到回款

**Liquidations vs 弃置 vs 移仓对比：**

| 方案 | 回收价值 | 适用场景 | 费用 |
|------|---------|---------|------|
| Liquidations | 5%~20% | 冗余滞销库存 | $0.25~$0.50/件 + 配送费 |
| 移除到海外仓 | 100%（换标后继续卖） | 有价值的滞销品/需要换标 | 移除费 + 海外仓费 |
| 弃置（Dispose） | 0% | 无价值废物/销毁 | $0.25~$0.50/件 |
| 折扣促销（Deal/ coupon） | 成本价~原价 | 有一定竞争力的品 | 较低 |

**注意事项：**
- 并非所有类目都开放 liquidation，需要查看是否在可 liquidation 类目列表
- 清算后无法撤销，库存不可回收
- 清算回款打入亚马逊账户（通常低于预期）

---

### 三、FBA 库龄自动移除（Automated Long-Term Storage Removal）

**亚马逊政策：超过 365 天的 FBA 超龄库存会被强制收长期仓储费（LTSF）**

- 6个月~12个月：$6.90/cubic foot/月
- 12个月以上：$15.00/cubic foot/月（极高！）

**Automated Long-Term Storage Removal（自动库龄移除）设置：**
- 在 Setting → Fulfillment by Amazon → Automated Long-Term Storage Removal 中开启
- 可选择：
  - **Convert to Gated Standard（转GS）**：自动将超龄库存转为 GS（Grade and Grading），以折扣价出售
  - **Liquidate（清算）**：自动通过 Liquidations 回收价值
  - **Remove（移除）**：移除到指定地址

**主动清仓策略：**
1. 每年 1月/2月（亚马逊清仓大拍卖前）提前处理节日季滞销品
2. 旺季结束后 2 月内清理冗余库存，避免 LTSF
3. 设置库存 aged-offer 预警，用 RestockPro / DataHawk 监控

---

### 四、跨站点库存调配（Cross-Border Inventory Transfer）

**亚马逊 FBA 跨境库存转移（北美→欧洲/日本）**
- 如果你在多个国家站点（US/CA/MX 或 EU/UK/JP）开通 FBA，可申请跨站点库存调配权限
- 需提交申请至 seller-performance@amazon.com，说明需求（SKU/数量/目的国）
- 调配费用：通常 $0.30~$0.50/unit + 跨境运费
- 调配时效：约 4~6 周

**什么时候用？**
- 欧洲站某 SKU 断货，但美国站同款有库存 → 跨站调配比空运补货便宜
- 日本站新品测款，从美国站 FBA 调拨库存（节省头程运费）
- 旺季前平衡各站点库存

---

### 五、多渠道库存协同（Multi-Channel Fulfillment / MCF）

**什么是 MCF？**
- 用 FBA 库存履独立站、Shopify、eBay、沃尔玛等其他平台的订单
- FBA 库存不仅可以给亚马逊订单发货，也可以给其他平台订单发货

**MCF 费用结构：**
- MCF 费用比标准 FBA 略高（含额外的处理费）
- 计费公式：履约费 + 配送费 + 重量费
-  пример: $3.99 + $0.50/lb（美国站 MCF）

**MCF 注意事项：**
- MCF 库存会从你的 FBA 可售库存中扣除，需同步监控可用库存
- MCF 预计时效比 FBA 稍长（通常 3~5 个工作日）
- 多渠道订单不受亚马逊 Prime 保障，不影响亚马逊绩效
- 适合独立站日均订单 10~30 单的小型卖家（避免自建仓）

---

### 六、决策框架：何时用哪种移仓/清理策略

```
库存有价值（能继续卖）？
├─ YES → 有换标价值? → YES → 移至海外仓换标，重新入FBA或自发货
│         └─ NO → 移到其他亚马逊站点? → YES → 申请跨站调配
│                            └─ NO → 多渠道配送(MCF)给独立站
└─ NO → 有清算价值? → YES → 申请FBA Liquidations
         └─ NO → 折扣促销(Deal/Coupon)? → YES → 提报LD/BD
                            └─ NO → 直接弃置(Dispose)
```

---

## 对不对的判断

✅ **正确核心逻辑：**
- FBA Liquidations 是一种止损手段，比直接弃置回收更多价值
- 超过365天库存会产生高额LTSF，主动清仓是标准运营动作
- 跨站点调配适合多站点卖家平衡库存，不是日常操作

⚠️ **需要验证：**
- 具体 liquidation fee 数字可能随亚马逊政策变动，需以卖家中心最新页面为准
- 跨站调配权限需要单独申请，不是所有账号都能用

---

## 是不是新知识

**新知识：** FBA Liquidations 机制和Automated Long-Term Storage Removal 的具体操作细节是新的知识，之前主题中提到过仓储成本但没有详细讲解 Liquidations 操作流程。

**已掌握可衔接：**
- 主题73（FBA库存管理）和主题96（仓储降本增效）已覆盖IPI和库龄管理，移仓策略是它们的自然延伸
- 主题139（清关与进口关税）涉及库存转运，但侧重点不同

---

## 是否好理解

**理解难度：★★☆☆☆（较容易）**

- 移仓、清算、MCF 三种工具的适用场景清晰，决策框架实用
- 费用结构明确（$0.25~0.50/liquidation + LTSF分两档）
- 操作路径在卖家中心固定，不复杂
- 唯一门槛：跨站点调配权限需申请，且亚马逊审核严格（需要真实业务理由）

---

## 补充：FBA 库存价值修复（FBA Value Recovery）新服务

亚马逊在2023-2024年在美国站推出 **FBA Value Recovery** 试点：
- 针对超龄库存，亚马逊帮你以更高价格（相比 Liquidations）出售给二手买家
- 回收率比 Liquidations 高约 30%~50%
- 目前仍属试点阶段，非全站点开放，有兴趣的卖家可联系账户经理申请加入

---

## 与其他主题的关联

- **主题73/96**：FBA库存管理/仓储降本 → 本文是库存出问题后的处理手段
- **主题81**：亚马逊欧洲站 → 泛欧计划下跨国库存调配
- **主题87**：跨境物流服务商 → 移仓到海外仓涉及物流服务商选择
- **主题139**：清关实务 → 跨境库存转移涉及清关流程
