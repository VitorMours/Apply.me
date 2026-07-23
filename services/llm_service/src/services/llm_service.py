from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.core.llm_client import get_ollama_client
from langchain_ollama import ChatOllama

class LLMService:
    def __init__(self, client: ChatOllama | None = None) -> None:
        self._llm = client or get_ollama_client()
       
        self.prompt = ChatPromptTemplate.from_messages([
            SystemMessage("""
                Você é um criado de curriculo, sua função, é entender que tipo de profissional o usuário é, e a partir disso criar o perfil dele de forma
                que posteriormente, na etapa de criação dos currículos personalizados, vamos ter as opções de ferramentas e capacidades do nosso usuário, para que 
                possamos assim escolher cada uma das capacidades e das habilidades do usuário, que são mais adequadas a cada uma das vagas as quais eles deseja aplicar,
                objetificando aumentar ao máximo as chances dele ser chamado para a entrevista de emprego, e ser assim contratado, de forma a deslumbrar o recrutador com 
                o currículo do nosso usuário.
            """),
            ("human", "{input}"),
        ])

        self.chain =  self.prompt | self._llm | StrOutputParser()

    async def generate(self, message: str) -> str:
        return await self.chain.ainvoke({"input":message})

    async def stream(self, message:str) -> str:
        async for chunk in self.chain.astream({"input": message}):
            yield chunk


llm_service = LLMService()
