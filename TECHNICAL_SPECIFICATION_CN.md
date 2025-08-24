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

#### Country (国家)
```python
class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=3, unique=True)
    flag_emoji = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
```

#### BaseModel (基础模型)
```python
class BaseModel(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    current_status = models.CharField(max_length=20, choices=[...])
    created_at = models.DateTimeField(auto_now_add=True)
```

#### AnalysisRun (分析运行)
```python
class AnalysisRun(models.Model):
    base_model = models.ForeignKey(BaseModel, on_delete=models.CASCADE)
    run_id = models.CharField(max_length=255)
    month = models.CharField(max_length=20, default="2025-07")
    customer_count = models.IntegerField(default=10000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('base_model', 'run_id')
```

#### ModelEvent (模型事件)
```python
class ModelEvent(models.Model):
    model = models.ForeignKey(BaseModel, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=20, choices=[...])
    event_date = models.DateTimeField()
    description = models.TextField()
    version = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
```

### 5.2 数据关系
- 每个国家可以有多个基础模型
- 每个基础模型可以有多个分析运行和模型事件
- `run_id`在同一基础模型下是唯一的
- 支持跨国家的数据隔离和管理

---

## 6. 用户界面设计

### 6.1 整体布局
应用包含两种主要布局：

**1. 全球入口页 (`/`)**
```
┌─────────────────────────────────────────────────┐
│          Model Lifecycle Center                 │
│        Global Model Management Portal          │
├─────────────────────────────────────────────────┤
│                                                 │
│              统计概览区域                        │
│                                                 │
│        • 四个国家卡片 (UK, HK, MX, SG)         │
│        • 每个卡片包含 "Timeline" 和 "Training" 链接│
│                                                 │
└─────────────────────────────────────────────────┘
```

**2. 国家级分析页 (`/<country_code>/...`)**
```
┌─────────────────────────────────────────────────┐
│               国家名称 + 标志                    │
│            Model Lifecycle Center              │
├─────────────┬───────────────────────────────────┤
│   侧边导航   │                                   │
│            │                                   │
│ • 全球仪表盘 │            主内容区                │
│ • 模型时间线 │                                   │
│ • 训练仪表盘 │        • 表单和数据               │
│            │        • 图表和表格               │
│ • 训练流程   │        • 分析结果                │
│   - 预测信息 │                                   │
│   - ...    │                                   │
└─────────────┴───────────────────────────────────┘
```

### 6.2 设计主题
- **主色调**：现代化渐变色方案，体现专业性
- **背景色**：浅灰色系，提供清爽的视觉体验
- **视觉增强**：国旗emoji、卡片悬停效果、现代化图标
- **响应式设计**：Bootstrap 5.3.3确保跨设备兼容性

---

## 7. 功能模块详述

### 7.1 全球入口页 (Home)
**路径**: `/`

**功能特性**:
- 展示所有支持的国家/地区（英国、香港、墨西哥、新加坡）
- 每个国家卡片包含：
  - 国旗和名称
  - 模型时间线链接
  - 模型训练链接
  - 当前活跃模型数量
- 全局统计信息展示
- 现代化设计，支持响应式布局

### 7.2 模型时间线页 (Model Timeline)
**路径**: `/<country_code>/timeline/`

**功能特性**:
- 展示特定国家的模型生命周期事件
- 时间线可视化展示
- 包含部署、重训练、更新等事件类型
- 当前模型状态概览
- 返回全球入口和进入训练仪表盘的导航

### 7.3 模型训练仪表盘 (Training Dashboard)
**路径**: `/<country_code>/training/`

**功能特性**:
- 国家级训练流程概览
- 工作流步骤展示
- 快速操作面板
- 当前模型管理
- 统计数据展示

### 7.4 训练流程页面
**路径**: `/<country_code>/training/...`

包含完整的ML训练流程：
- Prediction Information（预测信息）
- Transaction Analysis（交易分析）
- Target Analysis（目标分析）
- Model Proving（模型验证）
- Forecasting（预测）
- BTL Calculator（统计计算）
- Benchmark（基准测试）
- Documentation（文档生成）

---

## 8. 核心特性

### 8.1 多国家架构
- **URL驱动**：通过URL中的国家代码实现数据和视图隔离
- **数据隔离**：每个国家的模型和分析数据独立管理
- **可扩展性**：易于添加新的国家和市场

### 8.2 进度追踪系统
- **客户端存储**：使用localStorage追踪用户进度
- **视觉指示器**：完成状态的实时显示
- **按国家区分**：每个国家的进度独立追踪

### 8.3 用户体验优化
- **两级导航**：全球视图到国家视图的清晰层次
- **智能切换**：基础模型变更时的自动数据更新
- **响应式设计**：跨设备的一致体验

---

## 9. 项目部署

### 9.1 环境准备
```bash
# 创建虚拟环境
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# 或 .venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt
```

### 9.2 数据库初始化
```bash
# 执行迁移
python manage.py migrate

# 创建示例数据
python manage.py seed_countries
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
    │   ├── home.html
    │   ├── model_timeline.html
    │   ├── model_training_dashboard.html
    │   ├── country_base.html
    │   └── ... (其他分析页面)
    ├── static/core/                # 静态资源
    │   └── custom.css
    └── management/commands/        # 管理命令
        └── seed_countries.py
```

---

## 10. 开发规范

### 10.1 代码风格
- 使用Black进行代码格式化
- 遵循PEP 8编码规范
- 88字符行长度限制

### 10.2 命名规范
- **模型**: 使用驼峰命名法 (BaseModel, Country)
- **视图**: 使用下划线命名法 (home_view, model_timeline_view)
- **模板**: 使用下划线命名法 (home.html, model_timeline.html)
- **CSS类**: 使用短横线命名法 (nav-link, country-card)

### 10.3 文档规范
- 所有函数和类需要docstring
- 复杂逻辑需要行内注释
- API变更需要更新文档

---

## 11. 未来规划

### 11.1 第一阶段：真实数据集成（3个月）
- [ ] Google Cloud认证和权限配置
- [ ] BigQuery连接器开发（支持多国家数据集）
- [ ] SQL查询引擎重构
- [ ] 数据验证和错误处理机制

### 11.2 第二阶段：分析功能增强（6个月）
- [ ] 跨市场模型性能对比仪表盘
- [ ] 模型漂移检测（分国家）
- [ ] 自动化告警系统
- [ ] 历史趋势对比分析

### 11.3 第三阶段：企业级功能（12个月）
- [ ] 用户权限管理系统（区分全球/国家级角色）
- [ ] 审计日志和合规报告
- [ ] REST API接口开发
- [ ] 性能优化和水平扩展
- [ ] 高可用性部署方案

### 11.4 技术架构升级

#### BigQuery集成示例
```python
from google.cloud import bigquery

class BigQueryService:
    def __init__(self, country_code):
        self.client = bigquery.Client()
        self.dataset_id = f"aml_ai_results_{country_code}"

    def query_train_results(self, run_id):
        """查询训练结果表"""
        query = f"""
        SELECT * FROM `{self.dataset_id}.train_results`
        WHERE run_id = '{run_id}'
        """
        return self.client.query(query).to_dataframe()
```

#### 跨国家性能对比
```python
def compare_models_across_countries(model_name, metric='accuracy'):
    """比较同一模型在不同国家的性能"""
    countries = ['UK', 'HK', 'MX', 'SG']
    results = {}

    for country in countries:
        service = BigQueryService(country.lower())
        performance = service.get_model_performance(model_name, metric)
        results[country] = performance

    return results
```

---

## 结论

Model Lifecycle Center (MLC) 已从单一的分析工具演进为全球化的模型生命周期管理平台。通过引入多国家架构、现代化的UI设计和完整的工作流支持，MLC为银行AML业务提供了一个强大而灵活的解决方案。

当前的Demo版本建立了坚实的技术基础，为未来与Google Cloud和BigQuery的集成做好了准备。随着项目的持续发展，MLC将成为全球金融机构进行AML模型管理的标准平台。
