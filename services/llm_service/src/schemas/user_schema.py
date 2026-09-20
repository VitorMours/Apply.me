from pydantic import BaseModel

class UserSchema(BaseModel):
  firstName: str
  lastName: str 
  email: str
  
  
  

