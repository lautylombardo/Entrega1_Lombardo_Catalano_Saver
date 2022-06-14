from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.IntegerField()
    domicilio=models.CharField(max_length=50)
    mensaje=models.TextField()

    def __str__(self):
        return self.nombre