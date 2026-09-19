from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles 
from src.api.v1.chat import router as chat_router
from src.web.routes import router as web_router 

app = FastAPI()
app.mount("/static", StaticFiles(directory="src/static"), name="static")

app.include_router(chat_router)
app.include_router(web_router)

@app.get("/")
async def llm_service_health():
    return {"status":"ok"}

