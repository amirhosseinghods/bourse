import os

from celery import Celery
from celery.schedules import crontab
 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kernel.settings.development')

app = Celery()
app.config_from_object('django.conf:settings') # The Celery uses configuration of kernel settings
 
app.autodiscover_tasks() # The Celery discovers tasks from apps

# Load task modules from all registered Django app configs. 
app.conf.beat_schedule = {
    'send-report-every- 12AM': {
        'task': 'shop.tasks.send_alert_email',
        'schedule': crontab(minute = 0, hour = 0),   # Execute daily at midnight.
    },
}