# celery.py
import os
from celery import Celery, shared_task

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'snoop.celery_co')

app = Celery('snoop')

# Configure Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load tasks from all registered apps
app.autodiscover_tasks()