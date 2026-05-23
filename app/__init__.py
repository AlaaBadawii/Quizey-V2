"""Application factory for Quizey."""

from flask import Flask

from app.config.settings import get_config
from app.extensions import init_extensions
from app.auth import auth_bp
from app.exams import exams_bp
from app.attempts import attempts_bp
from app.grading import grading_bp


def create_app(config_name: str | None = None) -> Flask:
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))

    init_extensions(app)
    register_blueprints(app)

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    return app


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(auth_bp, url_prefix="/api/v1/auth")
    app.register_blueprint(exams_bp, url_prefix="/api/v1/exams")
    app.register_blueprint(attempts_bp, url_prefix="/api/v1/attempts")
    app.register_blueprint(grading_bp, url_prefix="/api/v1/grading")
