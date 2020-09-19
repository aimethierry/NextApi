from rest_framework import serializers
from .models import internetMonitor
from django.contrib.auth.models import User
from .models import vpnApi
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class internetMonitorAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = internetMonitor
        fields = ['employee', 'name']

class api(serializers.ModelSerializer):
    class Meta:
        model = vpnApi
        fields = ['name', 'username', 'password']
    