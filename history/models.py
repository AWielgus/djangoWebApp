from django.db import models


# Create your models here.
class History(models.Model):
    description = models.TextField()
    product_name = models.TextField()
    update_date = models.DateTimeField('modification date')
