## ADDED Requirements

### Requirement: 全量知识清单
刷新流程 SHALL 在提出内容补充或更新之前，扫描 `cross-border-ecommerce/` 下的所有 Markdown 文件。

#### Scenario: 清单包含正式笔记和学习日志
- **WHEN** 刷新流程开始执行
- **THEN** 它 SHALL 生成一个清单，包含每个 Markdown 文件的路径、识别出的标题、主要标题层级、分类，以及该文件看起来是正式主题笔记还是学习日志。

#### Scenario: 清单保留当前目录结构
- **WHEN** 刷新流程记录已有知识
- **THEN** 它 SHALL 保留原始文件路径和文件夹名称，不在清单阶段移动文件。

### Requirement: 缺失主题识别
刷新流程 SHALL 将当前知识清单与预期的跨境电商主题地图进行对比。

#### Scenario: 识别缺失主题
- **WHEN** 主题地图中存在必备主题，但当前清单中没有匹配的正式主题笔记
- **THEN** 刷新流程 SHALL 将该主题标记为缺失，并为它选择合适的 `cross-border-ecommerce/` 目标路径。

#### Scenario: 不重复创建已有主题
- **WHEN** 某个必备主题已经有匹配的正式主题笔记
- **THEN** 刷新流程 SHALL 避免创建重复笔记，并在需要改进时使用已有文件作为更新目标。

### Requirement: 过时内容识别
刷新流程 SHALL 识别可能因为包含时效性事实而过时的已有笔记。

#### Scenario: 标记时效性笔记
- **WHEN** 一篇笔记包含平台规则、费用、税务要求、合规义务、广告产品、物流限制、市场政策或工具推荐
- **THEN** 刷新流程 SHALL 在更新事实性表述之前，将该笔记标记为需要时效性检查。

#### Scenario: 稳定内容不强制查验
- **WHEN** 一篇笔记只覆盖稳定概念，且没有明显时效性事实
- **THEN** 刷新流程 SHALL 允许基于本地上下文做编辑改进，而不强制进行外部来源查验。

### Requirement: 来源验证后的更新
刷新流程 SHALL 在写入变化较快的事实之前，先用当前来源进行验证。

#### Scenario: 可以获得当前来源
- **WHEN** 刷新流程更新一个时效性事实
- **THEN** 它 SHALL 使用当前权威来源或高质量来源，并在更新后的笔记或刷新摘要中记录来源依据。

#### Scenario: 无法获得当前来源
- **WHEN** 某个时效性事实无法被验证
- **THEN** 刷新流程 SHALL 避免把该事实写成已确认结论，并 SHALL 将该项记录为待跟进内容。

### Requirement: 内容补充和更新行为
刷新流程 SHALL 在保留已有有效内容的前提下，补充缺失知识并更新过时或不完整笔记。

#### Scenario: 新增缺失笔记
- **WHEN** 某个缺失主题被选中创建
- **THEN** 刷新流程 SHALL 创建一篇 Markdown 笔记，包含清晰标题、结构化标题层级、可执行内容，以及必要的链接或参考来源。

#### Scenario: 更新已有笔记
- **WHEN** 一篇已有笔记过时、不完整或结构混乱
- **THEN** 刷新流程 SHALL 在原文件中更新内容，保留准确的已有材料，并只修改需要提升时效性、清晰度或覆盖度的部分。

### Requirement: 刷新摘要
刷新流程 SHALL 为每次执行生成摘要。

#### Scenario: 生成执行摘要
- **WHEN** 一次刷新执行完成
- **THEN** 它 SHALL 列出扫描文件数量、新增主题、更新主题、已检查的过时项、延后处理项，以及相关假设或来源限制。

### Requirement: 文档构建验证
刷新流程 SHALL 验证知识库在变更后仍然可以被渲染。

#### Scenario: MkDocs 构建成功
- **WHEN** 刷新流程修改了 Markdown 内容或文档配置
- **THEN** 它 SHALL 在项目环境中运行 `mkdocs build --strict`，并确认构建成功。

#### Scenario: MkDocs 构建失败
- **WHEN** `mkdocs build --strict` 在刷新后失败
- **THEN** 刷新流程 SHALL 在报告完成之前修复编码、路径、导航或 Markdown 问题。

### Requirement: 本地网页同步更新
刷新流程 SHALL 在每次内容变更后更新并验证 MkDocs 本地网页。

#### Scenario: 本地服务正在运行
- **WHEN** 刷新流程修改了 Markdown 内容且本地 MkDocs 服务正在运行
- **THEN** 它 SHALL 确认热重载后的页面包含本轮新增或更新内容。

#### Scenario: 本地服务未运行
- **WHEN** 刷新流程完成内容更新但本地 MkDocs 服务未运行
- **THEN** 它 SHALL 启动本地服务，或在刷新报告中记录启动命令和未启动原因。
