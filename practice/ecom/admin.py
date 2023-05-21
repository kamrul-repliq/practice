from django.contrib import admin
from ecom.models import Organization, Product, Stock


# Register your models here.
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "status")


class StockAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "stock", "status")


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Stock, StockAdmin)
