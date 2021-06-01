from django.urls import path
from . import views as order_views
app_name='order'

urlpatterns=[
    path('', order_views.order_check, name='order_check'),
    path('pay/', order_views.pay, name='pay'),
    path('paySuccess/', order_views.paySuccess),
    path('payFail/', order_views.payFail),
    path('payCancel/', order_views.payCancel),
    path('myOrder/', order_views.view_myOrder, name="view_myOrder"),
    path('detailOrder/<int:order_id>', order_views.order_detail, name="order_detail"),
    path('searchOrder/', order_views.search_order, name="search_order"),
]