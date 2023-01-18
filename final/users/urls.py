from django.urls import path, re_path, include
from users.views import Register
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.start),
    path('account/', views.account_menu),
    path('register/', Register.as_view(), name='register')

]


