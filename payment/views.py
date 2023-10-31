import stripe
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from basket.basket import Basket

@login_required
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)

    stripe.api_key = 'pk_test_51O7Gu9HtpNtph5DTmlqA7aEGuejHJHmdM4QyGfFisW90r4sNcsnDMljM9y9K2xWU0jZtoiJFOqNvIAqbj67T7WlD00tj1lvd6s'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency = 'gbp',
        metadata = {'userid': request.user.id}
    )

    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})
