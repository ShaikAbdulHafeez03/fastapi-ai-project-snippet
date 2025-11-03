# from fastapi import Depends
# from app.db import get_db
# from app.repositories.user_repository import UserRepository
# from app.services.user_service import UserService
# from app.schemas.user import UserCreate, UserRead
# from app.schemas.token import Token
# from app.core.handle_jwt import create_access_token

# async def register_controller(user_in: UserCreate, db=Depends(get_db)) -> UserRead:
#     repo = UserRepository(db)
#     svc = UserService(repo)
#     return await svc.register_user(user_in)

# async def login_controller(email: str, password: str, db=Depends(get_db)) -> Token:
#     repo = UserRepository(db)
#     svc = UserService(repo)
#     user = await svc.authenticate_user(email, password)
#     token = create_access_token(subject=str(user.id))
#     return Token(access_token=token)
