# MLC Demo 开发环境搭建指南

本文档帮助新同学在本地快速运行本项目（Django 5.2，Python 3.12+，SQLite）。

## 快速开始（TL;DR）

```bash
# 1) 准备虚拟环境（Linux / bash）
python3 -m venv .venv
source .venv/bin/activate

# 2) 安装依赖（使用已生成的 requirements.txt）
pip install -U pip
pip install -r requirements.txt

# 3) 初始化数据库（SQLite）
python manage.py migrate

# 4) 生成演示数据与占位图（可选但推荐）
python create_sample_data.py
python generate_chart.py

# 5) 启动开发服务
python manage.py runserver
```

访问：http://127.0.0.1:8000/

如需后台管理，先创建超级用户：

```bash
python manage.py createsuperuser
# 登录 http://127.0.0.1:8000/admin/
```

---

## 先决条件
- 操作系统：Linux 或 macOS/Windows（示例命令以 Linux bash 为准）
- Python 3.12+
- 可选：Git、VS Code

在 Debian/Ubuntu 上如缺少 venv：
```bash
sudo apt-get update
sudo apt-get install -y python3-venv
```

## 安装依赖
项目已提供 `requirements.txt`（由 `pyproject.toml` 编译而来），推荐直接安装：

```bash
pip install -U pip
pip install -r requirements.txt
```

可选：使用项目元数据进行安装（需要 pip 支持 PEP 660）
```bash
# 运行时依赖
pip install -e .
# 开发依赖（测试/格式/静态检查）
pip install -e .[dev]
```

可选：使用 uv 提速（若已安装 uv）
```bash
uv pip sync requirements.txt
```

主要依赖：
- django、django-crispy-forms、crispy-bootstrap5、django-htmx
- pandas、numpy、matplotlib

## 数据库初始化（SQLite）
本项目默认使用根目录下的 `db.sqlite3`。

全新环境建议：
```bash
# 若存在历史数据库且希望重置（可选）
rm -f db.sqlite3
python manage.py migrate
```

## 生成演示数据与资源
- Demo 数据：`create_sample_data.py`（会创建基础模型与多条分析运行记录）
- 占位图：`generate_chart.py`（在 `core/static/core/` 下生成 `placeholder_chart.png`）

```bash
python create_sample_data.py
python generate_chart.py
```

脚本会自动加载 Django 环境（无需额外环境变量）。重复执行是幂等的：已存在的数据会跳过创建。

## 启动与访问
```bash
python manage.py runserver
```
- 默认地址：http://127.0.0.1:8000/
- 管理后台：http://127.0.0.1:8000/admin/
- DEBUG 已在开发环境开启；本地无需配置 `ALLOWED_HOSTS`

## 静态资源与前端
- 开发模式下 Django 会自动提供静态资源；无需 `collectstatic`
- 静态目录：`core/static/...`（包含 Bootstrap、flags、htmx 等）
- 模板目录：`core/templates/...`



## 项目结构速览
- `manage.py`：Django 管理入口
- `mlc_center/`：项目配置（settings/urls/wsgi/asgi）
- `core/`：业务应用（models/views/forms/templates/static/migrations）
- `create_sample_data.py`：演示数据脚本
- `generate_chart.py`：占位图生成脚本
- `TECHNICAL_SPECIFICATION.md`：技术说明文档