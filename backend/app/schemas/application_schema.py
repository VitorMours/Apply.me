from pydantic import BaseModel 
from typing import Optional, List
from datetime import datetime

class ApplicationSchema(BaseModel):
    name: str
    company: str
    position: str
    
class CreateApplicationSchema(ApplicationSchema):
    status: str

class UpdateApplicationSchema(ApplicationSchema):
    name: str | None = None
    company: str | None = None
    position: str | None = None
    status: str | None = None
    created_at: datetime
    
    
class ReadApplicationSchema(ApplicationSchema):
    pass