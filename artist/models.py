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
        manager = self.manager.username if self.manager else "Orphaned"
        return manager + ": " + self.name + "/" + self.bornOn.isoformat()
    
    # Method partially genearated with ChatGPT
    def getSocials(self):
        if not self.socials:
            return []

        socials = []
        for url in self.socials.splitlines():
            url = url.strip()
            if not url:
                continue
            name = url.rstrip("/").split("/")[-1]  # last part of the URL
            socials.append({
                "url": url,
                "name": name
            })

        return socials

