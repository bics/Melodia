from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Artist
from album.models import Album
from .forms import AlbumCreationForm, EditArtistForm

# Create your views here.
def artist(request, name, pk):
    artist = Artist.objects.get(pk=pk)
    albums = Album.objects.filter(artist=artist)
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