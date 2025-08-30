from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import routes_auth, routes_predict
from app.middleware.logging_middleware import LoggingMiddleware
from app.core.exceptions import register_exception_handlers

app = FastAPI(title='FastAPI Car Prediction API')

app.add_middleware(LoggingMiddleware)

app.include_router(routes_auth.router,tags=['Auth'])
app.include_router(routes_predict.router, tags=['Predict'])

Instrumentator().instrument(app).expose(app)

register_exception_handlers(app)