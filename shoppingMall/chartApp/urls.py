from django.urls import path
from chartApp import views

app_name='chart'
urlpatterns = [
    path('',views.view_chart, name='view_chart'),
   
]