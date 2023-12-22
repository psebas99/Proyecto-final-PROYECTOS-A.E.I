from django.db import models

class Curso(models.Model):
    # Definir los campos del modelo Curso aquí
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    # Otros campos...

    def __str__(self):
        return self.nombre
    
Curso._meta.app_label = 'academia_de_ingenieria'
# Create your models here.
