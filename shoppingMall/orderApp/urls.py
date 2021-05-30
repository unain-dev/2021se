from django.urls import path
from . import views as order_views
app_name='order'

urlpatterns=[
    path('', order_views.order_check, name='order_check'),
    path('pay/', order_views.pay, name='pay'),
    path('paySuccess/', order_views.paySuccess),
    path('payFail/', order_views.payFail),
    path('payCancel/', order_views.payCancel),
]