from fastapi import APIRouter 
from uuid import UUID

router = APIRouter(tags=["users"])

@router.get("/")
async def get_all_users():
    pass

@router.get("/me")
async def get_user_by_id():
    """Pegar o usuário com base no seu ID, dado presente dentro do JWT"""
    pass



