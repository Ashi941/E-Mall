from django.urls import path
from .views import *


urlpatterns = [
    path('',  index, name="index"),
    path('orders-list',OrdersListCreateView.as_view(),name ="orders_list"),
    path('orders-details/<int:pk>',OrdersDetailsAPIView.as_view(), name="orders-details"),
    path('order-details/<str:uuid>/', OrdersDetailsAPIView.as_view(), name="order-details"),
    path('change-status/<str:uuid>/', ChangeOrderStatusView.as_view(), name="change-status"),


]
