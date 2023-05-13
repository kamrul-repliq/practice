from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "practice.settings")

app = Celery("practice")

app.conf.enable_utc = False

app.conf.update(timezone="Asia/Dhaka")

app.config_from_object(settings, namespace="CELERY")

# CELERY beat settings
app.conf.beat_schedule = {
    "send_mail-every-day-at-8": {
        "task": "send_email.tasks.send_email_func",
        "schedule": crontab(hour=00, minute=21),
        # "schedule": crontab(hour=00, minute=21,days_of_month=19,month_of_year=6),
        # "args": (1,),
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request {self.request}")
