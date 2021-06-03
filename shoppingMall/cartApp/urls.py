from django.urls import path, include
from . import views as cart_views
from productApp import views as product_views

app_name='cart'

urlpatterns=[
    path('add/<int:product_id>/', cart_views.add_cart, name='add_cart'),
    path('detail_add/<int:product_id>/', cart_views.detail_add_cart, name='detail_add_cart'),    
    path('', cart_views.cart_detail, name='cart_detail'),
    path('minus_cart/<int:product_id>/', cart_views.minus_cart_product, name="minus_cart_product"),
    path('remove/<int:product_id>/', cart_views.cart_remove, name="cart_remove"),
]