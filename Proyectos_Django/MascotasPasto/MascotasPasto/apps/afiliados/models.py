from django.db import models

# Create your models here.
class Afiliados(models.Model):
    id =models.AutoField(primary_key= True)
    nombres=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=30)
    telefono= models.IntegerField(max_length=10)
    direccion=models.CharField(max_length=25)
    email= models.EmailField(max_length=100)
    id_ciudad=models.ForeignKey("app.Model", verbose_name=("Ciudades"), on_delete=models.CASCADE)
    estado=models.BooleanField(_("true"))    
    fecha_creacion=models.DateTimeField
    fecha_modificacion=models.DateTimeField



class Paises(models.Model):
    id=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=10)
    nombre=models.CharField(max_length=30)
    abreviatura=models.CharField(max_length=6)
    estado=models.BooleanField(_("true"))
    fecha_creacion=models.DateTimeField
    fecha_modificacion=models.DateTimeField



class Ciudades(models.Model):
    id=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=10)
    nombre=models.CharField(max_length=30)
    abreviatura=models.CharField(max_length=10)
    id_pais=models.ForeignKey("app.Model", verbose_name=_("Paises"), on_delete=models.CASCADE)
    estado= models.BooleanField(_("true"))
    fecha_creacion=models.DateTimeField
    fecha_modificacion=models.DateTimeField
