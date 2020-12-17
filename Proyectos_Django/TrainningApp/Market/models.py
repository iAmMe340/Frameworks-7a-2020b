from django.db import models

class Category(models.Model) :
    code = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    description= models.TextField(default='Description here', max_length=20)
    create_date = models.DateTimeField('Date creation')
    update_date = models.DateTimeField('Date update')

class Vendor (models.Model):
    code = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    description= models.TextField(default='Description here')


class Products(models.Model):
    code = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    unity_price = models.IntegerField()
    quantity= models.IntegerField()
    id_category= models.ForeignKey(Category, on_delete= models.CASCADE)
    id_vendor= models.ForeignKey(Vendor, on_delete= models.CASCADE)
    status = models.BooleanField(default=True)
    description= models.TextField(default='Description here', max_length=20)
    create_date = models.DateTimeField('Date creation')
    update_date = models.DateTimeField('Date update')    

class Stock (models.Model):
    code = models.CharField(max_length=1000)
    id_product= models.ForeignKey(Products,on_delete= models.CASCADE)
    quantity= models.IntegerField()
    description= models.TextField(default='Description here', max_length=20)
    create_date = models.DateTimeField('Date creation')
    update_date = models.DateTimeField('Date update')    