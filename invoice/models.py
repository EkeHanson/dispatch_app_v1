from django.db import models

# Create your models here.

class Invoice(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    series = models.CharField(max_length=255)

    quantity_delivered = models.IntegerField()
    amount_paid = models.FloatField(max_length=255)
    balance = models.FloatField(max_length=255)
    discount = models.FloatField(max_length=255)
    # Choices for the confirmed field
    CONFIRMED = 'confirmed'
    PENDING = 'pending'
    CONFIRMATION_CHOICES = [
        (CONFIRMED, 'Confirmed'),
        (PENDING, 'Pending'),
    ]
    
    confirmed = models.CharField(
        max_length=20,
        choices=CONFIRMATION_CHOICES,
        default=PENDING  # Default value is set to 'Pending'
    )
   