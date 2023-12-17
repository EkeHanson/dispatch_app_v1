from django.db import models
from order.models import Order

class Invoice(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    series = models.CharField(max_length=255, null=True)

    quantity_delivered = models.IntegerField(null=True)
    amount_paid = models.FloatField(max_length=255, null=True)
    balance = models.FloatField(max_length=255, null=True)
    discount = models.FloatField(max_length=255, null=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} for {self.establishment.name}"
    # Choices for the confirmed field
    CONFIRMED = 'Approved'
    PENDING = 'Pending'
    CONFIRMATION_CHOICES = [
        (CONFIRMED, 'Approved'),
        (PENDING, 'Pending'),
    ]
    
    confirmed = models.CharField(
        max_length=20,
        choices=CONFIRMATION_CHOICES,
        default=PENDING  # Default value is set to 'Pending'
    )
   