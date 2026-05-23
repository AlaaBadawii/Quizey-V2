from flask import jsonify, request

from app.auth import auth_bp
from app.services.auth_service import login_user


@auth_bp.post("/login")
def login():
    result = login_user(request.get_json(silent=True) or {})
    return jsonify(result), 200
