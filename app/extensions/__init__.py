"""Flask extension initialization."""

from flask import Flask

from app.extensions.db import db


def init_extensions(app: Flask) -> None:
    db.init_app(app)
