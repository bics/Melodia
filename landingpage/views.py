from django.shortcuts import render
from artist.models import Artist

# Create your views here.
def index(request):
    # Random object retrieval generated using ChatGPT
    artists = sorted(
        Artist.objects.order_by('?')[:15],
        key=lambda x: x.rating or 0,
        reverse=True
    )
    return render(request, 'index.html', {"artists": artists})