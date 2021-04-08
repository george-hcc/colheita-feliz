from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def api_base(request):
    return HttpResponse('Bem vindo filho da puta!')

def api_list_endpoints(request):
    pass

def api_list_devices(request):
    pass

def api_status(request):
    pass

def api_order(request):
    pass
