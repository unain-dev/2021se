from django.db import models

class P_range(object):
    OPTION_0, OPTION_1, OPTION_2, OPTION_3, OPTION_4, OPTION_5 = range(0, 6)

    CHOICES = (
        (OPTION_0, 'under 10000'),
        (OPTION_1, '10000-19990'),
        (OPTION_2, '20000-29990'),
        (OPTION_3, '30000-39990'),
        (OPTION_4, '40000-49990'),
        (OPTION_5, 'up to 50000'),
    )

class product(models.Model):
    product_id=models.IntegerField()
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    description=models.TextField()
    stock=models.IntegerField()
    salesamount=models.IntegerField()

    status = models.IntegerField(
        choices=P_range.CHOICES,
        default=P_range.OPTION_0
    )