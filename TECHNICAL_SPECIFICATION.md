# **技术规格说明书：Model Lifecycle Center (MLC Demo)**

## 1. 项目概述

### 1.1. 背景
当前，我行的反洗钱（AML）机器学习模型分析流程依赖于 Jupyter Notebook。分析师需要为每次模型训练或预测手动输入 `run_id`，然后从 Notebook 中截图分析结果（如表格和图表）并手动整理。此过程效率低下、易于出错且难以追溯和共享。

### 1.2. 目标
本项目旨在开发一个名为 **Model Lifecycle Center (MLC)** 的Web应用原型（Demo）。该应用将取代现有的 Notebook 工作流，提供一个集中化、可交互的界面来管理和分析 AML 模型的生命周期。其核心目标是：
- **简化工作流程**：用户只需输入 `run_id` 即可自动获取和展示相关分析。
- **提升可视化效果**：以专业的仪表盘（Dashboard）形式展示数据表格和图表。
- **构建可扩展框架**：初期使用模拟数据（Mock Data）搭建应用框架，为未来接入真实数据和后端逻辑奠定基础。

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
- 顶部包含“Model Lifecycle Center”标题和基础模型选择器。
- 引入 htmx.js 和自定义的 CSS 文件（用于配色和布局）。

### 5.2. Prediction Information 页面
- **URL**: `/` or `/prediction-info/`
- **功能**:
  1. 允许用户输入一个或多个 `run_id`（以逗号分隔）。
  2. 表单提交后，后端接收 `run_id`，为其创建 `AnalysisRun` 记录（如果不存在）。
  3. 使用 `htmx` 异步请求，在下方区域显示每个 `run_id` 的详细信息。
- **后端逻辑**:
  - `views.py`:
    - `GET` 请求：渲染带表单的页面。
    - `POST` 请求 (由 htmx 触发)：
      - 解析输入的 `run_id` 列表。
      - **模拟数据生成**:
        - 对每个 `run_id`，生成模拟元数据（如月份、客户数）。
        - 定义一个预期的 Table 列表（如 `['transactions', 'customer_profiles', 'alerts']`）。
        - 随机将其中一两个 Table 标记为“不可用”。
      - 渲染一个 HTML 片段 (partial) 并返回，htmx 将其插入到页面指定位置。
- **UI 展示**:
  - 一个清晰的表单，使用 `django-crispy-forms`。
  - 结果区以卡片（Card）形式展示每个 `run_id` 的信息，包含：
    - Run ID
    - Month
    - Customer Number
    - 可用 Table 列表（不可用的项以红色字体高亮）。

### 5.3. Transaction Analysis 页面
- **URL**: `/transaction-analysis/`
- **功能**:
  1. 提供一个下拉菜单，列出在 "Prediction Information" 页面输入并保存的所有 `run_id`。
  2. 用户选择一个 `run_id` 后，页面自动加载并显示相关的分析结果。
- **后端逻辑**:
  - `views.py`:
    - 接收选择的 `run_id`。
    - **模拟分析逻辑**: 调用一个独立的 `services.py` 或 `utils.py` 中的函数。
      - 该函数接收 `run_id`，使用 `pandas` 生成一个模拟的交易数据 DataFrame。
      - 使用 `matplotlib` 基于此 DataFrame 生成一个分析图表（例如，每日交易量柱状图）。
      - **图表处理**: 将 Matplotlib `Figure` 对象保存到内存中的 `BytesIO` 对象，然后进行 Base64 编码，以便在 HTML `<img>` 标签中直接显示。
    - 将 DataFrame (转换为 HTML) 和 Base64 编码的图表字符串传递给模板。
- **UI 展示**:
  - 页面顶部是 `run_id` 选择器。
  - 下方分为两部分：
    - 左侧或上方：以 HTML 表格形式展示 Pandas DataFrame。
    - 右侧或下方：显示 Matplotlib 生成的图表图片。

### 5.4. Target Analysis 页面
- **URL**: `/target-analysis/`
- **功能与逻辑**: 与 "Transaction Analysis" 页面非常相似。
- **后端逻辑**:
  - **模拟分析逻辑**:
    - 生成模拟的 Target 数据（例如，包含月份、Target 数量、分类 'Main'/'Others' 的 DataFrame）。
    - 生成一个按月展示 Target 数量的条形图或折线图。
- **UI 展示**:
  - `run_id` 选择器。
  - Target 数据表格。
  - Target 数量可视化图表。

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

1.  **初始化项目**:
    ```bash
    # 创建并激活虚拟环境
    uv venv
    source .venv/bin/activate
    
    # 安装核心依赖
    uv pip install django django-crispy-forms crispy-bootstrap5 django-htmx matplotlib pandas
    
    # 创建 Django 项目和应用
    django-admin startproject mlc_center .
    python manage.py startapp core
    ```
2.  **目录结构**:
    ```
    mlc_demo/
    ├── .venv/
    ├── mlc_center/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── core/
    │   ├── migrations/
    │   ├── templates/
    │   │   └── core/
    │   │       ├── base.html
    │   │       └── ... (other templates)
    │   ├── static/
    │   │   └── core/
    │   │       └── custom.css
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   └── services.py  # 用于放置模拟数据和分析的逻辑
    └── manage.py
    ```
3.  **运行开发服务器**:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

## 7. 待确认的问题 (已解决)

1.  **“基础模型 (Base Model)” 的具体作用？**
    - **回答**: 是一个标签，但会影响分析行为。所有模型的预期 Table 列表是一致的。

2.  **多 `run_id` 的分析逻辑？**
    - **回答**: 暂时按“选择其中一个 `run_id`”进行分析。

3.  **“不可用 Table” 的判断标准？**
    - **回答**: 与一个预定义的标准列表进行比对。
