from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AccountUpdateForm, CreateArtistForm
from artist.models import Artist
import stripe
from django.conf import settings
from django.http import JsonResponse
import json
from allauth.account.models import EmailAddress

stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.
def account(request):
    accountUpdateForm = AccountUpdateForm(instance=request.user)
    user_email = request.user.email

    if request.method == "POST":
        if "account-update-submit" in request.POST:
            accountUpdateForm = AccountUpdateForm(request.POST, instance=request.user)
            if accountUpdateForm.is_valid():
                accountUpdateForm.save()
                new_email = accountUpdateForm.cleaned_data.get("email")

            # If block generated using ChatGPT
            if new_email and new_email != user_email:
                EmailAddress.objects.add_email(
                    request,
                    request.user,
                    new_email,
                    confirm=True
                )
                messages.success(request, "Your details have been updated.")
                return redirect("account")
            else:
                messages.success(request, ("There were some errors with some fields"))
        elif "account-link-submit" in request.POST:
            email = request.POST.get("email")

            # Try block copied from official Stripe documentation
            try:
                account = stripe.Account.create(
                    type="express",
                    email=email,
                    country="GB",
                )

                request.user.stripeUserId = account.id
                request.user.save()
                messages.success(request, "Account has been linked to Stripe")
                return redirect("account")
            except Exception as e:
                messages.success(request, str(e))
                return redirect("account")
        elif "manager-access-submit" in request.POST:
            # Feature to send email to staff
            messages.success(request, "A ticket has been created.")
            return redirect("account")
    else:
        accountUpdateForm = AccountUpdateForm(instance=request.user)
    return render(request, "account.html", {"accountUpdateForm": accountUpdateForm})


# Below 2 views were generated using ChatGPT and Claude
def account_status(request, account_id):
    try:
        account = stripe.Account.retrieve(account_id)
        data = {
            "id": account.id,
            "chargesEnabled": account.charges_enabled,
            "payoutsEnabled": account.payouts_enabled,
            "detailsSubmitted": account.details_submitted,
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


def create_account_link(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    data = json.loads(request.body)
    account_id = data.get("accountId")

    print(str(settings.STRIPE_REFRESH_URL))
    print(str(settings.STRIPE_RETURN_URL))

    account_link = stripe.AccountLink.create(
        account=account_id,
        refresh_url=str(settings.STRIPE_REFRESH_URL),  # if link expires
        return_url=str(settings.STRIPE_RETURN_URL),  # after onboarding
        type="account_onboarding",
    )
    return JsonResponse({"url": account_link.url})


def manage(request):
    managed_artists = Artist.objects.filter(manager=request.user).order_by("name")
    return render(request, "manage.html", {"managed_artists": managed_artists})


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
        return render(request, "create_artist.html", {"form": form})
