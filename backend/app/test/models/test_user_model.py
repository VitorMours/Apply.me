import pytest
import pytest_asyncio
from beanie.exceptions import RevisionIdWasChanged
from datetime import datetime, timezone
from beanie import Document


class TestUserModel:

    def test_if_can_import_user_model(self) -> None:
        try:
            from app.models.user_model import User
            assert User is not None, "O modelo User não foi encontrado"
        except ImportError:
            pytest.fail("Não foi possível importar o modelo User")

    def test_if_user_is_beanie_document(self) -> None:
        from app.models.user_model import User
        assert issubclass(User, Document), "O modelo User deve herdar de beanie.Document"

    def test_if_user_has_correct_fields(self) -> None:
        from app.models.user_model import User
        fields = User.model_fields
        assert "name" in fields, "O modelo está faltando o campo 'name'"
        assert "email" in fields, "O modelo está faltando o campo 'email'"
        assert "password" in fields, "O modelo está faltando o campo 'password'"
        assert "role" in fields, "O modelo está faltando o campo 'role'"
        assert "created_at" in fields, "O modelo está faltando o campo 'created_at'"
        assert "updated_at" in fields, "O modelo está faltando o campo 'updated_at'"

    def test_if_collection_name_is_users(self) -> None:
        from app.models.user_model import User
        assert User.Settings.name == "users", "O nome da coleção deve ser 'users'"

    def test_if_created_at_has_default_factory(self) -> None:
        from app.models.user_model import User
        field = User.model_fields.get("created_at")
        assert field is not None, "O campo created_at não existe"
        assert field.default_factory is not None, "O campo created_at deve ter default_factory"

    def test_if_updated_at_has_default_factory(self) -> None:
        from app.models.user_model import User
        field = User.model_fields.get("updated_at")
        assert field is not None, "O campo updated_at não existe"
        assert field.default_factory is not None, "O campo updated_at deve ter default_factory"

    def test_if_created_at_default_returns_datetime(self) -> None:
        from app.models.user_model import User
        field = User.model_fields.get("created_at")
        assert callable(field.default_factory), "default_factory de created_at deve ser callable"
        value = field.default_factory()
        assert isinstance(value, datetime), "O default_factory de created_at deve retornar um datetime"

    def test_if_updated_at_default_returns_datetime(self) -> None:
        from app.models.user_model import User
        field = User.model_fields.get("updated_at")
        assert callable(field.default_factory), "default_factory de updated_at deve ser callable"
        value = field.default_factory()
        assert isinstance(value, datetime), "O default_factory de updated_at deve retornar um datetime"

    def test_if_model_config_allows_arbitrary_types(self) -> None:
        from app.models.user_model import User
        config = User.model_config
        assert config.get("arbitrary_types_allowed") is True, \
            "O model_config deve ter arbitrary_types_allowed=True"

    def test_if_model_config_allows_populate_by_name(self) -> None:
        from app.models.user_model import User
        config = User.model_config
        assert config.get("populate_by_name") is True, \
            "O model_config deve ter populate_by_name=True"

    def test_if_name_field_is_str(self) -> None:
        from app.models.user_model import User
        field = User.model_fields.get("name")
        assert field.annotation is str, "O campo 'name' deve ser do tipo str"

    def test_if_password_field_is_str(self) -> None:
        from app.models.user_model import User
        field = User.model_fields.get("password")
        assert field.annotation is str, "O campo 'password' deve ser do tipo str"

    def test_if_role_field_is_str(self) -> None:
        from app.models.user_model import User
        field = User.model_fields.get("role")
        assert field.annotation is str, "O campo 'role' deve ser do tipo str"

    @pytest.mark.asyncio
    async def test_if_user_model_can_be_instantiated(self, mock_db) -> None:
        from app.models.user_model import User
        user = User(
            name="João Silva",
            email="joao@email.com",
            password="senha_segura_123",
            role="admin"
        )
        assert user.name == "João Silva"
        assert user.email == "joao@email.com"
        assert user.password == "senha_segura_123"
        assert user.role == "admin"
        assert isinstance(user.created_at, datetime)
        assert isinstance(user.updated_at, datetime)

    @pytest.mark.asyncio
    async def test_if_user_instantiation_fails_without_required_fields(self, mock_db) -> None:
        import pydantic
        from app.models.user_model import User
        with pytest.raises(pydantic.ValidationError):
            User(email="joao@email.com")

    @pytest.mark.asyncio
    async def test_if_two_users_with_same_data_are_equal_in_fields_without_saving_data(self, mock_db) -> None:
        from app.models.user_model import User
        user1 = User(name="Ana", email="ana@email.com", password="123", role="user")
        user2 = User(name="Ana", email="ana@email.com", password="123", role="user")
        assert user1.name == user2.name
        assert user1.email == user2.email
        assert user1.role == user2.role
        
        
class TestUserModelErrors:
    @pytest.mark.asyncio
    async def test_if_raise_errors_when_try_to_save_user_with_email_already_used(self, mock_db) -> None:
        from app.models.user_model import User
        user1 = User(name="Ana", email="ana.damasio@gmail.com", role="user", password="123asd")
        user2 = User(name="Ana", email="ana.damasio@gmail.com", role="user", password="123asd")
        await user1.save()
        
        with pytest.raises(RevisionIdWasChanged):
            await user2.save()
            
    @pytest.mark.asyncio
    async def test_if_not_raises_errors_with_duplicate_data_except_email_in_use(self, mock_db) -> None:
        from app.models.user_model import User
        user1 = User(name="Ana", email="ana.damasio@gmail.com", role="user", password="123asd")
        user2 = User(name="Ana", email="ana.demaise@gmail.com", role="user", password="123asd")
        await user1.save()
        await user2.save() 
        
        assert user2.name == user1.name
        assert user2.role == user1.role
        assert user2.password == user1.password
        assert user2.email != user1.email
        
    @pytest.mark.asyncio 
    async def test_if_can_create_user_with_email_already_registered_and_deleted(self, mock_db) -> None:
        from app.models.user_model import User 
        user1 = User(name="Ana", email="ana.damasio@gmail.com", role="user", password="123asd")
        user2 = User(name="Damasio", email="ana.damasio@gmail.com", role="admin", password="123123123asdasdasd")
        await user1.save()
        await user1.delete()
        await user2.save()
        
        assert user2.email == "ana.damasio@gmail.com"       