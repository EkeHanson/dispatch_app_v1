from rest_framework import serializers
from Rider.models import Rider
from .models import Establishment

class EstablishmentSerializer(serializers.ModelSerializer):
    rider = serializers.PrimaryKeyRelatedField(queryset=Rider.objects.all())
    rider_address = serializers.CharField(source='rider.address', read_only=True)
    rider_Phone_number = serializers.CharField(source='rider.phone', read_only=True)

    class Meta:
        model = Establishment
        fields = '__all__'
        # fields = ['name', 'contact_person','rider', 'rider_address', 'phone_number','rider_Phone_number',
        #           'order_number', 'reserved_quantity', 'amount_returned_by_customer', 'quantity_sold',
        #           'amount_charged', 'gift_or_discount']