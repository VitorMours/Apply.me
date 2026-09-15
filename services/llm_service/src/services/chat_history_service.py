import uuid

from src.services.llm_service import LLMService

class ChatService:
    def __init__(self, ollama_service: LLMService):
        self._ollama = ollama_service

    async def handle_message(self, message: str) -> dict:
        response = await self._ollama.generate(message)

        return {"response": response}