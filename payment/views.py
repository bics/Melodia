from django.shortcuts import render, redirect
from django.contrib import messages
from artist.models import Artist
import stripe
from django.conf import settings
from urllib.parse import quote
from decimal import Decimal

# Create your views here.
def donate(request, name, pk):
    artist = Artist.objects.get(pk=pk)

    # Statement block was partially generated using ChatGPT
    if request.method == "POST":
        amount = request.POST.get("amount")
        custom = request.POST.get("custom-amount")
        if amount:
            donation = int(amount) * 100
        elif custom:
            try:
                donation = int(Decimal(custom) * 100)
            except:
                messages.success(request, f"Invalid custom amount")
                return render(request, "stripe_payment.html", { "artist" : artist })
        else:
            messages.success(request, f"No amount was selected")
            return render(request, "stripe_payment.html", { "artist" : artist })
        
        # Try-catch block was copied from official Stripe documentation
        try:            
            safe_name = quote(artist.name)
            checkout_session = stripe.checkout.Session.create(
                line_items=[{
                'price_data': {
                    'currency': 'gbp',
                    'product_data': {
                        'name': f'Donation to {artist.name}',
                    },
                    'unit_amount': donation,
                },
                'quantity': 1,
            }],
                mode='payment',
                
                payment_intent_data={
                    'application_fee_amount': int(donation * 0.1),
                    'transfer_data': {
                        'destination': artist.manager.stripeUserId,
                    },
                },

                success_url= str(settings.STRIPE_PAYMENT_SUCCESS_URL),
                cancel_url= str(settings.STRIPE_PAYMENT_CANCEL_URL + f"{safe_name}/{artist.id}"),
            )

            return redirect(checkout_session.url)
        
        except Exception as e:
            messages.success(request, str(e))
            return redirect("donate", name=artist.name, pk=artist.pk)

    return render(request, "stripe_payment.html", { "artist" : artist })


def payment_success(request):
    return render(request, "payment_success.html")
