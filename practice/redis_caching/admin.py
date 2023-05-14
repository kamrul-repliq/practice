from django.contrib import admin
from redis_caching.models import Fruits
# Register your models here.

class FruitAdmin(admin.ModelAdmin):
    list_display = ("id","name","description","kind")

admin.site.register(Fruits,FruitAdmin)
