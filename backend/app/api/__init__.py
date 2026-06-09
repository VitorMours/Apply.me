from fastapi import APIRouter
import v1

api = APIRouter()


api.include_router(v1, prefix="v1")