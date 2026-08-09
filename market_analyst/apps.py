from django.apps import AppConfig


class MarketAnalystConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "market_analyst"
    verbose_name = "Market Analyst"

    def ready(self):
        import logging
        try:
            from .core.database import init_db
            init_db()
        except Exception as e:
            logging.getLogger(__name__).warning(
                "[market_analyst] DB init skipped at startup: %s", e
            )
