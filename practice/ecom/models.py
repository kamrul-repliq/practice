from django.db import models

# Create your models here.


class Status(models.TextChoices):
    ACTIVE = "ACTIVE", "Active"
    INACTIVE = "INACTIVE", "Inactive"


class Organization(models.Model):
    """Default model for organization."""

    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    price = models.IntegerField()
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.ACTIVE
    )

    def __str__(self):
        return f"{self.name}"


class Stock(models.Model):
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="products"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="stock_list"
    )
    stock = models.IntegerField(default=0)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.ACTIVE
    )

    def __str__(self):
        return f"{self.stock}"
