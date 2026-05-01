# Recipes Project (Django)

A minimal CRUD app for Stage 2 demo.

## Features
- Single-table schema: `Recipe` with fields (name, country, prep/cook time, serves, spice 1–5, prep complexity 1–5)
- Add / Edit / Delete recipes
- Filter report by dynamic DB-driven country dropdown (no hard-coding), serves range, spice range, max prep/cook time
- SQLite by default

## Quickstart
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py loaddata sample_data.json   # optional seed
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Admin (optional)
```bash
python manage.py createsuperuser
```
