from rest_framework import serializers
from .models import Subscription

class SubscriptionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = ['name', 'price', 'description']
    
