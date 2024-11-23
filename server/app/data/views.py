from django.shortcuts import render
from django import http
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json

# from .models import User
from . import models

# def user(request:http.HttpRequest):
#     if request.method != 'GET':
#         return http.HttpResponseBadRequest()
    
#     user = request.user
#     if not user.is_authenticated:
#         return http.HttpResponse(status=401)
    
#     user = User.objects.get(username=user.get_username())
#     data = {
#         'first_name': user.first_name,
#         'last_name': user.last_name,
#     }

#     return http.HttpResponse(json.dumps(data), content_type='application/json')

def session(request:http.HttpRequest):
    if request.method != 'GET':
        return http.HttpResponseBadRequest()
    
    user = request.user
    if not user.is_authenticated:
        return http.HttpResponse(status=401)
    
    user = User.objects.get(username=user.get_username())
    rule = models.UserProfileRules.objects.filter(user=user).first()
    
    if rule is None: # criando perfil caso nenhum exista
        rule = models.UserProfileRules.objects.create(user=user, profile=models.Profile.objects.create())

    data = {
        'name': f'{user.first_name} {user.last_name}',
        'profileId': rule.profile.pk,
        'profileName': rule.profile.name,
    }

    return http.HttpResponse(json.dumps(data), content_type='application/json')

def newRegistry(request:http.HttpRequest): ...
def queryRegistry(request:http.HttpRequest): ...
def queryRegistries(request:http.HttpRequest): ...