from datetime import datetime

from celery_app import celery_app


@celery_app.task
def fetch_latest_news():
    return {
        "status": "skipped",
        "message": "News aggregation will be added in future iterations.",
        "timestamp": datetime.utcnow().isoformat(),
    }
