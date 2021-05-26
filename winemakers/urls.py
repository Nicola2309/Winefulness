from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_winemakers, name='winemakers'),
    path('<int:winemaker_id>',
         views.winemaker_detail, name='winemaker_detail'),
    path('add_winemaker/', views.add_winemakers, name='add_winemakers'),
    path('edit_winemaker/<int:winemaker_id>/',
         views.edit_winemaker, name='edit_winemaker'),
    path('delete_winemaker/<int:winemaker_id>/',
         views.delete_winemaker, name='delete_winemaker'),
    path('add_comment/<int:winemaker_id>/',
         views.add_comment, name='add_comment'),
    path('delete_comment/<int:winemaker_id>/<int:comment_id>/',
         views.delete_comment, name='delete_comment'),
    path('edit_comment/<int:winemaker_id>/<int:comment_id>/',
         views.edit_comment, name='edit_comment'),
]
