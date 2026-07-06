import pytest 
import importlib 
import inspect 
from beanie import Document, Link
from app.models.user_model import User 
from datetime import datetime 

class TestApplicationModel:
    def test_if_can_import_application_model(self) -> None:
        try:
            from app.models.application_model import Application 
            assert inspect.isclass(Application)
            assert issubclass(Application, Document)
            assert Application is not None
        except Exception:
            raise ImportError("Was not possible to import the application model for tests")
        
    def test_if_application_model_have_correct_fields(self) -> None:
        module = importlib.import_module("app.models.application_model")
        fields = module.Application.model_fields
        assert "name" in fields, "name field not found in application model"
        assert "company" in fields, "company field not found in application model"
        assert "level" in fields, "level field not found in application model"
        assert "position" in fields, "position field not found in application model"
        assert "salary" in fields, "salary field not found in application model"
        assert "created_at" in fields, "created_at field not found in application model"
        assert "updated_at" in fields, "updated_at field not found in application model"
        assert "candidate" in fields, "candidate field not found in application model"
        
# Função auxiliar para verificar a anotação
    
    def test_if_application_model_fields_have_correct_types(self) -> None:
        module = importlib.import_module("app.models.application_model")
        fields = module.Application.model_fields
        
        def check_field(field_name: str, expected_type: type):
            field_info = fields.get(field_name)
            assert field_info is not None, f"O campo {field_name} não existe no modelo"
            assert field_info.annotation == expected_type, \
                f"O campo {field_name} deveria ser do tipo {expected_type}, mas é {field_info.annotation}"

        check_field("name", str)
        check_field("company", str)
        check_field("level", str)
        check_field("position", str)
        check_field("salary", float)
        check_field("created_at", datetime)
        check_field("updated_at", datetime)
        check_field("candidate", Link[User])
        
    def test_if_application_model_have_correct_settings_name(self) -> None:
        module = importlib.import_module("app.models.application_model")
        model = module.Application 
        assert model.Settings.name == "applications", "The model name its incorrect"

    def test_if_created_at_has_default_factory(self) -> None:
        module = importlib.import_module("app.models.application_model")
        field = module.Application.model_fields.get("created_at")
        assert field is not None 
        assert field.default_factory is not None
        
    def test_if_updated_at_has_default_factory(self) -> None:
        module = importlib.import_module("app.models.application_model")
        field = module.Application.model_fields.get("updated_at")
        assert field is not None    
        
    def test_if_can_create_application_instance(self) -> None:
        pass 
    
        