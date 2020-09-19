from .models import Subscription
from .serializers import SubscriptionTypeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import HttpResponse
import urllib.parse as urlparse
from urllib.parse import parse_qs


from rest_framework import viewsets


class SubscriptionType(APIView):
    '''
    this function is for creating a client 
    '''
    def get(self, request, format=None):
        
        snippets = Subscription.objects.all()
        serializer = SubscriptionTypeSerializer(snippets, many=True)
        return Response(serializer.data)
    

    def post(self, request, format=None):
        serializer = SubscriptionTypeSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            price = serializer.validated_data['price']
            description = serializer.validated_data['description']
            save = Subscription.objects.create(name=name, price=price,description=description)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
