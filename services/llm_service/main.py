from fastapi import FastAPI 
from src.api.v1.chat import router as chat_router

app = FastAPI()
app.include_router(chat_router)

@app.get("/")
async def llm_service_health():
    return {"status":"ok"}
