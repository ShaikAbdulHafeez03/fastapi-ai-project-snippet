from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID

class RequestContext(BaseModel):
    request_id: UUID        
    client_id: Optional[UUID] = None
    client_name: Optional[str] = None
    user_id: Optional[UUID] = None
    username: Optional[str] = None
    user_email: Optional[EmailStr] = None
