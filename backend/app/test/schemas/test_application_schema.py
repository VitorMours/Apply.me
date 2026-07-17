import importlib 
import inspect 
import pydantic
from pydantic import BaseModel 
import pytest

class TestApplicationSchema:
    def test_if_can_run_test(self) -> None:
        assert True 
        
    def test_if_can_import_application_schema(self) -> None:
        try:
            from app.schemas.application_schema import ApplicationSchema
            assert inspect.isclass(ApplicationSchema)
            assert issubclass(ApplicationSchema, BaseModel)
        except ImportError:
            raise ImportError("")
        
    def test_if_application_schema_have_correct_fields(self) -> None:
        module = importlib.import_module("app.schemas.application_schema")
        class_ = module.ApplicationSchema
        fields = class_.model_fields 
        assert "name" in fields, "Application schema precisa ter o campo name"
        assert "company" in fields, "Application schema precisa ter o campo company"
        assert "position" in fields, "Application schema precisa ter o campo position"

    def test_if_application_schema_can_validate_normal_common_data(self) -> None:
        module = importlib.import_module("app.schemas.application_schema")
        class_ = module.ApplicationSchema
        instance = class_(
            name = "Fullstack Vuejs & Laravel",
            company = "Demetrius",
            position = "Full Stack Developer",
        )        
        assert instance.name == "Fullstack Vuejs & Laravel", "O name da instance nao foi validado de maneira correta"
        assert instance.company == "Demetrius", "O Company da instancia nao foi validado de maneira correta"
        assert instance.position == "Full Stack Developer", "O position da instancia nao foi validado de maneira correta"

        
    def test_if_application_schema_raise_validations_errors_with_miss_values(self) -> None:
        module = importlib.import_module("app.schemas.application_schema")
        class_ = module.ApplicationSchema
        
        with pytest.raises(pydantic.ValidationError):
            instance = class_(
                company="Demetrius",
                position="Entry Level Developer"
            )
            
        with pytest.raises(pydantic.ValidationError):
            instance = class_(
                name="Demetrius",
                position="Entry Level Developer"
            )
            
        with pytest.raises(pydantic.ValidationError):
            instance = class_(
                company="Demetrius",
                name="Entry Level Developer"
            )
        
    def test_if_application_schema_raise_validations_errors_with_incorrect_values_types(self) -> None:
        module = importlib.import_module("app.schemas.application_schema")
        class_ = module.ApplicationSchema            
        
        with pytest.raises(pydantic.ValidationError):
            instance = class_(
                position = 123,
                company="Demetrius",
                name="Entry Level Developer"
            )
            
        with pytest.raises(pydantic.ValidationError):
            instance = class_(
                name = 123,
                company="Demetrius",
                position="Entry Level Developer"
            )
            
        with pytest.raises(pydantic.ValidationError):
            instance = class_(
                company = 123,
                position="Demetrius",
                name="Entry Level Developer"
            )
            
    def test_if_application_schema_raises_validation_error_with_empty_values(self) -> None:
        pass
            
class TestCreateApplicationSchema:
    def test_if_is_running(self) -> None:
        assert True 
        
    def test_if_can_import_the_create_application_schema_class(self) -> None:
        try:
            from app.schemas.application_schema import CreateApplicationSchema, ApplicationSchema
            assert inspect.isclass(CreateApplicationSchema)
            assert issubclass(CreateApplicationSchema, ApplicationSchema)
        except ImportError:
            pytest.fail("Was not possible to import the create application schema")
        

class TestUpdateApplicationSchema:
    def test_if_is_running(self) -> None:
        assert True 
    
    def test_if_can_import_the_update_application_schema_class(self) -> None:
        try:
            from app.schemas.application_schema import UpdateApplicationSchema, ApplicationSchema
            assert inspect.isclass(TestCreateApplicationSchema)
            assert issubclass(UpdateApplicationSchema, ApplicationSchema)
        except ImportError:
            pytest.fail("Was not possible to import the update application schema")