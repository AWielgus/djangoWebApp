from django.db import models


# Create your models here.
class History(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    update_date = models.DateTimeField('modification date')
