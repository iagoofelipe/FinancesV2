from django.urls import path
from . import views

urlpatterns = [
    path('auth', views.authentication, name='authentication'),
    path('token', views.token, name='token'),
    path('logout', views.logout, name='logout'),
]