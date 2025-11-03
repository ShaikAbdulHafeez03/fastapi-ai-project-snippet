from fastapi import APIRouter, Request  # ✅ add Request
from app.core.handle_jwt import create_client_jwt
from app.schemas.token import Token
from app.core.rate_limiter import limiter

router = APIRouter(prefix="/v1/authenticate", tags=["authenticate"])


@router.post("/access")
@limiter.limit("5/minute")
async def login(request: Request, token: Token):
    res = create_client_jwt(token=token)
    return res


@router.post("/test")
async def login(token: Token):
    res = "Hi"
    return res
