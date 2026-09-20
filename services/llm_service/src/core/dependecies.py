from fastapi import Header, HTTPException, status 
from typing import Annotated 


async def required_content_type_as_json(content_type: Annotated[str | None, Header()] = None ) -> str:
  if not content_type or not content_type.startswith("application/json"):
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Content-Type especifica dados de tipos incompativeis com a aplicacao",
    )
  return content_type