from pydantic import Field 
from beanie import Document, Link 
from datetime import datetime, timezone
from app.models.user_model import User 

class Application(Document):
    name: str 
    company: str 
    level: str
    position: str 
    salary: float 
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    candidate: Link[User]
    class Settings:
        name = "applications"