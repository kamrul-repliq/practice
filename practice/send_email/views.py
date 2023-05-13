from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from send_email.tasks import send_email_func


def send_email_to_all(request):
    send_email_func.delay()
    return HttpResponse("Send email to all task Started.")
