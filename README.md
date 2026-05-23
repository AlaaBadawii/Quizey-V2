# Quizey-V2

Quizey is a backend-powered exam and training platform that enables teachers to create, publish, and manage quizzes and exams with automated grading and future AI-powered analytics.

## Starter backend structure

```text
app/
├── auth/
├── exams/
├── attempts/
├── grading/
├── models/
├── services/
├── extensions/
├── config/
└── utils/
```

- Flask app factory: `app.create_app`
- SQLAlchemy extension: `app/extensions/db.py`
- Blueprint registration: `app/register_blueprints` in `app/__init__.py`
- Service-layer business logic in `app/services/*` (routes remain thin)

## Environment variables

Copy `.env.example` and configure:

- `FLASK_ENV` (`development`, `testing`, `production`)
- `SECRET_KEY`
- `DATABASE_URL`

## Run

```bash
python run.py
```
