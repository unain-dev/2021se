from django.contrib import admin
from .models import Coupon

class Coupon_Admin(admin.ModelAdmin):
    list_display = ['coupon_id', 'quantity', 'dueDate', 'type']

# Register your models here.
admin.site.register(Coupon, Coupon_Admin)
