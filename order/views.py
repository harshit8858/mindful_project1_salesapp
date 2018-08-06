from django.shortcuts import render
from cart.cart import Cart
from product.models import Product


# def add_to_cart(request, product_id, quantity):
def add_to_cart(request, product_id):

    product = Product.objects.get(id=product_id)
    print(product)
    cart = Cart(request)
    cart.add(product, product.price)

def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)

def get_cart(request):
    return render(request, 'cart/cart.html', dict(cart=Cart(request)))
