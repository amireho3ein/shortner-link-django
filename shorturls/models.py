from django.db import models

class URL(models.Model):
    long_url = models.URLField(unique=True)
    short_code = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_code