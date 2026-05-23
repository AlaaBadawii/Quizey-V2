"""Shared response helpers."""


def success_response(message: str, **data) -> dict:
    payload = {"message": message}
    payload.update(data)
    return payload
