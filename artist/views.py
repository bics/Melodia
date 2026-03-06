from django.shortcuts import render
from .models import Artist

# Create your views here.
def artist(request, pk):
    artist = Artist.objects.get(pk=pk)
    return render(request, 'artist.html', { "artist": artist})