from django.db import models
from hashlib import md5


# Create your models here.
class UrlEntry(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    full_url = models.URLField(unique=True)
    url_hash = models.TextField(unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_hash = md5(self.full_url.encode()).hexdigest()[:5]

        return super().save(*args, **kwargs)