from django.urls import path
from . import views as order_views
app_name='order'

urlpatterns=[
    path('', order_views.order_check, name='order_check'),
    path('pay/', order_views.pay, name='pay'),
    path('paySuccess/', order_views.paySuccess),
    path('payFail/', order_views.payFail),
    path('payCancel/', order_views.payCancel, name='payCancel'),
    path('myOrder/', order_views.view_myOrder, name="view_myOrder"),
    path('detailOrder/<int:order_id>', order_views.order_detail, name="order_detail"),
    path('searchOrder/', order_views.search_order, name="search_order"),
    path('couponCheck/', order_views.coupon_check, name="coupon_check"),
    path('viewOrderCheck/', order_views.view_after_coupon, name="view_after_coupon"),
    path('directPay/<int:product_id>', order_views.direct_pay, name="direct_pay"),
    path('user_complete_order/<int:order_id>', order_views.user_complete_order, name="user_complete_order"),
]