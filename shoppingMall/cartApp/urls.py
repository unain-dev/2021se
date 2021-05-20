from django.urls import path
from . import views as cart_views
app_name='cart'

urlpatterns=[
    path('add/<int:product_id>/', cart_views.add_cart, name='add_cart'),
    path('', cart_views.cart_detail, name='cart_detail'),
    path('minus_cart/<int:product_id>/', cart_views.minus_cart_product, name="minus_cart_product")
]