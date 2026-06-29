from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.middleware.logging_middleware import logging_middleware
from contextlib import asynccontextmanager 
from app.core.config.db import connect_db
from app.api import api 
import logging 

origins = ["*"]

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
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
 
@app.get("/health")
async def health():
    return {"status": "ok"}





