from beanie import Document, Indexed 
from bson import ObjectId
from datetime import datetime
from pydantic import Field
from uuid import UUID
from typing import Optional 

class User(Document):
    name: str
    email: Indexed(str, unique=True) # type: ignore
    password: str
    role: str

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "users"
        
    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True,
    }