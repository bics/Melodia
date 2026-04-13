from django.db import models
from artist.models import Artist
from members.models import MelodiaUser


# Create your models here.
class Donation(models.Model):
    amount = models.IntegerField()
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, blank=True)
    artist_name = models.CharField(max_length=255)

    manager_name = models.CharField(max_length=255)
    manager_stripe_id = models.CharField(max_length=255)

    donator = models.ForeignKey(
        MelodiaUser, on_delete=models.SET_NULL, null=True, blank=True
    )
    donator_email = models.CharField(max_length=255)

    stripe_session_id = models.CharField(max_length=255, unique=True)
    is_paid = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Donation for {self.artist_name}"
