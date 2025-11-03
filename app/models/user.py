from sqlalchemy import Column, Integer, String, Boolean, Enum
from app.db import Base,engine
import enum

ROLE_LIST = ["admin", "client_admin", "employee", "guest"]

UserRole = enum.Enum("UserRole", {role: role for role in ROLE_LIST})

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    is_allowed = Column(Boolean, default=True)
    role = Column(Enum(UserRole), default=UserRole.guest, nullable=False)

Base.metadata.create_all(bind=engine)