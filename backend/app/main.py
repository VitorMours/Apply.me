from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request
from app.core.exceptions import AppException, UserNotFoundException
from app.core.middleware.logging_middleware import logging_middleware
from app.core.config.db import connect_db
from app.api import api
from contextlib import asynccontextmanager
import logging


origins = ["*"]

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await connect_db()
        logger.info("Database connected successfully")
    except Exception as e:
        logger.critical(f"Failed to connect to database: {e}")
        raise
    yield


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.middleware("http")(logging_middleware)
app.include_router(api, prefix="/api")


@app.exception_handler(UserNotFoundException)
async def user_not_found_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "error_code": "USER_NOT_FOUND",
            "message": exc.message,
            "details": {"identifier": str(exc.identifier)},
        },
    )


@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=400,
        content={"error_code": "APP_ERROR", "message": exc.message},
    )


@app.get("/health")
async def health():
    return {"status": "ok"}
