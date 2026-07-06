from pydantic import Field 
from beanie import Document, Link 
from datetime import datetime 
from app.models.user_model import User 

class Application(Document):
    name: str 
    company: str 
    level: str
    position: str 
    salary: float 
    created_at: datetime = Field(default_factory=lambda: datetime.now(datetime.utc))
    uploaded_at: datetime = Field(default_factory=lambda: datetime.now(datetime.utc))
    candidate: Link[User]
    class Settings:
        name = "applications"