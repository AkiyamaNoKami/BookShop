from django.shortcuts import render
from django.http.response import JsonResponse

from basket.basket import Basket
from .models import Order, OrderItem

def add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        user_id = request.user.id
        order_key = request.POST.get('order_key')
        baskettotal = basket.get_total_price()

        #Check if order exists
        if Order.objects.filter(order_key=order_key).exists():
            pass