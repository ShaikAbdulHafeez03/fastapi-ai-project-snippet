from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "fastapi-ai-backend"
    DEBUG: bool = False

    DATABASE_URL: str  # postgresql+asyncpg://user:pass@host/db
    REDIS_URL: str = "redis://redis:6379/0"

    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

    # LOKI_URL: str = None

    # CELERY_BROKER_URL: str = None
    # CELERY_RESULT_BACKEND: str = None

    PROMETHEUS_METRICS_PATH: str = "/metrics"

    model_config = {
        "env_file": ".env",
        "extra": "allow"  # allow extra environment variables
    }
settings = Settings()
