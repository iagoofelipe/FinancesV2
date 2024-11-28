from django.urls import path
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse

import src.tools as tools
from .. import models

def login(request:HttpRequest):
    r = tools.checkRequest(request, False, 'POST')
    if r is not None:
        return r
    
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    if None in (username, password):
        return tools.jResponse('preencha todos os campos!', 400)
    
    user = auth.authenticate(request, username=username, password=password)

    if not user:
        return tools.jResponse('usuário ou senha incorretos!', 406)

    auth.login(request, user)
    return HttpResponse()

def logout(request):
    r = tools.checkRequest(request)
    if r is not None:
        return r
    
    auth.logout(request)
    return HttpResponse()

def token(request):
    return render(request, 'token.html')

def newUser(request:HttpRequest):
    r = tools.checkRequest(request, False, 'POST')
    if r is not None:
        return r
    
    fields = ('first_name', 'last_name', 'email', 'username', 'password')
    data = {}
    kw = dict(status=422, content_type='application/json')

    for field in fields:
        if field not in request.POST:
            return HttpResponse('{"msg": "preecha todos os campos necessários!"}', status=400, content_type='application/json')
        
        # validando valores
        val = request.POST[field]
        if not val:
            return HttpResponse('{"msg": "nenhum campo pode estar em branco!"}', **kw)
        
        if field == 'password' and len(val) < 4:
            return HttpResponse('{"msg": "senha muito curta!"}', **kw)
        
        data[field] = val

    print(data)

    if User.objects.filter(username=data['username']).first() is not None:
        return HttpResponse('{"msg": "já existe uma conta com este nome de usuário!"}', **kw)

    if User.objects.filter(email=data['email']).first() is not None:
        return HttpResponse('{"msg": "já existe uma conta com este e-mail!"}', **kw)
    
    # criando usuário e perfil
    user = User.objects.create_user(**data)
    profile = models.Profile(name='perfil principal')
    
    user.save()
    profile.save()

    # vinculando usuário a um novo perfil
    rule = models.UserProfileRules(user=user, profile=profile, default=True)
    rule.save()
    
    return HttpResponse()

urlpatterns = [
    path('login', login, name='login'),
    path('token', token, name='token'),
    path('logout', logout, name='logout'),
    path('newUser', newUser, name='newUser'),
]