from django.urls import path

from events.views import contato, home

urlpatterns = [
    path('', home),
    path('contato/', contato)
]