from django.urls import path
from django.http import HttpRequest, HttpResponse
from datetime import datetime
import time

import src.tools as tools
from ..models import Registry

def new_registry(request:HttpRequest):
    r = tools.checkRequest(request, method='POST')
    if r is not None:
        return r
    
    default = {
        'inout': 0,
        'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'description': '',
        # 'recorrenceFormatId': None,
    }
    params = ('inout', 'title', 'datetime', 'value', 'description')
    data = {}

    for param in params:
        if param not in request.POST and param not in default:
            return tools.jResponse('preencha todos os campos obrigatórios!', 400)
        
        # montando dados do registro
        data[param] = request.POST.get(param, default.get(param))

    # salvando registro
    reg = Registry(**data)
    reg.save()

    r = '{"id": %s}' % reg.pk
    time.sleep(5)
    return HttpResponse(r, content_type='application/json')

def regs(request:HttpRequest):
    pass

urlpatterns = [
    path('new', new_registry, name='new'),
]