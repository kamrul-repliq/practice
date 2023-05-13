from django.shortcuts import render
from django.http import HttpResponse
from django_celery_beat.models import PeriodicTask, CrontabSchedule

import json

# Create your views here.
from send_email.tasks import send_email_func


def send_email_to_all(request):
    send_email_func.delay()
    return HttpResponse("Send email to all task Started.")


def send_mail_particular_time(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=1, minute=34)
    task = PeriodicTask.objects.create(
        crontab=schedule,
        name="schedule_mail_task_" + "5",
        task="send_email.tasks.send_mail_func",
    )  # , args = json.dumps([[2,3]]))
    return HttpResponse("Done")
