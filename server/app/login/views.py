from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpRequest
import json

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

    return HttpResponse(json.dumps({'username': username, 'password': password}))
    