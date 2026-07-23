from functools import lru_cache
from langchain_ollama import ChatOllama 
from src.core.config import settings


@lru_cache
def get_ollama_client() -> ChatOllama:
    return ChatOllama(
        model = settings.MODEL_NAME,
        temperature = 0.3, 
        base_url= settings.OLLAMA_BASE_URL
    )
