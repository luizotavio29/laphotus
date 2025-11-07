from django.urls import path

from events.views import buscar, comofunciona, contato, fotografos, home

urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('fotografos/', fotografos),
    path('como-funciona/', comofunciona),
    path('buscar/', buscar),
    #path('temp/', temp),
]