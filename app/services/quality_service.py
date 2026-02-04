from schemas.quality_test import CreateTestDto, GetTestDto


class QualityService:
    def __init__(self, repo) -> None:
        self.repo = repo

    async def get_by_number(self, data: str) -> GetTestDto:
        result = await self.repo.get_test_by_batch_number(data)
        new_dto = GetTestDto(
            inspector_fullname=result.inspector_fullname,
            standart=result.standart,
            chemical_composition=result.chemical_composition,
            analysis_result=result.analysis_result,
            created_at=result.created_at
        )
        return new_dto

    async def create_test(
            self,
            data: CreateTestDto,
            batch_number: str
    ) -> CreateTestDto:
        result = await self.repo.create_test(data, batch_number)
        new_dto = CreateTestDto(
            inspector_fullname=result.inspector_fullname,
            standart=result.standart,
            chemical_composition=result.chemical_composition,
            analysis_result=result.analysis_result
        )
        return new_dto
