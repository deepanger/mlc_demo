# MLC Demo - Development Setup Guide

This guide helps you run the project locally quickly (Django 5.2, Python 3.12+, SQLite).

## Quick Start (TL;DR)

```bash
# 1) Create a virtual environment (Linux / bash)
python3 -m venv .venv
source .venv/bin/activate

# 2) Install dependencies (using the generated requirements.txt)
pip install -U pip
pip install -r requirements.txt

# 3) Initialize the database (SQLite)
python manage.py migrate

# 4) Create demo data and placeholder chart (optional but recommended)
python create_sample_data.py
python generate_chart.py

# 5) Start the dev server
python manage.py runserver
```

Open: http://127.0.0.1:8000/

If you need the admin site, create a superuser first:

```bash
python manage.py createsuperuser
# Then visit http://127.0.0.1:8000/admin/
```

---

## Prerequisites
- OS: Linux, macOS, or Windows (examples use Linux bash)
- Python 3.12+
- Optional: Git, VS Code

If venv is missing on Debian/Ubuntu:
```bash
sudo apt-get update
sudo apt-get install -y python3-venv
```

## Install dependencies
The project ships a compiled `requirements.txt` (from `pyproject.toml`). Install with:

```bash
pip install -U pip
pip install -r requirements.txt
```

Optional: install via project metadata (requires pip with PEP 660)
```bash
# Runtime deps
pip install -e .
# Dev extras (tests/format/lints/types)
pip install -e .[dev]
```

Optional: faster installs with uv (if uv is installed)
```bash
uv pip sync requirements.txt
```

Key dependencies:
- django, django-crispy-forms, crispy-bootstrap5, django-htmx
- pandas, numpy, matplotlib

## Database initialization (SQLite)
This project uses `db.sqlite3` in the repo root by default.

Fresh start recommendation:
```bash
# If you want a clean DB (optional)
rm -f db.sqlite3
python manage.py migrate
```


## Demo data and assets
- Demo data: `create_sample_data.py` (creates base models and multiple analysis runs)
- Placeholder chart: `generate_chart.py` (writes `core/static/core/placeholder_chart.png`)

```bash
python create_sample_data.py
python generate_chart.py
```

These scripts bootstrap the Django environment automatically. They are idempotent—existing rows are preserved.

## Run and access
```bash
python manage.py runserver
```
- App: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
- DEBUG is enabled for development; `ALLOWED_HOSTS` is not required locally.

## Static assets and frontend
- In development, Django serves static assets; no `collectstatic` needed
- Static dir: `core/static/...` (includes Bootstrap, flags, htmx, etc.)
- Templates: `core/templates/...`


## Project structure at a glance
- `manage.py`: Django entry point
- `mlc_center/`: project config (settings/urls/wsgi/asgi)
- `core/`: app code (models/views/forms/templates/static/migrations)
- `create_sample_data.py`: demo data script
- `generate_chart.py`: placeholder chart script
- `TECHNICAL_SPECIFICATION.md`: technical notes
