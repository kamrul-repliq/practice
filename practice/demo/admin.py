from django.contrib import admin
from demo.models import Author, Book, Album, Track, Profile


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["uid", "slug", "name"]


class BookAdmin(admin.ModelAdmin):
    list_display = ["uid", "title", "author", "slug", "published_date"]


class AlbumAdmin(admin.ModelAdmin):
    list_display = ["uid", "album_name", "artist"]


class TrackAdmin(admin.ModelAdmin):
    list_display = ["uid", "order", "title", "duration"]


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("uid", "name", "image", "width", "height")


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Profile, ProfileAdmin)
