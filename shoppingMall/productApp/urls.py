from django.urls import path
from productApp import views


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('',views.rings, name='rings')
]