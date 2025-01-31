from django.db import models

# Create your models here.


class CrawledPage(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
