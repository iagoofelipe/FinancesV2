from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
import json

from .models import User

def user(request:HttpRequest):
    if request.method != 'GET':
        return HttpResponseBadRequest()
    
    userId = request.GET.get('userId')
    if userId == None:
        return HttpResponseBadRequest('missing userId')

    user = User.objects.filter(id=userId).first()
    if user is None:
        return HttpResponseBadRequest('undefined id')
    
    return HttpResponse(json.dumps({'first_name': user.first_name, 'last_name': user.last_name}))