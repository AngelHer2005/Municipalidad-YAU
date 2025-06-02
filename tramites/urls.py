from django.urls import path
from . import views

urlpatterns = [
    path('priorizados/', views.lista_tramites_priorizados, name='lista_tramites_priorizados'),
    path('agregar/', views.agregar_tramite, name='agregar_tramite'),
]
