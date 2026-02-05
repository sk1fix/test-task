from pydantic import BaseModel


class UsersRegisterDto(BaseModel):
    login: str
    hashed_password: str
    fullname: str
    is_admin: str | bool | None = None


class UserResponseDto(BaseModel):
    login: str
    fullname: str
    is_admin: bool


class UserLoginDto(BaseModel):
    login: str
    password: str


class UserHashPass(BaseModel):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
