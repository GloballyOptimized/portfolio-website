from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from shortener.models import ShortURL
from shortener.redis_client import cache_delete


class Command(BaseCommand):
    help = "Delete short URLs not accessed in the last N days (default 30)"

    def add_arguments(self, parser):
        parser.add_argument("--days", type=int, default=30)
        parser.add_argument("--dry-run", action="store_true")

    def handle(self, *args, **options):
        days = options["days"]
        dry = options["dry_run"]
        cutoff = timezone.now() - timedelta(days=days)
        qs1 = ShortURL.objects.filter(last_accessed__lt=cutoff)
        qs2 = ShortURL.objects.filter(last_accessed__isnull=True, created_at__lt=cutoff)
        total = qs1.count() + qs2.count()
        self.stdout.write(f"Found {total} URLs expired (>{days} days without access)")
        if dry:
            self.stdout.write("Dry run — nothing deleted.")
            return
        for obj in list(qs1) + list(qs2):
            cache_delete(obj.code)
        d1, _ = qs1.delete()
        d2, _ = qs2.delete()
        self.stdout.write(self.style.SUCCESS(f"Deleted {d1 + d2} expired URLs"))
