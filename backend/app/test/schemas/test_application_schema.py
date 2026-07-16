import importlib 
import inspect 
from pydantic import BaseModel 


class TestApplicationSchema:
    def test_if_can_run_test(self) -> None:
        assert True 
        
    def test_if_can_import_application_schema(self) -> None:
        try:
            from app.schemas.application_schema import ApplicationSchema
            
        except ImportError:
            raise ImportError("")