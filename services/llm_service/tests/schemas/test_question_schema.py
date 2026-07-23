import pytest
import importlib
import inspect 
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

    
    def test_if_question_schema_can_correctly_validate_data(self) -> None:
        module = importlib.import_module("src.schemas.question_schema")
        class_ = module.QuestionSchema 
        instance = class_(
            question = "Pergunta do sistema de forma a serializar",
            multiple_choice = False 
        ) 
        assert instance.multiple_choice == False, ""
        assert instance.question == "Pergunta do sistema de forma a serializar", ""

class TestQuestionSchemaErrors:
    def test_if_is_running(self) -> None:
        assert True 

    def test_if_can_import_the_question_schema(self) -> None:
        try:
            from src.schemas.question_schema import QuestionSchema
            assert QuestionSchema is not None
            assert inspect.isclass(QuestionSchema)
            assert issubclass(QuestionSchema, BaseModel)

        except ImportError:
            pytest.fail("Was not possible to import the question schema module")


    def test_if_question_schema_can_raise_errors_with_incorrect_data_in_multiple_choice_fields(self) -> None:
        module = importlib.import_module("src.schemas.question_schema")
        class_ = module.QuestionSchema 
        incorrect_data = ["asd",123, 123.45, None, ""]

        # TODO: Corrijir
        #for data in incorrect_data:
        #    with pytest.raises(ValidationError, NameError):
        #        instance = class_(
        #            question="Question",
        #            multiple_choice=data
        #        )






