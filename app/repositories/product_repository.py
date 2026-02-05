from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from models.models import Product
from core.exceptions import ProductAlreadyExistsException, ProductNotFoundException
from schemas.product import GetProductDto, CreateProductDto


class ProductRepository:
    def __init__(self, session) -> None:
        self.session = session

    async def create_product(self, data: CreateProductDto) -> Product:
        if await self.check_product_exists(data.batch_number):
            raise ProductAlreadyExistsException(data.batch_number)

        query = Product(**data.model_dump())
        self.session.add(query)
        await self.session.commit()
        await self.session.refresh(query)

        return query

    async def get_product_by_number(self, batch_number: str) -> Product:
        query = select(Product).where(batch_number == Product.batch_number)
        result = await self.session.execute(query)
        product = result.scalar_one_or_none()
        
        if product is None:
            raise ProductNotFoundException(batch_number)
        
        return product

    async def delete_product(self, data: str):
        query = delete(Product).where(data == Product.batch_number)
        await self.session.execute(query)
        await self.session.commit()

        return True
    
    async def check_product_exists(self, batch_number: str) -> bool:
        query = select(Product.id).where(Product.batch_number == batch_number)
        result = await self.session.execute(query)
        return result.scalar_one_or_none() is not None
