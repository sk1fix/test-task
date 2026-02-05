from datetime import datetime, timedelta

import jwt
from passlib.context import CryptContext

from core.config import settings


pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_token(data: dict):
    payload = {
        **data,
        "exp": datetime.utcnow() + timedelta(hours=48),
        "iat": datetime.utcnow()
    }

    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")


def get_user_data_from_token(token: str) -> dict:
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    return {
        "user_id": payload.get("user_id"),
        "username": payload.get("username"),
        "login": payload.get("sub"),
        "is_admin": payload.get("is_admin", False)
    }


def is_admin_user(token: str) -> bool:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        return payload.get("is_admin", False)
    except:
        return False
