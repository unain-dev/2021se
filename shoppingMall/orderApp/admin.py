from django.contrib import admin
from .models import Order, OrderItem
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

class ItemAdmin(admin.TabularInline):
    model=OrderItem

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added',)
    list_display=['id', 'order_user', 'order_state', 'date_added']
    list_filter=(('date_added', DateRangeFilter), )
    inlines=[
        ItemAdmin
    ]
    def has_delete_permission(self, request, obj=None):
        return False

# Register your models here.
admin.site.register(Order, OrderAdmin)
