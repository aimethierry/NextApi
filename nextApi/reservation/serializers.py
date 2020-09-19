from rest_framework import serializers
from .models import Reservations

class ReservationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservations
        fields = ['company', 'subscription', 'starDate', 'endDate']
    
