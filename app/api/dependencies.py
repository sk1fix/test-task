from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.session import get_db
from services.product_service import ProductService
from services.quality_service import QualityService
from services.auth_service import AuthService
from repositories.product_repository import ProductRepository
from repositories.quality_test_repository import QualityRepository
from repositories.auth_repository import AuthRepository


async def get_product_repository(
        session: AsyncSession = Depends(get_db)
) -> ProductRepository:
    return ProductRepository(session)


async def get_product_service(
        repo: AsyncSession = Depends(get_product_repository)
) -> ProductService:
    return ProductService(repo)


async def get_quality_repository(
        session: AsyncSession = Depends(get_db)
) -> QualityRepository:
    return QualityRepository(session)


async def get_quality_service(
        repo: AsyncSession = Depends(get_quality_repository)
) -> QualityService:
    return QualityService(repo)


async def get_auth_repository(
        session: AsyncSession = Depends(get_db)
) -> AuthRepository:
    return AuthRepository(session)


async def get_auth_service(
        repo: AsyncSession = Depends(get_auth_repository)
) -> AuthService:
    return AuthService(repo)
