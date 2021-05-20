from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from productApp.models import product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

@csrf_exempt
def add_cart(request, product_id):
    id=product_id
    Product=product.objects.get(product_id=id)
#def add_cart(request):
#    Product=product.objects.get(id=request.POST['product_id'])
    try:
        cart= Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart= Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save()
    
    try:
        cart_item = CartItem.objects.get(product=Product, cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity+=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            product=Product,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cart:cart_detail')

def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cart_items=CartItem.objects.filter(cart=cart)
        for cart_item in cart_items:
            total+=(cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter))

def minus_cart_product(request, product_id):
    id=product_id
    Product=product.objects.get(product_id=id)
    try:
        cart= Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart= Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=Product, cart=cart)
        if cart_item.quantity<1:
            cart_item.quantity=1
        cart_item.quantity-=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            product=Product,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cart:cart_detail')