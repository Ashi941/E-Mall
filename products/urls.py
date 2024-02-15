from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('category-list',CategoryListCreateView.as_view(),name ="category_list"),
    path('category-details/<int:pk>',  CategoryDetailsAPIView.as_view(), name="category-details"),
    path('product-list',ProductListCreateView.as_view(),name ="product_list"),
    path('product-details/<int:pk>',ProductDetailsAPIView.as_view(), name="product-details"),
]