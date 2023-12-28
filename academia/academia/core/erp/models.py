from django.db import models
# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name ='Tipo'
        verbose_name_plural ='Tipos'
        db_table = 'Tipos'
        ordering = ['id']


class Usuario(models.Model):
    names = models.CharField(max_length=150)#,verbose_name='Nombres')
    appellidos = models.CharField(max_length=150)#,verbose_name='Apellidos')
    dpi = models.CharField(max_length=10)#, unique=True, verbose_name='Dpi')
    telefono = models.PositiveIntegerField(default=0)#,verbose_name='Telefono')
    name_usuario = models.CharField(max_length=150)#,unique=True,verbose_name='Nombre de Usuario')
    correo = models.CharField(max_length=150)#,unique=True,verbose_name='Correo Electronico')
    password = models.CharField(max_length=150)#,verbose_name='Password')
    type = models.ForeignKey(Type,on_delete=models.CASCADE)   #Relacionando tabla
    #flotante = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name ='Usuario'
        verbose_name_plural ='Usuarios'
        db_table = 'Usuarios'
        ordering = ['id']


class Cursos(models.Model):
    curso = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='cursos/%Y/%m/%d', null=True, blank=True)
    costo = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.curso
    
    class Meta:
        verbose_name ='Curso'
        verbose_name_plural ='Cursos'
        db_table = 'Cursos'
        ordering = ['id']


class Asignacion(models.Model):
    curso = models.ForeignKey(Cursos,on_delete=models.CASCADE)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=0)
    nit =  models.PositiveIntegerField(default=0)
    direccion = models.CharField(max_length=150)
    forma_pago = models.CharField(max_length=100)
    nombre_alumno = models.ForeignKey(Usuario,on_delete=models.CASCADE) 
    correo_conf = models.CharField(max_length=100)

    def __str__(self):
        return self.curso
    
    class Meta:
        verbose_name ='Asignacion'
        verbose_name_plural ='Asignaciones'
        db_table = 'Asignacion'
        ordering = ['id']        


opciones_consultas = [
    [0, "Desbloqueo"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "consulta"],
]


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    def __str__(self):
        return self.nombre
    
