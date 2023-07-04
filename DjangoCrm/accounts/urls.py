from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('create_order/', views.createOrder, name="create_order"),
    path('update_Order/<str:pk>/', views.updateOrder, name="update_Order"),
    path('delete_Order/<str:pk>/', views.deleteOrder, name="delete_Order"),
]
