from rest_framework import serializers
from .models import employeeAccount

class employeeAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = employeeAccount
        fields = ['company', 'usesrname', 'email', 'password']
    