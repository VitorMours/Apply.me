from pydantic import BaseModel

class QuestionSchema(BaseModel):
    message: str
    multiple_choice: bool