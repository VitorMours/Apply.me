import pytest_asyncio
from beanie import init_beanie
from mongomock_motor import AsyncMongoMockClient
from app.models.user_model import User
from app.models.application_model import Application  # Importe o modelo aqui

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "models: testes unitários rápidos"
    )
    config.addinivalue_line(
        "markers", "services: testes de integração"
    )
    config.addinivalue_line(
        "markers", "schemas: testes que demoram mais"
    )
    config.addinivalue_line(
        "markers", "api: testes críticos de smoke test"
    )

def pytest_collection_modifyitems(config, items):
    for item in items:
        path = str(item.fspath)
        if "/unit/" in path:
            item.add_marker("unit")
        elif "/integration/" in path:
            item.add_marker("integration")
            
            
# TODO: Precisa organizar os markers acima, ainda.


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