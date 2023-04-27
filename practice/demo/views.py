"""Views for Demo App."""
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from demo.models import Author, Book, Album, Track
from demo.serializers import (
    AlbumSerializer,
    AuthorSerializer,
    BookSerializer,
    TrackSerializer,
)


class AuthorList(APIView):
    """List create API view for Author."""

    serializer_class = AuthorSerializer

    def get(self, request, format=None):
        authors = Author.objects.filter()
        serializer = self.serializer_class(authors, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetail(APIView):
    """Author retrieve Update destroy API VIEW."""

    serializer_class = AuthorSerializer

    def _get_object(self, slug):
        return get_object_or_404(Author, slug=slug)

    def get(self, request, slug, format=None):
        author = self._get_object(slug=slug)
        serializer = self.serializer_class(author)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, slug, format=None):
        author = self._get_object(slug=slug)
        serializer = self.serializer_class(author, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, slug, format=None):
        author = self._get_object(slug=slug)
        serializer = self.serializer_class(author, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        author = self._get_object(slug)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookList(ListCreateAPIView):
    """Book List create api view."""

    queryset = Book.objects.filter()
    serializer_class = BookSerializer


class BookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.filter()
    serializer_class = BookSerializer
    lookup_field = "slug"


class AlbumList(ListCreateAPIView):
    queryset = Album.objects.filter()
    serializer_class = AlbumSerializer


class AlbumDetail(RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.filter()
    serializer_class = AlbumSerializer
    lookup_field = "uid"


class TrackList(ListCreateAPIView):
    queryset = Track.objects.filter()
    serializer_class = TrackSerializer
    lookup_field = "uid"

    def get_queryset(self):
        uid = self.kwargs.get("uid")
        return Track.objects.filter(album__uid=uid)


class TrackDetail(RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.filter()
    serializer_class = TrackSerializer
    lookup_field = "uid"
