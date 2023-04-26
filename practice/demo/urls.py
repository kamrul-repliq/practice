from django.urls import path
from demo import views

urlpatterns = [
    path("authors/", views.AuthorList.as_view(), name="authors"),
    path("authors/<slug:slug>/", views.AuthorDetail.as_view(), name="author-details"),
    path("books/", views.BookList.as_view(), name="books"),
    path("books/<slug:slug>/", views.BookDetail.as_view(), name="book-details"),
]
