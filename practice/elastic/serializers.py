"""Serializer for ElasticDemo."""
from elastic.models import ElasticDemo
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import NewsDocument


class NewsDocumentSerailizer(DocumentSerializer):
    class Meta:
        model = ElasticDemo
        document = NewsDocument

        fields = ("title","content")

        def get_location(self, obj):
            try:
                return obj.location.to_dict()
            except:
                return {}