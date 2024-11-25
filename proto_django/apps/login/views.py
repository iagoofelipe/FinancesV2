from django.shortcuts import render, redirect
from django.http import  HttpRequest

def index(request:HttpRequest):
    if request.user.is_authenticated:
        return redirect('/home')
    
    return render(request, 'login.html')