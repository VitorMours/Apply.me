from pydantic import BaseModel

class QuestionSchema(BaseModel):
  message: str
  multiple_choice: bool

class ResponseSchema(BaseModel):
  response: str