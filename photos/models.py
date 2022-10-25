from django.db import models


class Photo(models.Model):
    album_id = models.PositiveIntegerField()
    title = models.CharField(max_length=256)
    url = models.URLField()
    thumbnail_url = models.URLField(default=True, blank=True)
