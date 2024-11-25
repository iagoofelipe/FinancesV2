from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseBadRequest, HttpResponse

@login_required(login_url='/login')
def index(request):
    data = {
        'fullName': 'Iago Carvalho',
        'profile': 'perfil principal',
        'dateRange': '01/07/2024 - 31/07/2024',
    }
    return render(request, 'home.html', data)