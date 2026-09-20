import pydantic
import pytest 
import importlib 
import inspect 

class TestChatSchema:
  def test_if_is_running(self) -> None:
    assert True
    
  def test_if_can_import_the_chat_schema_file(self) -> None:
    try:
      from src.schemas import chat_schema
      assert chat_schema != None
       
    except ImportError:
      raise ImportError("Was not possible to import the chat schemas file")
    
  def test_if_chat_schema_file_have_question_schema(self) -> None:
    module = importlib.import_module("src.schemas.chat_schema")
    question_schema = module.QuestionSchema 
    assert question_schema is not None 
    assert inspect.isclass(question_schema)
    assert issubclass(question_schema, pydantic.BaseModel)
    
  def test_if_chat_schema_file_have_response_schema(self) -> None:
    module = importlib.import_module("src.schemas.chat_schema")
    response_schema = module.ResponseSchema
    assert response_schema is not None 
    assert inspect.isclass(response_schema)
    assert issubclass(response_schema, pydantic.BaseModel)
    

class TestQuestionSchema:
  def test_if_is_running(self) -> None:
    assert True
    
  def test_if_question_schema_have_correct_fields(self) -> None:
    pass
  
class TestResponseSchema:
  def test_if_is_running(self) -> None:
      assert True
    
  def test_if_response_schema_have_correct_fields(self) -> None:
    pass