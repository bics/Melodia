from django.shortcuts import render, redirect
from django.contrib import messages
from artist.models import Artist
from .models import Album, Track
from .forms import TrackCreationForm, TrackFormSet
from artist.forms import AlbumCreationForm
import cloudinary.uploader
from django.utils.text import slugify
from mutagen.mp3 import MP3

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
        formset = TrackFormSet(request.POST, request.FILES, queryset=Track.objects.none())

        #Formset save partially generated using ChatGPT
        if formset.is_valid():
            savedTracks = 0

            for form in formset:
                if form.cleaned_data.get("name"):   # skip empty forms
                    track = form.save(commit=False)
                    track.artist = artist
                    track.album = album

                    # Audio upload and length retrieval generated using ChatGPT
                    mp3_file = form.cleaned_data.get("track")
                    if mp3_file:
                        audio = MP3(mp3_file)
                        track.length = audio.info.length
                        upload_result = cloudinary.uploader.upload(
                            mp3_file,
                            resource_type="raw",   # important!
                            folder=f"melodia/artist_audios/{slugify(artist.name)}/{slugify(album.name)}"
                        )
                        # Save the Cloudinary URL in the model
                        track.track = upload_result["secure_url"]

                    track.save()
                    savedTracks += 1

            if savedTracks > 0:
                messages.success(request, f"Track(s) created successfully for {album.name}")
                return redirect("artist", name=artist.name, pk=artist.pk)
            else:
                messages.success(request, f"No Track(s) created for {album.name}")
                return redirect("artist", name=artist.name, pk=artist.pk)
        else:
            messages.success(request, ("There were some errors with some fields"))
    else:  
        formset = TrackFormSet(queryset=Track.objects.none())

    return render(request, 'create_track.html',  {'formset' : formset, 'album': album, 'artist': artist})
