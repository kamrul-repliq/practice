
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render

from redis_caching.models import Fruits


def all_fruits(request):
    payload = []
    if cache.get('fruits'):
        payload = cache.get("fruits")
        print("Data from cache")
        print(cache.ttl("fruits"))
    else:
        data = Fruits.objects.filter()
        print("Data from DB")
        for fruit in data:
            payload.append(fruit.name)
        
        cache.set('fruits',payload,timeout=10)

    return JsonResponse({'status':200,'db':'sqlite','data':payload})