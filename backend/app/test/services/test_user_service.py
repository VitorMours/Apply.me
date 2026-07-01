import pytest

from app.schemas.user_schemas import UserCreate
from app.services.security_service import AuthService
from app.services.user_service import UserService


class TestUserService:
    @pytest.mark.asyncio
    async def test_create_user_hashes_password(self, mock_db) -> None:
        service = UserService()
        user_data = UserCreate(
            name="Ana",
            email="ana@email.com",
            role="user",
            password="senha_segura_123"
        )

        created_user = await service.create_user(user_data)

        assert created_user.password != user_data.password
        assert AuthService().verify_password(user_data.password, created_user.password) is True