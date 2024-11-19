from django.shortcuts import render
from django import http
from django.contrib import auth
from django.contrib.auth.models import User
from ..data.models import Profile, UserProfileRules

def token(request:http.HttpRequest):
    if request.method != 'GET':
        return http.HttpResponseBadRequest()
    
    return render(request, 'login.html')

def login(request:http.HttpRequest):
    if request.method != 'POST':
        return http.HttpResponseBadRequest()
    
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(request, username=username, password=password)

    if user is None:
        return http.HttpResponse('{"message": "invalid credentials"}', content_type='application/json', status=400)
    
    auth.login(request, user)
    return http.HttpResponse()

    # if not username or not password:
    #     return http.HttpResponse(json.dumps({'success': False, 'error': 'missing data'}))
    
    # auth = Auth.objects.filter(username=username, password=password).first()
    # if auth is None:
    #     return http.HttpResponse(json.dumps({'success': False, 'error': 'invalid credentials'}))

    # user = User.objects.filter(auth_id=auth).first()
    # return http.HttpResponse(json.dumps({'success': True, 'error': '', 'userId': user.pk}), content_type='application/json')

def create_user(request:http.HttpRequest):
    if request.method != 'POST':
        return http.HttpResponseBadRequest()
    
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')

    if None in (username, password, email, first_name, last_name):
        return http.HttpResponse('{"message": "missing required fields"}', content_type='application/json', status=400)
    
    # verificando se existem usuários para este username
    user_found_uname = User.objects.filter(username=username).first() != None
    user_found_email = User.objects.filter(email=email).first() != None
    if user_found_uname or user_found_email:
        return http.HttpResponse('{"message": "user already cadastred"}', content_type='application/json', status=400)

    # criando usuário e perfil
    user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
    profile = Profile.objects.create()
    UserProfileRules.objects.create(user=user, profile=profile)

    return http.HttpResponse()

def logout(request:http.HttpRequest):
    auth.logout(request)
    return http.HttpResponse()