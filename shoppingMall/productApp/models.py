
from django.db import models

# Create your models here.
class product(models.Model):
    product_id=models.IntegerField()
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    description=models.TextField()
    stock=models.IntegerField()
    salesamount=models.IntegerField()