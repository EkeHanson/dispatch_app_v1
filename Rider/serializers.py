from rest_framework import serializers
from .models import Rider

class RiderCreateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    address = serializers.CharField()
    phone = serializers.CharField()

    class Meta:
        model = Rider
        fields = '__all__'
