from django.db import models
# Create your models here.
class Usuario(models.Model):
    names = models.CharField(max_length=150)#,verbose_name='Nombres')
    appellidos = models.CharField(max_length=150)#,verbose_name='Apellidos')
    dpi = models.CharField(max_length=10)#, unique=True, verbose_name='Dpi')
    telefono = models.PositiveIntegerField(default=0)#,verbose_name='Telefono')
    name_usuario = models.CharField(max_length=150)#,unique=True,verbose_name='Nombre de Usuario')
    correo = models.CharField(max_length=150)#,unique=True,verbose_name='Correo Electronico')
    password = models.CharField(max_length=150)#,verbose_name='Password')
    #flotante = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name ='Usuario'
        verbose_name_plural ='Usuarios'
        db_table = 'Usuarios'
        ordering = ['id']

    
