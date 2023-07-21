from django.db import models

# Create your models here.

from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    numero_telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

