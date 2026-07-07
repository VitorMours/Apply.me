import pytest_asyncio
from beanie import init_beanie
from mongomock_motor import AsyncMongoMockClient
from app.models.user_model import User
from app.models.application_model import Application  # Importe o modelo aqui

@pytest_asyncio.fixture(scope="function")
async def mock_db():
    client = AsyncMongoMockClient()
    db = client["test_db"]
    await init_beanie(database=db, document_models=[User, Application])
    yield db

@pytest_asyncio.fixture(scope="function")
async def mock_user(mock_db):
    instance = User(
        name="Vitor Moura",
        email="vitor.moura@gmail.com",
        password="32322916aA!",
        role="Student"
    ) 
    await instance.save()
    return instance