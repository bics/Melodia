from django.shortcuts import render

# Create your views here.
def members(request):
    return render(request, 'artist.html')


def favourites(request):
    return render(request, 'favourites.html')


def account(request):
    return render(request, 'account.html')