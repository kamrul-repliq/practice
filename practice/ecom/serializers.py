"""Serializers for ECOM app."""
from ecom.models import Organization, Product, Stock, Status

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"


class StockSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"


class ActiveStockIdField(serializers.Field):
    def to_representation(self, value):
        return [stock.id for stock in value.active_stock_list]


class ProductSerializer(ModelSerializer):
    # stocks = StockSerializer(many=True, source="*")
    # stocks = StockSerializer(source="stock_list", many=True)
    # stock_ids = serializers.ListSerializer(
    #     child=serializers.IntegerField(), source="active_stock_list"
    # )
    # stock_ids = serializers.ListField(
    #     child=serializers.IntegerField(), source="active_stock_list"
    # )
    stock_ids = ActiveStockIdField(source="*")
    # stock_ids = serializers.IntegerField(
    #     read_only=True,
    #     source="stock_ids_ac",
    # )

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "status",
            "price",
            "organization",
            # "stocks",
            "stock_ids",
        ]

    def create(self, validated_data):
        print("Product attributes:", validated_data)
        return super().create(validated_data)

    # def to_representation(self, value):
    #     print("VVVVVVVVVVVVVVV", dir(value.stock_list.filter(status=Status.ACTIVE)))
    #     # return [stock.id for stock in value.active_stock_list_ids]
