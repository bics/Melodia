from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AccountUpdateForm, CreateArtistForm
from artist.models import Artist

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

def manage(request):
    managed_artists = Artist.objects.filter(manager=request.user)
    return render(request, 'manage.html', {'managed_artists' : managed_artists})

def create_artist(request):

    if request.method == "POST":
        form = CreateArtistForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.manager = request.user
            obj.save()
            form.save_m2m()
            return redirect("manage")
        else:
            messages.success(request, ("There were some errors with some fields"))
    else:  
        form = CreateArtistForm()     
        return render(request, 'create_artist.html', {'form' : form})
