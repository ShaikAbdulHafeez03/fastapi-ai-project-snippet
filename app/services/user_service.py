# from app.repositories.user_repository import UserRepository
# from app.schemas.user import UserCreate, UserRead
# from app.core.security import get_password_hash, verify_password
# from fastapi import HTTPException, status

# class UserService:
#     def __init__(self, repo: UserRepository):
#         self.repo = repo

#     async def register_user(self, user_data: UserCreate) -> UserRead:
#         existing = await self.repo.get_user_by_email(user_data.email)
#         if existing:
#             raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
#         hashed = get_password_hash(user_data.password)
#         user = await self.repo.create_user(user_data.email, hashed)
#         return UserRead.model_validate(user)

#     async def authenticate_user(self, email: str, password: str):
#         user = await self.repo.get_user_by_email(email)
#         if not user or not verify_password(password, user.hashed_password):
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
#         return user

#     async def get_user(self, user_id: int):
#         user = await self.repo.get_user_by_id(user_id)
#         if not user:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
#         return UserRead.from_orm(user)

#     async def update_user(self, user_id: int, update_data: dict):
#         user = await self.repo.get_user_by_id(user_id)
#         if not user:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
#         # optionally filter allowed fields...
#         updated = await self.repo.update_user(user, update_data)
#         return UserRead.from_orm(updated)

#     async def delete_user(self, user_id: int):
#         user = await self.repo.get_user_by_id(user_id)
#         if not user:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
#         await self.repo.delete_user(user)
#         return {"status": "deleted"}
