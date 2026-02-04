from datetime import datetime

from pydantic import BaseModel

from models.models import ProductStatusEnum


class CreateProductDto(BaseModel):
    alloy_grade: str
    weight: float
    batch_number: str


class GetProductDto(BaseModel):
    alloy_grade: str
    weight: float
    batch_number: str
    status: str
    test_id: int | None
    created_at: datetime
