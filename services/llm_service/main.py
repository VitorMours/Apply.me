from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
async def llm_service_health():
    return {"status":"ok"}
