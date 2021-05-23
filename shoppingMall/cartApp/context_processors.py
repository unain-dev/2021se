from .models import Cart, CartItem

def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart= Cart.objects.filter(cart_id=request.session.get('user_id'))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                item_count+=cart_item.quantity
        except Cart.DoesNotExist:
            item_count=0
        
    return item_count
