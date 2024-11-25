from django.urls import path, include

urlpatterns = [
    path('auth/', include('apps.api.views.auth')),
    path('reg/', include('apps.api.views.reg')),
]