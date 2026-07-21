import pytest
import importlib
from pydantic import BaseModel

class TestQuestionSchema:
    def test_if_can_run(self) -> None:
        assert True 
        
    def test_if_can_import_the_question_schema(self) -> None:
        try:
            from src.schemas.question_schema import QuestionSchema
            assert QuestionSchema is not None
            assert issubclass(QuestionSchema, BaseModel)
        except ImportError:
            raise ImportError("Was not possible to import the error")
        
    def test_if_schema_have_correct_fields(self) -> None:
        module = importlib.import_module("src.schemas.question_schema")
        class_ = module.QuestionSchema
        fields = class_.model_fields
        assert "question" in fields, "O campo de question precisa estar no schema"
        assert "multiple_choice" in fields, "O campo de multiple_choices precisa estar no schema"
        