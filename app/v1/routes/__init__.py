from fastapi import APIRouter
from app.config.routes import include_route

# Import specific routes
# Example: from app.v1.routes.file import file
from app.v1.routes.example_route import router as example_router

router = APIRouter()

# Custom routes
# Example: include_route(router, file_route, prefix="/file", tags=["file"])
include_route(router, example_router, prefix="/example", tags=["example"])

# Generic routes
# Example: include_route(router, "example", prefix="/example", tags=["example"])
include_route(router, "my_route", prefix="/my_route", tags=["example"])


__all__ = ["router"]


