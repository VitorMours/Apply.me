import pytest 
import importlib 
import inspect 
import pydantic 
from pydantic import BaseModel 

class TestUserSchemas:
    def test_if_can_import_the_user_schema(self) -> None:
        try:
            from app.schemas import user_schemas
            assert hasattr(user_schemas, "UserCreate"), "O arquivo nao possui schema de criacao de usuario"
            assert hasattr(user_schemas, "UserRead"), "O arquivo nao possui schema de leitura de usuarios"
            assert hasattr(user_schemas, "BaseUser"), "O Arquivo nao possui o schema basico de usuario"
            assert hasattr(user_schemas, "UserUpdate"), "O arquivo nao possui o schema de atualização de usuario"
        except ImportError:
            pytest.fail("Was not possible to import the user schema to test")        
        
    def test_if_base_user_schema_is_pydantic_model(self) -> None:
        module = importlib.import_module("app.schemas.user_schemas")
        class_ = module.BaseUser
        assert issubclass(class_, BaseModel), "O modelo base dos schemas nao possui a herança correta do pydantic"
        
    def test_if_others_schemas_area_pydantic_base_models(self) -> None:
        module = importlib.import_module("app.schemas.user_schemas")
        create_class  = module.UserCreate
        update_class = module.UserUpdate
        read_class = module.UserRead
        
        assert issubclass(create_class, module.BaseUser), "O schema de criação de usuário não possui a herança correta"
        assert issubclass(update_class, module.BaseUser), "O schema de atualização de usuário não possui a herança correta"
        assert issubclass(read_class, module.BaseUser), "O schema de leitura de usuário não possui a herança correta"
    
    def test_if_base_user_have_correct_fields(self) -> None:
        module = importlib.import_module("app.schemas.user_schemas")
        class_ = module.BaseUser
        fields = class_.model_fields 
        assert "name" in fields, "O schema base esta faltando o campo de nome" 
        assert "email" in fields, "O schema base esta faltando o campo de email" 
        assert "role" in fields, "O schema base esta faltando o campo de cargo" 
    
    def test_if_create_schema_have_correct_fields(self) -> None:
        module = importlib.import_module("app.schemas.user_schemas")
        class_ = module.UserCreate 
        fields = class_.model_fields
        assert "name" in fields, "O schema de criacao de usuario esta faltando o campo de nome"
        assert "email" in fields, "O schema de criacao de usuario  esta faltando o campo de email"
        assert "role" in fields, "O schema de criacao de usuario  esta faltando o campo de cargo"
        assert "password" in fields, "O schema de criacao de usuario  esta faltando o campo de senha"
    
    def test_if_update_schema_have_correct_fields(self) -> None:
        module = importlib.import_module("app.schemas.user_schemas")
        class_ = module.UserUpdate 
        fields = class_.model_fields 
        assert "name" in fields, "O schema de atualização de usuario esta faltando o campo de nome, e ele deve ser opcional"
        assert "email" in fields, "O schema de atualização de usuario esta faltando com o campo de email, e ele deve ser opcional"
        assert "role" in fields, "O schema de atualização de usuario esta faltando com o campo de cargo, e ele deve ser opcional"
        
    def test_if_read_schema_have_correct_fields(self) -> None:
        module = importlib.import_module("app.schemas.user_schemas")
        class_ = module.UserRead 
        fields = class_.model_fields
        assert "id" in fields, "O schema de leitura de usuario esta faltando o campo de id"
        assert "name" in fields, "O schema de leitura de usuario esta faltando o campo de nome"
        assert "email" in fields, "O schema de leitura de usuario esta faltando o campo de email"
        assert "role" in fields, "O schema de leitura de usuario esta faltando o campo de cargo"
        assert "created_at" in fields, "O schema de leitura de usuario esta faltando o timestamp de criacao"
        assert "updated_at" in fields, "O schema de leitura de usuario esta faltando o timestamp de atualizacao"
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def test_to_schema_user_in_the_create_user_schema_model(self) -> None:
        pass
        