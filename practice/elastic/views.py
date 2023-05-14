from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
from elastic.models import ElasticDemo
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend,
    # CompoundFilterBackend,
)

from elastic.documents import NewsDocument
from elastic.serializers import NewsDocumentSerailizer
# Create your views here.

def generate_random_data():
    url = "https://jsonplaceholder.typicode.com/posts/"
    response = requests.get(url)
    data = json.loads(response.text)
    count= 0
    for item in data:
        ElasticDemo.objects.create(
            title=item['title'],
            content=item['body'],
        )
        count+=1
    print(count,'data has been added!')


def news_data(request):
    generate_random_data()
    return JsonResponse("Fetched",safe=False)


class PublisherDocument(DocumentViewSet):
    document = NewsDocument
    serializer_class = NewsDocumentSerailizer

    filter_backends = [
        FilteringFilterBackend,
        CompoundSearchFilterBackend,
    ]

    search_fields = ("title", "content")
    multi_match_search_fields = ("title","content")
    filter_fields = {
        "title": "title",
        "content": "content",
    }