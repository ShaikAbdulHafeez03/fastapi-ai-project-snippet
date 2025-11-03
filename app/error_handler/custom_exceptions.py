from fastapi import HTTPException, status
from app.middlewares.request_context import request_ctx_var

class AppBaseException(HTTPException):
    def __init__(self, detail: str, status_code: int = status.HTTP_400_BAD_REQUEST, code: str = None):
        self.code = code or "error"
        # Include request_id in the detail
        ctx = request_ctx_var.get()
        request_id = ctx.request_id
        super().__init__(
            status_code=status_code,
            detail={
                "code": self.code,
                "message": detail,
                "request_id": str(request_id)
            }
        )

class UnauthorizedException(AppBaseException):
    def __init__(self, detail: str = "Unauthorized"):
        super().__init__(detail=detail, status_code=status.HTTP_401_UNAUTHORIZED, code="unauthorized")

class NotFoundException(AppBaseException):
    def __init__(self, detail: str = "Resource not found"):
        super().__init__(detail=detail, status_code=status.HTTP_404_NOT_FOUND, code="not_found")

class BadRequestException(AppBaseException):
    def __init__(self, detail: str = "Bad request"):
        super().__init__(detail=detail, status_code=status.HTTP_400_BAD_REQUEST, code="bad_request")

class RateLimitExceededException(AppBaseException):
    def __init__(self, detail: str = "Rate Limit exceeded"):
        super().__init__(detail=detail, status_code=status.HTTP_429_TOO_MANY_REQUESTS, code="too_many_requests")        
