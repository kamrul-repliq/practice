"""URL mappings for redis caching."""

from django.urls import path
from redis_caching import views
urlpatterns = [
    path('',views.all_fruits,name='fruits'),
]

