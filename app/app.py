from fastapi import FastAPI
from app.api.v1.articles.router import router as articles_router_v1
from app.api.v2.articles.router import router as articles_router_v2

from app.core.middlewares import ClientAccessMiddleware

app = FastAPI(title="Article API")

app.add_middleware(ClientAccessMiddleware)
app.include_router(articles_router_v1)
app.include_router(articles_router_v2)
