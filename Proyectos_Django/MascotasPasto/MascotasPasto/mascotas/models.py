from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Mascotas(models.Model):
    id =models.AutoField(primary_key= True)
    codigo=models.CharField(max_length=10)
    id_tipo=models.ForeignKey("app.Model", Tipos=("id"), on_delete=models.CASCADE)
    id_raza=models.ForeignKey("app.Model", Razas=("Ciudades"), on_delete=models.CASCADE)
    nombre=models.CharField(max_length=30)
    Vacunacion=models.BooleanField(_("true"))    
    fecha_creacion=models.DateTimeField
    fecha_modificacion=models.DateTimeField



class Tipos(models.Model):
    id=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=10)
    nombre=models.CharField(max_length=30)
    abreviatura=models.CharField(max_length=6)
    estado=models.BooleanField(("true"))
    fecha_creacion=models.DateTimeField
    fecha_modificacion=models.DateTimeField



class Razas(models.Model):
    id=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=10)
    nombre=models.CharField(max_length=30)
    abreviatura=models.CharField(max_length=10)
    id_tipo=models.ForeignKey("app.Model", Tipos=("id"), on_delete=models.CASCADE)
    estado= models.BooleanField(("true"))
    fecha_creacion=models.DateTimeField
    fecha_modificacion=models.DateTimeField
