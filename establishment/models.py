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

    order_number = models.CharField(max_length=255, unique=True)
    series = models.CharField(max_length=255)

    
    reserved_quantity = models.IntegerField()
    amount_returned_by_customer = models.FloatField(max_length=255)
    quantity_sold = models.CharField(max_length=255)
    amount_charged = models.CharField(max_length=255)
    gift_or_discount = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    
    quantity_delivered = models.CharField(max_length=255)
    amount_paid = models.CharField(max_length=255)
    balance = models.FloatField(max_length=255)
    discount = models.FloatField(max_length=255)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name