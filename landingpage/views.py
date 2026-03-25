from django.shortcuts import render
from artist.models import Artist
import random
from django.db.models import Avg

# Create your views here.
def index(request):
    # Random object retrieval and sorting generated using ChatGPT
    artists = list(
        Artist.objects.annotate(
        avg_rating=Avg("tracks__rating__ratingValue")
        )
    )
    random.shuffle(artists)
    artists = sorted(artists[:15], key=lambda x: x.avg_rating or 0, reverse=True)

    return render(request, 'index.html', {"artists": artists})