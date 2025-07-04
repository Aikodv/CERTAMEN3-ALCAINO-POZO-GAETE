from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    TIPO_USUARIO = [
        ('vecino', 'Vecino'),
        ('junta', 'Junta de Vecinos'),
        ('funcionario', 'Funcionario Municipal'),
        ('admin', 'Administrador'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_USUARIO, default='vecino')

    def __str__(self):
        return f"{self.username} ({self.get_tipo_display()})"
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Lugar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre_completo = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre_completo

class Taller(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('aceptado', 'Aceptado'),
        ('rechazado', 'Rechazado'),
    ]

    titulo = models.CharField(max_length=150)
    fecha = models.DateField()
    duracion_horas = models.FloatField()
    estado = models.CharField(max_length=10, choices=ESTADOS, default='pendiente')
    observacion = models.TextField(null=True, blank=True)

    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
