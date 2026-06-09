from typing import Annotated 
import pyjwt 

from pwdlib import PasswordHash
from jwt.exceptions import InvalidTokenError

class SecurityService:
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    @staticmethod
    def verify_password() -> None:
        pass 
    
    @staticmethod 
    def hash_password() -> None:
        pass
    
    def authenticate_user() -> None:
        pass 
    
    def create_access_token() -> None:
        pass 
    
    def create_refresh_token() -> None:
        pass

    