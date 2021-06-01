from django.contrib import admin
from .models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
    model=Order

class ItemAdmin(admin.ModelAdmin):
    inlines=[
        OrderAdmin
    ]

# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
