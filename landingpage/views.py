from django.shortcuts import render
from artist.models import Artist

# Create your views here.
def index(request):
    # Random object retrieval generated using ChatGPT
    artists = Artist.objects.order_by('?')[:15]
    return render(request, 'index.html', {"artists": artists})