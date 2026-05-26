# 跨境电商学习笔记 — 2026-04-23 08:49

## 主题：Google Shopping Ads + 电商再营销像素实战

---

## 一、学习内容摘要

### 1. Google Shopping 广告基础

**什么是 Google Shopping**
- 基于产品 Feed 的图文广告，直接展示产品图片、价格、名称、评分
- 用户搜索相关商品时直接出现，比文字广告点击率更高
- 适合：有明确购买意向的消费者（高转化意图）

**Shopping 广告 vs 搜索广告**
| 维度 | 搜索广告（Text） | Shopping 广告 |
|------|-----------------|--------------|
| 展示内容 | 文字 | 产品图片+价格+评分 |
| 关键词 | 手动设置 | 系统根据产品属性匹配 |
| 点击率 | 较低 | 较高（图文更吸睛） |
| 适用阶段 | 品牌建设 | 直接转化 |

**Shopping Feed 核心字段**
- 产品ID（唯一标识）
- 标题（建议含核心关键词，最多150字符）
- 描述（详细说明，突出卖点）
- 价格（必填，含货币单位）
- 图片URL（主图，清晰白底）
- 可用性（库存状态：in stock/out of stock/preorder）
- Google产品类别（g:google_product_category）
- 条码（GTIN/UPC/EAN）
- 品牌（brand）
- 条件（condition：new/refurbished/used）

### 2. Google Merchant Center（GMC）设置

**GMC 作用**
- 存储和托管产品 Feed
- 将产品数据同步到 Google Ads 和 Google 发现广告

**GMC 常见被拒登原因**
1. 图片不符合规范（文字过多、模糊、非白底）
2. 价格与网站不一致
3. 税费/运费信息缺失或不完整
4. 产品ID重复
5. 违规产品类别（如：药品、武器、电子烟）
6. 跳转页面问题（URL无法访问或与Feed不符）

**GMC  Feed 提交方式**
- Google Sheets 手动上传（适合产品<1000个）
- CSV/TXT 文件上传（支持增量更新）
- API 接入（适合大量SKU，实时同步）
- Cronjob/定时任务自动更新（最佳实践：每天至少更新一次）

### 3. Google Ads  Shopping 广告系列设置

**出价策略选择**
- 智能购物（Smart Shopping）：机器学习优化，，适合有一定数据积累的账户
- 搜索广告 + Shopping 广告分开跑（更可控）
- 手动CPC（更精细，适合测试期）

**竞价维度**
- 按转化价值（ROAS）出价：设置目标ROAS，算法自动优化
- 按点击付费（CPC）：手动控制每次点击成本上限

**广告创意优化**
- 产品标题权重最高：品牌+核心关键词+规格参数
- 图片清晰、白底、无水印
- 价格要与网站同步（汇率变化时及时更新）

### 4. 再营销像素（Remarketing Pixel）

**什么是再营销**
- 用户访问过你的网站但未转化，通过广告再次触达
- 典型转化路径：访问 → 加购 → 未付款 → 再营销广告 → 完成购买

**Google Tag（gtag.js）基础**
```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

**关键事件追踪**
- view_item（浏览产品页）：触发购买意向
- add_to_cart（加入购物车）：高意图信号
- purchase（完成购买）：最终转化

**Facebook Pixel（Meta Pixel）对比**
| 维度 | Google Tag | Meta Pixel |
|------|------------|-----------|
| 平台 | Google Ads/Analytics | Facebook/Instagram |
| 优势 | 搜索意图强 | 社交属性强，覆盖面广 |
| 劣势 | 触达范围有限 | 用户社交数据隐私限制 |
| 最佳用途 | 搜索广告再营销 | 社交媒体再营销 |

**TikTok Pixel**
- 功能类似Facebook Pixel，用于TikTok广告追踪
- 支持：PageView、ViewContent、AddToCart、InitiateCheckout、Purchase

### 5. 跨平台再营销策略

**用户旅程再营销分层**
1. **品牌认知层**：吸引新用户，broad targeting
2. **考虑层**：对浏览过产品但未加购的用户，推送产品优势内容
3. **转化层**：对加购未付款用户，提供限时折扣或激励
4. **忠诚层**：对已购买用户，推送复购激励或交叉销售

**DPA（动态产品广告）**
- 根据用户浏览过的产品，自动展示对应的广告
- Facebook/Instagram/Google均支持DPA
- 适合：SKU多、产品更新快的电商

**频次控制（Frequency Capping）**
- 避免同一用户被过度曝光（引起反感）
- 建议：每周同一用户最多看到同一广告3-5次
- Google Ads和Meta Ads均可设置频次上限

---

## 二、对不对的判断

✅ **正确理解的部分：**
- Google Shopping 基于产品Feed匹配用户搜索的逻辑正确
- GMC拒登的常见原因识别准确
- 再营销分层策略框架合理
- 像素追踪事件类型（view_item/add_to_cart/purchase）是标准实现

⚠️ **需要补充或调整的部分：**
- Smart Shopping 实际上需要至少15-30天数据积累才能有较好表现，冷启动期效果可能不佳
- GMC政策经常更新，需要定期查阅官方政策页面
- 第三方Cookie（Chrome从2024年开始逐步淘汰）正在影响再营销精度，需要向第一方数据策略转型
- Facebook Pixel 14事件限制需要注意（14个标准事件上限）

---

## 三、是不是新知识

**新知识：**
- GMC Feed 字段规范的具体要求（特别是GTIN、税费设置）
- Google Smart Shopping 的冷启动限制
- 第三方Cookie淘汰对再营销的影响
- DPA动态产品广告的完整流程

**已掌握但加深理解的部分：**
- 再营销分层策略框架（之前有实战经验）
- Google Tag基础代码（之前接触过GA）
- 频次控制概念（已在FB广告中使用过）

---

## 四、是否好理解

**理解难度：★★★☆☆（中等）**

- Google Shopping的Feed结构和GMC设置有较多细节，需要实际操作才能掌握
- 再营销像素的代码实现对非技术人员有一定门槛
- 跨平台策略的整合思维是关键，需要经验积累

**实操建议：**
1. 先用Google Sheets测试Feed格式，熟悉后再上自动化
2. Google Tag和Facebook Pixel可以同时安装，不会冲突
3. 再营销频次要从低开始测试，逐步找到最优值
4. 关注Google Analytics 4（GA4）替代第三方Cookie的解决方案

---

## 五、相关主题

- Amazon SP广告 vs Google Shopping广告的选择
- Facebook/Instagram广告投放策略
- TikTok Pixel安装与转化追踪
- GA4（Google Analytics 4）事件追踪配置
- 邮件营销与再营销的协同

---

## 六、参考来源

- Google Ads 官方帮助文档
- Google Merchant Center 政策指南
- Meta Business 官方广告指南
- 行业实战经验总结
