import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI

from api.controllers.product import product
from api.controllers.quality_test import quality
from api.controllers.auth import auth
from core.config import settings


app = FastAPI()

app.include_router(product)
app.include_router(quality)
app.include_router(auth)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )
