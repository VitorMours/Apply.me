from fastapi import FastAPI
from contextlib import asynccontextmanager 
from app.core.config.db import connect_db
from app.api import api 

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    yield 

app = FastAPI(lifespan=lifespan)
app.include_router(api, prefix="api")    

@app.get("/health")
async def health():
    return {"status": "ok"}





