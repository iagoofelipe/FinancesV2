from django.shortcuts import render
from django.http import HttpRequest, HttpResponseBadRequest, HttpResponse

def index(request):
    return HttpResponse('Home')