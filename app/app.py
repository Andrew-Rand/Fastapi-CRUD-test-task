from fastapi import FastAPI
from app.api.articles.router import router as articles_router

from app.core.middlewares import ClientAccessMiddleware

app = FastAPI(title="Article API")

app.add_middleware(ClientAccessMiddleware)
app.include_router(articles_router)
