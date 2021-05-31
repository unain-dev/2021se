from django.shortcuts import render, redirect
from cartApp import context_processors
from cartApp.models import Cart, CartItem
from shoppingApp.models import UserAccounts,address
from django.core.exceptions import ObjectDoesNotExist
import requests
from .models import OrderItem, Order

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
        cart.save()
        cart_items=CartItem.objects.filter(cart=cart)
        for cart_item in cart_items:
            total+=(cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity

    uid=request.session.get('user_id')
    get_all=UserAccounts.objects.all()
    get_user=get_all.filter(user_id=uid)
    shippings = address.objects.filter(accounts__in=get_user)

    if Order.DoesNotExist:
        order=Order.objects.create(
            order_user=request.session.get('user_id'),
            total_price=total,
            total_quantity=counter,
            order_state='order_continue'
        )
        order.save()

    try:
        order_items=OrderItem.objects.get(order=order)
    except OrderItem.DoesNotExist :
        for cart_item in cart_items:
            order_items=OrderItem.objects.create(
                order=order,
                order_id=cart_item.product.product_id,
                product_id=cart_item.product.product_id,
                quantity=cart_item.quantity,
                price=cart_item.product.price
            )
            order_items.save()

    cart_count=context_processors.counter(request)
    cart_count=int(cart_count)
    count={'cart_count':cart_count}

    order_items=OrderItem.objects.filter(order=order)
    return render(request, 'order.html', dict(order_items=order_items, total=total, count=count, cart_count=cart_count, shippings=shippings, order_id=order.id))

def cancle_order(request):
    return render(request, '')

def pay(request):
    if request.method == "POST":
        URL = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            "Authorization": "KakaoAK " + "432f6f7ce279b9adf9723cf13773d0b4",   # 변경불가
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
        }
        params = {
            "cid": "TC0ONETIME",    # 테스트용 코드
            "partner_order_id": "1001",     # 주문번호
            "partner_user_id": "german",    # 유저 아이디
            "item_name": "연어초밥",        # 구매 물품 이름
            "quantity": "1",                # 구매 물품 수량
            "total_amount": "12000",        # 구매 물품 가격
            "tax_free_amount": "0",         # 구매 물품 비과세
            "approval_url": "http://127.0.0.1:8000/order/paySuccess",
            "cancel_url": "http://127.0.0.1:8000/order/payCancel",
            "fail_url": "http://127.0.0.1:8000/order/payFail",
        }

        res = requests.post(URL, headers=headers, params=params)
        request.session['tid'] = res.json()['tid']      # 결제 승인시 사용할 tid를 세션에 저장
        next_url = res.json()['next_redirect_pc_url']   # 결제 페이지로 넘어갈 url을 저장
        return redirect(next_url)

def paySuccess(request):
    URL = 'https://kapi.kakao.com/v1/payment/approve'
    headers = {
            "Authorization": "KakaoAK " + "432f6f7ce279b9adf9723cf13773d0b4",   # 변경불가
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
        }
    params = {
        "cid": "TC0ONETIME",    # 테스트용 코드
        "tid": request.session['tid'],  # 결제 요청시 세션에 저장한 tid
        "partner_order_id": "1001",     # 주문번호
        "partner_user_id": "german",    # 유저 아이디
        "pg_token": request.GET.get("pg_token"),     # 쿼리 스트링으로 받은 pg토큰
    }

    res = requests.post(URL, headers=headers, params=params)
    amount = res.json()['amount']['total']
    res = res.json()
    context = {
        'res': res,
        'amount': amount,
    }
    return render(request, 'paySuccess.html', context)

def payFail(request):
    return render(request, 'payFail.html')

def payCancel(request):
    return render(request, 'payCancel.html')