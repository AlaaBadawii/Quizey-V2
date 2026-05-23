"""Grading business logic."""


def grade_attempt(payload: dict) -> dict:
    return {
        "message": "Grading service placeholder",
        "attempt_id": payload.get("attempt_id"),
    }
