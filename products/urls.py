from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_wines, name='products'),
    path('<int:product_id>/', views.wine_details, name="wine_details"),
    path('add/', views.add_products, name='add_products'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
]
