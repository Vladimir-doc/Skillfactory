from django.apps import AppConfig
import redis


red = redis.Redis(
    host='redis-18119.c135.eu-central-1-1.ec2.cloud.redislabs.com',
    port=18119,
    password='UIieGNkXAz1if9z69I0dB60Sz6DEkG4u'
)


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):
        from . import signals