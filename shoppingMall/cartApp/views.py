from django.contrib.auth import authenticate
from django.shortcuts import redirect, render, get_object_or_404
from productApp.models import product as Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from . import context_processors
from django.db.models import Max

# Create your views here.
def cart_remove(request, product_id):
    cart=Cart.objects.get(cart_id = request.session.get('user_id'))
    product = get_object_or_404(Product, product_id=product_id)
    cart_item=CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')

@csrf_exempt
def detail_add_cart(request, product_id):
    product=Product.objects.get(product_id=product_id)
    add_quantity=request.POST.get('detail_quantity')
    add_quantity=int(add_quantity)
    if request.session.get('user_id') is None:
        errorMsg = "로그인 해주세요"
        return render(request, "error.html", {'errorMsg' : errorMsg})

    try:
        cart= Cart.objects.get(cart_id=request.session.get('user_id'))
    except Cart.DoesNotExist:
        cart= Cart.objects.create(
            cart_id=request.session.get('user_id')
        )
        cart.save()
    
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity+=add_quantity
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            product=product,
            quantity=add_quantity,
            cart=cart,
            shipping_fee=product.shipping_fee
        )
        cart_item.save()
    
    return redirect('cart:cart_detail')




@csrf_exempt
def add_cart(request, product_id):
    product=Product.objects.get(product_id=product_id)
    if request.session.get('user_id') is None:
        errorMsg = "로그인 해주세요"
        return render(request, "error.html", {'errorMsg' : errorMsg})

    try:
        cart= Cart.objects.get(cart_id=request.session.get('user_id'))
    except Cart.DoesNotExist:
        cart= Cart.objects.create(
            cart_id=request.session.get('user_id')
        )
        cart.save()
    
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity+=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
            shipping_fee=product.shipping_fee
        )
        cart_item.save()
    return redirect('cart:cart_detail')

def cart_detail(request, total=0, counter=0, cart_items=None):
    if request.session.get('user_id') is None:
        errorMsg = "로그인 해주세요"
        return render(request, "error.html", {'errorMsg' : errorMsg})
    try:
        user_id=request.session.get('user_id')

        cart=Cart.objects.get(cart_id=user_id)
        cart_items=CartItem.objects.filter(cart=cart)
        for cart_item in cart_items:
            total+=(cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity

        max_shipping=CartItem.objects.filter(cart=cart)
        max_shipping.aggregate(shipping_fee=Max('shipping_fee'))
        max_shipping=max_shipping.order_by('-shipping_fee')[0].shipping_fee
        total+=int(max_shipping)
        cart.total_shipping_fee=max_shipping
        cart.save()

    except ObjectDoesNotExist:
        pass
    
    cart_count=context_processors.counter(request)
    cart_count=int(cart_count)
    count={'cart_count':cart_count}
    return render(request, 'cart.html', dict(cart=cart, cart_items=cart_items, total=total, count=count, cart_count=cart_count))

def minus_cart_product(request, product_id):
    product=Product.objects.get(product_id=product_id)
    try:
        cart= Cart.objects.get(cart_id=request.session.get('user_id'))
    except Cart.DoesNotExist:
        cart= Cart.objects.create(
            cart_id=request.session.get('user_id')
        )
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity<1:
            cart_item.quantity=1
        cart_item.quantity-=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cart:cart_detail')