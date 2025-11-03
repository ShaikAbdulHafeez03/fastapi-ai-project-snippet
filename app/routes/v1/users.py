from fastapi import APIRouter, Depends, HTTPException
from app.core.handle_jwt import create_client_jwt
# from app.schemas.user import UserCreate, UserRead
from app.schemas.token import Token
# from app.controllers.user_controller import register_controller, login_controller
# from app.db import get_db
# from app.core.rate_limiter import limit
router = APIRouter(prefix="/v1/users", tags=["users"])

# @router.post("/register", response_model=UserRead)
# async def register_user(body: UserCreate, db=Depends(get_db)):
#     return await register_controller(body, db)


# @router.post("/login")
# @rate_limiter.limit("5/minute")
# async def login(token: Token):
#     res=create_client_jwt(token=token)
#     return res
