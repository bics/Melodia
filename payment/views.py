from django.shortcuts import render
from artist.models import Artist

# Create your views here.
def donate(request, name, pk):
    artist = Artist.objects.get(pk=pk)
    return render(request, "stripe_payment.html", { "artist" : artist })
