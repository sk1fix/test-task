from pydantic import BaseModel

from models.models import ProductStatusEnum

class CreateProductDto(BaseModel):
    alloy_grade: str
    weight: float
    batch_number: str
    status: ProductStatusEnum