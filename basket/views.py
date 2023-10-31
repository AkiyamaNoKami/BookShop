from django.shortcuts import render, get_object_or_404
from .basket import Basket
from store.models import Product
from django.http import JsonResponse, HttpResponseBadRequest

def basket_summary(request):
    basket = Basket(request)
    return render(request, 'basket/summary.html', {'basket': basket})

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response

def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id_str = request.POST.get('productid')
        if product_id_str is not None and product_id_str.isdigit():
            product_id = int(product_id_str)
            basket.delete(product=product_id)
            basketqty = basket.__len__()
            baskettotal = basket.get_total_price()
            response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
            return response
        else:
            # Обработка случаев, когда 'productid' отсутствует или не является числом
            return HttpResponseBadRequest('Invalid productid')
    else:
        # Обработка случая, когда action не равен 'post'
        return HttpResponseBadRequest('Invalid action')

def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)
        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty':basketqty, 'subtotal': baskettotal})
        return response