from rest_framework import serializers
from .models import CompanyAccount

class CompanyAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyAccount
        fields = ['company', 'usesrname', 'email', 'password']
    