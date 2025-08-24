# Model Lifecycle Center (MLC) - Technical Specification

## Table of Contents
1. [Project Overview](#1-project-overview)
2. [Business Scenario Analysis](#2-business-scenario-analysis)
3. [System Architecture](#3-system-architecture)
4. [Technology Stack](#4-technology-stack)
5. [Data Model Design](#5-data-model-design)
6. [User Interface Design](#6-user-interface-design)
7. [Feature Modules](#7-feature-modules)
8. [Core Features](#8-core-features)
9. [Project Deployment](#9-project-deployment)
10. [Development Standards](#10-development-standards)
11. [Future Roadmap](#11-future-roadmap)

---

## 1. Project Overview

### 1.1 Background & Problems
In banking Anti-Money Laundering (AML) operations, we utilize Google AML AI platform for machine learning model training and prediction. The current analysis workflow faces several challenges:

**Business Context**:
- Using Google AML AI functionality for model training and prediction operations
- Training and prediction results are stored as tables in BigQuery datasets
- Need to periodically retrain models to adapt to new financial crime behavior patterns
- Complete model validation and analysis required after each retraining
- **New Challenge**: Business expansion to global markets (UK, Hong Kong, Singapore, Mexico) requires independent management and tracking of model lifecycles across different markets.

**Current Pain Points**:
- Analysts need to manually input run_id and other parameters in Jupyter Notebooks
- Process is inefficient, error-prone, and difficult to trace and share
- Lack of unified platform for analysis result presentation and management
- **New Pain Point**: Missing a global perspective for model management entry point, unable to conveniently switch between different market analysis environments.

### 1.2 Solution
Model Lifecycle Center (MLC) is a web application prototype, now upgraded to a global model lifecycle management platform, specifically designed for banking AML model analysis scenarios:

**Core Value**:
- **Global Market Entry**: Provides a unified homepage displaying all supported countries/regions as a portal to enter market-specific analysis environments.
- **Country-Level Model Lifecycle**: Offers independent model timeline and retraining entry points for each country.
- **Jupyter Notebook Workflow Replacement**: Web-ifies the manual run_id and parameter input process within specific country contexts.
- **Automated Data Querying**: Integrates BigQuery connections for automatic SQL analysis query execution (future planning).
- **Unified Result Display**: Presents country-specific model analysis results in professional dashboard format.

**Technical Architecture**:
- **Frontend Web Interface**: Provides clear global-to-country two-tier navigation structure.
- **Backend Data Processing**: Python + Django, handling country-differentiated business logic.
- **Demo Framework Design**: Uses simulated data to establish complete architecture with real data integration points reserved.
- **Scalable Design**: Facilitates future integration with Google AML AI and BigQuery real data.

### 1.3 Target Users
- **AML Analysts**: Conducting analysis and validation work for models after training across different markets.
- **Global Model Management Teams**: Requiring overview of model states across markets for unified coordination.
- **Machine Learning Engineers**: Responsible for model retraining and performance monitoring across markets.
- **Compliance Teams**: Need to view market-specific model validation results and compliance reports.
- **Risk Management Teams**: Evaluate new model effectiveness in detecting financial crimes across different global markets.

### 1.4 Project Positioning
**Demo Nature**:
- Currently in concept validation and framework construction phase
- Uses simulated data to mimic real BigQuery query results
- Focus on establishing complete country-specific web-based analysis workflows
- Preparation for future Google AML AI and BigQuery integration

**Future Expansion**:
- Integration with Google Cloud BigQuery data sources
- Connection to Google AML AI model training and prediction results
- Implementation of real SQL query and data analysis logic
- Addition of cross-country model performance comparison functionality

---

## 2. Business Scenario Analysis

### 2.1 Real Business Workflow
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Global Market   │    │ Select Specific │    │ Model Lifecycle │
│ Overview        │    │ Market          │    │                 │
│                 │    │ (UK,HK,SG,MX)   │    │                 │
│ • Country Entry │───►│                 │───►│ • Timeline      │
│ • Unified Portal│    │                 │    │ • Retrain       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │                       │
                       ┌─────────────────┐    ┌─────────────────┐
                       │ Model Analysis  │    │ Result          │
                       │ (Country-specific)│    │ Validation      │
                       │                 │    │ (Country-specific)│
                       │ • Prediction Info│───►│ • Transaction   │
                       │ • Web-based Input│    │   Analysis      │
                       │ • Automated Query│    │ • Target Analysis│
                       └─────────────────┘    └─────────────────┘
```

### 2.2 Current Pain Point Analysis
| Problem Category | Specific Issues | Impact Level |
|------------------|-----------------|--------------|
| **Global Management** | Lack of unified global market model entry | High |
| **Efficiency Issues** | Cumbersome switching between different market analysis environments | High |
| **Consistency Issues** | Different analysts may use different query logic | Medium |
| **Traceability** | Analysis results depend on screenshots, hard to trace and reproduce | High |
| **Collaboration Issues** | Result sharing depends on document organization, low efficiency | Medium |

### 2.3 Solution Value
| Improvement | Current State | Target |
|-------------|---------------|--------|
| **Global Navigation** | None | Unified global market entry page |
| **Parameter Input** | Manual modification in Notebooks | Web form input (country-specific) |
| **Data Querying** | Manual SQL execution each time | Automated backend queries (country-specific) |
| **Result Display** | Screenshots + manual organization | Unified web dashboard (country-specific) |
| **Process Standardization** | Depends on personal experience | Standardized, country-specific analysis workflows |

---

## 3. System Architecture

### 3.1 Overall Architecture
**Current Demo Architecture**:
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Frontend UI     │    │ Django Backend  │    │ Simulated Data  │
│ (Global/Country │    │                 │    │                 │
│ Two-tier)       │    │                 │    │                 │
│ • Bootstrap UI  │◄──►│ • View Logic    │◄──►│ • SQLite DB     │
│ • Responsive    │    │   (Country-     │    │ • Mock BigQuery │
│   Design        │    │   specific)     │    │   Results       │
│ • HTMX          │    │ • Business Logic│    │                 │
│   Interaction   │    │ • Data Analysis │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                       ┌─────────────────┐
                       │ Analysis Engine │
                       │                 │
                       │ • Pandas        │
                       │   Processing    │
                       │ • Matplotlib    │
                       │   Charts        │
                       │ • Mock SQL Logic│
                       └─────────────────┘
```

**Future Target Architecture**:
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Frontend UI     │    │ Django Backend  │    │ Google Cloud    │
│                 │    │                 │    │                 │
│ • Unified       │◄──►│ • Parameter     │◄──►│ • BigQuery      │
│   Analysis UI   │    │   Validation    │    │ • AML AI Tables │
│ • Real-time     │    │ • SQL Query     │    │ • Train/Predict │
│   Results       │    │   Engine        │    │   Run Results   │
│ • History Mgmt  │    │ • Data          │    │                 │
└─────────────────┘    │   Processing    │    └─────────────────┘
                       └─────────────────┘
                                │
                       ┌─────────────────┐
                       │ Analysis Engine │
                       │                 │
                       │ • Real SQL      │
                       │   Queries       │
                       │ • Data          │
                       │   Aggregation   │
                       │ • Automated     │
                       │   Charts        │
                       └─────────────────┘
```

### 3.2 Application Layers
**Current Demo Implementation**:
- **Presentation Layer**: Bootstrap + Custom CSS + HTMX, implementing global entry and country-specific two-tier responsive web interface.
- **Business Layer**: Django views and form processing, handling data validation and business flow by country code.
- **Data Layer**: Django ORM + SQLite, `AnalysisRun` model simulating country-specific data structure through `country` field.
- **Analysis Layer**: Pandas data processing + Matplotlib chart generation, simulating SQL analysis logic.

### 3.3 Data Flow Design
**Simulated Data Flow (Current)**:
```
User selects country → Enter country-level page → User inputs run_id → Hash generates seed → Simulated data generation → Chart rendering → Web display
```

**Real Data Flow (Target)**:
```
User selects country → User inputs run_id → Parameter validation → BigQuery query (with country filter) → Data aggregation analysis → Chart generation → Web display
```

---

## 4. Technology Stack

### 4.1 Backend Technologies
| Technology | Version | Purpose |
|------------|---------|---------|
| Django | 5.2.5 | Web framework providing ORM, routing, template system |
| SQLite | Built-in | Lightweight database suitable for prototype development |
| Python | 3.12.7 | Primary programming language |

### 4.2 Frontend Technologies
| Technology | Version | Purpose |
|------------|---------|---------|
| Bootstrap | 5.3.3 | Responsive UI framework |
| django-crispy-forms | 2.x | Form beautification and validation |
| htmx | 1.9.10 | Enhanced page partial refresh and interaction experience |
| Vanilla JavaScript | ES6+ | Basic interaction functionality like progress tracking |

### 4.3 Data Analysis Technologies
| Technology | Version | Purpose |
|------------|---------|---------|
| Pandas | 2.0+ | Data processing and table generation |
| Matplotlib | 3.7+ | Chart drawing and visualization |
| NumPy | 1.24+ | Numerical computation support |

### 4.4 Development Tools
| Tool | Purpose |
|------|---------|
| uv | Python package manager |
| pyproject.toml | Project configuration management |
| Black | Code formatting |
| Flake8 | Code quality checking |

---

## 5. Data Model Design

### 5.1 Core Entities

#### Country
```python
class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=3, unique=True)
    flag_emoji = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
```

#### BaseModel
```python
class BaseModel(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    current_status = models.CharField(max_length=20, choices=[...])
    created_at = models.DateTimeField(auto_now_add=True)
```

#### AnalysisRun
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

#### ModelEvent
```python
class ModelEvent(models.Model):
    model = models.ForeignKey(BaseModel, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=20, choices=[...])
    event_date = models.DateTimeField()
    description = models.TextField()
    version = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
```

### 5.2 Data Relationships
- Each country can have multiple base models
- Each base model can have multiple analysis runs and model events
- `run_id` is unique within the same base model
- Supports cross-country data isolation and management

---

## 6. User Interface Design

### 6.1 Overall Layout
The application contains two main layout types:

**1. Global Entry Page (`/`)**
```
┌─────────────────────────────────────────────────┐
│          Model Lifecycle Center                 │
│        Global Model Management Portal          │
├─────────────────────────────────────────────────┤
│                                                 │
│              Statistics Overview                │
│                                                 │
│        • Four Country Cards (UK,HK,MX,SG)      │
│        • Each card contains "Timeline" and      │
│          "Training" links                       │
│                                                 │
└─────────────────────────────────────────────────┘
```

**2. Country-Level Analysis Pages (`/<country_code>/...`)**
```
┌─────────────────────────────────────────────────┐
│             Country Name + Flag                 │
│            Model Lifecycle Center              │
├─────────────┬───────────────────────────────────┤
│ Side        │                                   │
│ Navigation  │                                   │
│             │            Main Content           │
│ • Global    │                                   │
│   Dashboard │        • Forms and Data           │
│ • Model     │        • Charts and Tables       │
│   Timeline  │        • Analysis Results        │
│ • Training  │                                   │
│   Dashboard │                                   │
│             │                                   │
│ • Training  │                                   │
│   Workflow  │                                   │
│   - Predict │                                   │
│     Info    │                                   │
│   - ...     │                                   │
└─────────────┴───────────────────────────────────┘
```

### 6.2 Design Theme
- **Primary Colors**: Modern gradient color schemes reflecting professionalism
- **Background Colors**: Light gray series providing fresh visual experience
- **Visual Enhancement**: Flag emojis, card hover effects, modern icons
- **Responsive Design**: Bootstrap 5.3.3 ensures cross-device compatibility

---

## 7. Feature Modules

### 7.1 Global Entry Page (Home)
**Path**: `/`

**Features**:
- Displays all supported countries/regions (UK, Hong Kong, Mexico, Singapore)
- Each country card contains:
  - Flag and name
  - Model timeline link
  - Model training link
  - Current active model count
- Global statistics display
- Modern design with responsive layout

### 7.2 Model Timeline Page
**Path**: `/<country_code>/timeline/`

**Features**:
- Displays model lifecycle events for specific country
- Timeline visualization
- Includes deployment, retraining, update event types
- Current model status overview
- Navigation to global entry and training dashboard

### 7.3 Model Training Dashboard
**Path**: `/<country_code>/training/`

**Features**:
- Country-level training workflow overview
- Workflow step display
- Quick action panel
- Current model management
- Statistical data display

### 7.4 Training Workflow Pages
**Path**: `/<country_code>/training/...`

Includes complete ML training workflow:
- Prediction Information
- Transaction Analysis
- Target Analysis
- Model Proving
- Forecasting
- BTL Calculator
- Benchmark
- Documentation

---

## 8. Core Features

### 8.1 Multi-Country Architecture
- **URL-Driven**: Data and view isolation through country codes in URLs
- **Data Isolation**: Independent management of models and analysis data for each country
- **Scalability**: Easy addition of new countries and markets

### 8.2 Progress Tracking System
- **Client Storage**: Uses localStorage to track user progress
- **Visual Indicators**: Real-time display of completion status
- **Country-Specific**: Independent progress tracking for each country

### 8.3 User Experience Optimization
- **Two-Tier Navigation**: Clear hierarchy from global view to country view
- **Smart Switching**: Automatic data updates when base model changes
- **Responsive Design**: Consistent experience across devices

---

## 9. Project Deployment

### 9.1 Environment Setup
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or .venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### 9.2 Database Initialization
```bash
# Execute migrations
python manage.py migrate

# Create sample data
python manage.py seed_countries
```

### 9.3 Run Service
```bash
# Start development server
python manage.py runserver

# Access application
# http://localhost:8000
```

### 9.4 Project Structure
```
mlc_demo/
├── .venv/                          # Virtual environment
├── pyproject.toml                  # Project configuration
├── manage.py                       # Django management entry
├── mlc_center/                     # Django project configuration
│   ├── settings.py
│   └── urls.py
└── core/                           # Core application
    ├── models.py                   # Data models
    ├── views.py                    # View logic
    ├── forms.py                    # Form definitions
    ├── urls.py                     # Application routing
    ├── analysis_utils.py           # Analysis tools
    ├── templates/core/             # Template files
    │   ├── home.html
    │   ├── model_timeline.html
    │   ├── model_training_dashboard.html
    │   ├── country_base.html
    │   └── ... (other analysis pages)
    ├── static/core/                # Static resources
    │   └── custom.css
    └── management/commands/        # Management commands
        └── seed_countries.py
```

---

## 10. Development Standards

### 10.1 Code Style
- Use Black for code formatting
- Follow PEP 8 coding standards
- 88-character line length limit

### 10.2 Naming Conventions
- **Models**: Use CamelCase (BaseModel, Country)
- **Views**: Use snake_case (home_view, model_timeline_view)
- **Templates**: Use snake_case (home.html, model_timeline.html)
- **CSS Classes**: Use kebab-case (nav-link, country-card)

### 10.3 Documentation Standards
- All functions and classes require docstrings
- Complex logic needs inline comments
- API changes require documentation updates

---

## 11. Future Roadmap

### 11.1 Phase 1: Real Data Integration (3 months)
- [ ] Google Cloud authentication and permission configuration
- [ ] BigQuery connector development (supporting multi-country datasets)
- [ ] SQL query engine refactoring
- [ ] Data validation and error handling mechanisms

### 11.2 Phase 2: Analysis Feature Enhancement (6 months)
- [ ] Cross-market model performance comparison dashboard
- [ ] Model drift detection (country-specific)
- [ ] Automated alerting system
- [ ] Historical trend comparison analysis

### 11.3 Phase 3: Enterprise-Level Features (12 months)
- [ ] User permission management system (distinguishing global/country-level roles)
- [ ] Audit logs and compliance reporting
- [ ] REST API development
- [ ] Performance optimization and horizontal scaling
- [ ] High availability deployment solutions

### 11.4 Technical Architecture Upgrade

#### BigQuery Integration Example
```python
from google.cloud import bigquery

class BigQueryService:
    def __init__(self, country_code):
        self.client = bigquery.Client()
        self.dataset_id = f"aml_ai_results_{country_code}"

    def query_train_results(self, run_id):
        """Query training results table"""
        query = f"""
        SELECT * FROM `{self.dataset_id}.train_results`
        WHERE run_id = '{run_id}'
        """
        return self.client.query(query).to_dataframe()
```

#### Cross-Country Performance Comparison
```python
def compare_models_across_countries(model_name, metric='accuracy'):
    """Compare same model performance across different countries"""
    countries = ['UK', 'HK', 'MX', 'SG']
    results = {}

    for country in countries:
        service = BigQueryService(country.lower())
        performance = service.get_model_performance(model_name, metric)
        results[country] = performance

    return results
```

---

## Conclusion

Model Lifecycle Center (MLC) has evolved from a single analysis tool to a globalized model lifecycle management platform. Through the introduction of multi-country architecture, modernized UI design, and complete workflow support, MLC provides a powerful and flexible solution for banking AML operations.

The current Demo version establishes a solid technical foundation, preparing for future integration with Google Cloud and BigQuery. As the project continues to develop, MLC will become the standard platform for global financial institutions to conduct AML model management.
