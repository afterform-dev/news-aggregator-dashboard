import os

from celery import Celery

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(
    "news_aggregator",
    broker=REDIS_URL,
    backend=REDIS_URL,
    include=["tasks.news_aggregator"],
)

celery_app.conf.update(
    timezone="Europe/Moscow",
    enable_utc=True,
)
