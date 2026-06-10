from beanie import Document, Indexed
from datetime import datetime
from pydantic import Field
from uuid import UUID

class User(Document):
    name: str
    email: Indexed(str, unique=True) # type: ignore
    password: str
    role: str

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "users"