# from contextvars import ContextVar
# import uuid
# from starlette.middleware.base import BaseHTTPMiddleware
# from starlette.requests import Request

# from app.schemas.request import RequestContext

# request_ctx_var: ContextVar[RequestContext] = ContextVar("request_ctx")

# class RequestContextMiddleware(BaseHTTPMiddleware):
#     async def dispatch(self, request: Request, call_next):
#         rid = uuid.uuid4()
#         ctx = RequestContext(request_id=str(rid))
#         request_ctx_var.set(ctx)
#         request.state.request_id = rid
#         response = await call_next(request)
#         response.headers['X-Request-ID'] = rid
#         return response
# app/middlewares/request_context.py
from contextvars import ContextVar
from app.schemas.request import RequestContext

request_ctx_var: ContextVar[RequestContext] = ContextVar("request_ctx")
