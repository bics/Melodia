from django.shortcuts import render, redirect
from django.contrib import messages
from artist.models import Artist
from .models import Album, Track
from .forms import TrackCreationForm, TrackFormSet, UpdateTrackFormSet
from artist.forms import AlbumCreationForm
import cloudinary.uploader
from django.utils.text import slugify
from mutagen.mp3 import MP3


# Create your views here.
def edit_album(request, name, pk, artistPK):
    album = Album.objects.get(pk=pk)
    artist = Artist.objects.get(pk=artistPK)

    edit_album_form = AlbumCreationForm(instance=album)
    edit_tracks_formset = UpdateTrackFormSet(
        queryset=album.tracks.all().order_by("position")
    )

    if request.method == "POST":
        if "album-update-submit" in request.POST:
            edit_album_form = AlbumCreationForm(
                request.POST, request.FILES, instance=album
            )
            if edit_album_form.is_valid():
                edit_album_form.save()
                messages.success(
                    request, f"Album edited successfully for {artist.name}"
                )
                return redirect("artist", name=artist.name, pk=artist.pk)
            else:
                messages.success(request, ("There were some errors with some fields"))

        elif "update-tracks-submit" in request.POST:
            edit_tracks_formset = UpdateTrackFormSet(
                request.POST,
                request.FILES,
                queryset=album.tracks.all().order_by("position"),
            )
            if edit_tracks_formset.is_valid():
                edit_tracks_formset.save()
                messages.success(
                    request, f"Track(s) have been updated for {album.name}"
                )
                return redirect("artist", name=artist.name, pk=artist.pk)
            else:
                messages.success(request, ("There were some errors with some fields"))

    return render(
        request,
        "edit_album.html",
        {
            "edit_album_form": edit_album_form,
            "edit_tracks_formset": edit_tracks_formset,
            "album": album,
            "artist": artist,
        },
    )


def create_track(request, name, pk, artistPK):
    album = Album.objects.get(pk=pk)
    current_tracks = album.tracks.count()
    artist = Artist.objects.get(pk=artistPK)

    if request.method == "POST":
        formset = TrackFormSet(
            request.POST, request.FILES, queryset=Track.objects.none()
        )

        # Formset save partially generated using ChatGPT
        if formset.is_valid():
            savedTracks = 0

            for form in formset:
                if form.cleaned_data.get("name"):  # skip empty forms
                    track = form.save(commit=False)
                    track.artist = artist
                    track.album = album
                    track.position = current_tracks + 1
                    current_tracks += 1

                    # Audio upload and length retrieval generated using ChatGPT
                    mp3_file = form.cleaned_data.get("track")
                    if mp3_file:
                        audio = MP3(mp3_file)
                        track.length = audio.info.length

                        mp3_file.seek(0)

                        upload_result = cloudinary.uploader.upload(
                            mp3_file,
                            resource_type="raw",  # important!
                            folder=(
                                f"melodia/artist_audios/"
                                f"{slugify(artist.name)}/{slugify(album.name)}"
                            ),
                        )
                        # Save the Cloudinary URL in the model
                        track.track = upload_result["secure_url"]

                    track.save()
                    savedTracks += 1

            if savedTracks > 0:
                messages.success(
                    request, f"Track(s) created successfully for {album.name}"
                )
                return redirect("artist", name=artist.name, pk=artist.pk)
            else:
                messages.success(request, f"No Track(s) created for {album.name}")
                return redirect("artist", name=artist.name, pk=artist.pk)
        else:
            messages.success(request, ("There were some errors with some fields"))
    else:
        formset = TrackFormSet(queryset=Track.objects.none())

    return render(
        request,
        "create_track.html",
        {"formset": formset, "album": album, "artist": artist},
    )
