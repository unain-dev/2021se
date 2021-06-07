from django.db import models

# Create your models here.
class Coupon(models.Model):
    TYPE_CHOICES=(
        ('price', 'price'),
        ('percentage', 'percentage'),
    )
    CATEGORY_CHOICES=(
        ('rings', 'rings'),
        ('glasses', 'glasses'),
        ('hats', 'hats'),
        ('necklace', 'necklace'),
    )

    coupon_id = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now_add=True)
    dueDate = models.DateTimeField()
    activation = models.BooleanField()
    type=models.CharField(max_length=20, choices=TYPE_CHOICES)
    discount_percentage=models.IntegerField()
    discount_price=models.IntegerField()
    min_price=models.IntegerField()
    discount_category=models.CharField(max_length=20, choices=CATEGORY_CHOICES)
