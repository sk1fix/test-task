from schemas.product import CreateProductDto, GetProductDto


class ProductService:
    def __init__(self, repo, user_repo, user_data) -> None:
        self.repo = repo
        self.user_repo = user_repo
        self.user_data = user_data

    async def get_by_number(self, data: str) -> GetProductDto:
        await self.user_repo.get_by_id(self.user_data.get("user_id"))
        result = await self.repo.get_product_by_number(data)
        new_dto = GetProductDto(
            alloy_grade=result.alloy_grade,
            weight=result.weight,
            batch_number=result.batch_number,
            status=result.status.value,
            test_id=result.test_id,
            created_at=result.created_at
        )
        return new_dto

    async def create_product(
            self,
            data: CreateProductDto
    ) -> CreateProductDto:
        await self.user_repo.get_by_id(self.user_data.get("user_id"))
        result = await self.repo.create_product(data)
        new_dto = CreateProductDto(
            alloy_grade=result.alloy_grade,
            weight=result.weight,
            batch_number=result.batch_number
        )
        return new_dto

    async def delete_product(self, data: str):
        await self.user_repo.get_by_id(self.user_data.get("user_id"))
        result = await self.repo.delete_product(data)
        return result
