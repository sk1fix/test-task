from fastapi import HTTPException

from core.security import (
    verify_password,
    get_password_hash,
    create_token,
    get_user_data_from_token
)
from schemas.auth import (
    UsersRegisterDto,
    Token,
    UserResponseDto,
    UserLoginDto
)
from core.exceptions import InvalidCredentialsException
from core.config import settings


class AuthService:
    def __init__(self, repo):
        self.repo = repo

    async def register_user(self, data: UsersRegisterDto) -> UserResponseDto:
        is_admin = False
        if data.is_admin:
            if data.is_admin == settings.ADMIN_KEY:
                is_admin = True
        hashed_password = get_password_hash(data.hashed_password)
        new_dto = UsersRegisterDto(
            login=data.login,
            hashed_password=hashed_password,
            fullname=data.fullname,
            is_admin=is_admin
        )
        result = await self.repo.create_user(new_dto)
        response_dto = UserResponseDto(
            login=result.login,
            fullname=result.fullname,
            is_admin=result.is_admin
        )
        return response_dto

    async def login_user(self, data: UserLoginDto) -> Token:
        _ = await self.repo.get_by_login(data.login)
        hash_pass = await self.repo.get_pass_by_login(data.login)
        if verify_password(data.password, hash_pass.hashed_password):
            token_payload = {
                "sub": hash_pass.login,
                "fullname": hash_pass.fullname,
                "is_admin": hash_pass.is_admin,
                "user_id": hash_pass.id
            }
            access_token = create_token(token_payload)
            return Token(access_token=access_token)
        else:
            raise InvalidCredentialsException()
