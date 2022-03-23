import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'checkmate.settings')

app = Celery('checkmate')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.conf.beat_schedule = {
    "hikHddStatus": {
        'task': 'infrastructure.tasks.hikHddStatus',
        'schedule': crontab(minute="*/2")
    },
    "vighZoneStatus": {
        'task': 'infrastructure.tasks.vighZoneStatus',
        'schedule': crontab(minute="*/20")
    },
    "HikNvrAlert": {
        'task': 'surveillance.tasks.fetch_post_data',
        'schedule': crontab(minute="*/2")
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
