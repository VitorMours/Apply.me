from fastapi import APIRouter 
from uuid import UUID

router = APIRouter(tags=["users"])

@router.get("/")
async def get_all_users():
    pass

@router.get("/{id}")
async def get_user_by_id(id: UUID):
    pass

