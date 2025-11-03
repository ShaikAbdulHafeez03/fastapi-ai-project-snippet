from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from fastapi import FastAPI, Request
from app.config import settings
from app.error_handler.custom_exceptions import RateLimitExceededException


limiter = Limiter(
    key_func=get_remote_address,
    storage_uri=settings.REDIS_URL,
    default_limits=["10/minute"],
)

async def custom_rate_limit_handler(request: Request, exc: RateLimitExceeded):
    raise RateLimitExceededException(
        detail=f"Rate limit exceeded: {getattr(exc, 'detail', 'Try again later')}"
    )
    
def init_rate_limiter(app: FastAPI):
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, custom_rate_limit_handler)


