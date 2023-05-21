from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Prefetch, Case, When, F, Value, IntegerField

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import OrganizationSerializer, ProductSerializer, StockSerializer
from .models import Organization, Product, Stock, Status

# Create your views here.


def home(request):
    # product = (
    #     Product.objects.filter(status=Status.ACTIVE, organization_id=1)
    #     .only("id", "name", "organization_id", "price")
    #     .prefetch_related("stock_list")
    #     .prefetch_related("stock_list__status")
    #     .filter(stock_list__status=Status.ACTIVE)
    # )
    product = (
        Product.objects.filter(status=Status.ACTIVE, organization_id=1)
        .only("id", "name", "organization_id", "price")
        .prefetch_related(
            Prefetch(
                "stock_list",
                queryset=Stock.objects.filter(status=Status.ACTIVE, organization_id=1),
                to_attr="active_stock_list",
            )
        )
    )
    print(product)
    # for prod in product:
    #     print(prod.active_stock_list)
    # return HttpResponse(f"Hello")
    # return None


class ProductList(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = (
        Product.objects.filter(status=Status.ACTIVE, organization_id=1)
        .only("id", "name", "organization_id", "price")
        .prefetch_related(
            Prefetch(
                "stock_list",
                queryset=Stock.objects.filter(status=Status.ACTIVE, organization_id=1),
                to_attr="active_stock_list",
            )
        )
        # .annotate(
        #     stock_ids_ac=Case(
        #         When(stock_list__status=Status.ACTIVE, then="stock_list__id"),
        #         default=Value(None),
        #         output_field=IntegerField(),
        #     )
        # )
    )

    # queryset = Product.objects.filter(
    #     status=Status.ACTIVE, organization_id=1
    # ).prefetch_related("stock_list")
