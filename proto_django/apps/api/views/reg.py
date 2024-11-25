from django.urls import path
from django import http
from django.http import HttpRequest, HttpResponse
from datetime import datetime

import tools
from ..models import Registry

def new_registry(request:HttpRequest):
    r = tools.checkRequest(request, method='POST')
    if r is not None:
        return r
    
    default = {
        'type': 0,
        'datetime': datetime.now().strftime('%Y-%m-%d %H-%M-%S'),
        'description': '',
        # 'recorrenceFormatId': None,
    }
    params = ('type', 'title', 'datetime', 'value', 'description')
    data = {}

    for param in params:
        if param not in request.POST and param not in default:
            return tools.jResponse('preencha todos os campos obrigatórios!', 400)
        
        # montando dados do registro
        data[param] = request.POST.get(param, default[param])

    # salvando registro
    # Registry(data)


urlpatterns = [
    path('new', new_registry, name='new'),
]