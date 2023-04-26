"""Serializers for our models."""

from rest_framework import serializers
from demo.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for author model."""

    class Meta:
        model = Author
        fields = ["name", "slug"]


class BookSerializer(serializers.ModelSerializer):
    """Serializer for Book models."""

    author = serializers.SlugRelatedField(
        queryset=Author.objects.all(), slug_field="slug"
    )

    class Meta:
        model = Book
        fields = ["title", "author", "slug", "published_date"]
