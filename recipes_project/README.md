# Recipes Project (Django)

A minimal CRUD app for the 348 Project

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
