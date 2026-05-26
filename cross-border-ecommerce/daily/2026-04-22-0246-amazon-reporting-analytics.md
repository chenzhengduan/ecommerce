# 2026-04-22 02:46 - 跨境电商学习

## 主题 160：亚马逊订单报告与数据分析系统

---

### 一、亚马逊报告体系总览

亚马逊Seller Central提供完整的运营数据报告体系，分为以下几大模块：

| 报告类型 | 核心内容 | 访问路径 |
|---------|---------|---------|
| **销售报告** | 订单量、销售额、退款、绩效 | Reports → Fulfillment → Sales |
| **广告报告** | ACOS、ACoAS、RoAS、点击、曝光 | Reports → Advertising |
| **库存报告** | 可售天数、库龄、IPI、FBA库存 | Reports → Fulfillment → Inventory |
| **财务报告** | 收入、成本、利润、账目明细 | Reports → Payments |
| **税务报告** | VAT申报、销售税、1099-K | Reports → Tax Document Library |

---

### 二、销售报告（Sales Reports）

**核心报告：**

1. **Amazon Order Report（订单报告）**
   - 订单号、ASIN、数量、单价、运费、促销折扣
   - 购买时间、买家信息（部分遮蔽）
   - 用于分析订单趋势、热销时段、促销效果

2. **Flat File Order Report（平面文件订单报告）**
   - 比标准报告包含更多字段（SKU、item-quantity、item-price）
   - 适合批量数据处理和Excel/Power BI分析

3. **Sales Dashboard（销售仪表盘）**
   - 可视化展示：日/周/月销售额趋势
   - 热销ASIN排名
   - 购买按钮赢得率（Buy Box %）

**关键指标解读：**
- **Ordered Revenue（订购收入）**：买家下单时的金额（含预付款）
- **Net Revenue（净收入）**：实际到账金额（扣除退款）
- **Units Ordered（订购件数）**：订单包含的总商品数量

---

### 三、广告报告（Advertising Reports）

**亚马逊广告报告层级：**

| 层级 | 报告类型 | 核心指标 |
|------|---------|---------|
| **Campaign** | 活动总览 | Spend、Orders、ACOS |
| **Ad Group** | 广告组 | Bid、Impressions、Clicks |
| **Keyword** | 关键词 | Search terms、Match type |
| **Product Targeting** | 商品投放 | ASIN、Category targeting |
| **Placement** | 投放位置 | Top of search / Product page |

**核心指标计算公式：**

```
ACOS = 广告Spend ÷ 广告带来的Revenue × 100%
ACOS = 广告Spend ÷ (广告带来的Orders × 平均客单价) × 100%

TACOS（Total Advertising Cost of Sales）= 广告Spend ÷ 总Revenue × 100%
TACOS = ACOS × (广告Revenue ÷ 总Revenue)

RoAS（Return on Advertising Spend）= Revenue ÷ Spend
RoAS = 1 ÷ ACOS（RoAS = 4 等价于 ACOS = 25%）
```

**广告归因窗口：**
- **点击归因**：客户点击广告后7天内购买（SP/SB）
- **浏览归因**：客户未点击但浏览了商品详情页后7天内购买（SD展示型推广）
- 归因窗口直接影响ACOS计算准确性

**广告报表下载格式：**
- CSV格式支持自定义时间范围
- 可按Campaign/Ad Group/Keyword多层级汇总
- 建议每日下载存档（亚马逊仅保留90天数据）

---

### 四、库存报告（Inventory Reports）

**核心库存报告：**

1. **FBA Inventory Report**
   - 当前库存数量、可售数量、正在接收数量
   - 亚马逊运营中心位置
   - 库存龄期（Age）分布

2. **Aged Inventory Report（库龄报告）**
   - 识别超过90天、180天、365天的库存
   - 与LTSF长期仓储费直接关联
   - 按ASIN细分，帮助制定清仓策略

3. **Inventory Dashboard（库存仪表盘）**
   - DoS（Days of Supply）：可售天数
   - IPI Score：库存绩效指标（亚马逊每季度考核）
   - Restock Alerts：补货提醒

**库龄分级：**
- 0-90天：正常库存（无额外费用）
- 90-180天：开始产生标准仓储费
- 180-365天：费用增加，需关注
- 365天以上：LTSF长期仓储费（高额）

**安全库存计算公式：**
```
安全库存 = (日均销量 × 备货天数) + 安全缓冲

备货天数 = 生产/运输时间 + 处理时间 + 缓冲时间

例：日均销量20件，生产运输30天，处理7天，缓冲5天
安全库存 = 20 × (30+7+5) = 20 × 42 = 840件
```

---

### 五、财务报告（Payments Reports）

**核心报告：**

1. **Transaction Report（交易报告）**
   - 每笔订单的详细收支明细
   - 包含：商品收入、FBA费用、广告费、仓储费、退款等
   - 是利润计算的核心数据源

2. **Date Range Report（日期范围报告）**
   - 按时间段汇总收入与支出
   - 用于月度/季度财务复盘

3. **Statement（对账单）**
   - 银行转账记录
   - 每月汇总，可用于对账

**费用类别：**
- **Referral Fee（推荐费）**：亚马逊收取的成交佣金（6%-15%，类目不同）
- **FBA Fees（FBA费用）**：仓储费、配送费
- **Advertising Cost（广告成本）**：点击付费广告支出
- **Refund（退款）**：退款的金额（部分退款会按比例返还费用）

**利润计算示例：**
```
客单价：$50
商品成本：$15
物流成本：$8
亚马逊费用：$15（含Referral Fee 15% + FBA配送费）
广告费用：$5

毛利润 = $50 - $15 - $8 - $15 - $5 = $7
毛利率 = $7 / $50 = 14%
```

---

### 六、税务报告（Tax Document Library）

**关键报告：**

1. **VAT Settings（增值税设置）**
   - 各站点VAT税率配置
   - 发票开具设置

2. **Tax Document Library（税务文件库）**
   - 存储所有税务相关文件
   - 包含：VAT申报回执、所得税表、1099-K等

3. **跨境税务申报节点**
   - 英国站：季度VAT申报
   - 德国站：月度/季度VAT申报
   - 欧盟OSS/IOSS：一站式申报

---

### 七、第三方BI工具与SP API报告集成

**常见BI工具：**
- **DataHawk**：亚马逊数据分析平台，支持销售/广告/库存/财务多维分析
- **Helium 10**：选品+运营综合工具，含Cerebro关键词反查、Maria商品追踪
- **Sellics**：广告优化+财务分析+评论管理
- **Keepa**：价格追踪+历史数据
- **Excel/Power BI**：自建利润分析模型（需要整合Transaction Report数据）

**SP API报告接口（开发参考）：**
```json
// 可调用的报告类型
reports = [
    "GET_FBA_SALES_REPORT",       // 销售报告
    "GET_FBA_INVENTORY_REPORT",    // 库存报告
    "GET_FBA_REIMBURSEMENTS_REPORT", // 赔偿报告
    "GET_ADVERTISING_REPORT",      // 广告报告（需通过SP API广告模块）
    "GET_FLAT_FILE_ORDERS_DATA",   // 平面文件订单
]
```

**自建利润计算模型要素：**
1. 收入 = 订单金额（扣除退款）
2. 成本 = 商品成本 + 头程物流 + 关税
3. 亚马逊费用 = Referral Fee + FBA Fees
4. 广告费用 = PPC Spend
5. 利润 = 收入 - 成本 - 费用 - 广告

---

## 学习内容摘要

**主题：亚马逊订单报告与数据分析系统**

1. **销售报告**：订单报告、平板文件报告、销售仪表盘，核心指标为Ordered Revenue、Units Ordered、Buy Box %。

2. **广告报告**：ACOS = Spend÷Revenue，RoAS = Revenue÷Spend，TACOS = 广告Spend÷总Revenue（更全面）。归因窗口影响ACOS准确性（SP/SB 7天点击归因，SD 7天浏览归因）。

3. **库存报告**：Aged Inventory Report与LTSF直接关联，库龄分级决定费用等级。安全库存公式：日均销量×备货天数+缓冲。

4. **财务报告**：Transaction Report是利润计算核心，包含收入、FBA费用、广告费、退款等全明细。

5. **税务报告**：VAT设置和文件库需定期核查，欧盟OSS一站式申报可简化多国申报。

6. **第三方工具**：DataHawk/Helium10/Sellics为主流分析平台，SP API支持多类型报告接口，可自建BI。

## 对不对的判断

✅ **基本准确** — ACOS/RoAS计算公式、库龄分级与LTSF对应关系、亚马逊费用结构等核心逻辑正确。

⚠️ **注意**：亚马逊费用结构（Referral Fee、 fulfillment fees）因类目和尺寸而异，实际计算需参考亚马逊官方Fee Preview工具。

## 是不是新知识

**部分新知** — SP API报告类型和调用方式、广告归因窗口的精确描述，属于技术细节新知。财务报告的利润计算模型此前有涉及但较零散，本主题系统化了这些概念。

## 是否好理解

**较好理解** — 报告类型和指标体系清晰，逻辑为：销售数据（做什么）→ 广告数据（怎么推）→ 库存数据（怎么备）→ 财务数据（赚多少）。各模块数据可串联分析，适合搭建完整的数据驾驶舱。

---

🦞 今天的虾也努力工作中