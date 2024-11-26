from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def index(request):
    data = {
        'fullName': 'Iago Carvalho',
        'profile': 'perfil principal',
        'dateRange': '01/07/2024 - 31/07/2024',
    }
    return render(request, 'home.html', data)

def dash(request):
    return render(request, 'home/dash.html')

def reg(request):
    return render(request, 'home/reg.html')

def card(request):
    return render(request, 'home/card.html')

def settings(request):
    return render(request, 'home/settings.html')