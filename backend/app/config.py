from celery import Celery
import os

REDIS_URL = os.getenv("REDIS_URL")

celery_app = Celery(
    "api_testing_platform",
    broker=REDIS_URL,
    backend=REDIS_URL
)
