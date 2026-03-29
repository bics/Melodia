from django.shortcuts import render
from artist.models import Artist
from album.models import Track
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

    all_tracks = list(Track.objects.filter(artist__in=artists))
    random.shuffle(all_tracks)
    random_tracks = all_tracks[:10]


    return render(request, 'index.html', {"artists": artists, "random_tracks": random_tracks})

def search_result(request):
    return render(request, "search_result.html")