from fastapi import APIRouter, Request 
from fastapi.templating import Jinja2Templates

router = APIRouter(tags=["web"])

templates = Jinja2Templates(directory="src/templates")

@router.get('/')
async def web_index(request: Request):
  return templates.TemplateResponse(
    request=request,
    name="web/index.html" 
  )

@router.get("/chat")
async def web_chat(request: Request):
  return templates.TemplateResponse(
    request = request,
    name="web/chat.html"
  )