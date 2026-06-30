from fastapi import APIRouter, Depends, HTTPException, Response, status
from app.services.security_service import AuthService
from app.schemas.auth_schemas import LoginCredentials, ReceiveToken, SigninCredentials
from app.services.user_service import UserService
import logging
from app.core.exceptions import UserNotFoundException

logger = logging.getLogger(__name__)

router = APIRouter(tags=["auth"])


def get_user_service():
    return UserService()


def get_auth_service():
    return AuthService()


@router.post("/login", response_model=ReceiveToken)
async def login(
    response: Response,
    data: LoginCredentials,
    user_service: UserService = Depends(get_user_service),
    auth_service: AuthService = Depends(get_auth_service),
):
    searched_user = await user_service.fetch_user_by_email(data.email)
    if not searched_user or not auth_service.verify_password(
        data.password, searched_user.password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas"
        )

    access_token = auth_service.create_access_token(
        data={"email": data.email, "id": str(searched_user.id)}
    )

    response.set_cookie(
        key="access_token",
        httponly=True,
        value=access_token,
        max_age=3600,
        secure=False,
        samesite="lax",
    )

    return {"user_id": str(searched_user.id)}


@router.post("/signin")
async def signin(
    response: Response,
    data: SigninCredentials,
    user_service: UserService = Depends(get_user_service),
    auth_service: AuthService = Depends(get_auth_service),
):
    if not (finded_user := await user_service.fetch_user_by_email(data.email)):
        raise UserNotFoundException(f"Nao existe registro com: {data.email} dentro do banco de dados")
        
