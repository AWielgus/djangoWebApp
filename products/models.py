from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.TextField()
    description = models.TextField()
    amount = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    creation_date = models.DateTimeField('creation date')
    modification_date = models.DateTimeField('modification date')
