
# Student Directory API (FastAPI + PostgreSQL)

A secure RESTful API for managing student records.

## Tech
- FastAPI, Pydantic, SQLAlchemy 2.0
- PostgreSQL
- Alembic migrations
- CORS enabled
- Swagger UI at `/docs`

## Quickstart

1) Create `.env` from template:
```bash
cp .env.example .env
# edit DATABASE_URL if needed
```

2) Create and migrate DB:
```bash
python -m venv .venv && . .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head
python seed.py
```

3) Run API:
```bash
uvicorn app.main:app --reload
```

## Endpoints
- `GET /api/students`
- `GET /api/students/{id}`
- `POST /api/students`
- `PUT /api/students/{id}`
- `DELETE /api/students/{id}`

Validation rules:
- name: str, min 2
- age: int, 16..100
- group: str, required
- email: valid email, unique
- avatar_url: optional URL

## Project Structure
```
app/
  main.py
  database.py
  models/student.py
  schemas/student.py
  routers/students.py
migrations/
  env.py
  versions/<timestamp>_create_students_table.py
seed.py
requirements.txt
.env.example
```
