from django.contrib import admin
from .models import Winemakers, Comments


class WinemakersAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'heading',
        'description',
        'content',
        'image',
    )


class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        'winemakers',
        'user',
        'date_time',
        'comment',
    )


admin.site.register(Winemakers, WinemakersAdmin)
admin.site.register(Comments, CommentsAdmin)
