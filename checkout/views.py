from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IYZDACAex9kg2wRbP4B4aONDQGY9X9ZKgB1w5jYrpM2OzkGiqPcIxSGOJ20DqMGK9IDG6Vw6Fp2hbdWTh27ECHb00vs0WCVwW',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
