"""URLS mapping for elastic Search."""

from django.urls import path

from elastic import views

urlpatterns = [
    path("/get-news",views.news_data,name='get-news'),
    path("/news",views.PublisherDocument.as_view({'get':'list'}),name='news'),
]