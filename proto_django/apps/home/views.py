from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from apps.api import models

@login_required(login_url='/login')
def index(request:HttpRequest):
    user = User.objects.filter(username=request.user.username).first()
    rules = models.UserProfileRules.objects.filter(user=user).all() # conjunto de perfis que este usuário está vinculado
    
    # caso este usuário não possua perfil
    if not len(rules):
        # TODO: requisitar que crie um novo perfil
        return HttpResponse('{"msg": "nenhum perfil localizado!"}', content_type="application/json")


    # coletando o perfil principal, caso haja
    rules_default = tuple(filter(lambda r: r.default, rules))
    if rules_default:
        profile = rules_default[0].profile
    else:
        profile = rules.first().profile

    data = {
        'fullName': f'{user.first_name} {user.last_name}',
        'profileName': profile.name,
        'profileId': profile.pk,
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