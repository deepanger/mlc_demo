# **技术规格说明书：Mode## 2. 技术选型

项目采用以下技术组合实现快速开发：

- ## 3. UI/UX 设计

- **项目名称**: Model Lifecycle Center（已实现完整标题## 3. UI/UX 设计

- **项目名称**: Model Lifecycle Center
- **整体布局**:
  - **左侧导航栏 (Sidebar)**：固定宽度，包含指向不同功能页面的链接。
  - **右侧主内容区 (Main Content)**：展示表单、数据表格、图表等核心内容。
- **色彩主题**:
  - **主色调**: 暗红色 (Dark Red, `#9A2A2A`)，用于标题、高亮和关键元素。
  - **背景色**: 浅灰色 (`#f8f9fa`)，营造清爽专业的视觉感受。
  - **侧边栏**: 白色背景 (`#ffffff`)，带有阴影效果。
  - **文本色**: 深灰色 (`#333333`, `#495057`)，确保良好的可读性。
- **核心交互**:
  - **基础模型选择器**: 在左侧导航栏上方，提供下拉菜单选择基础模型。
  - **动态内容加载**: 基础模型切换时自动更新关联的run_id列表。
  - **表单验证**: run_id必须以字母开头，包含字母、数字和下划线。
  - **响应式设计**: 使用Bootstrap实现移动端适配。布局**:
  - **左侧导航栏 (Sidebar)**：固定宽度，包含指向不同功能页面的链接。
  - **右侧主内容区 (Main Content)**：展示表单、数据表格、图表等核心内容。
- **色彩主题**（已更新为浅色主题）:
  - **主色调**: 暗红色 (Dark Red, `#9A2## 7. 核心功能特性

### 7.1. 数据验证与格式控制
- **Run ID格式验证**: 使用正则表达式确保run_id以字母开头，只包含字母、数字和下划线
- **基础模型关联**: run_id与特定的基础模型绑定，确保数据一致性
- **表单验证**: 实时验证用户输入，提供清晰的错误提示

### 7.2. 动态数据生成
- **一致性数据**: 使用run_id的哈希值作为随机种子，确保相同run_id总是生成相同的分析结果
- **多样化图表**:
  - Transaction Analysis: 交易量柱状图 + 告警率趋势图
  - Target Analysis: 目标数量堆叠条形图 + 检测率折线图
- **响应式表格**: 使用pandas生成的HTML表格，配合Bootstrap样式实现响应式设计

### 7.3. 用户体验优化
- **自动加载**: 页面加载时自动显示最近5个运行记录
- **智能切换**: 基础模型切换时自动更新关联的run_id列表
- **清爽界面**: 浅色主题设计，提升可读性
- **完整标题**: 显示"Model Lifecycle Center"完整名称

### 7.4. 技术架构优势
- **模块化设计**: 分析逻辑独立于视图逻辑，便于维护和扩展
- **Base64图表**: 图表直接嵌入HTML，无需静态文件管理
- **数据一致性**: 通过Django ORM确保数据关系完整性
- **可扩展性**: 预留接口便于接入真实数据源

## 8. 设计决策说明

1.  **基础模型 (Base Model) 的作用**:
    - 基础模型作为分类标签，不同模型有独立的run_id列表，实现了数据隔离

2.  **多 `run_id` 的分析逻辑**:
    - 在Prediction Information页面支持批量输入，在Analysis页面支持单选分析

3.  **"不可用 Table" 的判断标准**:
    - 与预定义的标准列表进行比对，随机模拟部分表格不可用的情况

4.  **Run ID格式要求**:
    - 必须以字母开头，支持字母、数字和下划线，提供实时验证

5.  **用户界面设计**:
    - 采用浅色主题、响应式设计和完整的用户交互流程、高亮和关键元素。
  - **背景色**: 浅灰色 (`#f8f9fa`)，营造清爽专业的视觉感受。
  - **侧边栏**: 白色背景 (`#ffffff`)，带有阴影效果。
  - **文本色**: 深灰色 (`#333333`, `#495057`)，确保良好的可读性。
- **核心交互**（已实现）:
  - **基础模型选择器**: 在左侧导航栏上方，提供下拉菜单选择基础模型。
  - **动态内容加载**: 基础模型切换时自动更新关联的run_id列表。
  - **表单验证**: run_id必须以字母开头，包含字母、数字和下划线。
  - **响应式设计**: 使用Bootstrap实现移动端适配。Django 5.2.5**
  - 功能强大，生态成熟，能快速构建稳健的Web应用。自带ORM、路由、模板系统。
- **数据库**: **SQLite**
  - 轻量级，无需额外配置，非常适合本地开发和原型演示。
- **前端增强**:
  - **django-crispy-forms + crispy-bootstrap5**: 用于美化 Django 表单，使其更专业、更易于管理。
  - **Bootstrap 5.3.3**: 提供响应式布局和现代化UI组件。
  - **原生JavaScript**: 实现基础模型切换和表单交互。
- **数据分析与可视化**:
  - **pandas**: 用于生成模拟数据表格。
  - **matplotlib**: 生成分析图表，支持Base64编码直接嵌入HTML。
  - **numpy**: 支持数据计算和随机数生成。
- **包管理**: **uv + virtual environment**
  - 新一代的 Python 包管理工具，速度极快，兼容 `pip` 和 `venv`。ter (MLC Demo)**

## 1. 项目概述

### 1.1. 背景
当前，我行的反洗钱（AML）机器学习模型分析流程依赖于 Jupyter Notebook。分析师需要为每次模型训练或预测手动输入 `run_id`，然后从 Notebook 中截图分析结果（如表格和图表）并手动整理。此过程效率低下、易于出错且难以追溯和共享。

### 1.2. 目标
本项目开发了一个名为 **Model Lifecycle Center** 的Web应用原型（Demo）。该应用取代了现有的 Notebook 工作流，提供了一个集中化、可交互的界面来管理和分析 AML 模型的生命周期。其核心目标：
- **简化工作流程**：用户只需选择基础模型和输入 `run_id` 即可自动获取和展示相关分析。
- **提升可视化效果**：以专业的仪表盘（Dashboard）形式展示数据表格和图表。
- **构建可扩展框架**：使用模拟数据（Mock Data）搭建了完整的应用框架，为未来接入真实数据和后端逻辑奠定了基础。

### 1.3. 目标用户
银行内部的机器学习工程师、数据分析师和模型验证团队。

## 2. 技术选型

为了实现快速开发和满足“尽可能少的技术栈”要求，我们采用以下技术组合：

- **后端框架**: **Django (最新版)**
  - 理由：功能强大，生态成熟，能快速构建稳健的Web应用。自带ORM、路由、模板系统，能很好地满足本项目需求。
- **数据库**: **SQLite**
  - 理由：轻量级，无需额外配置，非常适合本地开发和原型演示。
- **前端增强**:
  - **django-crispy-forms**: 用于美化 Django 表单，使其更专业、更易于管理。
  - **htmx**: 用于实现页面的局部动态刷新（如提交表单后只更新结果区域），避免全页面重新加载，提升用户体验，同时无需编写复杂的 JavaScript。
- **包管理**: **uv**
  - 理由：新一代的 Python 包管理工具，速度极快，兼容 `pip` 和 `venv`。
- **图表生成**: **Matplotlib**
  - 理由：延续现有 Notebook 的技术栈，易于将现有绘图逻辑迁移至后端。

## 3. UI/UX 设计

- **项目名称**: Model Lifecycle Center
- **整体布局**:
  - **左侧导航栏 (Sidebar)**：固定宽度，包含指向不同功能页面的链接。
  - **右侧主内容区 (Main Content)**：展示表单、数据表格、图表等核心内容。
- **色彩主题**:
  - **主色调**: 暗红色 (Dark Red, e.g., `#9A2A2A`)，用于标题、高亮和关键元素。
  - **辅助色**: 灰色 (Gray, e.g., `#333333` for background, `#CCCCCC` for text)，用于背景、文本和边框，营造专业稳重的视觉感受。
- **核心交互**:
  - **顶部模型选择器**: 在页面顶部或左侧导航栏上方，提供一个下拉菜单，用于选择“基础模型”。选定的模型ID将始终显示在该区域。
  - **动态内容加载**: 使用 `htmx` 实现，例如在输入 `run_id` 后，仅刷新下方的结果展示区。

## 4. 数据模型 (Database Schema)

由于是 Demo 阶段，我们仅需定义最核心的模型来支撑应用框架。数据将存储在 SQLite 中。

```python
# models.py

from django.db import models

class BaseModel(models.Model):
    """
    代表一个基础模型，例如 'AML_Model_v3'。
    """
    name = models.CharField(max_length=100, unique=True, help_text="基础模型的名称")
    description = models.TextField(blank=True, null=True, help_text="模型的简要描述")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class AnalysisRun(models.Model):
    """
    存储用户输入的 run_id 及其关联的基础模型。
    一个 run_id 对应一次分析会话。
    """
    base_model = models.ForeignKey(BaseModel, on_delete=models.CASCADE, related_name="runs")
    run_id = models.CharField(max_length=255, help_text="用户输入的 run_id")
    # 存储一些模拟的元数据
    month = models.CharField(max_length=20, default="2025-07")
    customer_count = models.IntegerField(default=10000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('base_model', 'run_id') # 同一模型下 run_id 是唯一的

    def __str__(self):
        return f"{self.run_id} for {self.base_model.name}"
```

## 5. 功能模块与页面设计

### 5.1. 基础布局 (base.html)
- 定义包含左侧导航栏和右侧内容区的 HTML 骨架。
- 顶部包含"Model Lifecycle Center"完整标题和基础模型选择器。
- 引入 Bootstrap 5.3.3 和自定义的 CSS 文件（用于配色和布局）。
- 实现了响应式设计和现代化的UI界面。

### 5.2. Prediction Information 页面
- **URL**: `/` or `/prediction-info/`
- **功能**:
  1. 允许用户选择基础模型并输入一个或多个 `run_id`（以逗号分隔）。
  2. **表单验证**: run_id必须以字母开头，包含字母、数字和下划线。
  3. 表单提交后，后端接收基础模型和 `run_id`，为其创建 `AnalysisRun` 记录（如果不存在）。
  4. **自动显示**: 页面加载时自动显示所选基础模型的最近5个run记录。
  5. 切换基础模型时，自动更新显示对应的最近记录。
- **后端逻辑**:
  - `views.py` - `prediction_info_view`:
    - `GET` 请求：渲染带表单的页面，显示所选基础模型的最近5个run。
    - `POST` 请求：
      - 解析输入的基础模型和 `run_id` 列表。
      - 表单验证：检查run_id格式（必须以字母开头）。
      - **模拟数据生成**:
        - 对每个 `run_id`，生成模拟元数据（如月份、客户数）。
        - 定义预期的 Table 列表（`['transactions', 'customer_profiles', 'alerts', 'sar_filings']`）。
        - 随机将其中一两个 Table 标记为"不可用"。
      - 渲染结果并返回。
- **UI 展示**:
  - 使用 `django-crispy-forms` 的清晰表单。
  - 基础模型选择器。
  - 结果区以卡片（Card）形式展示每个 `run_id` 的信息，包含：
    - Run ID
    - Month
    - Customer Number
    - 可用 Table 列表（不可用的项以红色字体高亮）。

### 5.3. Transaction Analysis 页面
- **URL**: `/transaction-analysis/`
- **功能**:
  1. 提供基础模型选择器和run_id下拉菜单，列出所选基础模型的所有 `run_id`。
  2. 用户选择基础模型和 `run_id` 后，页面自动加载并显示相关的分析结果。
  3. **数据验证**: 确保run_id属于所选的基础模型。
- **后端逻辑**:
  - `views.py` - `transaction_analysis_view`:
    - 接收选择的基础模型和 `run_id`。
    - **分析逻辑**: 调用 `analysis_utils.py` 中的 `generate_transaction_analysis` 函数。
      - 该函数接收 `run_id`，使用 `pandas` 生成模拟的交易数据 DataFrame。
      - 使用 `matplotlib` 基于此 DataFrame 生成分析图表（每日交易量柱状图和告警率趋势图）。
      - **图表处理**: 将 Matplotlib `Figure` 对象保存到内存中的 `BytesIO` 对象，然后进行 Base64 编码，以便在 HTML `<img>` 标签中直接显示。
    - 将 DataFrame (转换为 HTML) 和 Base64 编码的图表字符串传递给模板。
- **UI 展示**:
  - 页面顶部是基础模型和 `run_id` 选择器（两列布局）。
  - 下方分为两个卡片区域：
    - 第一个卡片：显示 Matplotlib 生成的图表图片。
    - 第二个卡片：以 HTML 表格形式展示 Pandas DataFrame。
    - 表格使用Bootstrap样式，具有良好的响应式设计。

### 5.4. Target Analysis 页面
- **URL**: `/target-analysis/`
- **功能与逻辑**: 与 "Transaction Analysis" 页面架构相同。
- **后端逻辑**:
  - `views.py` - `target_analysis_view`: 功能与transaction_analysis_view类似。
  - **分析逻辑**: 调用 `analysis_utils.py` 中的 `generate_target_analysis` 函数。
    - 生成模拟的 Target 数据（包含月份、Main Targets、Other Targets、Detection Rate的 DataFrame）。
    - 生成两个图表：按月展示 Target 数量的堆叠条形图和检测率趋势折线图。
- **UI 展示**:
  - 基础模型和 `run_id` 选择器。
  - Target 数据表格（使用相同的Bootstrap样式）。
  - Target 数量可视化图表（双图表布局）。

### 5.5. Model Proving & Forecasting 页面
- **URL**: `/model-proving/`, `/forecasting/`
- **功能**: 作为占位符页面。
- **后端逻辑**:
  - `views.py`:
    - 调用一个通用函数，生成一个随机的 Matplotlib 图表（例如，简单的正弦曲线或散点图）。
    - 将其转换为 Base64 编码并传递给模板。
- **UI 展示**:
  - 页面标题。
  - 一张居中显示的占位图表。

## 6. 项目设置与管理

1.  **项目初始化**:
    ```bash
    # 创建并激活虚拟环境
    uv venv
    source .venv/bin/activate

    # 安装核心依赖
    uv pip install django django-crispy-forms crispy-bootstrap5 matplotlib pandas numpy

    # 创建 Django 项目和应用
    django-admin startproject mlc_center .
    python manage.py startapp core
    ```

2.  **目录结构**:
    ```
    mlc_demo/
    ├── .venv/                          # 虚拟环境
    ├── db.sqlite3                      # SQLite数据库
    ├── manage.py                       # Django管理脚本
    ├── create_sample_data.py           # 示例数据创建脚本
    ├── TECHNICAL_SPECIFICATION.md     # 技术规格文档
    ├── mlc_center/                     # Django项目配置
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py                 # 项目设置
    │   ├── urls.py                     # 主URL配置
    │   └── wsgi.py
    └── core/                           # 核心应用
        ├── migrations/                 # 数据库迁移文件
        ├── templates/core/             # 模板文件
        │   ├── base.html              # 基础模板
        │   ├── prediction_info.html   # 预测信息页面
        │   ├── transaction_analysis.html # 交易分析页面
        │   ├── target_analysis.html   # 目标分析页面
        │   ├── model_proving.html     # 模型证明页面
        │   ├── forecasting.html       # 预测页面
        │   └── partials/              # 部分模板
        │       ├── run_details.html
        │       └── form_errors.html
        ├── static/core/               # 静态文件
        │   └── custom.css            # 自定义样式
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py                 # 数据模型
        ├── views.py                  # 视图函数
        ├── urls.py                   # URL路由
        ├── forms.py                  # 表单定义
        └── analysis_utils.py         # 分析工具函数
    ```

3.  **运行项目**:
    ```bash
    # 激活虚拟环境
    source .venv/bin/activate

    # 执行数据库迁移
    python manage.py migrate

    # 创建示例数据
    python create_sample_data.py

    # 启动开发服务器
    python manage.py runserver
    ```

4.  **示例数据**:
    - **基础模型**: AML_Model_v3, AML_Model_v4, Fraud_Detection_v2
    - **分析运行**: 每个模型包含4-5个符合格式的run_id（以字母开头）
    - **模拟数据**: 自动生成的交易和目标分析数据

## 7. 待确认的问题 (已解决)

1.  **“基础模型 (Base Model)” 的具体作用？**
    - **回答**: 是一个标签，但会影响分析行为。所有模型的预期 Table 列表是一致的。

2.  **多 `run_id` 的分析逻辑？**
    - **回答**: 暂时按“选择其中一个 `run_id`”进行分析。

3.  **“不可用 Table” 的判断标准？**
    - **回答**: 与一个预定义的标准列表进行比对。
