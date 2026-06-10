from fastapi import APIRouter, Depends, HTTPException, status
from app.services.security_service import AuthService
from app.schemas.auth_schemas import LoginCredentials, ReceiveToken
from app.services.user_service import UserService 


router = APIRouter(tags=["auth"])

def get_user_service():
    return UserService()

def get_auth_service():
    return AuthService()

@router.post("/login", response_model=ReceiveToken)
async def login(
    data: LoginCredentials, 
    user_service: UserService = Depends(get_user_service), 
    auth_service: AuthService = Depends(get_auth_service)
):
    searched_user = await user_service.fetch_user_by_email(data.email)
    
    if not searched_user or not auth_service.verify_password(data.password, searched_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas"
        )
    
    access_token = auth_service.create_access_token(
        data={"email": data.email, "id": str(searched_user.id)}
    )
    
    return {
        "access_token": access_token, 
        "token_type": "bearer", 
        "user_id": str(searched_user.id)
    }

@router.post("/signin")
async def signin():
    pass