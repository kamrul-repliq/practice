"""URL mappings for ecom app"""

from django.urls import path

from ecom import views

app_name = "ecom"

urlpatterns = [
    path("", views.home, name="home"),
    path("/products", views.ProductList.as_view(), name="products"),
]
