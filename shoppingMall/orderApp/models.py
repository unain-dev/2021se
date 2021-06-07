from django.db import models
from django.utils import timezone

# Create your models here.
class Order(models.Model):
    CATEGORY_CHOICES=(
        ('order_continue', 'order_continue'),
        ('order_cancle', 'order_cancle'),
        ('pay_cancle', 'pay_cancle'),
        ('pay_complete', 'pay_complete'),
        ('shipping', 'shipping'),
        ('shipping_complete', 'shipping_complete'),
        ('order_complete', 'order_complete')
    )

    order_user=models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    total_price = models.IntegerField()
    total_quantity = models.IntegerField()
    order_state=models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    total_shipping_fee=models.IntegerField()
    shipping_address=models.CharField(max_length=1000)
    coupon_id=models.CharField(max_length=1000, null=True, blank=True)
    discount_price=models.IntegerField()
    before_discount=models.IntegerField()

    class Meta:
        db_table='Order'
        ordering=['date_added']

class OrderItem(models.Model):
    CATEGORY_CHOICES=(
        ('rings', 'rings'),
        ('glasses', 'glasses'),
        ('hats', 'hats'),
        ('necklace', 'necklace'),
    )

    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price=models.IntegerField()
    category=models.CharField(max_length=20, choices=CATEGORY_CHOICES, null=True)
    product_id = models.IntegerField()
    product_title=models.CharField(max_length=500)
    shipping_fee=models.IntegerField()

    class Meta:
        db_table='OrderItem'

    def sub_total(self):
        return self.price * self.quantity
'''
    def __str__(self):
        return self.product.name    
    '''