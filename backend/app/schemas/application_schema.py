from pydantic import BaseModel 
from typing import Optional, List
from datetime import datetime

class ApplicationSchema(BaseModel):
    name: str
    company: str
    position: str
    
    
class CreateApplicationSchema(ApplicationSchema):
    pass 

class UpdateApplicationSchema(ApplicationSchema):
    pass