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

class productAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'name', 'price', 'stock', 'salesamount']
    search_fields=['product_id', 'name', 'price']
    list_filter=['price_range']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        # You need to define a character for splitting your range, in this example I'll use a hyphen (-)
        try:
            # This will get me the range values if there's only 1 hyphen
            min_price, max_price = search_term.split('-')
        except ValueError:
            # Otherwise it will do nothing
            pass
        else:
            # If the try was successful, it will proceed to do the range filtering
            queryset |= self.model.objects.filter(price__gte=min_price, price__lte=max_price)
        return queryset, use_distinct



admin.site.register(product, productAdmin)