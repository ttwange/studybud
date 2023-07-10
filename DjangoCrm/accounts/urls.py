from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('',views.home, name="home"),
    path('user/', views.userPage, name="user-page"),
    path('account/', views.accountSettings,name="account"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_Order/<str:pk>/', views.updateOrder, name="update_Order"),
    path('delete_Order/<str:pk>/', views.deleteOrder, name="delete_Order"),

    path('reset_password/', auth_views.PasswordResetView.as_view()),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view()),
    path('reset_password/', auth_views.PasswordResetConfirmView.as_view()),
    path('reset_password/', auth_views.PasswordResetView.as_view()),
]
