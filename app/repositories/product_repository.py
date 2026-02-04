from sqlalchemy import select
from sqlalchemy.orm import Session

from models.models import Product
from schemas.product import GetProductDto, CreateProductDto


class ProductRepository:
    def __init__(self, session) -> None:
        self.session = session

    async def create_product(self, data: CreateProductDto) -> Product:
        query = Product(**data.model_dump())
        self.session.add(query)
        await self.session.commit()
        await self.session.refresh(query)

        return query

    async def get_product_by_grade(self, data: str) -> Product:
        query = select(Product).where(data == Product.alloy_grade)
        result = await self.session.execute(query)

        return result.scalars().first()
