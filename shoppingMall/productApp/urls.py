from django.urls import path
from productApp import views


urlpatterns = [
    path('',views.rings, name='rings'),
    path('socks/',views.socks, name='socks'),
    path('necklace/',views.necklace, name='necklace')   
    
]