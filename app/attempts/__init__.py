from flask import Blueprint

attempts_bp = Blueprint("attempts", __name__)

from app.attempts import routes  # noqa: E402,F401
