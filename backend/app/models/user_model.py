from pydantic import Field 
from beanie import Document
from datetime import datetime

class User(Document):
    email: str
    password: str
    role: str
    created_at: datetime
    updated_at: datetime
    
    class Settings:
        name = "users"