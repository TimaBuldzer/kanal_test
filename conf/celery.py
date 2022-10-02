import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")

app = Celery("conf")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "apps_orders_tasks_create_orders": {
        "task": "apps.orders.tasks.create_orders",
        "schedule": crontab(minute="*/5"),
    },

}
