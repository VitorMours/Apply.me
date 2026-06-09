from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager 
from app.core.config.db import connect_db
from app.api import api 

origins = ["*"]

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

app.include_router(api, prefix="api")   
 
@app.get("/health")
async def health():
    return {"status": "ok"}





