from django.db import models
from register.models import CustomUser
from Rider.models import Rider

# Create your models here.
class Order(models.Model):
    order_number = models.CharField(max_length=255, unique=True)
    reserved_quantity = models.IntegerField()
    amount_returned_by_customer = models.FloatField(max_length=255)
    quantity_sold = models.CharField(max_length=255)
    amount_charged = models.CharField(max_length=255)
    gift_or_discount = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    series = models.CharField(max_length=255)
    quantity_delivered = models.CharField(max_length=255)
    amount_paid = models.CharField(max_length=255)
    balance = models.FloatField(max_length=255)
    discount = models.FloatField(max_length=255)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.order_number





