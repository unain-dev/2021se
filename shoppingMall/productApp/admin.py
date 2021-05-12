'''
from django.contrib import admin
from .models import product
# Register your models here.
class productAdmin(admin.ModelAdmin):
    list_display=['name','price']


admin.site.register(product,productAdmin)
'''
from django.contrib import admin
from .models import product

admin.site.register(product)