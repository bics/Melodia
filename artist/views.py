from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Artist
from album.models import Album, Track, Rating
from .forms import AlbumCreationForm, EditArtistForm
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Avg, Prefetch, Count, Case, When, FloatField

# Create your views here.
def artist(request, name, pk):
    artist = Artist.objects.get(pk=pk)

    # Rating retrieval partially generated using Claude
    albums = Album.objects.filter(artist=artist).prefetch_related(
        Prefetch(
            "tracks",
            queryset=Track.objects.annotate(
                rating_count=Count("rating"),
                avg_rating=Case(
                    When(rating_count__gte=3, then=Avg("rating__ratingValue")),
                    default=None,
                    output_field=FloatField()
                )
            ).order_by("position")
        )
    )

    for album in albums:
        for track in album.tracks.all():
            if track.avg_rating:
                filled = int(track.avg_rating)
                track.stars = [True] * filled + [False] * (5 - filled)
            else:
                track.stars = [False] * 5

    return render(request, 'artist.html', { "artist": artist, 'albums': albums})

def create_album(request, name, pk):
    
    artist = Artist.objects.get(pk=pk)
    if request.method == "POST":
        form = AlbumCreationForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.manager = request.user
            obj.artist = artist
            obj.save()
            form.save_m2m()
            messages.success(request, f"Album created successfully for {artist.name}")
            return redirect("artist", name=artist.name, pk=artist.pk)
        else:
            messages.success(request, ("There were some errors with some fields"))
    else:  
        form = AlbumCreationForm()

    return render(request, 'create_album.html', {'form' : form, 'artist': artist})

def edit_artist(request, name, pk):
    artist = Artist.objects.get(pk=pk)
    if request.method == "POST":
        form = EditArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            messages.success(request, "Details have been updated.")
            return redirect("edit_artist", name= artist.name, pk=artist.pk)
        else:
            messages.success(request, ("There were some errors with some fields"))
    else:  
        form = EditArtistForm(instance=artist)      
    
    form = EditArtistForm(instance=artist)
    return render(request, "edit_artist.html", {"form" : form, 'artist': artist})

# View generated using ChatGPT
@require_POST
def rate_track(request):
    data = json.loads(request.body)

    track_id = data.get('track_id')
    rating_value = data.get('rating')

    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Not logged in'}, status=403)

    track = Track.objects.get(id=track_id)

    rating, created = Rating.objects.update_or_create(
        ratingTrack=track,
        ratingUser=request.user,
        defaults={'ratingValue': rating_value}
    )

    return JsonResponse({
        'success': True,
        'rating': rating.ratingValue
    })