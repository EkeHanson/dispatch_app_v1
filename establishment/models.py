from django.db import models
from Rider.models import Rider

# Create your models here.

class Establishment(models.Model):
    name = models.CharField(max_length=255, unique=True)
    contact_person = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    rider = models.ForeignKey(Rider, on_delete=models.SET_NULL, null=True)
    rider_address = models.CharField(max_length=255) # (which would populate after the name has been chosen)
    rider_Phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name