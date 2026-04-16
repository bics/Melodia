from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class MelodiaUser(AbstractUser):
    isManager = models.BooleanField(default=False)
    stripeUserId = models.CharField(blank=True, null=True)
    stripeAccessToken = models.CharField(blank=True, null=True)
