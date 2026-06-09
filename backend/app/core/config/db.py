from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie 
from app.models.user_model import User 

async def connect_db():
    client = AsyncIOMotorClient("") # url
    await init_beanie(database=client.db_name, document_models=[User])