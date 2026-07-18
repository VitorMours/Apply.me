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
        
        
    def test_if_can_validate_base_user_data(self) -> None:
        module = importlib.import_module("app.schemas.user_schemas")
        class_ = module.BaseUser
        
        valid_user = class_(
            name = "Vitor Moura",
            email = "jvrezendemoura@gmail.com",
            role = "Student"
        )
        assert valid_user.name == "Vitor Moura", "O nome do usuario nao esta sendo validado corretamente" 
        assert valid_user.email == "jvrezendemoura@gmail.com", "O email do usuario nao esta sendo validado corretamente "
        assert valid_user.role == "Student", "O cargo do usuario nao esta sendo validado corretamente"
        
    def test_if_user_base_schema_validation_raise_errors_with_empty_class(self) -> None:
        module = importlib.import_module("app.schemas.user_schemas")
        class_ = module.BaseUser
        
        with pytest.raises(pydantic.ValidationError):
            invalid_user = class_()
            
    def test_if_user_base_schema_validation_raise_erros_with_numerical_name(self) -> None:
        module = importlib.import_module("app.schemas.user_schemas")
        class_ = module.BaseUser 
        
        with pytest.raises(pydantic.ValidationError):
            invalid_user = class_(
                name=123,
                email="jvrezendemoura@gmail.com",
                role="Student"
            )    
    
    def test_if_user_base_schema_validation_raise_erros_with_numerical_email(self) -> None:
        module = importlib.import_module("app.schemas.user_schemas")
        class_ = module.BaseUser
        
        with pytest.raises(pydantic.ValidationError):
            invalid_user = class_(name="Lucas", email=123, role="Student")
            
    def test_if_user_base_schema_validation_raises_errors_with_numerical_role(self) -> None:
        module = importlib.import_module("app.schemas.user_schemas")
        class_ = module.BaseUser
        
        with pytest.raises(pydantic.ValidationError):
            invalid_user = class_(name="Vitor Lucas", email="jvrezendemoura@gmail.com", role=123)
            
    def test_if_user_create_schema_validate_user_data(self) -> None:
        module = importlib.import_module("app.schemas.user_schemas")
        class_ = module.UserCreate
        user_instance = class_(
            name="Joao Vitor", 
            email="jvrezendemoura@gmail.com",
            password="123asd",
            role="Student",
        )
        assert user_instance.name == "Joao Vitor", "O campo de nome nao foi corretamente validado"
        assert user_instance.email == "jvrezendemoura@gmail.com", "O campo de email nao foi corretamente validado"
        assert user_instance.password == "123asd", "O campo de senha nao foi corretamente validado"
        assert user_instance.role == "Student", "O campo de cargo nao foi corretamente validado"
    
    def test_user_create_schema_validation_raises_error_with_numerical_password(self) -> None:
        module = importlib.import_module("app.schemas.user_schemas")
        class_ = module.UserCreate 
        
        with pytest.raises(pydantic.ValidationError):
            user_instance = class_(
                name = "Vitor",
                email = "vitor.moura@gmail.com",
                role = "Student",
                password = 123,
            )
        
    def test_user_create_schema_validation_raises_error_with_empty_password(self) -> None:
        module = importlib.import_module("app.schemas.user_schemas")
        class_ = module.UserCreate 
        
        with pytest.raises(pydantic.ValidationError):
            user_instancer = class_(
                name = "Vitor Lucas",
                email = "vitor.lucas@gmail.com",
                role = "Student",
            )
            
    def test_user_update_schema_validate_data(self) -> None:
        module = importlib.import_module("app.schemas.user_schemas")
        class_ = module.UserUpdate
        
        user_instance = class_(
            name="Vitor Mario",
            email="vitor.mario@gmail.com",
            role="Teatcher"
        )
        
        assert user_instance.name == "Vitor Mario", "A validacao do nome foi feita incorretamente"
        assert user_instance.email == "vitor.mario@gmail.com", "A validacao do email foi feita incorretamente"
        assert user_instance.role == "Teatcher", "A validacao do cargo foi feita incorretamente"
        
    def test_if_user_update_schema_accepts_empty_values_except_the_email(self) -> None:
        module = importlib.import_module("app.schemas.user_schemas")
        class_ = module.UserUpdate
        
        user_instance = class_(
            name="",
            email="email@email.com",
            role=""
        )
        assert user_instance.name == ""
        assert user_instance.role == ""
        assert user_instance.email == "email@email.com"
            
            
class TestUserReadSchemas:
    pass 

# TODO: Criar o schema relacionado ao mesmo
        