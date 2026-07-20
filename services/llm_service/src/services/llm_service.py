from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from services.llm_service.src.core.llm_client import get_ollama_client

class LLMService:
    def __init__(self) -> None:
        self._llm = get_ollama_client()
    