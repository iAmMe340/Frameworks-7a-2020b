from django.db import models

class Category(models.Model) :
    code = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    description= models.TextField(default='Description here', max_length=20)
    create_date = models.DateTimeField('Date creation')
    update_date = models.DateTimeField('Date update')

    def __str__(self):
        return self.name, self.code
