from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpRequest
import json

from .models import User

def index(request:HttpRequest):

    match request.method:
        case 'GET':
            return render(request, 'login.html')
        case 'POST':
            pass
        case _:
            return HttpResponseBadRequest()

    username = request.POST.get('username')
    password = request.POST.get('password')

    if not username or not password:
        return HttpResponse(json.dumps({'success': False, 'error': 'missing data'}))
    
    if username != 'iago' or password != '1234':
        return HttpResponse(json.dumps({'success': False, 'error': 'invalid credentials'}))

    return HttpResponse(json.dumps({'success': True, 'error': ''}))

def create_user(request:HttpRequest):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')

    user = User(first_name=first_name, last_name=last_name)
    user.save()