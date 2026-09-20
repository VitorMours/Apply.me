from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from src.core.llm_client import get_ollama_client
from src.schemas.chat_schema import QuestionSchema
from src.services import llm_service
from src.services.llm_service import LLMService
from src.services.chat_history_service import ChatService

router = APIRouter(prefix="/chat")

def get_ollama_service(client=Depends(get_ollama_client)) -> LLMService:
    """
    Ollama Service Dependency Injector to be used in the routes     
    """
    return LLMService(client)

def get_chat_service(ollama_service: LLMService = Depends(get_ollama_service)) -> ChatService:
    """
    Chat Service that gets the ollama model service and injects in the own llm service     
    """
    return ChatService(ollama_service)

@router.post(
    "/",
    status_code=200,
    summary="simple LLM answer, without using the stream of data to give the fluid processing experience"
)
async def chat(request: QuestionSchema, chat_service = Depends(get_chat_service)):
    result = await chat_service.handle_message(request.message)
    return result

@router.post(
    "/stream",
    summary="LLM answer utilizing the streaming element to give a more fluid answer for the user"
)
async def chat_stream(request: QuestionSchema, llm_service = Depends(get_ollama_service)):
    async def event_generator():
        async for chunk in llm_service.stream(request.message):
            yield f"{chunk}"
    return StreamingResponse(event_generator(), media_type="text/event-stream")