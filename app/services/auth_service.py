"""Auth business logic."""


def login_user(payload: dict) -> dict:
    return {
        "message": "Login service placeholder",
        "email": payload.get("email"),
    }
