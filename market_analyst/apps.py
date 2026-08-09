from django.apps import AppConfig


class MarketAnalystConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "market_analyst"
    verbose_name = "Market Analyst"

    def ready(self):
        from .core.database import init_db
        init_db()
