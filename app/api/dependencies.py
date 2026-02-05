from fastapi import Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from database.session import get_db
from services.product_service import ProductService
from services.quality_service import QualityService
from services.auth_service import AuthService
from repositories.product_repository import ProductRepository
from repositories.quality_test_repository import QualityRepository
from repositories.auth_repository import AuthRepository
from core.exceptions import InvalidTokenException, InsufficientPermissionsException
from core.security import get_user_data_from_token


async def get_token_from_cookie(request: Request) -> str:
    return request.cookies.get("access_token")


async def get_current_user(token: str = Depends(get_token_from_cookie)) -> dict:
    if not token:
        raise InvalidTokenException("Токен отсутствует. Войдите в систему.")

    user_data = get_user_data_from_token(token)

    return user_data


async def get_current_admin_user(user_data: dict = Depends(get_current_user)) -> dict:
    if not user_data.get("is_admin", False):
        raise InsufficientPermissionsException()

    return user_data


async def get_auth_repository(
        session: AsyncSession = Depends(get_db)
) -> AuthRepository:
    return AuthRepository(session)


async def get_product_repository(
        session: AsyncSession = Depends(get_db)
) -> ProductRepository:
    return ProductRepository(session)


async def get_quality_repository(
        session: AsyncSession = Depends(get_db)
) -> QualityRepository:
    return QualityRepository(session)


async def get_product_service(
        repo: ProductRepository = Depends(get_product_repository),
        user_repo: AuthRepository = Depends(get_auth_repository),
        user_data: dict = Depends(get_current_user)
) -> ProductService:
    return ProductService(repo, user_repo, user_data)


async def get_quality_service(
        repo: QualityRepository = Depends(get_quality_repository),
        user_repo: AuthRepository = Depends(get_auth_repository),
        user_data: dict = Depends(get_current_user)
) -> QualityService:
    return QualityService(repo, user_repo, user_data)


async def get_auth_service(
        repo: AsyncSession = Depends(get_auth_repository)
) -> AuthService:
    return AuthService(repo)


async def get_product_admin_service(
        repo: ProductRepository = Depends(get_product_repository),
        user_repo: AuthRepository = Depends(get_auth_repository),
        user_data: dict = Depends(get_current_admin_user)
) -> ProductService:
    return ProductService(repo, user_repo, user_data)


async def get_quality_admin_service(
        repo: QualityRepository = Depends(get_quality_repository),
        user_repo: AuthRepository = Depends(get_auth_repository),
        user_data: dict = Depends(get_current_admin_user)
) -> QualityService:
    return QualityService(repo, user_repo, user_data)
