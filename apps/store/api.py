from django.http import JsonResponse
from apps.cart.cart import Cart
from .models import Product
from django.shortcuts import get_object_or_404, redirect 
import json
from apps.order.models import Order, OrderItem
from apps.order.utils import checkout


def api_add_to_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    product_id = data['product_id']
    update = data['update']
    quantity = data['quantity']

    cart = Cart(request)

    product = get_object_or_404(Product, pk=product_id)

    if not update:

        cart.add(product=product, quantity=1, update_quantity =False)

    else:

        cart.add(product=product, quantity=quantity, update_quantity=True)

    return JsonResponse(jsonresponse)

def api_remove_from_cart(request):

    cart = Cart(request)

    data = json.loads(request.body)
    jsonresponse = {'success': True}
    product_id = str(data['product_id'])

    cart = Cart(request)
    cart.remove(product_id)
    
    return JsonResponse(jsonresponse)

def api_checkout(request):

    cart = Cart(request)


    data = json.loads(request.body)
    jsonresponse = {'sucess': True}
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    address = data['address']
    zipcode = data['zipcode']
    place = data['place']

    order_id = checkout(request, first_name, last_name,email,address, zipcode,place)

    paid = True

    if paid == True:
        order = Order.objects.get(pk = order_id)
        order.paid = True
        order.paid_amount = cart.get_total_cost()
        order.save()

        cart.clear()

    return JsonResponse(jsonresponse)


