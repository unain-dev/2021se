'''
from django.contrib import admin
from .models import product
# Register your models here.
class productAdmin(admin.ModelAdmin):
    list_display=['name','price']


admin.site.register(product,productAdmin)
'''
from django.contrib import admin
from django_admin_multiple_choice_list_filter.list_filters import MultipleChoiceListFilter
from .models import P_range, product,Photo,review

class StatusListFilter(MultipleChoiceListFilter):
    title = 'Price_range'
    parameter_name = 'status__in'

    def lookups(self, request, model_admin):
        return P_range.CHOICES
class PhotoInline(admin.TabularInline):
    model = Photo
class reviewInline(admin.TabularInline):
    model = review

class productAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'name', 'price', 'stock', 'salesamount','thumbnail']
    search_fields=['product_id', 'name', 'price']
    list_filter = (StatusListFilter, 'category')
    inlines = [PhotoInline, reviewInline]



admin.site.register(product, productAdmin)
