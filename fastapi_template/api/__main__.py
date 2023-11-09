import uvicorn

from fastapi_template.config import settings
from fastapi_template.api.v1.router import api_router


if __name__ == "__main__":
    uvicorn.run(
        "fastapi_template.api.app:init_app",
        host=settings.api_host,
        port=settings.api_port,
        reload=True,
    )
