import uvicorn
from fastapi_template.config import settings


def main() -> None:
    """Entrypoint de la aplicación."""
    uvicorn.run(
        "fastapi_template.run:init_app",
        host=settings.api_host,
        port=settings.api_port,
        reload=True,
    )


if __name__ == "__main__":
    main()
