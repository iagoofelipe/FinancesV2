from django.http import HttpRequest, HttpResponse
from django.urls import path
from django.db.models import Sum
import json
from src import tools, consts
from .. import models

def reg(request:HttpRequest):
    r = tools.checkRequest(request)
    if r is not None:
        return r
    
    regs = models.Registry.objects
    regs_in = models.Registry.objects.filter(inout=consts.TYPE_INOUT_IN)
    regs_out = models.Registry.objects.filter(inout=consts.TYPE_INOUT_OUT)
    data = {}

    for obj, name in ((regs, 'registries'), (regs_in, 'in'), (regs_out, 'out')):
        data[name] = {
            'qtd': obj.count(),
            'sum': float(obj.aggregate(Sum('value'))['value__sum']),
        }

    return HttpResponse(json.dumps(data), content_type='application/json')


urlpatterns = [
    path('reg', reg, name='reg'),
]