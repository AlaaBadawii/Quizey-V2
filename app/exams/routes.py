from flask import jsonify

from app.exams import exams_bp
from app.services.exam_service import list_exams


@exams_bp.get("/")
def get_exams():
    result = list_exams()
    return jsonify(result), 200
