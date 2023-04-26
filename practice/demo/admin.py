from django.contrib import admin
from demo.models import Author, Book


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["uid", "slug", "name"]


class BookAdmin(admin.ModelAdmin):
    list_display = ["uid", "title", "author", "slug", "published_date"]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
