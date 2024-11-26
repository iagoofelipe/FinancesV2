from django.urls import path
from django.shortcuts import render
from django.contrib import auth
from django.http import HttpRequest, HttpResponse

import src.tools as tools

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

urlpatterns = [
    path('login', login, name='login'),
    path('token', token, name='token'),
    path('logout', logout, name='logout'),
]