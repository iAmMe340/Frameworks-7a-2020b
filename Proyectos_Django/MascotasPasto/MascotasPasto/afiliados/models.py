from django.db import models

class Paises(models.Model):
    id=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=10)
    nombre=models.CharField(max_length=30)
    abreviatura=models.CharField(max_length=6)
    estado=models.BooleanField(True)
    fecha_creacion=models.DateTimeField ("Date Creation")
    fecha_modificacion=models.DateTimeField ("Date modification")

class Ciudades(models.Model):
    id=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=10)
    nombre=models.CharField(max_length=30)
    abreviatura=models.CharField(max_length=10)
    id_pais=models.ForeignKey(Paises, on_delete=models.CASCADE)
    estado= models.BooleanField(True)
    fecha_creacion=models.DateTimeField
    fecha_modificacion=models.DateTimeField

class Afiliados(models.Model):
    id =models.AutoField(primary_key= True)
    nombres=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=30)
    telefono= models.IntegerField(max_length=10)
    direccion=models.CharField(max_length=25)
    email= models.EmailField(max_length=100)
    id_ciudad=models.ForeignKey(Ciudades, on_delete=models.CASCADE)
    estado=models.BooleanField()    
    fecha_creacion=models.DateTimeField
    fecha_modificacion=models.DateTimeField

