from .models import Category, Cart, CartItem

def common_data(request):
    categories = Category.objects.all()
    cart_items_count = 0
    
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            cart_items = CartItem.objects.filter(cart=cart)
            cart_items_count = cart_items.count()
        except Cart.DoesNotExist:
            pass
    
    return {
        'categories': categories,
        'cart_items_count': cart_items_count,
    } 