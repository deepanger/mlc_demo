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

**现有痛点**：
- 分析师需要在Jupyter Notebook中手动输入run_id和其他参数
- 使用Python调用SQL查询BigQuery数据进行分析和聚合
- 结果需要截图保存并手动整理到网页文档中
- 过程效率低下、易于出错且难以追溯和共享
- 缺乏统一的分析结果展示和管理平台

### 1.2 解决方案
Model Lifecycle Center (MLC) 是一个Web应用原型，专为银行AML模型分析场景设计：

**核心价值**：
- **替代Jupyter Notebook工作流**：将手动输入run_id和参数的过程Web化
- **自动化数据查询**：集成BigQuery连接，自动执行SQL分析查询
- **统一结果展示**：以专业仪表盘形式展示分析结果，无需截图整理
- **模型验证流程**：支持transaction analysis、target analysis、proving等完整分析流程

**技术架构**：
- **前端Web界面**：替代Jupyter Notebook的交互方式
- **后端数据处理**：Python + SQL查询逻辑，模拟真实BigQuery操作
- **Demo框架设计**：使用模拟数据建立完整架构，预留真实数据接入点
- **可扩展设计**：便于未来接入Google AML AI和BigQuery真实数据

### 1.3 目标用户
- **AML分析师**：进行模型训练后的分析验证工作
- **机器学习工程师**：负责模型重训练和性能监控
- **合规团队**：需要查看模型验证结果和合规报告
- **风险管理团队**：评估新模型对金融犯罪检测的有效性

### 1.4 项目定位
**Demo性质**：
- 当前为概念验证和框架搭建阶段
- 使用模拟数据模拟真实BigQuery查询结果
- 重点在于建立完整的Web化分析流程
- 为未来接入Google AML AI和BigQuery做准备

**未来扩展**：
- 集成Google Cloud BigQuery数据源
- 接入Google AML AI模型训练和预测结果
- 实现真实的SQL查询和数据分析逻辑
- 添加模型生命周期管理功能

---

## 2. 业务场景分析

### 2.1 真实业务流程
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   市场变化      │    │   模型重训练    │    │   结果验证      │
│                 │    │                 │    │                 │
│ • 新犯罪模式    │───►│ • Google AML AI │───►│ • Transaction   │
│ • 监管要求变化  │    │ • BigQuery存储  │    │   Analysis      │
│ • 业务规则调整  │    │ • Train/Predict │    │ • Target Analysis│
└─────────────────┘    │   Run Tables    │    │ • Model Proving │
                       └─────────────────┘    └─────────────────┘
                                │                       │
                       ┌─────────────────┐    ┌─────────────────┐
                       │   数据查询      │    │   结果整理      │
                       │                 │    │                 │
                       │ • Python + SQL  │───►│ • 截图保存      │
                       │ • Jupyter NB    │    │ • 手动整理      │
                       │ • 手动输入参数  │    │ • 文档汇总      │
                       └─────────────────┘    └─────────────────┘
```

### 2.2 当前痛点分析
| 问题类别 | 具体问题 | 影响程度 |
|----------|----------|----------|
| **效率问题** | 每次分析需要手动输入run_id和参数 | 高 |
| **一致性问题** | 不同分析师可能使用不同的查询逻辑 | 中 |
| **可追溯性** | 分析结果依赖截图，难以追溯和复现 | 高 |
| **协作问题** | 结果分享依赖文档整理，效率低下 | 中 |
| **维护成本** | Jupyter Notebook模板分散维护 | 中 |

### 2.3 解决方案价值
| 改进点 | 现状 | 目标 |
|--------|------|------|
| **参数输入** | 手动在Notebook中修改 | Web表单化输入 |
| **数据查询** | 每次手动执行SQL | 自动化后台查询 |
| **结果展示** | 截图+手动整理 | 统一Web仪表盘 |
| **结果保存** | 分散的图片文件 | 数据库统一存储 |
| **流程标准化** | 依赖个人经验 | 标准化分析流程 |

---

## 3. 系统架构

### 3.1 整体架构
**当前Demo架构**：
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   前端界面      │    │   Django后端    │    │   模拟数据      │
│                 │    │                 │    │                 │
│ • Bootstrap UI  │◄──►│ • 视图逻辑      │◄──►│ • SQLite数据库  │
│ • 响应式设计    │    │ • 业务逻辑      │    │ • 模拟BigQuery  │
│ • 表单验证      │    │ • 数据分析      │    │   查询结果      │
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
- **表现层**：Bootstrap + 自定义CSS，响应式Web界面
- **业务层**：Django视图和表单处理，数据验证
- **数据层**：Django ORM + SQLite，模拟BigQuery数据结构
- **分析层**：Pandas数据处理 + Matplotlib图表生成，模拟SQL分析逻辑

**未来生产架构**：
- **表现层**：保持现有Web界面设计
- **业务层**：增加BigQuery连接和SQL查询管理
- **数据层**：Google Cloud BigQuery，真实AML AI训练结果
- **分析层**：真实SQL查询引擎，替代模拟数据生成逻辑

### 3.3 数据流设计
**模拟数据流（当前）**：
```
用户输入run_id → 哈希生成种子 → 模拟数据生成 → 图表渲染 → Web展示
```

**真实数据流（目标）**：
```
用户输入run_id → 参数验证 → BigQuery查询 → 数据聚合分析 → 图表生成 → Web展示
```

---

## 3. 技术栈选择

### 3.1 后端技术
| 技术 | 版本 | 用途 |
|------|------|------|
| Django | 5.2.5 | Web框架，提供ORM、路由、模板系统 |
| SQLite | 内置 | 轻量级数据库，适合原型开发 |
| Python | 3.12.7 | 主要编程语言 |

### 3.2 前端技术
| 技术 | 版本 | 用途 |
|------|------|------|
| Bootstrap | 5.3.3 | 响应式UI框架 |
| django-crispy-forms | 2.x | 表单美化和验证 |
| 原生JavaScript | ES6+ | 基础交互功能 |

### 3.3 数据分析技术
| 技术 | 版本 | 用途 |
|------|------|------|
| Pandas | 2.0+ | 数据处理和表格生成 |
| Matplotlib | 3.7+ | 图表绘制和可视化 |
| NumPy | 1.24+ | 数值计算支持 |

### 3.4 开发工具
| 工具 | 用途 |
|------|------|
| uv | Python包管理器 |
| pyproject.toml | 项目配置管理 |
| Black | 代码格式化 |
| Flake8 | 代码质量检查 |

---

## 4. 数据模型设计

### 4.1 核心实体

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
    run_id = models.CharField(max_length=255)
    month = models.CharField(max_length=20, default="2025-07")
    customer_count = models.IntegerField(default=10000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('base_model', 'run_id')
```

### 4.2 数据关系
- 一个基础模型可以有多个分析运行
- 每个run_id在同一基础模型下是唯一的
- 支持跨模型的run_id重复（不同模型可以有相同的run_id）

---

## 5. 用户界面设计

### 5.1 整体布局
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
│   - 预测信息 │        • 分析结果                │
│   - 交易分析 │                                   │
│   - 目标分析 │                                   │
│   - 模型证明 │                                   │
│   - 预测    │                                   │
└─────────────┴───────────────────────────────────┘
```

### 5.2 设计主题
- **主色调**：暗红色 (`#9A2A2A`) 用于标题和重要元素
- **背景色**：浅灰色 (`#f8f9fa`) 提供清爽的视觉体验
- **侧边栏**：白色背景 (`#ffffff`) 带阴影效果
- **文本色**：深灰色 (`#333333`, `#495057`) 确保可读性

### 5.3 响应式设计
- 使用Bootstrap网格系统
- 支持桌面、平板、手机等多种设备
- 表格和图表自适应屏幕尺寸

---

## 6. 功能模块详述

### 6.1 Prediction Information (预测信息)
**路径**: `/` 或 `/prediction-info/`

**功能特性**:
- 基础模型选择器
- Run ID批量输入（支持逗号分隔）
- Run ID格式验证（必须以字母开头）
- 自动显示最近5个运行记录
- 表可用性状态显示

**工作流程**:
1. 用户选择基础模型
2. 页面自动加载该模型的最近5个运行记录
3. 用户可输入新的run_id创建分析记录
4. 系统验证格式并保存到数据库
5. 显示运行详情和表可用性状态

### 6.2 Transaction Analysis (交易分析)
**路径**: `/transaction-analysis/`

**功能特性**:
- 基础模型和Run ID联动选择
- 动态数据生成和可视化
- 交易量趋势图表
- 告警率分析图表
- 详细数据表格展示

**数据生成逻辑**:
- 基于run_id哈希值确保数据一致性
- 生成30天交易数据
- 包含交易量、金额、可疑交易数、告警率等指标

### 6.3 Target Analysis (目标分析)
**路径**: `/target-analysis/`

**功能特性**:
- 与交易分析类似的界面结构
- 目标数量堆叠条形图
- 检测率趋势折线图
- 月度目标分析数据表格

**数据生成逻辑**:
- 生成12个月的目标数据
- 包含Main Targets、Other Targets、检测率等指标
- 双图表展示（条形图+折线图）

### 6.4 Model Proving (模型证明)
**路径**: `/model-proving/`

**功能特性**:
- 占位符页面
- 基础布局展示
- 为未来功能预留接口

### 6.5 Forecasting (预测)
**路径**: `/forecasting/`

**功能特性**:
- 占位符页面
- 基础布局展示
- 为未来功能预留接口

---

## 7. 核心特性

### 7.1 数据验证
- **Run ID格式控制**: 正则表达式 `^[a-zA-Z][a-zA-Z0-9_]*$`
- **基础模型关联**: 确保run_id属于正确的基础模型
- **实时表单验证**: 前端和后端双重验证

### 7.2 数据生成
- **一致性保证**: 使用run_id哈希值作为随机种子
- **多样化图表**: 支持柱状图、折线图、堆叠图等多种类型
- **Base64图表**: 图表直接嵌入HTML，无需文件管理

### 7.3 用户体验
- **自动加载**: 页面初始化时显示相关数据
- **智能切换**: 基础模型变更时自动更新关联选项
- **响应式表格**: 使用Bootstrap样式的自适应表格

### 7.4 技术架构
- **模块化设计**: 分析逻辑与视图逻辑分离
- **ORM数据管理**: Django模型确保数据一致性
- **可扩展接口**: 预留真实数据接入点

---

## 8. 项目部署

### 8.1 环境准备
```bash
# 创建虚拟环境
uv venv
source .venv/bin/activate

# 安装依赖
uv pip install -e .
```

### 8.2 数据库初始化
```bash
# 执行迁移
python manage.py migrate

# 创建示例数据
python create_sample_data.py
```

### 8.3 运行服务
```bash
# 启动开发服务器
python manage.py runserver

# 访问应用
# http://localhost:8000
```

### 8.4 项目结构
```
mlc_demo/
├── .venv/                          # 虚拟环境
├── pyproject.toml                  # 项目配置
├── manage.py                       # Django管理入口
├── create_sample_data.py           # 示例数据脚本
├── mlc_center/                     # Django项目配置
│   ├── settings.py                 # 项目设置
│   ├── urls.py                     # URL路由
│   └── wsgi.py                     # WSGI配置
└── core/                           # 核心应用
    ├── models.py                   # 数据模型
    ├── views.py                    # 视图逻辑
    ├── forms.py                    # 表单定义
    ├── urls.py                     # 应用路由
    ├── analysis_utils.py           # 分析工具
    ├── templates/core/             # 模板文件
    │   ├── base.html
    │   ├── prediction_info.html
    │   ├── transaction_analysis.html
    │   └── target_analysis.html
    └── static/core/                # 静态资源
        └── custom.css
```

---

## 9. 开发规范

### 9.1 代码风格
- 使用Black进行代码格式化
- 遵循PEP 8编码规范
- 88字符行长度限制

### 9.2 命名规范
- **模型**: 使用驼峰命名法 (BaseModel)
- **视图**: 使用下划线命名法 (prediction_info_view)
- **模板**: 使用下划线命名法 (prediction_info.html)
- **CSS类**: 使用短横线命名法 (nav-link)

### 9.3 文档规范
- 所有函数和类需要docstring
- 复杂逻辑需要行内注释
- API变更需要更新文档

### 9.4 测试规范
- 使用pytest进行单元测试
- 视图函数需要测试覆盖
- 表单验证需要测试覆盖

### 9.5 版本控制
- 使用语义化版本号 (Semantic Versioning)
- 提交信息遵循约定式提交规范
- 功能开发使用feature分支

---

## 附录

### A. 示例数据
项目包含以下示例数据：
- **基础模型**: AML_Model_v3, AML_Model_v4, Fraud_Detection_v2
- **分析运行**: 每个模型包含4-5个run_id
- **数据格式**: 所有run_id以字母开头，符合验证规则

### B. API设计原则
1. **基础模型关联**: 所有操作基于基础模型进行数据隔离
2. **Run ID唯一性**: 在同一基础模型下run_id唯一
3. **数据一致性**: 相同run_id始终生成相同的分析结果
4. **表可用性**: 随机模拟部分数据表不可用的情况

### C. 扩展计划
1. **真实数据接入**: 替换模拟数据生成逻辑
2. **用户认证**: 添加用户管理和权限控制
3. **API接口**: 提供RESTful API供第三方调用
4. **数据导出**: 支持分析结果导出为PDF/Excel
5. **实时更新**: 添加WebSocket支持实时数据更新

---

## 11. 未来规划

### 11.1 技术架构升级

#### 数据源集成
```python
# 未来BigQuery连接配置
from google.cloud import bigquery

class BigQueryService:
    def __init__(self):
        self.client = bigquery.Client()
        self.dataset_id = "aml_ai_results"

    def query_train_results(self, run_id):
        """查询训练结果表"""
        query = f"""
        SELECT * FROM `{self.dataset_id}.train_results`
        WHERE run_id = '{run_id}'
        """
        return self.client.query(query).to_dataframe()

    def query_prediction_results(self, run_id):
        """查询预测结果表"""
        query = f"""
        SELECT * FROM `{self.dataset_id}.prediction_results`
        WHERE run_id = '{run_id}'
        """
        return self.client.query(query).to_dataframe()
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
  FROM `{dataset}.prediction_results`
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
- [ ] BigQuery连接器开发
- [ ] SQL查询引擎重构
- [ ] 数据验证和错误处理

#### 第二阶段：分析功能增强（6个月）
- [ ] 模型漂移检测
- [ ] 自动化告警系统
- [ ] 历史趋势对比分析
- [ ] 多模型版本比较

#### 第三阶段：企业级功能（12个月）
- [ ] 用户权限管理系统
- [ ] 审计日志和合规报告
- [ ] API接口开发
- [ ] 性能优化和扩展

### 11.3 替代现有Jupyter Notebook流程

#### 当前Notebook流程
```python
# 现有notebook典型流程
run_id = "input_manually"  # 手动输入
suffix = "202501"          # 手动输入

# SQL查询（每个notebook重复）
query = f"""
SELECT * FROM dataset.table
WHERE run_id = '{run_id}' AND month = '{suffix}'
"""

# 数据处理和可视化
df = client.query(query).to_dataframe()
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['count'])
plt.show()  # 需要截图保存
```

#### 目标Web流程
```python
# Web界面流程
class TransactionAnalysisView(TemplateView):
    def get_context_data(self, **kwargs):
        run_id = self.request.GET.get('run_id')

        # 自动查询和处理
        data = self.query_service.get_transaction_data(run_id)
        chart = self.chart_service.generate_chart(data)

        # 自动保存和展示
        return {
            'data': data,
            'chart': chart,
            'run_id': run_id
        }
```

### 11.4 集成Google AML AI

#### AML AI结果表结构（预期）
```sql
-- 训练结果表
CREATE TABLE `project.dataset.train_results` (
  run_id STRING,
  model_version STRING,
  training_timestamp TIMESTAMP,
  metrics JSON,
  status STRING
);

-- 预测结果表
CREATE TABLE `project.dataset.prediction_results` (
  run_id STRING,
  transaction_id STRING,
  ml_score FLOAT64,
  prediction_timestamp TIMESTAMP,
  features JSON
);

-- 目标分析表
CREATE TABLE `project.dataset.target_analysis` (
  run_id STRING,
  month STRING,
  target_type STRING,
  count INT64,
  detection_rate FLOAT64
);
```

### 11.5 监控和运维

#### 性能监控
- BigQuery查询成本监控
- 页面响应时间追踪
- 用户访问模式分析
- 系统资源使用监控

#### 错误处理
```python
class AMLAnalysisService:
    def safe_query(self, query, run_id):
        try:
            result = self.bigquery_client.query(query)
            return result.to_dataframe()
        except Exception as e:
            logger.error(f"Query failed for run_id {run_id}: {e}")
            # 返回友好错误信息给用户
            raise AnalysisError(f"数据查询失败，请检查run_id: {run_id}")
```

### 11.6 成功指标

#### 技术指标
- [ ] 查询响应时间 < 10秒
- [ ] 系统可用性 > 99%
- [ ] 错误率 < 1%
- [ ] BigQuery成本控制在预算内

#### 业务指标
- [ ] 分析效率提升 50%以上
- [ ] 结果一致性提升（减少人为错误）
- [ ] 用户满意度 > 90%
- [ ] Notebook使用频率下降 80%
