import enum
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base


class ProductStatusEnum(enum.Enum):
    PENDING = "в ожидании тестов"
    PASSED = "соответствует"
    FAILED = "брак"


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    alloy_grade: Mapped[str]
    weight: Mapped[float]
    batch_number: Mapped[str]
    status: Mapped[ProductStatusEnum] = mapped_column(
        Enum(ProductStatusEnum), default=ProductStatusEnum.PENDING)
    test_id: Mapped[int | None] = mapped_column(ForeignKey(
        'quality_test.id', ondelete="SET NULL"), unique=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )


class QualityTest(Base):
    __tablename__ = "quality_test"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    inspector_fullname: Mapped[str]
    standart: Mapped[str]
    chemical_composition: Mapped[str]
    analysis_result: Mapped[bool]
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )
