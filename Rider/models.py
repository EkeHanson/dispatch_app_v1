from django.db import models

# Create your models here.
class Rider(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)  
    phone = models.CharField(max_length=255,unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    