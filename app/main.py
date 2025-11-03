import time
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import redis.asyncio as redis
from app.config import settings
# from app.core.logging_config import get_logger, request_id_ctx_var, user_id_ctx_var
from app.core.rate_limiter import init_rate_limiter
from app.error_handler.custom_exceptions import RateLimitExceededException
from app.middlewares.auth_middleware import  RequestContextJWTMiddleware
# from app.core.metrics import record_request, metrics_endpoint
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from app.routes.v1 import users as user_route
from app.routes.v1 import token as auth_routes
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
# from slowapi.errors import RateLimitExceeded
# from celery.result import AsyncResult
# from app.tasks.celery_app import long_running_task
from app.config import settings

# logger = get_logger("fastapi-app", loki_url=settings.LOKI_URL)

app = FastAPI(title=settings.PROJECT_NAME)

REDIS_URL =  settings.REDIS_URL
app.add_middleware(RequestContextJWTMiddleware)
app.add_middleware(SlowAPIMiddleware) 

init_rate_limiter(app)


# Routes
app.include_router(user_route.router)
app.include_router(auth_routes.router)


# Metrics endpoint
# app.add_route(settings.PROMETHEUS_METRICS_PATH, metrics_endpoint, methods=["GET"])

# def get_user_id_from_request(request: Request):
#     """
#     Returns request.state.user_id if available,
#     otherwise falls back to IP address.
#     """
#     user_id = getattr(request.state, "user_id", None)
#     if user_id:
#         return str(user_id)
#     return None

# tracing middleware for metrics and logging
@app.middleware("http")
async def metrics_and_logging(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    latency = time.time() - start
    print(f"start {start} latency {latency}")
    # print(latency)
    # endpoint = request.url.path
    # record_request(request.method, endpoint, response.status_code, latency)

    # rid = request_id_ctx_var.get()
    # uid = user_id_ctx_var.get()
    # put request_id and user_id into log record via extra if needed
    # logger.info("request_finished", extra={"request_id": rid, "user_id": uid, "path": endpoint, "status": response.status_code, "latency": latency})
    # response.headers["X-Request-ID"] = rid
    return response


# # Celery endpoints
# @app.post("/v1/tasks/submit")
# async def submit_task(payload: dict):
#     task = long_running_task.apply_async((payload,))
#     return {"task_id": task.id}

# @app.get("/v1/tasks/{task_id}")
# async def get_task_status(task_id: str):
#     res = AsyncResult(task_id, app=long_running_task._get_app())
#     return {"task_id": task_id, "state": res.state, "result": res.result}
