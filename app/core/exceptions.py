from fastapi import HTTPException, status


class ProductNotFoundException(HTTPException):
    def __init__(self, batch_number: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Продукты с номером партии {batch_number} не найден"
        )


class ProductAlreadyExistsException(HTTPException):
    def __init__(self, batch_number: str):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Продукты с номером партии {batch_number} уже существует"
        )


class QualityTestNotFoundException(HTTPException):
    def __init__(self, batch_number: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Теста качества для номером партии {batch_number} не найдено"
        )
