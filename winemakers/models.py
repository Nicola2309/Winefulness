from django.db import models


class Winemakers(models.Model):
    class Meta:
        verbose_name_plural = 'Winemakers'

    title = models.CharField(max_length=120)
    heading = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(max_length=254, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    image_url = models.URLField(
        max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
