from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from app.services.user_service import UserService
from app.schemas.user_schemas import UserCreate, UserRead, UserResponse, UserUpdate

router = APIRouter(tags=["users"])

def get_user_service() -> UserService:
    return UserService()

@router.get("/", response_model=List[UserResponse])
async def get_all_users(service=Depends(get_user_service)) -> List[UserRead]:
    try:
        return await service.fetch_users()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, user_service: UserService = Depends(get_user_service)):
    try:
        return await user_service.create_user(user)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )

@router.patch("/{id}", response_model=UserRead, status_code=status.HTTP_200_OK)
async def update_user(user: UserUpdate, user_service: UserService = Depends(get_user_service)):
    try:
        #user_service.
        pass
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            deftail=str(e)
        )




@router.get("/me")
async def get_user_by_id():
    pass
