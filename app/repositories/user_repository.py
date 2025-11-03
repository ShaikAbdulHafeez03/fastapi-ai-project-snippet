# from sqlalchemy import select
# from app.models.user import User
# from sqlalchemy.ext.asyncio import AsyncSession

# class UserRepository:
#     def __init__(self, db: AsyncSession):
#         self.db = db

#     async def get_user_by_email(self, email: str):
#         q = await self.db.execute(select(User).where(User.email == email))
#         return q.scalars().first()

#     async def get_user_by_id(self, user_id: int):
#         q = await self.db.execute(select(User).where(User.id == user_id))
#         return q.scalars().first()

#     async def create_user(self, email: str, hashed_password: str):
#         user = User(email=email, hashed_password=hashed_password)
#         self.db.add(user)
#         await self.db.flush()
#         await self.db.commit()
#         await self.db.refresh(user)
#         return user

#     async def update_user(self, user: User, update_data: dict):
#         for k, v in update_data.items():
#             setattr(user, k, v)
#         self.db.add(user)
#         await self.db.commit()
#         await self.db.refresh(user)
#         return user

#     async def delete_user(self, user: User):
#         await self.db.delete(user)
#         await self.db.commit()
#         return True
