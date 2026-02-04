from sqlalchemy import select, update

from models.models import QualityTest, Product, ProductStatusEnum


class QualityRepository:
    def __init__(self, session):
        self.session = session

    async def create_test(self, data, product_batch_number):
        async with self.session.begin():
            query = QualityTest(**data.model_dump())
            self.session.add(query)
            await self.session.flush()

            new_status = ProductStatusEnum.PASSED if data.analysis_result else ProductStatusEnum.FAILED
            stmt = update(Product).where(
                Product.batch_number == product_batch_number
            ).values(test_id=query.id, status=new_status)
            await self.session.execute(stmt)

        return query

    async def get_test_by_batch_number(self, batch_number):
        query = select(QualityTest).join(Product, Product.test_id ==
                                         QualityTest.id).where(Product.batch_number == batch_number)
        result = await self.session.execute(query)

        return result.scalars().first()
