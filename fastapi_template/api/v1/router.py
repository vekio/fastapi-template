from fastapi.routing import APIRouter

from ejercicio_curso_python.api.api_v1.endpoints import hello_world


api_router = APIRouter()


api_router.include_router(
    hello_world.router, prefix="/hello-world", tags=["hello-world"]
)
