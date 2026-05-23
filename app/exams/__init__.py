from flask import Blueprint

exams_bp = Blueprint("exams", __name__)

from app.exams import routes  # noqa: E402,F401
