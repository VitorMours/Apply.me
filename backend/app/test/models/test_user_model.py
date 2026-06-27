import pytest 
import importlib 
import inspect 
from beanie import Document 

class TestUserModel:
    def test_if_can_import_the_user_model(self) -> None:
        try:
            from app.models.user_model import User
            assert issubclass(User, Document)     
        except ImportError:
            pytest.fail("Houve um problema importando o modelo de usuario")
            
    def test_if_user_model_have_correct_fields(self) -> None:
        try:
            pass
        except ImportError:
            pass
            
    def test_if_can_create_the_user_instance(self) -> None:
        pass 