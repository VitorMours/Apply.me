from pydantic import BaseModel, EmailStr
from datetime import datetime 
from typing import Optional 

class BaseUser(BaseModel):
    name: str 
    email: EmailStr

class UserCreate(BaseUser):
    password: str

class UserRead(BaseUser):
    pass 
    created_at: datetime

    class Config: 
        from_attributes = True 
        
class UserUpdate(BaseUser):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
