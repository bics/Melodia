from django.db import models
from artist.models import Artist
from django.utils.text import slugify

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    released = models.DateField()
    length = models.IntegerField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")

    def __str__(self):
        return self.name
    
    def imageFileUpload(self, filename):
        safe_name = slugify(self.artist.name)
        return f"melodia/artist_images/{safe_name}/{filename}"
    
    
    image = models.ImageField(blank=True, null=True, upload_to=imageFileUpload)

class Track(models.Model):
    name = models.CharField(max_length=255)
    position = models.IntegerField(blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True, related_name="tracks")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="tracks")
    featured_artist = models.ManyToManyField(Artist, blank=True, related_name="feat")

    def __str__(self):
        return self.name