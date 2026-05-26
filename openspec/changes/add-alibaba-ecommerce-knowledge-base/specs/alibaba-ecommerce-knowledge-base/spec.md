## ADDED Requirements

### Requirement: 独立阿里巴巴知识库目录
系统 SHALL 新增一个独立的阿里巴巴电商 Markdown 知识库目录，用于承载阿里巴巴相关电商知识。

#### Scenario: 创建独立目录
- **WHEN** 实施该变更
- **THEN** 系统 SHALL 创建独立目录，并 SHALL 避免把阿里巴巴主题混入现有 `cross-border-ecommerce/` 专题目录。

#### Scenario: 目录包含首页
- **WHEN** 用户打开阿里巴巴知识库目录
- **THEN** 目录 SHALL 包含可作为知识库入口的 `index.md` 首页。

### Requirement: 初始知识体系
阿里巴巴知识库 SHALL 包含覆盖主要阿里巴巴电商场景的初始主题结构。

#### Scenario: 初始模块可见
- **WHEN** 首次创建知识库
- **THEN** 它 SHALL 至少包含平台基础、1688、Alibaba.com/阿里国际站、采购供应链、商品发布、询盘转化、交易履约、支付结算、营销获客、数据分析、风控合规等模块。

#### Scenario: 主题地图可维护
- **WHEN** 后续继续补充知识
- **THEN** 知识库 SHALL 提供主题地图，用于记录应覆盖主题、优先级、目标路径和当前状态。

### Requirement: MkDocs 网页接入
阿里巴巴知识库 SHALL 接入现有 MkDocs Material 本地网页。

#### Scenario: 本地网页展示入口
- **WHEN** 用户访问本地 MkDocs 网页
- **THEN** 页面 SHALL 提供阿里巴巴电商知识库入口，并 SHALL 保留现有跨境电商知识库入口。

#### Scenario: 左侧目录可浏览
- **WHEN** 用户进入阿里巴巴知识库页面
- **THEN** 用户 SHALL 能通过 MkDocs 左侧目录浏览阿里巴巴知识库的 Markdown 文档。

### Requirement: 现有跨境电商知识库不被破坏
实施阿里巴巴知识库 SHALL 不破坏现有跨境电商知识库内容和网页浏览能力。

#### Scenario: 现有内容仍可构建
- **WHEN** 变更完成后运行 `mkdocs build --strict`
- **THEN** 构建 SHALL 成功，并 SHALL 包含现有跨境电商知识库内容。

#### Scenario: 现有目录不被重写
- **WHEN** 新增阿里巴巴知识库
- **THEN** 实施 SHALL 避免批量重写 `cross-border-ecommerce/` 下无关内容。

### Requirement: 刷新机制支持阿里巴巴知识库
知识刷新机制 SHALL 支持阿里巴巴知识库的扫描、报告和后续补全。

#### Scenario: 扫描阿里巴巴目录
- **WHEN** 对阿里巴巴知识库执行扫描
- **THEN** 工具 SHALL 生成该知识库的 inventory，包含文件路径、标题、标题层级、分类、文件类型和时效性标记。

#### Scenario: 生成刷新报告
- **WHEN** 阿里巴巴知识库执行一次刷新
- **THEN** 系统 SHALL 生成报告，记录新增主题、更新主题、延后项、来源依据和网页验证结果。

### Requirement: 时效性内容来源验证
阿里巴巴知识库中涉及平台规则、费用、交易保障、物流、支付和合规的内容 SHALL 在写入或更新前查验当前来源。

#### Scenario: 写入时效性主题
- **WHEN** 新增或更新阿里巴巴平台规则、费用、物流、支付或合规内容
- **THEN** 内容 SHALL 记录官方或高质量来源依据，或将无法确认的内容标记为待跟进。

### Requirement: 本地网页同步验证
每次阿里巴巴知识库内容变更后，系统 SHALL 验证本地网页已更新。

#### Scenario: 网页包含新增内容
- **WHEN** 新增阿里巴巴知识库页面并运行 MkDocs
- **THEN** 本地网页 SHALL 能访问新增页面，并 SHALL 在报告中记录验证结果。
