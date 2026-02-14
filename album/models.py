from django.db import models

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    released = models.DateField()
    length = models.IntegerField()
    rating = models.FloatField(blank=True, null=True)

    # TODO implement relation/extra fields
    # artist
    # tracks
    # manager