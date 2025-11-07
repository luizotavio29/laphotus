from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'events/pages/home.html')

def contato(request):
    return render(request, 'events/pages/contato.html')

def fotografos(request):
    return render(request, 'events/pages/fotografos.html')

def comofunciona(request):
    return render(request, 'events/pages/comofunciona.html')

def buscar(request):
    return render(request, 'events/pages/buscar.html')

#def temp(request):
#   return render(request, 'me-apague/temp.html')