from fastapi import FastAPI, APIRouter, Request
# from config import settings
from api import router
from typing import Any
from fastapi.responses import HTMLResponse
from config import settings
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title= settings.PROJECT_NAME,openapi_url=settings.API_V1_STR+"/openapi.json")

root_router = APIRouter()
@root_router.get("/")
def index(request: Request) -> Any:
    """Basic HTML response."""
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Welcome to the API</h1>"
        "<div>"
        "Check the docs: <a href='/docs'>here</a>"
        "</div>"
        "</body>"
        "</html>"
    )

    return HTMLResponse(content=body)

app.include_router(router, prefix=settings.API_V1_STR)
app.include_router(root_router)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=settings.BACKEND_CORS_ORIGINS,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

if __name__ == "__main__":
    # Use this for debugging purposes only
    # logger.warning("Running in development mode. Do not run like this in production.")
    import uvicorn

    uvicorn.run(app, host="localhost", port=3000, log_level="info")

