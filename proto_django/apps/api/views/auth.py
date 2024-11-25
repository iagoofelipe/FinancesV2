from django.urls import path
from django.shortcuts import render
from django.contrib import auth
from django.http import HttpRequest, HttpResponseBadRequest, HttpResponse

def login(request:HttpRequest):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    
    username = request.POST.get('username')
    password = request.POST.get('password')
    # user = User.objects.filter(username=username, password=password).first()
    print(username, password)
    user = auth.authenticate(request, username=username, password=password)

    if not user:
        return HttpResponse('invalid credentials', status=403)

    auth.login(request, user)
    return HttpResponse()

def token(request):
    return render(request, 'token.html')

def logout(request):
    auth.logout(request)
    return HttpResponse()


urlpatterns = [
    path('login', login, name='login'),
    path('token', token, name='token'),
    path('logout', logout, name='logout'),
]