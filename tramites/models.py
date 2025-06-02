from django.db import models

class Ciudadano(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=12, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Tramite(models.Model):
    TIPO_CHOICES = [
        ('LICENCIA', 'Licencia'),
        ('PERMISO', 'Permiso'),
        ('SERVICIO', 'Servicio Público'),
    ]
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROCESO', 'En Proceso'),
        ('FINALIZADO', 'Finalizado'),
        ('RECHAZADO', 'Rechazado'),
    ]
    ciudadano = models.ForeignKey(Ciudadano, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descripcion = models.TextField()
    urgente = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PENDIENTE')

    def __str__(self):
        return f"{self.tipo} - {self.ciudadano.nombre}"

# Si necesitas predicciones ML, puedes agregar el modelo TramiteMLPrediction aquí.
