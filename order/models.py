from django.db import models
from register.models import CustomUser
from establishment.models import Establishment

# Create your models here.
class Order(models.Model):
    order_number = models.CharField(max_length=255, unique=True)
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)
    
    reserved_quantity = models.IntegerField()

    amount_returned_by_customer = models.FloatField(max_length=255)
    quantity_sold = models.CharField(max_length=255)
    amount_charged = models.FloatField(max_length=255)
    gift_or_discount = models.FloatField(max_length=255)

    created = models.DateTimeField(auto_now_add=True)
    series = models.CharField(max_length=255, null=True)

    quantity_delivered = models.IntegerField(null=True)
    amount_paid = models.FloatField(max_length=255, null=True)
    balance = models.FloatField(max_length=255, null=True)
    discount = models.FloatField(max_length=255, null=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} for {self.establishment.name}"





