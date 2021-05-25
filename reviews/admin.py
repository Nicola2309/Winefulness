from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """
    Admin display for reviews
    """
    list_display = (
        'product',
        'review_title',
        'created_on',
        'user_profile',
    )
    list_filter = ("product",)
    search_fields = ['product', 'review_title', 'review_content']


admin.site.register(Review, ReviewAdmin)
