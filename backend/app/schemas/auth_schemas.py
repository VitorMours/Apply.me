from pydantic import BaseModel, Field 
from typing import Optional 
from datetime import datetime 



class Credentials(BaseModel):
    email: str 
    password: str 

class LoginCredentials(Credentials):
    pass 

class SigninCredentials(Credentials):
    name: str 
    role: str | None = Field(default="student")
    
    
class ReceiveToken(BaseModel):
    access_token: str
    token_type: str
    user_id: str 