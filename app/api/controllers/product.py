from fastapi import Depends, APIRouter

from api.dependencies import get_product_service
from services.product_service import ProductService
from schemas.product import CreateProductDto, GetProductDto

product = APIRouter(tags=['Products Route'])


@product.post('/product', summary='Register product', tags=['Products Route'])
async def create(data: CreateProductDto, service: ProductService = Depends(get_product_service)) -> CreateProductDto:
    result = await service.create_product(data)
    return result


@product.get('/product/{grade}', summary='Get product by alloy grade', tags=['Products Route'])
async def get_by_grade(grade: str, service: ProductService = Depends(get_product_service)) -> GetProductDto:
    result = await service.get_by_grade(grade)
    return result
