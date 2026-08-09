from django.db import models
from django.utils import timezone


class ShortURL(models.Model):
    code = models.CharField(max_length=12, unique=True, db_index=True)
    original_url = models.URLField(max_length=2048)
    created_at = models.DateTimeField(auto_now_add=True)
    last_accessed = models.DateTimeField(null=True, blank=True, db_index=True)
    access_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.code} → {self.original_url[:60]}"

    def record_access(self):
        self.access_count += 1
        self.last_accessed = timezone.now()
        self.save(update_fields=["access_count", "last_accessed"])
