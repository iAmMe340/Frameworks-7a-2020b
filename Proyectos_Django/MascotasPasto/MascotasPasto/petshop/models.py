from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Productos(models.Model):
    id =models.AutoField(primary_key= True)
    nombres=models.CharField(max_length=30)
    id_proveedor=models.ForeignKey("app.Model", Proovedores=("id"), on_delete=models.CASCADE)
    estado=models.BooleanField(("true"))    
    fecha_creacion=models.DateTimeField
    fecha_modificacion=models.DateTimeField



class Poveedores(models.Model):
    id=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=10)
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=20)
    telefono= models.IntegerField(max_length=22)
    estado=models.BooleanField(("true"))
    fecha_creacion=models.DateTimeField
    fecha_modificacion=models.DateTimeField



class Clientes(models.Model):
    id=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=10)
    nombres=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=30)
    cedula=models.CharField(max_length=15)
    direccion=models.CharField(max_length=50)
    fecha_creacion=models.DateTimeField
    fecha_modificacion=models.DateTimeField
