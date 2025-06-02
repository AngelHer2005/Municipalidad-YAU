from django.shortcuts import render, redirect
from .models import Tramite, Ciudadano
from .forms import TramiteForm
import numpy as np

def priorizar_tramites(tramites):
    # ML simple: urgente tiene máxima prioridad, luego tipo y fecha
    prioridad_tipo = {'LICENCIA': 3, 'PERMISO': 2, 'SERVICIO': 1}
    X = []
    for t in tramites:
        X.append([
            1 if t.urgente else 0,
            prioridad_tipo.get(t.tipo, 0),
            t.fecha_creacion.timestamp()
        ])
    X = np.array(X)
    if X.size == 0:
        return []
    if X.ndim == 1:
        X = X.reshape(1, -1)
    prioridades = X[:,0]*100 + X[:,1]*10 - X[:,2]/1e10  # Urgente pesa mucho, luego tipo, luego antigüedad
    return prioridades

def lista_tramites_priorizados(request):
    tramites = Tramite.objects.all().order_by('-fecha_creacion')
    prioridades = priorizar_tramites(tramites)
    tramites_con_prioridad = sorted(
        zip(tramites, prioridades),
        key=lambda x: x[1],
        reverse=True
    )
    return render(request, 'tramites/lista_priorizados.html', {'tramites_con_prioridad': tramites_con_prioridad})

def agregar_tramite(request):
    if request.method == 'POST':
        form = TramiteForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            dni = form.cleaned_data['dni']
            email = form.cleaned_data['email']
            ciudadano, created = Ciudadano.objects.get_or_create(
                dni=dni,
                defaults={'nombre': nombre, 'email': email}
            )
            # Si el ciudadano ya existe, actualiza nombre/email si han cambiado
            if not created:
                if ciudadano.nombre != nombre or ciudadano.email != email:
                    ciudadano.nombre = nombre
                    ciudadano.email = email
                    ciudadano.save()
            tramite = Tramite(
                ciudadano=ciudadano,
                tipo=form.cleaned_data['tipo'],
                descripcion=form.cleaned_data['descripcion'],
                urgente=form.cleaned_data['urgente']
            )
            tramite.save()
            return redirect('lista_tramites_priorizados')
    else:
        form = TramiteForm()
    return render(request, 'tramites/agregar_tramite.html', {'form': form})
