from django import forms
from .models import Tramite, Ciudadano

class TramiteForm(forms.ModelForm):
    nombre = forms.CharField(label="Nombre del Ciudadano", max_length=100)
    dni = forms.CharField(label="DNI", max_length=12)
    email = forms.EmailField(label="Email")

    class Meta:
        model = Tramite
        fields = ['nombre', 'dni', 'email', 'tipo', 'descripcion', 'urgente']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
