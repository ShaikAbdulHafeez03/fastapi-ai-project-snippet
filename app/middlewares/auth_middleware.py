import uuid
from contextvars import ContextVar
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
# from fastapi import HTTPException, status
from app.error_handler.custom_exceptions import UnauthorizedException
import jwt
from app.middlewares.request_context import request_ctx_var
from app.schemas.request import RequestContext
from app.config import settings  # JWT_SECRET, JWT_ALGORITHM


class RequestContextJWTMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        rid = str(uuid.uuid4())

        ctx = RequestContext(request_id=rid)

        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            try:
                payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
                ctx.user_id = payload.get("user_id")
                ctx.username = payload.get("username")
                ctx.user_email = payload.get("user_email")
                ctx.client_id = payload.get("client_id")
                ctx.client_name = payload.get("client_name")
            except jwt.ExpiredSignatureError:
                raise UnauthorizedException(detail="Token expired")
            except jwt.InvalidTokenError:
                raise UnauthorizedException(detail="Invalid token")

        request_ctx_var.set(ctx)
        request.state.request_id = rid
        response: Response = await call_next(request)
        response.headers["X-Request-ID"] = rid

        return response
