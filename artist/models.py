from django.db import models
from members.models import MelodiaUser

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True, upload_to="melodia/artist_images/")
    description = models.TextField(blank=True, null=True)
    bornOn = models.DateField()
    socials = models.TextField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    manager = models.ForeignKey(MelodiaUser, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
