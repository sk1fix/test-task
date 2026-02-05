from sqlalchemy import select, update

from models.models import QualityTest, Product, ProductStatusEnum
from schemas.quality_test import GetTestDto, CreateTestDto
from core.exceptions import QualityTestNotFoundException


class QualityRepository:
    def __init__(self, session):
        self.session = session

    async def create_test(
            self,
            data: CreateTestDto,
            product_batch_number: str
    ) -> QualityTest:
        async with self.session.begin():
            query = QualityTest(**data.model_dump())
            self.session.add(query)
            await self.session.flush()

            if data.analysis_result:
                new_status = ProductStatusEnum.PASSED
            else:
                new_status = ProductStatusEnum.FAILED
            stmt = update(Product).where(
                Product.batch_number == product_batch_number
            ).values(test_id=query.id, status=new_status)
            await self.session.execute(stmt)

        return query

    async def get_test_by_batch_number(
            self,
            batch_number: str
    ) -> QualityTest:
        query = select(QualityTest).join(
            Product,
            Product.test_id == QualityTest.id
        ).where(Product.batch_number == batch_number)
        result = await self.session.execute(query)

        test = result.scalar_one_or_none()
        
        if test is None:
            raise QualityTestNotFoundException(batch_number)
        
        return test
