
from django.urls import path
from products.views import (product_detail, product_list, manufacturer_detail, manufacturer_list)


urlpatterns = [
    path('products/', product_list, name="product_list"),
    path('products/<int:pk>/', product_detail, name="product_detail"),
    path('manufacturers/', manufacturer_list, name="manufacturer_list"),
    path('manufacturers/<int:pk>/', manufacturer_detail, name="manufacturer_detail"),
]