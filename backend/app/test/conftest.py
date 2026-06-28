import pytest_asyncio
import pytest
from beanie import init_beanie
from mongomock_motor import AsyncMongoMockClient
from app.models.user_model import User


@pytest_asyncio.fixture(scope="function")
async def mock_db():
    client = AsyncMongoMockClient()
    db = client["test_db"]
    await init_beanie(database=db, document_models=[User])
    yield db
    client.close()