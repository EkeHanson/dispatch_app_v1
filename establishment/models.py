from django.db import models
from Rider.models import Rider

class Establishment(models.Model):
    name = models.CharField(max_length=255, unique=True)
    contact_person = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    rider = models.ForeignKey(Rider, on_delete=models.SET_NULL, null=True, blank=True)
    rider_address = models.CharField(max_length=255, null=True, blank=True)
    rider_phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.rider_id:  # If rider is not supplied
            self.rider = None  # Set rider to None
        
        if not self.rider_address:  # If rider_address is not supplied
            self.rider_address = None  # Set rider_address to None
        
        if not self.rider_phone_number:  # If rider_phone_number is not supplied
            self.rider_phone_number = None  # Set rider_phone_number to None
        
        super().save(*args, **kwargs)
