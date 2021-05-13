
from django.db import models

# Create your models here.
class product(models.Model):

    PRICE_RANGE_FIELD={
        ('under 10000', 'under 10000'),
        ('10000-19990', '10000-19990'),
        ('20000-29990', '20000-29990'),
        ('30000-39990', '30000-39990'),
        ('40000-49990', '40000-49990'),
        ('upper 50000', 'upper 50000')
    }

    product_id=models.IntegerField()
    name=models.CharField(max_length=50)
    price_range=models.CharField(max_length=30, choices=PRICE_RANGE_FIELD, null=True)
    price=models.IntegerField()
    description=models.TextField()
    stock=models.IntegerField()
    salesamount=models.IntegerField()