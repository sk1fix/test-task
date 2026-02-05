from fastapi import Depends, APIRouter

from api.dependencies import get_quality_service, get_quality_admin_service
from services.quality_service import QualityService
from schemas.quality_test import GetTestDto, CreateTestDto


quality = APIRouter(tags=['Quality Test Route'])


@quality.post(
    '/tests/{batch_number}',
    summary='Register Test',
    tags=['Quality Test Route']
)
async def create(
    data: CreateTestDto,
    batch_number: str,
    service: QualityService = Depends(get_quality_admin_service)
) -> CreateTestDto:
    result = await service.create_test(data, batch_number)
    return result


@quality.get(
    '/tests/{batch_number}',
    summary='Get Test by batch number',
    tags=['Quality Test Route']
)
async def get_by_number(
    batch_number: str,
    service: QualityService = Depends(get_quality_service)
) -> GetTestDto:
    result = await service.get_by_number(batch_number)
    return result
