from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    amount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    creation_date = models.DateTimeField('creation date')
    modification_date = models.DateTimeField('modification date')
    hidden = models.BooleanField(default=False)

