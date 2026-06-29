import logging 
import time 
from fastapi import Request 

logger = logging.getLogger("api")

async def logging_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    
    duration = time.time() - start_time
    
    logger.info(
        f"{request.method} {request.url.path} "
        f"| status: {response.status_code} "
        f"| duration: {duration:.3f}s "
        f"| ip: {request.client.host}"
    )

    return response