from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth', views.authentication, name='authentication'),
    path('token', views.token, name='token'),
]