from django.db import models
from profiles.models import User


class Winemakers(models.Model):
    class Meta:
        verbose_name_plural = 'Winemakers'

    producer_name = models.CharField(max_length=120)
    heading = models.CharField(max_length=150, null=False, blank=False)
    location = models.TextField(max_length=254, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    image_url = models.URLField(
        max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.producer_name


class Comments(models.Model):
    winemakers = models.ForeignKey(
        'Winemakers', null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, blank=True, default='Anonymous')
    comment = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True,)

    class Meta:
        verbose_name_plural = 'Comments'
        ordering = ['-date_time']

    def __str__(self):
        return self.comment
