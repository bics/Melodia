from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    bornOn = models.DateField()
    socials = models.TextField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)

    # TODO implement relation/extra fields
    # albums
    # tracks
    # manager
    
