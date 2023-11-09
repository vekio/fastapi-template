from fastapi import FastAPI

from fastapi_template.config import settings
from fastapi_template.api.v1.router import api_router


def init_app() -> FastAPI:
    app = FastAPI(
        title=settings.project, openapi_url=f"/{settings.api_version}/openapi.json"
    )

    # @app.on_event("startup")
    # def _startup():
    #     print("Running")

    # @app.on_event("shutdown")
    # def _shutdown():
    #     print("Shutdown")

    app.include_router(router=api_router, prefix=f"/api/{settings.api_version}")

    return app
