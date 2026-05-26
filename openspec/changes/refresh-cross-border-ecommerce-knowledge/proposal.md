## Why

当前 `cross-border-ecommerce/` 知识库已经积累了大量 Markdown 笔记，但缺失主题、过时的平台规则、税务合规变化和内容结构不一致，很难靠人工逐个发现。需要一个可重复执行的刷新计划：每次运行时先检查当前目录里的跨境电商知识，再补齐缺失内容，并更新已经过时的内容。

## What Changes

- 新增一个面向 `cross-border-ecommerce/` Markdown 目录的知识刷新流程。
- 定义每次执行时如何扫描已有文件、生成主题清单、识别缺失主题，并标记可能过时的内容。
- 定义如何补充缺失主题，以及如何在保留现有目录结构的前提下更新旧内容。
- 增加验证要求，确保刷新后的 Markdown 文件和 MkDocs 本地站点仍然可用。
- 不包含破坏性变更。

## Capabilities

### New Capabilities

- `cross-border-ecommerce-knowledge-refresh`: 定义跨境电商知识库的周期性刷新能力，包括全量扫描、缺口识别、过时内容检查、内容补充、内容更新和验证。

### Modified Capabilities

- 无。

## Impact

- 影响内容：`cross-border-ecommerce/` 下的 Markdown 文件，尤其是主题笔记、总览文件、索引文件和学习进度文件。
- 影响工具：可使用当前 MkDocs Material 配置做本地构建验证，但不需要替换现有文档站点方案。
- 外部依赖：对于平台规则、市场政策、税务合规、广告产品、物流限制、工具推荐等变化较快的内容，实施时需要查验当前公开来源。
