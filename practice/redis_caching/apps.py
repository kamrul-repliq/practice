from django.apps import AppConfig


class RedisCachingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'redis_caching'
