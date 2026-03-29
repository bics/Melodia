from django.shortcuts import render
from artist.models import Artist
from album.models import Track, Album
import random
from django.db.models import Avg, Value, Count, Case, When, FloatField
from django.db.models.functions import Replace

# Create your views here.
def index(request):
    # Random object retrieval, sorting and rating generated using ChatGPT
    artists = list(
        Artist.objects.annotate(
        avg_rating=Avg("tracks__rating__ratingValue")
        )
    )
    random.shuffle(artists)
    artists = sorted(artists[:15], key=lambda x: x.avg_rating or 0, reverse=True)

    all_tracks = list(
        Track.objects.filter(artist__in=artists).annotate(
            rating_count=Count("rating"),
            avg_rating=Case(
                When(rating_count__gte=3, then=Avg("rating__ratingValue")),
                default=None,
                output_field=FloatField()
            )
        )
    )
    random.shuffle(all_tracks)
    random_tracks = all_tracks[:10]

    for track in random_tracks:
        if track.avg_rating:
            filled = int(track.avg_rating)
            track.stars = [True] * filled + [False] * (5 - filled)
        else:
            track.stars = [False] * 5


    return render(request, 'index.html', {"artists": artists, "random_tracks": random_tracks})

# View inspired by tutorial from Codemy
def search_result(request):
    if request.method == "POST":
        # Input sanitation generated using ChatGPT
        searched = request.POST.get('search_input', '').strip().lower().replace(" ", "")
        print("SEARCHED:", searched)
        track_results = Track.objects.annotate(
        name_clean=Replace('name', Value(' '), Value(''))
            ).filter(name_clean__icontains=searched)

        album_results = Album.objects.annotate(
            name_clean=Replace('name', Value(' '), Value(''))
            ).filter(name_clean__icontains=searched)

        artist_results = Artist.objects.annotate(
            name_clean=Replace('name', Value(' '), Value(''))
            ).filter(name_clean__icontains=searched)
    return render(request, "search_result.html", {"searched" : searched, "track_results" : track_results, "album_results" : album_results, "artist_results": artist_results})