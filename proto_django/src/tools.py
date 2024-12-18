from django.http import HttpRequest, HttpResponse

def checkRequest(request:HttpRequest, checkUser=True, method='GET') -> HttpResponse | None:
    """
    realiza uma série de verificações

    Respostas de erro, em ordem de verificação:
        - 405: método correto
        - 401: usuário autenticado (caso checkUser verdadeiro)
    """
    if request.method != method:
        return HttpResponse(status=405)
    
    if checkUser and not request.user.is_authenticated:
        return HttpResponse('{"msg": "usuário não autenticado"}', status=401, content_type='application/json')

def jResponse(msg:str, status=200):
        return HttpResponse('{"msg": "%s"}' % msg, status=status, content_type="application/json")