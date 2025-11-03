import jwt
from app.schemas.token import Token
import app.core.handle_jwt as handle_jwt
from datetime import datetime, timedelta, timezone
from app.config import settings
from app.error_handler.custom_exceptions import UnauthorizedException


JWT_SECRET = settings.JWT_SECRET
JWT_ALGORITHM = settings.JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * settings.ACCESS_TOKEN_EXPIRE_MINUTES

# Valid clients
VALID_CLIENTS = {
    "3fa85f64-5717-4562-b3fc-2c963f66afa6": "test_api_key_123"
}

def create_client_jwt(token: Token) -> str:
    if VALID_CLIENTS.get(str(token.client_id)) != str(token.client_key):
        raise UnauthorizedException("Invalid client credentials")  
    now = datetime.now(timezone.utc)
    payload = {
        "user_id": str(token.user_id),
        "username": token.username,
        "user_email": token.user_email,
        "client_id": str(token.client_id),
        "client_name": token.client_name,
        "created_at": now.isoformat(),
        "exp": now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    print(payload)
    jwt_token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return jwt_token


