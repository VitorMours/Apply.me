import certifi
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models.user_model import User
from app.core.config import settings

async def connect_db():
    is_local = settings.IS_LOCAL
    client_kwargs = {}
    if not is_local:
        client_kwargs = {
            "tls": True,
            "tlsCAFile": certifi.where()
        }

    client = AsyncIOMotorClient(settings.MONGODB_URL, **client_kwargs)
    database = client[settings.DB_NAME]
    await init_beanie(database=database, document_models=[User])