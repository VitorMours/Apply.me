from fastapi import APIRouter 
from .users import router as users
from .auth import router as auth 

v1 = APIRouter()

v1.include_router(users, prefix="/users")
v1.include_router(auth, prefix="/auth")
