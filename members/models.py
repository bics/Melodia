from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MelodiaUser(AbstractUser):
    isManager = models.BooleanField(default=False)
