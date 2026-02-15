from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AccountUpdateForm

# Create your views here.
def members(request):
    return render(request, 'artist.html')


def favourites(request):
    return render(request, 'favourites.html')


def account(request):
    if request.method == "POST":
        form = AccountUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your details have been updated.")
            return redirect("account")
    else:
        form = AccountUpdateForm(instance=request.user)
    return render(request, "account.html", {"form": form})