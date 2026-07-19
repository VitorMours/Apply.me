from app.services.security_service import AuthService
from typing import Optional, List
from app.models.application_model import Application as ApplicationModel
from app.schemas.application_schema import ApplicationSchema, CreateApplicationSchema

class ApplicationService:
    def __init__(self, auth_service: AuthService) -> None:
        self.auth_service =  auth_service or AuthService()
        
    def create_application(self, application_data: CreateApplicationSchema) -> None:
        pass
    
    def update_application(self, application_id, application_new_data) -> None:
        pass
    
    def search_application(self) -> None:
        pass
    
    def search_application_by_id(self) -> None:
        pass
    
    def delete_application(self) -> None:
        pass