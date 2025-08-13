# Model Lifecycle Center (MLC) - 技术规格说明书

## 目录
1. [项目概述](#1-项目概述)
2. [系统架构](#2-系统架构)
3. [技术栈选择](#3-技术栈选择)
4. [数据模型设计](#4-数据模型设计)
5. [用户界面设计](#5-用户界面设计)
6. [功能模块详述](#6-功能模块详述)
7. [核心特性](#7-核心特性)
8. [项目部署](#8-项目部署)
9. [开发规范](#9-开发规范)

---

## 1. 项目概述

### 1.1 背景与问题
当前，银行的反洗钱（AML）机器学习模型分析流程依赖于 Jupyter Notebook，存在以下问题：
- 分析师需要手动输入 `run_id` 进行模型训练或预测
- 需要从 Notebook 中截图分析结果并手动整理
- 过程效率低下、易于出错且难以追溯和共享

### 1.2 解决方案
Model Lifecycle Center (MLC) 是一个Web应用原型，旨在：
- **简化工作流程**：通过选择基础模型和输入 `run_id` 自动获取分析结果
- **提升可视化效果**：以专业仪表盘形式展示数据表格和图表
- **构建可扩展框架**：使用模拟数据建立完整应用架构，便于未来接入真实数据

### 1.3 目标用户
- 银行内部机器学习工程师
- 数据分析师
- 模型验证团队

---

## 2. 系统架构

### 2.1 整体架构
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   前端界面      │    │   Django后端    │    │   数据存储      │
│                 │    │                 │    │                 │
│ • Bootstrap UI  │◄──►│ • 视图逻辑      │◄──►│ • SQLite数据库  │
│ • 响应式设计    │    │ • 业务逻辑      │    │ • 模拟数据      │
│ • 表单验证      │    │ • 数据分析      │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                       ┌─────────────────┐
                       │   分析引擎      │
                       │                 │
                       │ • Pandas处理    │
                       │ • Matplotlib图表│
                       │ • 数据可视化    │
                       └─────────────────┘
```

### 2.2 应用层次
- **表现层**：Bootstrap + 自定义CSS，响应式Web界面
- **业务层**：Django视图和表单处理，数据验证
- **数据层**：Django ORM + SQLite，模型关系管理
- **分析层**：Pandas数据处理 + Matplotlib图表生成

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
