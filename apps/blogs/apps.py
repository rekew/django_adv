from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'apps.blogs'

    def ready(self):
        import apps.blogs.signals  # noqa