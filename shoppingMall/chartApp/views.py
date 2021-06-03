from django.shortcuts import redirect, render
from orderApp.models import Order, OrderItem
from productApp.models import product
from collections import Counter
from django.db.models import F, Sum, Count, Case, When

# Create your views here.
def view_chart(request):
    user_id=request.session.get('user_id')
    if request.method == 'POST':
        minDate=request.POST['minDate']
        maxDate=request.POST['maxDate']
        if minDate=="" or maxDate=="":
            return redirect('chart:view_chart')
        #
        orders=Order.objects.filter(order_user=user_id, order_state="order_complete", date_added__range=[minDate, maxDate])
        
        #설정된 기간의 총 판매금액
        total_sales_price=orders.aggregate(Sum('total_price'))

        #설정된 기간 동안 많이 판매된 상품
        product_obj={}
        for order in orders:
            order_items=OrderItem.objects.filter(order=order)
            for order_item in order_items:
                if order_item.product_title in product_obj:
                    q=product_obj[order_item.product_title]
                else:
                    q=0
                product_obj[order_item.product_title]=q+order_item.quantity
        
        sort_item=sorted(product_obj.items(), reverse=True, key=lambda item: item[1])[0:3]
        best_item=dict(sort_item)

        #설정된 기간 동안 많이 판매된 카테고리
        best_cate={}
        for order in orders:
            order_items=OrderItem.objects.filter(order=order)
            for order_item in order_items:
                if order_item.category in best_cate:
                    q=best_cate[order_item.category]
                else:
                    q=0
                best_cate[order_item.category]=q+order_item.quantity
        sort_cate=sorted(best_cate.items(), reverse=True, key=lambda item: item[1])[0:3]
        best_category=dict(sort_cate)

        return render(request, 'chart.html', {'total_sales_price':total_sales_price, 'best_item':best_item, 'best_category':best_category, 'minDate':minDate, 'maxDate':maxDate})

    return render(request, 'chart.html')
