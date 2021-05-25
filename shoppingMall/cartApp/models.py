from django.db import models
from productApp.models import product as shop_product

# Create your models here.
class Cart(models.Model):
    cart_id=models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    class Meta:
        db_table='Cart'
        ordering=['date_added']

class CartItem(models.Model):
    product=models.ForeignKey(shop_product, on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    class Meta:
        db_table='cartItem'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name