from fastapi import APIRouter, Depends, Response, status

from services.auth_service import AuthService
from schemas.auth import UsersRegisterDto, Token, UserLoginDto, UserResponseDto
from api.dependencies import get_auth_service

auth = APIRouter(prefix="/auth", tags=["Authentication"])


@auth.post(
    "/register",
    summary="Registering a new user",
    tags=["Authentication"]
)
async def register(
    user_data: UsersRegisterDto,
    service: AuthService = Depends(get_auth_service)
) -> UserResponseDto:
    return await service.register_user(user_data)


@auth.post(
    "/login",
    summary="User authentication",
    tags=["Authentication"]
)
async def login(
    response: Response,
    login_data: UserLoginDto,
    service: AuthService = Depends(get_auth_service)
) -> dict:
    token_result = await service.login_user(login_data)

    response.set_cookie(
        key="access_token",
        value=token_result.access_token,
        httponly=True,
        max_age=48 * 60 * 60,
        path="/"
    )

    return {"message": "Успешный вход", "token_type": "bearer"}
