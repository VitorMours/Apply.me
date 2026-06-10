from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie 
from app.models.user_model import User 
from app.core.config import settings

async def connect_db():
    # 1. Cria o cliente do MongoDB usando a URL
    client = AsyncIOMotorClient(settings.MONGODB_URL)
    
    # 2. Obtém a instância do banco de dados explicitamente
    # Substitua 'settings.DB_NAME' pelo nome do seu banco de dados
    database = client[settings.DB_NAME]
    
    # 3. Inicializa o Beanie passando o objeto database (MotorDatabase)
    await init_beanie(
        database=database, 
        document_models=[User]
    )
