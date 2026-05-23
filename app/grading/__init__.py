from flask import Blueprint

grading_bp = Blueprint("grading", __name__)

from app.grading import routes  # noqa: E402,F401
