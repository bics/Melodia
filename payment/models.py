from django.db import models
from artist.models import Artist

# Create your models here.
class Donation(models.Model):
    amount = models.IntegerField()
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, blank=True)
    artist_name = models.CharField()
    stripe_session_id = models.CharField()
    is_paid = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)


