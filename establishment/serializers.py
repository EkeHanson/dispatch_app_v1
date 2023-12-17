from rest_framework import serializers
from Rider.models import Rider
from .models import Establishment

class EstablishmentSerializer(serializers.ModelSerializer):
    rider = serializers.PrimaryKeyRelatedField(queryset=Rider.objects.all(), required=False)
    rider_address = serializers.CharField(source='rider.address', read_only=True,  required=False)
    rider_phone_number = serializers.CharField(source='rider.phone', read_only=True,  required=False)

    class Meta:
        model = Establishment
        fields = '__all__'
