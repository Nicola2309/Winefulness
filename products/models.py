from django.db import models
from django.db.models import Avg

# Create your models here.


class Category(models.Model):
    """
    Category model
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, default='', blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Products Form Fields
    """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, default='',
                           blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image_url = models.URLField(max_length=1024, default='',
                                blank=True)
    image = models.ImageField(default='', blank=True)

    def calculate_rating(self):
        """
        Calculate rating from reviews, as understood in the code of my \
        fellow student Gregory Lewis project \
        'https://github.com/Gregory4321/cooks_finest'
        """
        self.rating = self.reviews.aggregate(Avg("review_rating"))[
            'review_rating__avg']
        self.save()

    def __str__(self):
        return self.name
