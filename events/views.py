from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'events/home.html')

def contato(request):
    return render(request, 'events/contato.html')