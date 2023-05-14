from django.contrib import admin
from elastic.models import ElasticDemo
# Register your models here.

class ElasticDemoAdmin(admin.ModelAdmin):
    list_display = ("id","title",)


admin.site.register(ElasticDemo,ElasticDemoAdmin)

