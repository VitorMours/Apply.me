from pydantic import BaseModel 
from typing import Optional, List
from datetime import datetime

class ApplicationSchema(BaseModel):
    name: str
    company: str
    position: str
    
class CreateApplicationSchema(ApplicationSchema):
    created_at: datetime
    status: str

class UpdateApplicationSchema(ApplicationSchema):
    status: str | None = None
    updated_at: datetime 
    