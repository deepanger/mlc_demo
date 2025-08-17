# Model Lifecycle Center (MLC) - 技术规格说明书

## 目录
1. [项目概述](#1-项目概述)
2. [业务场景分析](#2-业务场景分析)
3. [系统架构](#3-系统架构)
4. [技术栈选择](#4-技术栈选择)
5. [数据模型设计](#5-数据模型设计)
6. [用户界面设计](#6-用户界面设计)
7. [功能模块详述](#7-功能模块详述)
8. [核心特性](#8-核心特性)
9. [项目部署](#9-项目部署)
10. [开发规范](#10-开发规范)
11. [未来规划](#11-未来规划)

---

## 1. 项目概述

### 1.1 背景与问题
在银行反洗钱（AML）业务中，我们使用Google AML AI平台进行机器学习模型的训练和预测。当前分析流程存在以下问题：

**业务背景**：
- 使用Google AML AI功能进行模型训练和预测操作
- 训练结果和预测结果以tables形式存储在BigQuery数据集中
- 需要定期重新训练模型以适应新的金融犯罪行为模式
- 每次重训练后需要进行完整的模型验证和分析
- **新增挑战**：业务扩展到全球多个市场（如英国、香港、新加坡、墨西哥），需要对各市场的模型生命周期进行独立管理和追踪。

**现有痛点**：
- 分析师需要在Jupyter Notebook中手动输入run_id和其他参数
- 过程效率低下、易于出错且难以追溯和共享
- 缺乏统一的分析结果展示和管理平台
- **新痛点**：缺乏一个全球视角的模型管理入口，无法便捷地在不同市场的分析环境间切换。

### 1.2 解决方案
Model Lifecycle Center (MLC) 是一个Web应用原型，现已升级为全球模型生命周期管理平台，专为银行AML模型分析场景设计：

**核心价值**：
- **全球市场入口**：提供一个统一的首页，展示所有支持的国家/地区，作为进入各个市场特定分析环境的门户。
- **国家级模型生命周期**：为每个国家提供独立的模型时间线（Timeline）和重训练（Retrain）入口。
- **替代Jupyter Notebook工作流**：将手动输入run_id和参数的过程Web化，并在特定国家的上下文中进行。
- **自动化数据查询**：集成BigQuery连接，自动执行SQL分析查询（未来规划）。
- **统一结果展示**：以专业仪表盘形式展示特定国家模型的分析结果。

**技术架构**：
- **前端Web界面**：提供清晰的全球-国家两级导航结构。
- **后端数据处理**：Python + Django，处理按国家区分的业务逻辑。
- **Demo框架设计**：使用模拟数据建立完整架构，预留真实数据接入点。
- **可扩展设计**：便于未来接入Google AML AI和BigQuery真实数据。

### 1.3 目标用户
- **AML分析师**：进行各市场模型训练后的分析验证工作。
- **全球模型管理团队**：需要概览各市场的模型状态，并进行统一协调。
- **机器学习工程师**：负责各市场模型的重训练和性能监控。
- **合规团队**：需要查看各市场模型验证结果和合规报告。
- **风险管理团队**：评估新模型在全球不同市场对金融犯罪检测的有效性。

### 1.4 项目定位
**Demo性质**：
- 当前为概念验证和框架搭建阶段
- 使用模拟数据模拟真实BigQuery查询结果
- 重点在于建立完整的、分国家的Web化分析流程
- 为未来接入Google AML AI和BigQuery做准备

**未来扩展**：
- 集成Google Cloud BigQuery数据源
- 接入Google AML AI模型训练和预测结果
- 实现真实的SQL查询和数据分析逻辑
- 添加跨国模型性能对比功能

---

## 2. 业务场景分析

### 2.1 真实业务流程
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   全球市场概览  │    │   选择特定市场  │    │   模型生命周期  │
│                 │    │ (UK, HK, SG, MX)│    │                 │
│ • 各国入口      │───►│                 │───►│ • 时间线 (Timeline)│
│ • 统一门户      │    │                 │    │ • 重训练 (Retrain) │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │                       │
                       ┌─────────────────┐    ┌─────────────────┐
                       │   模型分析 (分国家)│    │   结果验证 (分国家)│
                       │                 │    │                 │
                       │ • Prediction Info│───►│ • Transaction   │
                       │ • Web化参数输入 │    │   Analysis      │
                       │ • 自动化查询    │    │ • Target Analysis│
                       └─────────────────┘    └─────────────────┘
```

### 2.2 当前痛点分析
| 问题类别 | 具体问题 | 影响程度 |
|----------|----------|----------|
| **全局管理** | 缺乏统一的全球市场模型入口 | 高 |
| **效率问题** | 在不同市场的分析环境间切换繁琐 | 高 |
| **一致性问题** | 不同分析师可能使用不同的查询逻辑 | 中 |
| **可追溯性** | 分析结果依赖截图，难以追溯和复现 | 高 |
| **协作问题** | 结果分享依赖文档整理，效率低下 | 中 |

### 2.3 解决方案价值
| 改进点 | 现状 | 目标 |
|--------|------|------|
| **全局导航** | 无 | 统一的全球市场入口页 |
| **参数输入** | 手动在Notebook中修改 | Web表单化输入（按国家区分） |
| **数据查询** | 每次手动执行SQL | 自动化后台查询（按国家区分） |
| **结果展示** | 截图+手动整理 | 统一Web仪表盘（按国家区分） |
| **流程标准化** | 依赖个人经验 | 标准化、分国家的分析流程 |

---

## 3. 系统架构

### 3.1 整体架构
**当前Demo架构**：
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   前端界面      │    │   Django后端    │    │   模拟数据      │
│ (全球/国家两级) │    │                 │    │                 │
│ • Bootstrap UI  │◄──►│ • 视图逻辑(分国家)│◄──►│ • SQLite数据库  │
│ • 响应式设计    │    │ • 业务逻辑      │    │ • 模拟BigQuery  │
│ • HTMX交互      │    │ • 数据分析      │    │   查询结果      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                       ┌─────────────────┐
                       │   分析引擎      │
                       │                 │
                       │ • Pandas处理    │
                       │ • Matplotlib图表│
                       │ • 模拟SQL逻辑   │
                       └─────────────────┘
```

**未来目标架构**：
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   前端界面      │    │   Django后端    │    │  Google Cloud   │
│                 │    │                 │    │                 │
│ • 统一分析界面  │◄──►│ • 参数验证      │◄──►│ • BigQuery      │
│ • 实时结果展示  │    │ • SQL查询引擎   │    │ • AML AI Tables │
│ • 历史记录管理  │    │ • 数据处理      │    │ • Train/Predict │
└─────────────────┘    └─────────────────┘    │   Run Results   │
                                │              └─────────────────┘
                       ┌─────────────────┐
                       │   分析引擎      │
                       │                 │
                       │ • 真实SQL查询   │
                       │ • 数据聚合分析  │
                       │ • 自动化图表    │
                       └─────────────────┘
```

### 3.2 应用层次
**当前Demo实现**：
- **表现层**：Bootstrap + 自定义CSS + HTMX，实现全球入口和分国家的两级响应式Web界面。
- **业务层**：Django视图和表单处理，按国家代码处理数据验证和业务流。
- **数据层**：Django ORM + SQLite，`AnalysisRun`模型通过`country`字段模拟分国家的数据结构。
- **分析层**：Pandas数据处理 + Matplotlib图表生成，模拟SQL分析逻辑。

### 3.3 数据流设计
**模拟数据流（当前）**：
```
用户选择国家 → 进入国家级页面 → 用户输入run_id → 哈希生成种子 → 模拟数据生成 → 图表渲染 → Web展示
```

**真实数据流（目标）**：
```
用户选择国家 → 用户输入run_id → 参数验证 → BigQuery查询（含国家过滤） → 数据聚合分析 → 图表生成 → Web展示
```

---

## 4. 技术栈选择

### 4.1 后端技术
| 技术 | 版本 | 用途 |
|------|------|------|
| Django | 5.2.5 | Web框架，提供ORM、路由、模板系统 |
| SQLite | 内置 | 轻量级数据库，适合原型开发 |
| Python | 3.12.7 | 主要编程语言 |

### 4.2 前端技术
| 技术 | 版本 | 用途 |
|------|------|------|
| Bootstrap | 5.3.3 | 响应式UI框架 |
| django-crispy-forms | 2.x | 表单美化和验证 |
| htmx | 1.9.10 | 提升页面局部刷新和交互体验 |
| 原生JavaScript | ES6+ | 基础交互功能，如进度追踪 |

### 4.3 数据分析技术
| 技术 | 版本 | 用途 |
|------|------|------|
| Pandas | 2.0+ | 数据处理和表格生成 |
| Matplotlib | 3.7+ | 图表绘制和可视化 |
| NumPy | 1.24+ | 数值计算支持 |

### 4.4 开发工具
| 工具 | 用途 |
|------|------|
| uv | Python包管理器 |
| pyproject.toml | 项目配置管理 |
| Black | 代码格式化 |
| Flake8 | 代码质量检查 |

---

## 5. 数据模型设计

### 5.1 核心实体

#### BaseModel (基础模型)
```python
class BaseModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
```

#### AnalysisRun (分析运行)
```python
class AnalysisRun(models.Model):
    base_model = models.ForeignKey(BaseModel, on_delete=models.CASCADE)
    country = models.CharField(max_length=10, default='uk', help_text="Country code, e.g., uk/hk/mx/sg")
    run_id = models.CharField(max_length=255)
    month = models.CharField(max_length=20, default="2025-07")
    customer_count = models.IntegerField(default=10000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('base_model', 'run_id', 'country')
```

### 4.2 数据关系
- 一个基础模型可以有多个分析运行。
- 每个`run_id`在同一基础模型和同一国家的组合下是唯一的。
- 支持跨国家的`run_id`重复（例如，英国和香港可以有相同的`run_id`）。

---

## 6. 用户界面设计

### 6.1 整体布局
应用包含两种主要布局：

**1. 全球入口页 (`/`)**
```
┌─────────────────────────────────────────────────┐
│                页面标题栏                        │
│        Model Lifecycle Center · Global Markets │
├─────────────────────────────────────────────────┤
│                                                 │
│                 主内容区 (无侧边栏)              │
│                                                 │
│        • 四个国家卡片 (UK, HK, MX, SG)         │
│        • 每个卡片包含 "Timeline" 和 "Retrain" 链接 │
│                                                 │
└─────────────────────────────────────────────────┘
```

**2. 国家级分析页 (`/<country_code>/...`)**
```
┌─────────────────────────────────────────────────┐
│                页面标题栏                        │
│            Model Lifecycle Center              │
├─────────────┬───────────────────────────────────┤
│   侧边导航   │                                   │
│            │                                   │
│ • 基础模型   │            主内容区                │
│   选择器    │                                   │
│            │        • 表单和数据               │
│ • 页面导航   │        • 图表和表格               │
│   - Timeline (新增) │        • 分析结果                │
│   - 预测信息 │                                   │
│   - ...    │                                   │
└─────────────┴───────────────────────────────────┘
```

### 6.2 设计主题
- **主色调**：暗红色 (`#9A2A2A`) 用于标题、按钮和视觉强调元素。
- **背景色**：浅灰色 (`#fafafa` 或 `#f8f9fa`) 提供清爽的视觉体验。
- **视觉增强**：首页使用几何分割线、卡片悬停效果、圆形国旗等元素提升设计感。
- **侧边栏**：白色背景 (`#ffffff`) 带阴影效果。

### 6.3 响应式设计
- 使用Bootstrap网格系统，确保在桌面、平板和手机上均有良好表现。
- 首页国家卡片布局会根据屏幕宽度自动调整。
- 分析页面的表格和图表自适应屏幕尺寸。

---

## 7. 功能模块详述

### 7.1 Home (全球入口)
**路径**: `/`

**功能特性**:
- 无需登录的公开访问页面。
- 以卡片形式展示所有支持的国家/地区（英国、香港、墨西哥、新加坡）。
- 每个国家卡片包含其国旗、名称以及两个主要操作链接：
  - **Timeline**: 跳转到该国的模型生命周期时间线页面。
  - **Retrain**: 跳转到该国的模型重训练快捷入口页面。
- 页面设计经过美化，包含标题栏、几何分割线和交互式卡片。

### 7.2 Country Timeline (国家时间线)
**路径**: `/<slug:country_code>/timeline/`

**功能特性**:
- 展示特定国家模型的关键生命周期事件（模拟数据）。
- 包含侧边栏，允许在不同基础模型间切换。
- 提供返回全球首页和进入重训练页面的链接。

### 7.3 Country Retrain (国家重训练)
**路径**: `/<slug:country_code>/retrain/`

**功能特性**:
- 作为特定国家所有分析页面的快捷方式中心。
- 包含侧边栏，允许在不同基础模型间切换。
- 链接到该国家的所有核心分析页面（如预测信息、交易分析等）。

### 7.4 Prediction Information (预测信息)
**路径**: `/<slug:country_code>/prediction-info/`

**功能特性**:
- **国家限定**: 所有操作和数据显示都基于URL中的`country_code`。
- 基础模型选择器。
- Run ID批量输入（支持逗号分隔）。
- 自动显示该国家、该模型下最近5个运行记录。
- 使用HTMX实现表单提交和结果的局部刷新。

### 7.5 Transaction & Target Analysis (交易与目标分析)
**路径**: `/<slug:country_code>/transaction-analysis/`, `/<slug:country_code>/target-analysis/`

**功能特性**:
- **国家限定**: 所有操作和数据显示都基于URL中的`country_code`。
- 基础模型和Run ID联动选择，下拉框只显示属于当前国家和模型的Run ID。
- 动态生成和可视化特定国家运行的分析数据。

### 7.6 其他分析页面
**路径**: `/<slug:country_code>/...`

**功能特性**:
- 所有其他分析页面（Model Proving, Forecasting等）都已适配国家限定的URL结构。
- 均包含侧边栏，并能在不同基础模型间切换。

---

## 8. 核心特性

### 8.1 多国架构
- **URL驱动**: 通过URL中的国家代码实现清晰的数据和视图隔离。
- **数据隔离**: `AnalysisRun`模型中的`country`字段确保了数据的国家归属。
- **可扩展性**: `SUPPORTED_COUNTRIES`配置使得未来增加新国家变得容易。

### 8.2 数据验证
- **Run ID格式控制**: 正则表达式 `^[a-zA-Z][a-zA-Z0-9_]*$`
- **唯一性约束**: `(base_model, run_id, country)` 联合唯一。
- **实时表单验证**: 前端和后端双重验证。

### 8.3 用户体验
- **两级导航**: 从宏观（全球）到微观（国家）的清晰导航路径。
- **智能切换**: 基础模型变更时，页面自动刷新以显示相关数据。
- **进度追踪**: 使用localStorage在客户端追踪用户在分析流程中的完成状态。
- **HTMX增强**: 在预测信息页面实现无刷新提交和响应，提升流畅度。

---

## 9. 项目部署

### 9.1 环境准备
```bash
# 创建虚拟环境
uv venv
source .venv/bin/activate

# 安装依赖
uv pip install -r requirements.txt
# 或者，如果使用pyproject.toml
uv pip install -e .
```

### 9.2 数据库初始化
```bash
# 执行迁移
python manage.py migrate

# 创建示例数据
python create_sample_data.py
```

### 9.3 运行服务
```bash
# 启动开发服务器
python manage.py runserver

# 访问应用
# http://localhost:8000
```

### 9.4 项目结构
```
mlc_demo/
├── .venv/                          # 虚拟环境
├── pyproject.toml                  # 项目配置
├── manage.py                       # Django管理入口
├── create_sample_data.py           # 示例数据脚本
├── mlc_center/                     # Django项目配置
│   ├── settings.py
│   └── urls.py
└── core/                           # 核心应用
    ├── models.py                   # 数据模型
    ├── views.py                    # 视图逻辑
    ├── forms.py                    # 表单定义
    ├── urls.py                     # 应用路由
    ├── analysis_utils.py           # 分析工具
    ├── templates/core/             # 模板文件
    │   ├── base.html
    │   ├── home.html               # 全球入口页
    │   ├── country_timeline.html   # 国家时间线
    │   ├── country_retrain.html    # 国家重训练入口
    │   ├── prediction_info.html
    │   ├── transaction_analysis.html
    │   └── ... (其他分析页面)
    └── static/core/                # 静态资源
        ├── custom.css
        └── vendor/flags/           # 国旗图片
```

---

## 10. 开发规范

### 10.1 代码风格
- 使用Black进行代码格式化
- 遵循PEP 8编码规范
- 88字符行长度限制

### 10.2 命名规范
- **模型**: 使用驼峰命名法 (BaseModel)
- **视图**: 使用下划线命名法 (prediction_info_view)
- **模板**: 使用下划线命名法 (prediction_info.html)
- **CSS类**: 使用短横线命名法 (nav-link, country-card)

### 10.3 文档规范
- 所有函数和类需要docstring
- 复杂逻辑需要行内注释
- API变更需要更新文档

### 10.4 测试规范
- 使用pytest进行单元测试
- 视图函数需要测试覆盖
- 表单验证需要测试覆盖

### 10.5 版本控制
- 使用语义化版本号 (Semantic Versioning)
- 提交信息遵循约定式提交规范
- 功能开发使用feature分支

---

## 11. 未来规划

### 11.1 技术架构升级

#### 数据源集成
```python
# 未来BigQuery连接配置
from google.cloud import bigquery

class BigQueryService:
    def __init__(self, country_code):
        self.client = bigquery.Client()
        # 数据集可以根据国家进行区分
        self.dataset_id = f"aml_ai_results_{country_code}"

    def query_train_results(self, run_id):
        """查询训练结果表"""
        query = f"""
        SELECT * FROM `{self.dataset_id}.train_results`
        WHERE run_id = '{run_id}'
        """
        return self.client.query(query).to_dataframe()
# ...
```

#### SQL查询模板化
```python
# 分析查询模板
TRANSACTION_ANALYSIS_QUERY = """
WITH daily_stats AS (
  SELECT
    DATE(transaction_timestamp) as date,
    COUNT(*) as transaction_count,
    SUM(amount) as total_amount,
    SUM(CASE WHEN ml_score > {threshold} THEN 1 ELSE 0 END) as alerts
  FROM `{dataset}.prediction_results_{country_code}` -- 表名也可分国家
  WHERE run_id = '{run_id}'
  GROUP BY DATE(transaction_timestamp)
)
SELECT
  date,
  transaction_count,
  total_amount,
  alerts,
  SAFE_DIVIDE(alerts, transaction_count) * 100 as alert_rate
FROM daily_stats
ORDER BY date
"""
```

### 11.2 功能扩展路线图

#### 第一阶段：真实数据集成（3个月）
- [ ] Google Cloud认证和权限配置
- [ ] BigQuery连接器开发（支持多国家数据集）
- [ ] SQL查询引擎重构
- [ ] 数据验证和错误处理

#### 第二阶段：分析功能增强（6个月）
- [ ] **跨市场模型性能对比仪表盘**
- [ ] 模型漂移检测（分国家）
- [ ] 自动化告警系统
- [ ] 历史趋势对比分析

#### 第三阶段：企业级功能（12个月）
- [ ] 用户权限管理系统（区分全球/国家级角色）
- [ ] 审计日志和合规报告
- [ ] API接口开发
- [ ] 性能优化和扩展
