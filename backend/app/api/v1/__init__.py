from fastapi import APIRouter 
from .users import router as users

v1 = APIRouter()

v1.include_router(users, prefix="users")
