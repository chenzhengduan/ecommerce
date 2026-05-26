# 2026-04-21 跨境电商学习日志

## 主题：亚马逊API与数据接口（SP API / Seller Central API）

## 学习时间
2026-04-21 03:46（Asia/Shanghai）

---

## 学习内容摘要

### 什么是亚马逊 SP API？

**SP API（ Selling Partner API）** 是亚马逊官方提供的RESTful API接口，允许第三方开发者以编程方式接入亚马逊卖家平台（Seller Central），实现数据读取、功能自动化和业务流程集成。

前身为 MWS（Marketplace Web Service），**MWS已于2024年4月停用**，SP API全面取而代之。

---

### 核心API模块

**1. 目录API（Catalog API）**
- 获取商品目录信息（ASIN详情、变体关系、分类节点）
- 用途：选品调研、竞品分析、批量查ASIN信息

**2. 订单API（Orders API）**
- 获取订单列表、订单详情、退货信息
- 支持增量拉取（基于更新时刻戳）
- 用途：订单管理、发货同步、退款处理

**3. 报表API（Reports API）**
- 拉取各类业务报表（广告数据、库存报告、销售数据）
- 需先提交报表请求，再轮询获取
- 用途：数据分析、财务对账、库存预测

**4. 商品API（Products API / Pricing API）**
- 获取当前商品定价、库存状态、竞品价格
- 用途：智能定价、竞品监控

**5. FBA库存API（FBA Inventory API）**
- 实时库存量、预估入库时间、FBA健康状态
- 用途：FBA库存管理、避免断货

**6. 促销API（Promotions API）**
- 创建和管理促销活动（LD、DOTD、Coupon）
- 用途：促销自动化

**7. 品牌API（Brand Analytics / Brand Registry API）**
- 亚马逊品牌备案、品牌分析数据
- 用途：品牌运营分析

**8. 财务API（Finances API）**
- 获取收款明细、平台费用、退款等财务数据
- 用途：财务对账、利润核算

---

### 接入方式

**方式一：卖家自行开发**
- 在亚马逊 Seller Central → 整合 → API Section 注册应用
- 选择 appropriate API scopes（需要哪些权限）
- 获取 Client ID + Client Secret
- 通过 OAuth 2.0 完成授权
- 调用对应 endpoint

**方式二：使用现成工具（基于SP API构建）**
- **Helium 10**（选品+关键词+库存）
- **Perpetua**（自动广告投放，基于SP API）
- **Teikametrics**（广告+库存联动优化）
- **Sellics**（全流程一体化）
- **DataHawk**（数据分析+竞品监控）
- **Shopify亚马逊channel**（订单/库存自动同步）

**方式三：使用中间件平台**
- **Cloud.convert** / **Zapier** → 连接SP API到其他系统（Shopify、仓库系统、财务软件）
- **Integromat（Make）** → 低代码自动化

---

### 关键概念

**Rate Limit（速率限制）**
- 不同endpoint有不同的请求频率上限
- 通常：每个endpoint 2-6 requests/second
- 超出限制会返回429错误，需退避重试

**Pagination（分页）**
- 列表类API默认有最大返回条数限制
- 使用 `NextToken` 参数翻页

**Marketplace ID（市场ID）**
- 不同站点的Marketplace ID不同，例如：
  - US: `ATVPDKIKX0DER`
  - UK: `A1FCE83Z4GVMWS`
  - DE: `A1PA6795UKMFR9`
  - JP: `A1VC38T7YXB528`

**Refresh Token vs Access Token**
- Refresh Token：长期有效（通常1年内），用于换发Access Token
- Access Token：短期有效（通常1小时），实际调用API用

---

### 应用场景举例

**场景1：自动化订单处理**
Shopify收到订单 → SP API创建发货通知 → 追踪号自动同步亚马逊

**场景2：智能调价**
cron job 定时拉取竞品价格 → 算法计算最优价格 → SP API更新定价

**场景3：财务对账自动化**
每日自动拉取财务API数据 → 对比自有ERP系统 → 自动生成利润报表

**场景4：FBA库存预警**
监控FBA库存低于阈值 → 自动发送告警 → 触发补货流程

---

## 对不对的判断

✅ **基本准确**，SP API确实是亚马逊官方API标准，2024年MWS停用后SP API是唯一官方接口。

⚠️ **需要注意**：
- 具体Rate Limit数字因endpoint和卖家级别不同而有差异，以上数字为典型参考值
- 部分敏感API（如广告API）需要亚马逊白名单审批
- 开发者注册应用需要公司信息或个人身份证验证

---

## 是不是新知识

**是。** 对跨境电商从业者来说，SP API属于"会用工具"和"自己造工具"的分水岭。大部分中小卖家使用现成工具就够了，但中大型卖家或技术型团队，掌握SP API可以实现高度自动化和定制化。

---

## 是否好理解

**比较好理解。** SP API本质是标准REST API，有完善文档，对有开发基础的人容易上手。没有编程背景的运营者来说，理解为"亚马逊给开发者提供的官方数据通道"即可，具体调用可交给技术人员。

---

## 值得记住的点

1. MWS已死，SP API是唯一官方接口（2024年后）
2. SP API覆盖：订单、库存、广告、财务、促销、目录、报告等核心模块
3. 可自己开发，也可基于Helium 10、Perpetua等现成工具
4. OAuth 2.0授权流程是接入门槛
5. Rate Limit和Marketplace ID是实际开发中容易踩坑的点
