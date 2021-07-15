from django.apps import AppConfig


class UsageConfig(AppConfig):
    name = 'usage'

    def ready(self):
        from usage import signals