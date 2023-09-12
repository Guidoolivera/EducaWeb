from django.db import models
from django.utils import timezone

# Create your models here.

class Contacto(models.Model):
    nombre_apellido= models.CharField(max_length=100)
    email= models.EmailField()
    asunto= models.CharField(max_length=50)
    mensaje= models.TextField()
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre_apellido

class Inscripcion(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.PositiveIntegerField()
    SEXO_CHOICES = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
    ]
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)
    email_tutor = models.EmailField()
    telefono_tutor = models.PositiveIntegerField()
    CURSO_CHOICES = [
        ('Jardin', 'Educación Inicial'),
        ('Educacion', 'Educación Primaria'),
        ('Secundaria', 'Educación Secundaria'),
    ]
    curso_interes = models.CharField(max_length=20, choices=CURSO_CHOICES)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.curso_interes}'