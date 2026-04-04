from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AccountUpdateForm, CreateArtistForm
from artist.models import Artist
import stripe
from django.conf import settings
from stripe import StripeClient
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe_client = StripeClient(str(settings.STRIPE_SECRET_KEY))

# Create your views here.
def members(request):
    return render(request, 'artist.html')


def favourites(request):
    return render(request, 'favourites.html')


def account(request):
    accountUpdateForm = AccountUpdateForm(instance=request.user)
    #accountLinkForm = StripeLinkForm()

    if request.method == "POST":
        if "account-update-submit" in request.POST:
            accountUpdateForm = AccountUpdateForm(request.POST, request.FILES, instance=request.user)
            if accountUpdateForm.is_valid():
                accountUpdateForm.save()
                messages.success(request, "Your details have been updated.")
                return redirect("account")
            else:
                messages.success(request, ("There were some errors with some fields"))
        elif "account-link-submit" in request.POST:
            email = request.POST.get("email")

            # Try block copied from official Stripe documentation
            try:
                account = stripe_client.v2.core.accounts.create({
                    "display_name": email,
                    "contact_email": email,
                    "dashboard": "express",
                    "defaults": {
                        "responsibilities": {
                            "fees_collector": "application",
                            "losses_collector": "application",
                        }
                    },
                    "identity": {
                        "country": "GB",
                        "entity_type": "company",
                    },
                    "configuration": {
                        "recipient": {
                            "capabilities": {
                                "stripe_balance": {
                                    "stripe_transfers": {"requested": True},
                                }
                            }
                        },
                    },
                })

                request.user.stripe_account_id = account.id
                messages.success(request, "Account has been linked to Stripe")
                return redirect("account")
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
    else:
        accountUpdateForm = AccountUpdateForm(instance=request.user)
    return render(request, "account.html", {"accountUpdateForm": accountUpdateForm})

def manage(request):
    managed_artists = Artist.objects.filter(manager=request.user).order_by('name')
    return render(request, 'manage.html', {'managed_artists' : managed_artists})

def create_artist(request):

    if request.method == "POST":
        form = CreateArtistForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.manager = request.user
            obj.save()
            form.save_m2m()
            messages.success(request, ("Artist created successfully"))
            return redirect("manage")
        else:
            messages.success(request, ("There were some errors with some fields"))
    else:  
        form = CreateArtistForm()     
        return render(request, 'create_artist.html', {'form' : form})
    
# TODO implement view to update artists records with the below access decorator
# Code block generated using ChatGPT for safekeeping
# from django.contrib.auth.decorators import user_passes_test

# def is_manager_or_staff(user):
#     return user.is_authenticated and (user.isManager or user.is_staff)

# @user_passes_test(is_manager_or_staff)
# def update_artist(request, pk):
#     ...
