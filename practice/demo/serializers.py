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

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation["author"] = {"name": representation["author"]}
    #     return representation

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["author"] = {"Author Name": representation["author"]}
        return representation
