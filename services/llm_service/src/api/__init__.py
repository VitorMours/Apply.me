from fastapi import APIRouter, Depends
from src.core.dependecies import required_content_type_as_json 
from .v1 import router as v1_router

router = APIRouter(prefix="/api", tags=["api"], dependencies=[Depends(required_content_type_as_json)])



router.include_router(v1_router)

