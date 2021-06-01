from django.contrib import admin
from .models import Order, OrderItem

class ItemAdmin(admin.TabularInline):
    model=OrderItem

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added',)
    inlines=[
        ItemAdmin
    ]

# Register your models here.
admin.site.register(Order, OrderAdmin)
