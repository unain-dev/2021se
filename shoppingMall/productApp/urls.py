from django.urls import path
from productApp import views

app_name='products'
urlpatterns = [
    path('',views.rings, name='rings'),
    path('glasses/',views.glasses, name='glasses'),
    path('necklace/',views.necklace, name='necklace'),
    path('hats/',views.hats, name='hats'),
    path('search/', views.search, name="search"),
    path('<int:product_id>',views.product_detail,name='product_detail')
]