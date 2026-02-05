from fastapi import Depends, APIRouter

from api.dependencies import get_product_service, get_product_admin_service
from services.product_service import ProductService
from schemas.product import CreateProductDto, GetProductDto

product = APIRouter(tags=['Products Route'])


@product.post(
    '/product',
    summary='Register product',
    tags=['Products Route']
)
async def create(
    data: CreateProductDto,
    service: ProductService = Depends(get_product_admin_service)
) -> CreateProductDto:
    result = await service.create_product(data)
    return result


@product.get(
    '/product/{batch_number}',
    summary='Get product by batch number',
    tags=['Products Route']
)
async def get_by_batch_number(
    batch_number: str,
    service: ProductService = Depends(get_product_service)
) -> GetProductDto:
    result = await service.get_by_number(batch_number)
    return result


@product.delete(
    '/product/{batch_number}',
    summary='Remove product by batch number',
    tags=['Products Route']
)
async def delete_product(
    batch_number: str,
    service: ProductService = Depends(get_product_admin_service)
):
    result = await service.delete_product(batch_number)
    return result
