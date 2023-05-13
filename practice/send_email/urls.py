"""URL mapping for email sender"""
from django.urls import path
from send_email import views


app_name = "email_sender"

urlpatterns = [path("/mail-send", views.send_email_to_all, name="mail-send")]
