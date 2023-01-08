from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog),
    path('order-custom', views.custom),
    path('cart', views.cart)
]