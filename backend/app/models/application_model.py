from pydantic import Field 
from beanie import Document 
from datetime import datetime 

class Application(Document):
    name: str 
    company: str 
    level: str
    position: str 
    salary: float 
    created_at: datetime
    uploaded_at: datetime 
    
    class Settings:
        name = "applications"