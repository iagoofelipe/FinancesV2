from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpRequest
import json

from .models import Auth
from ..data.models import User

def token(request:HttpRequest):
    if request.method != 'GET':
        return HttpResponseBadRequest()
    
    return render(request, 'login.html')

def login(request:HttpRequest):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    
    username = request.POST.get('username')
    password = request.POST.get('password')

    if not username or not password:
        return HttpResponse(json.dumps({'success': False, 'error': 'missing data'}))
    
    auth = Auth.objects.filter(username=username, password=password).first()
    if auth is None:
        return HttpResponse(json.dumps({'success': False, 'error': 'invalid credentials'}))

    user = User.objects.filter(auth_id=auth).first()
    return HttpResponse(json.dumps({'success': True, 'error': '', 'userId': user.pk}))

def create_user(request:HttpRequest):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')

    # user = User(first_name=first_name, last_name=last_name)
    # user.save()
