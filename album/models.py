from django.db import models
from artist.models import Artist
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from members.models import MelodiaUser

# Helper methods
def audioFileUpload(self, filename):
    safe_artist = slugify(self.artist.name)
    safe_album = slugify(self.album.name)
    return f"melodia/artist_audios/{safe_artist}/{safe_album}/{filename}"

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    released = models.DateField()
    length = models.FloatField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")

    def __str__(self):
        return self.name
    
    def imageFileUpload(self, filename):
        safe_artist = slugify(self.artist.name)
        return f"melodia/artist_images/{safe_artist}/{filename}"
    
    
    image = models.ImageField(blank=True, null=True, upload_to=imageFileUpload)

class Track(models.Model):
    name = models.CharField(max_length=255)    
    track = models.FileField(blank=True, null=True, upload_to=audioFileUpload, max_length=600)
    position = models.IntegerField(blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True, related_name="tracks")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="tracks")
    featured_artist = models.ManyToManyField(Artist, blank=True, related_name="feat")

    def __str__(self):
        return self.name
    
    def getTrackLength(self):
        if (self.length):
            # Proper length return generated using ChatGPT
            total_seconds = int(self.length)
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            return f"{minutes}:{seconds:02d}"
        return "0:00"
    

class Rating(models.Model):
    ratingTrack = models.ForeignKey(Track, on_delete=models.CASCADE)
    ratingUser = models.ForeignKey(MelodiaUser, on_delete=models.CASCADE)
    ratingValue = models.IntegerField()

    def getRating(self):
        return self.ratingValue
    
    def __str__(self):
        return f"{self.ratingTrack.name} rating by user, {self.ratingUser.username} is {self.ratingValue}"

