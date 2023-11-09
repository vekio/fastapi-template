from fastapi import FastAPI
import uvicorn

from fastapi_template.config import settings
from fastapi_template.api.v1.router import api_router


app = FastAPI(
    title=settings.project, openapi_url=f"/{settings.api_version}/openapi.json"
)
app.include_router(router=api_router, prefix=f"/api/{settings.api_version}")


@app.on_event("startup")
def _startup():
    print("Running")


@app.on_event("shutdown")
def _shutdown():
    print("Shutdown")


def main() -> None:
    """Entrypoint de la aplicación."""

    uvicorn.run(
        "fastapi_template.run:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=True,
    )


if __name__ == "__main__":
    main()
