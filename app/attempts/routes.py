from flask import jsonify, request

from app.attempts import attempts_bp
from app.services.attempt_service import submit_attempt


@attempts_bp.post("/")
def create_attempt():
    result = submit_attempt(request.get_json(silent=True) or {})
    return jsonify(result), 201
