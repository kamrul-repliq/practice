"""Serializers for our models."""
from django.urls import reverse
from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from demo.models import Author, Book, Album, Track, Profile


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


class AlbumSerializer(serializers.ModelSerializer):
    """Album Serializer."""

    tracks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Album
        fields = ["uid", "album_name", "artist", "tracks"]


class TrackSerializer(serializers.ModelSerializer):
    """Serializer for tracks."""

    class Meta:
        model = Track
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for Profile"""

    image = VersatileImageFieldSerializer(
        sizes=[
            ("original", "url"),
            ("at300x300", "crop__300x300"),
            ("at500x500", "crop__500x500"),
        ],
        required=False,
    )

    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        request = self.context.get("request")
        if request is not None:
            return request.build_absolute_uri(
                reverse("demo:profile-detail", args=[obj.uid])
            )
        return reverse("demo:profile-detail", args=[obj.uid])

    class Meta:
        model = Profile
        fields = ("uid", "name", "image", "url")
