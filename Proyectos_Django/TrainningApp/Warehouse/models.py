from django.db import models

class Category(models.Model) :
    code = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    description= models.TextField(default='Description here', max_length=20)
    create_date = models.DateTimeField('Date creation')
    update_date = models.DateTimeField('Date update')

   #descripcion en el panel de animistracion Category
    def __str__(self):
        return self.name, self.code

class Sector(models.Model) :
    code = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    id_category= models.ForeignKey(Category, on_delete= models.CASCADE)
    description= models.TextField(default='Description here', max_length=20)
    create_date = models.DateTimeField('Date creation')
    update_date = models.DateTimeField('Date update')

       #descripcion en el panel de animistracion Sector
    def __str__(self):
        return self.name, self.code, self.status


