from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.ERROR(request, "There's nothing in your bag right now.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51N7F5HL4vQV3gL48EzSUe3YV1PdilzzcCrC4RbO392IeUTKklA4irCNk5bWHDFtNm3G4Ko7tAnfqiJ5wsCzL0IW4002siCy5TX',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
