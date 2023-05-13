from django.urls import path
from demo import views

app_name = "demo"

urlpatterns = [
    path("authors/", views.AuthorList.as_view(), name="authors"),
    path("authors/<slug:slug>/", views.AuthorDetail.as_view(), name="author-details"),
    path("books/", views.BookList.as_view(), name="books"),
    path("books/<slug:slug>/", views.BookDetail.as_view(), name="book-details"),
    path("albums/", views.AlbumList.as_view(), name="albums"),
    path("albums/<uid>/", views.AlbumDetail.as_view(), name="album-details"),
    path("albums/<uid>/tracks/", views.TrackList.as_view(), name="tracks"),
    path("profile", views.ProfileList.as_view(), name="profile"),
    path("profile/<uuid:uid>/", views.ProfileDetail.as_view(), name="profile-detail"),
]
