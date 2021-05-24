from django.urls import path
from . import views

urlpatterns = [
    path("", views.store, name="store"),
    path("localstore/", views.localstore, name="store"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("cart/", views.cart, name="cart"),
    path("checkout", views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]
