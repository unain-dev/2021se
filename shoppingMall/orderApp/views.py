from django.shortcuts import render, redirect
from requests.models import get_cookie_header
from cartApp import context_processors
from cartApp.models import Cart, CartItem
from shoppingApp.models import UserAccounts,address
from django.core.exceptions import ObjectDoesNotExist
import requests
from .models import OrderItem, Order
from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt
from productApp.models import product
from django.contrib import messages
from django.core.paginator import Paginator
from couponApp.models import Coupon
from django.utils.dateformat import DateFormat
from datetime import datetime

# Create your views here.
def get_items(request, total=0, counter=0):
    uid=request.session.get('user_id')
    get_all=UserAccounts.objects.all()
    get_user=get_all.filter(user_id=uid)
    shippings = address.objects.filter(accounts__in=get_user)

    user_id=request.session.get('user_id')
    cart=Cart.objects.get(cart_id=user_id)
    cart_items=CartItem.objects.filter(cart=cart)
    for cart_item in cart_items:
        total+=(cart_item.product.price * cart_item.quantity)
        counter += cart_item.quantity

    return shippings, total, counter

def order_check(request, total=0, counter=0, cart_items=None):
    if request.session.get('user_id') is None:
        errorMsg = "로그인 해주세요"
        return render(request, "error.html", {'errorMsg' : errorMsg})
    else :
        user_id=request.session.get('user_id')
        cart=Cart.objects.get(cart_id=user_id)
        #cart.save()
        cart_items=CartItem.objects.filter(cart=cart)
        for cart_item in cart_items:
            total+=(cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
        max_shipping=CartItem.objects.filter(cart=cart)
        max_shipping.aggregate(shipping_fee=Max('shipping_fee'))
        max_shipping=max_shipping.order_by('-shipping_fee')[0].shipping_fee
        total+=int(max_shipping)
    
    uid=request.session.get('user_id')
    get_all=UserAccounts.objects.all()
    get_user=get_all.filter(user_id=uid)
    shippings = address.objects.filter(accounts__in=get_user)

    order=Order.objects.create(
        order_user=request.session.get('user_id'),
        total_price=total,
        total_quantity=counter,
        order_state='order_continue',
        total_shipping_fee=cart.total_shipping_fee,
        discount_price=0,
        before_discount=total
    )
    order.save()
    request.session['order_id']=order.id

    order_set=Order.objects.get(id=order.id)
    for cart_item in cart_items:
        order_items=OrderItem.objects.create(
            order=order_set,
            product_id=cart_item.product.product_id,
            product_title=cart_item.product.name,
            quantity=cart_item.quantity,
            price=cart_item.product.price,
            shipping_fee=cart_item.shipping_fee,
            category=cart_item.product.category
        )
        order_items.save()

    cart_count=context_processors.counter(request)
    cart_count=int(cart_count)
    count={'cart_count':cart_count}

    order_items=OrderItem.objects.filter(order=order)
    request.session['cart_pay']=False

    if request.session.get('pay_state')=='pay_cancle':
        request.session['pay_state']=''
        order_cancle=True
    else :
        order_cancle=False


    return render(request, 'order.html', dict(order=order, order_items=order_items, count=count, cart_count=cart_count, shippings=shippings, order_id=order.id, order_cancle=order_cancle))

def cancle_order(request):
    return render(request, '')

def pay(request):
    order_id=request.session.get('order_id')
    order=Order.objects.get(id=order_id)
    request.session['order_id']=order_id
    item_name=''

    select_address=request.POST.get('address_select')
    shipping_address=address.objects.get(id=select_address)
    get_address=shipping_address.road_address+shipping_address.detail_address
    order.shipping_address=get_address
    order.save()
    
    order_items=OrderItem.objects.filter(order=order)
    for item in order_items:
        item_name+=str(item.product_title)

    if request.method == "POST":
        URL = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            "Authorization": "KakaoAK " + "432f6f7ce279b9adf9723cf13773d0b4",   # 변경불가
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
        }
        params = {
            "cid": "TC0ONETIME",    # 테스트용 코드
            "partner_order_id": order_id,     # 주문번호
            "partner_user_id": request.session.get('user_id'),    # 유저 아이디
            "item_name": item_name,        # 구매 물품 이름
            "quantity": order.total_quantity,                # 구매 물품 수량
            "total_amount": order.total_price,        # 구매 물품 가격
            "tax_free_amount": "0",         # 구매 물품 비과세
            "approval_url": "http://127.0.0.1/order/paySuccess",
            "cancel_url": "http://127.0.0.1/order/payCancel",
            "fail_url": "http://127.0.0.1/order/payFail",
        }

        res = requests.post(URL, headers=headers, params=params)
        _result=res.json()
        request.session['tid'] = _result['tid']      # 결제 승인시 사용할 tid를 세션에 저장
        next_url = res.json()['next_redirect_pc_url']   # 결제 페이지로 넘어갈 url을 저장
        return redirect(next_url)

def paySuccess(request):
    order_id=request.session.get('order_id')
    user_id=request.session.get('user_id')
    order=Order.objects.get(id=order_id)
    order.order_state='pay_complete'
    order.save()
    
    if request.session.get('cart_pay')==True:
        cart=Cart.objects.get(cart_id = request.session.get('user_id'))
        cart.delete()

    URL = 'https://kapi.kakao.com/v1/payment/approve'
    headers = {
            "Authorization": "KakaoAK " + "432f6f7ce279b9adf9723cf13773d0b4",   # 변경불가
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
        }
    params = {
        "cid": "TC0ONETIME",    # 테스트용 코드
        "tid": request.session['tid'],  # 결제 요청시 세션에 저장한 tid
        "partner_order_id": order_id,     # 주문번호
        "partner_user_id": user_id,    # 유저 아이디
        "pg_token": request.GET.get("pg_token"),     # 쿼리 스트링으로 받은 pg토큰
    }

    res = requests.post(URL, headers=headers, params=params)
    amount = res.json()['amount']['total']
    res = res.json()
    context = {
        'res': res,
        'amount': amount,
    }

    order_items=OrderItem.objects.filter(order=order)
    for item in order_items:
        product_id=item.product_id
        get_product=product.objects.get(product_id=product_id)
        get_product.salesamount+=item.quantity
        get_product.stock-=item.quantity
        get_product.save()

    return render(request, 'paySuccess.html', context)

def payFail(request):
    order=Order.objects.get(id=request.session.get('order_id'))
    order.order_state='pay_cancle'
    order.save()

    request.session['pay_state']='pay_cancle'

    return redirect('order:order_check')

def payCancel(request):
    order=Order.objects.get(id=request.session.get('order_id'))
    order.order_state='pay_cancle'
    order.save()

    request.session['pay_state']='pay_cancle'

    return redirect('order:order_check')

def view_myOrder(request):
    cart_count=context_processors.counter(request)
    cart_count=int(cart_count)
    count={'cart_count':cart_count}

    user_id=request.session.get('user_id')
    orders=Order.objects.filter(order_user=user_id)

    paginator=Paginator(orders, 5)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    
    for order in orders:
        if order.order_state == 'order_continue':
            order.order_state='order_cancle'
            order.save()

    return render(request, 'my_order.html', {'count':count, 'posts':posts})

def order_detail(request, order_id):
    cart_count=context_processors.counter(request)
    cart_count=int(cart_count)
    count={'cart_count':cart_count}

    orders=Order.objects.get(id=order_id)
    order_items=OrderItem.objects.filter(order=orders)
    
    return render(request, 'order_detail.html', {'orders':orders, 'order_items':order_items, 'count':count})

@csrf_exempt
def search_order(request):
    cart_count=context_processors.counter(request)
    cart_count=int(cart_count)
    count={'cart_count':cart_count}

    user_id=request.session.get('user_id')
    if request.method == 'POST':
        minDate=request.POST['minDate']
        maxDate=request.POST['maxDate']
        orders=Order.objects.filter(order_user=user_id, date_added__range=[minDate, maxDate])
    
    paginator=Paginator(orders, 5)
    page=request.GET.get('page')
    posts=paginator.get_page(page)

    return render(request, 'my_order.html', {'posts':posts, 'minDate':minDate, 'maxDate':maxDate, 'count':count})


def coupon_check(request):
    coupon_get=Coupon.objects.filter(activation=True)
    for coupon in coupon_get :
        now=DateFormat(datetime.now()).format('Ymd')
        dueDate=DateFormat(coupon.dueDate).format('Ymd')
        if int(dueDate)-int(now)>0:
            pass
        else:
            coupon.activation=False
            coupon.save()

    order_id=request.session.get('order_id')
    order=Order.objects.get(id=order_id)
    order_items=OrderItem.objects.filter(order=order)

    uid=request.session.get('user_id')
    get_all=UserAccounts.objects.all()
    get_user=get_all.filter(user_id=uid)
    shippings = address.objects.filter(accounts__in=get_user)

    cart_count=context_processors.counter(request)
    cart_count=int(cart_count)
    count={'cart_count':cart_count}
    real_price=order.total_price

    coupon_id=request.POST['coupon']
    try:
        coupon_list=Coupon.objects.get(activation=True, coupon_id=coupon_id)
    except:
        return render(request, 'order.html', dict(order=order, order_items=order_items, count=count, cart_count=cart_count, shippings=shippings, order_id=order.id, coupon_error='limit_coupon'))

    if order.coupon_id is None:
        if coupon_list.type == 'price' and order.total_price>=coupon_list.min_price:
            order.coupon_id=coupon_id
            order.discount_price=coupon_list.discount_price
            order.total_price-=coupon_list.discount_price
            order.save()
            return render(request, 'order.html', dict(order=order, order_items=order_items, count=count, cart_count=cart_count, shippings=shippings, order_id=order.id, coupon_price=coupon_list.discount_price, coupon_per=coupon_list.discount_percentage, real_price=real_price))

        elif coupon_list.type == 'percentage':
            for item in order_items:
                if item.category == coupon_list.discount_category:
                    order.coupon_id=coupon_id
                    cal_dis=order.total_price/coupon_list.discount_percentage
                    order.discount_price=round(cal_dis)
                    order.total_price-=round(cal_dis)
                    order.save()
            return render(request, 'order.html', dict(order=order, order_items=order_items, count=count, cart_count=cart_count, shippings=shippings, order_id=order.id, coupon_price=coupon_list.discount_price, coupon_per=coupon_list.discount_percentage, real_price=real_price))
        else :
            msg='쿠폰 조건 미달'
            return render(request, 'order.html', dict(order=order, order_items=order_items, count=count, cart_count=cart_count, shippings=shippings, order_id=order.id, coupon_error='under_condition'))
    else:
        msg='쿠폰 중복 적용 금지'
        return render(request, 'order.html', dict(order=order, order_items=order_items, count=count, cart_count=cart_count, shippings=shippings, order_id=order.id, coupon_error='no_duplicated'))
    return render(request, 'order.html', dict(order=order, order_items=order_items, count=count, cart_count=cart_count, shippings=shippings, order_id=order.id))

def view_after_coupon(request):
    return render(request, 'payFail.html')

@csrf_exempt
def direct_pay(request, product_id):
    product_get=product.objects.get(product_id=product_id)
    total_direct=(product_get.price*int(request.POST['detail_quantity']))+product_get.shipping_fee
    get_product=product.objects.get(product_id=product_id)
    if request.session.get('user_id') is None:
        errorMsg = "로그인 해주세요"
        return render(request, "error.html", {'errorMsg' : errorMsg})

    elif get_product.stock>=int(request.POST['detail_quantity']):
        order=Order.objects.create(
            order_user=request.session.get('user_id'),
            total_price=total_direct,
            total_quantity=request.POST['detail_quantity'],
            order_state='order_continue',
            total_shipping_fee=product_get.shipping_fee,
            discount_price=0,
            before_discount=total_direct
        )
        order.save()
        request.session['order_id']=order.id

        
        order_items=OrderItem.objects.create(
            order=order,
            product_id=product_id,
            product_title=product_get.name,
            quantity=request.POST['detail_quantity'],
            price=product_get.price,
            shipping_fee=product_get.shipping_fee,
            category=product_get.category
        )
        order_items.save()

        cart_count=context_processors.counter(request)
        cart_count=int(cart_count)
        count={'cart_count':cart_count}

        uid=request.session.get('user_id')
        get_all=UserAccounts.objects.all()
        get_user=get_all.filter(user_id=uid)
        shippings = address.objects.filter(accounts__in=get_user)

        if request.session.get('pay_state')=='pay_cancle':
            request.session['pay_state']=''
            order_cancle=True
        else :
            order_cancle=False

        order_items=OrderItem.objects.filter(order=order)
        
        return render(request, 'order.html', dict(order=order, order_items=order_items, count=count, cart_count=cart_count, shippings=shippings, order_id=order.id, order_cancle=order_cancle))
    else:
        errorMsg = "입력한 수량만큼의 재고가 남아있지 않습니다."
        return render(request, "error.html", {'errorMsg' : errorMsg})
        

def user_complete_order(request, order_id):
    order=Order.objects.get(id=order_id)
    order.order_state='order_complete'
    order.save()
    return redirect('order:view_myOrder')