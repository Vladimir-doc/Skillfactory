from django.apps import AppConfig


class PostboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'postboard'

    def ready(self):
        from . import signals