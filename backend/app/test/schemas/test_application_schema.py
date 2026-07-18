import importlib 
import inspect 
import pydantic
from pydantic import BaseModel 
import pytest
from datetime import datetime  



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
        
    def test_if_create_application_schema_have_correct_fields(self) -> None:
        module = importlib.import_module("app.schemas.application_schema")
        class_ = module.CreateApplicationSchema
        fields = class_.model_fields
        assert "name" in fields, "Name precisa estar dentro dos campos de CreateApplicationSchema"
        assert "company" in fields, "Company precisa estar dentro dos campos de CreateApplicationSchema"
        assert "position" in fields, "Position precisa estar dentro dos campos de CreateApplicationSchema"
        assert "status" in fields, "Status precisa estar dentro dos campos de CreateApplicationSchema"
        assert "created_at" in fields, "created_at precisa estar dentro dos campos de CreateApplicationSchema"


    def test_if_can_validate_correct_data_in_the_schema(self) -> None:
        module = importlib.import_module("app.schemas.application_schema")
        class_ = module.CreateApplicationSchema
        time = datetime.now()
        instance = class_(

            name="Fullstack with laravel",
            company="Demetriux",
            position="Entry-Level",
            status="DONE",
            created_at=time
        )
        
        assert instance.name == "Fullstack with laravel", "A instance precisa do campo de nome preenchido"
        assert instance.company == "Demetriux", "A instance precisa do campo de company preenchido"
        assert instance.position == "Entry-Level", "A instance precisa do campo de position preenchido"
        assert instance.status == "DONE", "A instance precisa do campo de status preenchido"
        assert instance.created_at == time, "A instance precisa do campo de dadata preeenchido, em especial esse campo é gerado automaticamente pelo modelo"

    def test_if_can_raise_value_with_empty_fields_in_schema(self) -> None:
        module = importlib.import_module("app.schemas.application_schema")
        class_ = module.CreateApplicationSchema
        with pytest.raises(pydantic.ValidationError):
            instance = class_(
                name = "",
                company = "Demetrius",
                position = "Mid-Level",
                status = "INPROGRESS",
                created_at = datetime.date
            )
            
        with pytest.raises(pydantic.ValidationError):
            instance = class_(
                name = "Demetrius",
                company = "",
                position = "Mid-Level",
                status = "INPROGRESS",
                created_at = datetime.date
            )
        
        with pytest.raises(pydantic.ValidationError):
            instance = class_(
                name = "Demetrius",
                company = "Demetrius",
                position = "",
                status = "INPROGRESS",
                created_at = datetime.date
            )
        
        with pytest.raises(pydantic.ValidationError):
            instance = class_(
                name = "Demetrius",
                company = "Demetrius",
                position = "Mid-Level",
                status = "",
                created_at = datetime.date
            )
            
    def test_if_can_raise_value_with_miss_value_fields_in_schema(self) -> None:
        module = importlib.import_module("app.schemas.application_schema")
        class_ = module.CreateApplicationSchema
        
        with pytest.raises(pydantic.ValidationError):
            instance = class_(
                company = "Demetrius",
                position = "Mid-Level",
                status = "Entry Elvel",
                created_at = datetime.date
            )
 
        with pytest.raises(pydantic.ValidationError):
            instance = class_(
                name = "Demetrius",
                position = "Mid-Level",
                status = "Entry Level",
                created_at = datetime.date
            )
 
        with pytest.raises(pydantic.ValidationError):
            instance = class_(
                name = "Demetrius",
                company = "Mid-Level",
                status = "Entry Level",
                created_at = datetime.date
            )
 
        with pytest.raises(pydantic.ValidationError):
            instance = class_(
                name = "Demetrius",
                position = "Mid-Level",
                company = "Entry Level",
                created_at = datetime.date
            )
 
    
    def test_if_can_raise_error_with_incorrect_types_values_in_schema(self) -> None:
        module = importlib.import_module("app.schemas.application_schema")
        class_ = module.CreateApplicationSchema
        
        with pytest.raises(pydantic.ValidationError):
            instane = class_(
                name = 123,
                company = "Demetrius",
                position = "Mid-Level",
                status = "INPROGRESS",
                created_at = datetime.date
            )
            
        with pytest.raises(pydantic.ValidationError):
            instane = class_(
                name = "Fullstack with laravel and vuejs",
                company = 123,
                position = "Entry=level",
                status = "ACTIVE",
                created_at = datetime.date
            )
            
        with pytest.raises(pydantic.ValidationError):
            instane = class_(
                name = "Full stack laravel and vue",
                company = "Demetrius",
                position = 123,
                status = "DONE",
                created_at = datetime.date
            )
            
        with pytest.raises(pydantic.ValidationError):
            instane = class_(
                name = "FullStack vye and alaravel",
                company = "Demetrius",
                position = "Full Stack developer",
                status = 123,
                created_at = datetime.date
            )
            
        with pytest.raises(pydantic.ValidationError):
            instane = class_(
                name = "FullStack vye and alaravel",
                company = "Demetrius",
                position = "Full Stack developer",
                status = "IN PROGRESS",
                created_at = "asdsad"
            )

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
            
    def test_if_can_validate_correct_data_in_the_schema(self) -> None:
        module = importlib.import_module("app.schemas.application_schema")
        class_ = module.UpdateApplicationSchema
        time = datetime.now()
        instance = class_(
            name = "Demetrius",
            company = "Demetriux",
            position = "Entry Level",
            updated_at = time
        )
        assert instance.name == "Demetrius", "Falta o nome da vaga"
        assert instance.company == "Demetriux", "falta o nome da companhia"
        assert instance.position == "Entry Level", "Falta o nivel da vaga"
        assert instance.updated_at == time, "O timestamp de criacao esta incorreto"
        
        