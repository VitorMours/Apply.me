from pydantic import BaseModel 
import importlib 
import inspect 

class TestResponseSchema:
    def test_if_its_running(self) -> None:
        assert True 
        
    def test_if_can_import_the_response_schema(self) -> None:
        try:
            from src.schemas.response_schema import ResponseSchema
            assert ResponseSchema is not None 
            assert inspect.isclass(ResponseSchema)
            assert issubclass(ResponseSchema, BaseModel)
        except ImportError:
            raise ImportError("Was not possible to import the response schema")