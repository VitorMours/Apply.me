import pytest 
import importlib 
import inspect 
from pydantic import BaseModel, Field

class TestAuthCredentialsSchema:
  def test_if_can_import_credentials_schema(self) -> None:
    module = importlib.import_module("app.schemas.auth_schemas")
    class_ = module.Credentials
    assert inspect.isclass(class_)
    assert issubclass(class_, BaseModel)    
    
  def test_if_credentials_class_have_correct_fields(self) -> None:
    from app.schemas.auth_schemas import Credentials
    fields = Credentials.model_fields 
    assert fields.get("email") is not None
    assert fields.get("password") is not None

  def test_if_credentials_class_parse_data_correctly(self) -> None:
    from app.schemas.auth_schemas import Credentials 
    credentials_instance = Credentials(email="jvrezendemoura@gmail.com", password="32322916")
    assert credentials_instance.email == "jvrezendemoura@gmail.com"
    assert credentials_instance.password == "32322916"    
    assert isinstance(credentials_instance.password, str)    
    
    
  def test_if_crendetials_class_raise_error_with_empty_email(self) -> None:
    pass
    
    
class TestLoginCrendetialsSchema:
  pass 

class TestSigninCredentialsSchema:
  pass
