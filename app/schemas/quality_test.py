from datetime import datetime

from pydantic import BaseModel


class CreateTestDto(BaseModel):
    inspector_fullname: str
    standart: str
    chemical_composition: str
    analysis_result: bool


class GetTestDto(BaseModel):
    inspector_fullname: str
    standart: str
    chemical_composition: str
    analysis_result: bool
    created_at: datetime