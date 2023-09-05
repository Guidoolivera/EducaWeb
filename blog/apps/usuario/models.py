from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# models
# modelo standard de usuario, falta profesor y tutor
class Usuario(AbstractUser):
    imagen = models.ImageField(null=True, blank=True, upload_to='usuario', default='usuario/user-default.png')
    # podemos agregar nombre y apellido y otros datos mas
    def get_absolute_url(self):
        return reverse('index')
