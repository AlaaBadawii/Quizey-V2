"""Attempt business logic."""


def submit_attempt(payload: dict) -> dict:
    return {
        "message": "Attempt submitted",
        "exam_id": payload.get("exam_id"),
    }
