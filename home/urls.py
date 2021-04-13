from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<product_id>', views.wine_details, name='wine_details'),
]
