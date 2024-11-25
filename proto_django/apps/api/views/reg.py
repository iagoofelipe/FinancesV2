from django.urls import path
from django.http import HttpRequest, HttpResponse

def new_registry(request:HttpRequest):
    return HttpResponse('teste')

urlpatterns = [
    path('new', new_registry, name='new'),
]