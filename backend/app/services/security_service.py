from typing import Annotated, Any
import jwt
from pwdlib import PasswordHash
from datetime import datetime, timezone, timedelta
from starlette.concurrency import run_in_threadpool

class AuthService:
    ALGORITHM = "HS256"
    # Changed default to a proper timedelta object
    ACCESS_TOKEN_EXPIRE_MINUTES = timedelta(minutes=30)
    SECRET_KEY = "change-me"  # In production, use environment variables!
    
    def __init__(self) -> None:
        self.password_hash = PasswordHash.recommended()

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.password_hash.verify(plain_password, hashed_password)

    async def hash_password(self, password: str) -> str:
        
        return await run_in_threadpool(self.password_hash.hash, password)
    
    def create_access_token(self, data: dict[str, Any], expires_delta: timedelta | None = None) -> str:
        to_encode = data.copy()
        
        # Determine expiration time
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + self.ACCESS_TOKEN_EXPIRE_MINUTES
            
        to_encode.update({"exp": expire})
        
        encoded_jwt = jwt.encode(
            to_encode, 
            self.SECRET_KEY, 
            algorithm=self.ALGORITHM
        )
        return encoded_jwt

    def authenticate_user(self, username: str, password: str) -> dict[str, Any] | None:
        """
        Placeholder: You would typically fetch user from DB here
        and use self.verify_password.
        """
        # Logic: 
        # user = db.get_user(username)
        # if user and self.verify_password(password, user.hashed_password):
        #     return user
        return None