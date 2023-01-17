from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.start),
    path('shop/', views.shop),
    path('cart/', views.cart),
    path('add_cart/<int:id1>/', views.add_cart),
    path('delete_cart/<int:id1>/', views.delete_cart),
    path('shop/<str:category>/', views.products_filter),
    path('shop/sort/cheap/', views.sort_cheapest),
    path('shop/sort/expensive/', views.sort_expensive)
]