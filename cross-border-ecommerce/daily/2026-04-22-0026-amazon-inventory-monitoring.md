# Topic 147: 亚马逊库存监控与智能预警系统

**学习时间：** 2026-04-22 00:26  
**主题编号：** 147

---

## 一、核心概念

### 1. Inventory Dashboard（库存仪表盘）

亚马逊卖家中心提供 `Inventory > Inventory Plan` 和 `Manage Inventory` 两个核心页面：
- **Inventory Dashboard**：展示整体库存健康状态，包括 FBA 库存量、可售天数、滞留库存
- **Manage Inventory**：具体到每个 SKU 的库存状态（active/inbound/reserved）

### 2. 关键监控指标

| 指标 | 含义 | 警戒值 |
|------|------|--------|
| **On-Hand Quantity** | 当前可用库存 | — |
| **Reserved Inventory** | 预留中（待处理/预处理） | — |
| **Inbound to Amazon** | 运输中库存 | — |
| **Days of Supply (DoS)** | 库存可售天数 = On-Hand / 日均销量 | <7天为预警 |
| **Sell-Through Rate** | 销转率 = 售出数 / 平均库存 | <1.0需警惕 |
| **Aged Inventory** | 超90天库存（超龄附加费触发线） | 库存龄达180天产生高额费 |

### 3. FBA 库存龄期（Age）分级

| 龄期 | 附加费风险 | 处置策略 |
|------|-----------|---------|
| 0-90天 | 无 | 正常销售 |
| 91-180天 | 中等费用 | 监控补货 |
| 181-270天 | 高额费用 | 优先清仓（Outlet/ liquidation） |
| 271-365天 | 极高费用 | 强制移除或销毁 |
| >365天 | 封顶费用（max） | 必须处理 |

---

## 二、智能预警系统

### 1. 亚马逊原生预警

- **Restock Alerts**：亚马逊根据历史销量自动计算补货建议，在 Inventory Dashboard 显示红色"Restock Alert"标记
- **Low Inventory Alert**：当库存低于四周销量时触发警告
- **Stranded Inventory Alert**：Listing 有问题导致的无法销售库存

### 2. 第三方工具预警系统

**常用工具：**

| 工具 | 功能 | 特点 |
|------|------|------|
| **RestockPro** | 补货计算+预警 | 基于算法计算最佳补货时机 |
| **DataHawk** | 库存健康+趋势 | 可设置自定义阈值报警 |
| **Helium10** | Inventory Manager | 支持批量编辑+补货计算器 |
| **SellerMobile** | 库存预警+钉钉推送 | 支持企业微信/钉钉通知 |

### 3. 自建预警系统逻辑

```
IF DaysOfSupply < SafetyStockDays THEN
  SendAlert(product_id, "库存不足")
  CalculateRestockQuantity
  UpdatePOstatus

IF InventoryAge > 180 THEN
  SendAlert(product_id, "超龄库存风险")
  TriggerLiquidationFlow

IF InboundInventory == 0 AND OnHand == 0 THEN
  SendAlert(product_id, "完全断货")
  PauseAdForSKU
```

---

## 三、补货公式详解

### 安全库存公式

```
Reorder Point = (Average Daily Sales × Lead Time Days) + Safety Stock

Safety Stock = Z-score × σ_demand × √(Lead Time + Review Period)

其中：
- Z-score: 95%置信度取1.65
- σ_demand: 需求标准差
- Lead Time: 供应商交货天数
- Review Period: 补货检查周期
```

### 简化实战公式（卖家常用）

```
补货数量 = 日均销量 × (交期天数 + 安全天数) × 1.2倍安全系数
```

例如：日均销量10，交期30天，安全天数7天  
补货量 = 10 × (30+7) × 1.2 = **444件**

### ABC分类补货策略

| 分类 | 日均销量 | 安全库存倍数 | 补货频率 |
|------|---------|------------|---------|
| **A类**（爆款） | >50单/天 | ×2.0 | 每周补货 |
| **B类**（稳定款） | 10-50单/天 | ×1.5 | 每两周补货 |
| **C类**（长尾） | <10单/天 | ×1.2 | 每月补货 |

---

## 四、库存健康监控维度

### 1. IPI（Inventory Performance Index）评分

亚马逊IPI评分四个维度：
1. **FBA Inventory Age**（库存龄期）
2. **Stranded Inventory Rate**（滞留库存率）
3. **FBA Sell-Through**（FBA销转率）
4. **In-Stock Rate**（在库率）

| IPI分数 | 风险等级 | 影响 |
|--------|---------|------|
| ≥500 | 🟢 正常 | 无限制 |
| 350-500 | 🟡 警告 | 可能受限 |
| <350 | 🔴 危险 | 仓储容量受限 |

### 2. 七天内断货预警

触发条件：
```
IF (On-Hand - Reserved) < (DailySales × 7) THEN
  Alert: "预计七天内断货"
```

---

## 五、新知识判断

- **智能预警阈值自定义**：✅ 是新知识——默认阈值不一定适合所有品类，理解如何配置安全天数和报警触发条件很重要
- **IPI评分四个维度**：✅ 是新知识——系统理解亚马逊如何评分IPI才能有效优化
- **超龄库存费用分级**：✅ 是新知识——之前学过头但不够系统，这条补充了具体费用触发线
- **安全库存公式（Z-score）**：⚠️ 有基础但补充了完整版公式
- **ABC分类补货**：✅ 新知识，实战价值高

---

## 六、内容判断

| 观点 | 是否正确 | 说明 |
|------|---------|------|
| Days of Supply < 7天需预警 | ✅ 正确 | 行业通行经验值 |
| 超180天产生高额附加费 | ✅ 正确 | 亚马逊官方政策 |
| IPI需≥500分才无限制 | ✅ 正确 | 亚马逊官方要求 |
| 安全库存公式 | ✅ 基本正确 | Z-score 1.65对应95%置信度 |
| ABC分类标准 | ⚠️ 经验值 | 各家标准略有不同，供参考 |

---

## 七、关联已学主题

- **Topic 73**（亚马逊仓储IPI优化）：IPI四维评分体系已学，本主题是监控工具补充
- **Topic 135**（亚马逊仓储IPI优化深度攻略）：重复但更深入，本主题不重复
- **Topic 136**（FBA库存补货公式与智能补货策略）：两者高度关联，可合并复习
- **Topic 109**（亚马逊库存预警与风险管理）：内容高度重合，**本主题无需单独学习**，建议跳过或合并

---

## 八、实战要点

1. **设置双重预警**：同时监控"七天内断货"和"十四天内断货"，给补货留出缓冲
2. **关注Reserved库存**：不能仅看 On-Hand，实际可售 = On-Hand - Reserved
3. **IPI优化优先处理滞留库存**：Stranded Inventory 是最容易解决的问题
4. **A类产品补货系数用1.5-2.0倍**：防止突发断货影响排名
5. **超270天库存立即启动清仓**：费用会迅速侵蚀利润

---

## 九、易混淆概念

| 混淆项 | 区别 |
|--------|------|
| On-Hand vs Available | On-Hand包含Reserved，Available = 可售数量 |
| Days of Supply vs Lead Time | DoS是库存够卖多少天，Lead Time是交货需要多少天 |
| Restock Alert vs Low Inventory Alert | Restock是亚马逊计算的建议，Low Inventory是固定阈值 |

---

## 十、总结

本主题覆盖库存监控的核心工具和智能预警逻辑，是所有运营人员每天必看的仪表盘。核心干货：
1. **DoS（可售天数）是最重要单值指标**
2. **超180天库存要立即处理**
3. **IPI四个维度决定仓储容量**
4. **安全库存公式 = 日均销量 × (交期+安全天数) × 系数**
5. **预警系统必须配合补货公式，不能只报警不自动计算补货量**

> 🦞 今天的虾也努力搞懂库存预警系统