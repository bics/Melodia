from django.shortcuts import render, redirect
from django.contrib import messages
from artist.models import Artist
from django.conf import settings
from urllib.parse import quote
from decimal import Decimal
from .models import Donation
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

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
            
            if (request.user.is_authenticated):
                user_id = request.user.id
                user_email = request.user.email or ""
            else:
                user_id = None
                user_email = "not registered"

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

                metadata={
                    "artist_id": str(artist.id),
                    "artist_name": str(artist.name),
                    "amount": str(donation),
                    "manager_name" : str(artist.manager.name),
                    "manager_stripe_id" : str(artist.manager.stripeUserId),
                    "donator" : str(user_id),
                    "donator_email" : str(user_email),
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

# Webhook view was copied from official Stripe documentation and modified using ChatGPT
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except Exception:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        if session['payment_status'] == 'paid':
            artist_id = session['metadata'].get('artist_id')
            artist_name = session['metadata'].get('artist_name')
            amount = session['metadata'].get('amount')

            artist = None
            if artist_id:
                try:
                    artist = Artist.objects.get(id=artist_id)
                except Artist.DoesNotExist:
                    pass

            donation, created = Donation.objects.get_or_create(
                stripe_session_id=session['id'],
                defaults={
                    "artist": artist,
                    "artist_name": artist_name,
                    "amount": int(amount),
                    "is_paid": True,
                }
            )

            # idempotency safety
            if not created and not donation.is_paid:
                donation.is_paid = True
                donation.save()

            print(f"✅ Donation recorded: {session['id']}")

    return HttpResponse(status=200)
