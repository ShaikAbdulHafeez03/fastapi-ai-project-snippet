from pydantic import BaseModel, EmailStr
from uuid import UUID

class Token(BaseModel):
    client_id: UUID
    client_name: str
    client_key: str
    user_id: UUID
    username: str
    user_email: EmailStr
