from beanie import PydanticObjectId
from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime 
from typing import Optional 

class BaseUser(BaseModel):
    name: str 
    email: EmailStr
    role: str

class UserCreate(BaseUser):
    password: str

class UserRead(BaseUser):
    id: PydanticObjectId
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(
        from_attributes=True,
        json_encoders={
            PydanticObjectId: str
        }
    )    
    
class UserUpdate(BaseUser):
    username: Optional[str] = None
    role: Optional[str] = None
    email: Optional[EmailStr] = None
