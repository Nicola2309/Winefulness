from django.contrib import admin
from .models import Winemakers, Comments


class WinemakersAdmin(admin.ModelAdmin):
    """
    Admin display for winemakers
    """
    list_display = (
        'producer_name',
        'heading',
        'location',
        'content',
        'image',
    )


class CommentsAdmin(admin.ModelAdmin):
    """
    Admin display for comments, inspired
    by https://github.com/Jthomp1993/ms4-premier-league-store/tree/master/cart
    """
    list_display = (
        'winemakers',
        'user',
        'date_time',
        'comment',
    )


admin.site.register(Winemakers, WinemakersAdmin)
admin.site.register(Comments, CommentsAdmin)
