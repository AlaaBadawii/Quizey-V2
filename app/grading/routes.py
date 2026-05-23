from flask import jsonify, request

from app.grading import grading_bp
from app.services.grading_service import grade_attempt


@grading_bp.post("/")
def grade():
    result = grade_attempt(request.get_json(silent=True) or {})
    return jsonify(result), 200
