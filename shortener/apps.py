import os
import threading
import time
import logging

from django.apps import AppConfig

logger = logging.getLogger(__name__)
_cleanup_started = False


def _run_cleanup():
    from django.utils import timezone
    from datetime import timedelta
    from .models import ShortURL
    cutoff = timezone.now() - timedelta(days=30)
    d1, _ = ShortURL.objects.filter(last_accessed__lt=cutoff).delete()
    d2, _ = ShortURL.objects.filter(last_accessed__isnull=True, created_at__lt=cutoff).delete()
    if d1 + d2:
        logger.info(f"[shortener] deleted {d1 + d2} expired URLs")


def _cleanup_loop():
    time.sleep(600)
    while True:
        try:
            _run_cleanup()
        except Exception as e:
            logger.exception(f"[shortener] cleanup error: {e}")
        time.sleep(3600)


class ShortenerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "shortener"
    verbose_name = "AnotherURLShortener"

    def ready(self):
        global _cleanup_started
        if _cleanup_started or os.environ.get("RUN_MAIN") == "true":
            return
        _cleanup_started = True
        threading.Thread(target=_cleanup_loop, daemon=True).start()
