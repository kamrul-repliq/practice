from django.db import models
from uuid import uuid4
from autoslug import AutoSlugField


# Create your models here.


class BaseModel(models.Model):
    """Base model for common fields."""

    uid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(BaseModel):
    """Model for author"""

    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="name")

    def __str__(self):
        return self.name


class Book(BaseModel):
    """Model for author books."""

    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)
    slug = AutoSlugField(populate_from="title")

    def __str__(self):
        return self.title
