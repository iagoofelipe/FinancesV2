from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dash', views.dash, name='dash'),
    path('reg', views.reg, name='reg'),
    path('card', views.card, name='card'),
    path('settings', views.settings, name='settings'),
]