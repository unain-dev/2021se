from django.db import models

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

    class Meta:
        db_table='Order'
        ordering=['date_added']

class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price=models.IntegerField()
    product_id = models.IntegerField()

    class Meta:
        db_table='OrderItem'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name    
    