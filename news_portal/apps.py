from django.apps import AppConfig
import redis


class NewsPortalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news_portal'

    def ready(self):
        import news_portal.signals





