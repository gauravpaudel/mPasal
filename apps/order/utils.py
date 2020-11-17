import datetime
import os

from random import randint

from apps.cart.cart import Cart


from .models import Order, OrderItem


def checkout(request, first_name, last_name, email, address , zipcode, place):
    order = Order(first_name = first_name, last_name= last_name, email = email, address= address, zipcode= zipcode,place=place)
    order.save()

    cart = Cart(request)

    for item in cart:
        OrderItem.objects.create(order = order, product= item['product'],quantity = item['quantity'],price = item['price'])

    return order.id