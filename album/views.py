from django.shortcuts import render, redirect
from django.contrib import messages
from artist.models import Artist
from .models import Album
from .forms import TrackCreationForm, TrackFormSet
from artist.forms import AlbumCreationForm

# Create your views here.
def edit_album(request, name, pk, artistPK):
    album = Album.objects.get(pk=pk)
    artist = Artist.objects.get(pk=artistPK)

    if request.method == "POST":
        form = AlbumCreationForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            messages.success(request, f"Album edited successfully for {artist.name}")
            return redirect("artist", name=artist.name, pk=artist.pk)
        else:
            messages.success(request, ("There were some errors with some fields"))
    else:  
        form = AlbumCreationForm(instance=album)


    return render(request, 'edit_album.html', {'form' : form, 'album': album, 'artist': artist})


def create_track(request, name, pk, artistPK):
    album = Album.objects.get(pk=pk)
    artist = Artist.objects.get(pk=artistPK)

    if request.method == "POST":
        formset = TrackFormSet(request.POST, request.FILES)

        if formset.is_valid():
            formset.save()
            messages.success(request, f"Track(s) created successfully for {album.name}")
            return redirect("artist", name=artist.name, pk=artist.pk)
        else:
            messages.success(request, ("There were some errors with some fields"))
    else:  
        formset = TrackFormSet()

    return render(request, 'create_track.html',  {'formset' : formset, 'album': album, 'artist': artist})
