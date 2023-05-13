"""Urls Mappings for celery_learn app"""

from django.urls import path
from celery_learn import views

urlpatterns = [path("", views.test, name="test")]
