from django.shortcuts import render
from .models import Reservations
from .serializers import ReservationsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import HttpResponse
import urllib.parse as urlparse
from urllib.parse import parse_qs
from rest_framework import viewsets


class ReservationsView(APIView):
    '''
    this function is for creating a client 
    '''
    def get(self, request, format=None):
        
        snippets = Reservations.objects.all()
        serializer = ReservationsSerializer(snippets, many=True)
        return Response(serializer.data)
    

    def post(self, request, format=None):
        serializer = ReservationsSerializer(data=request.data)
        if serializer.is_valid():
            company = serializer.validated_data['company']
            subscription = serializer.validated_data['subscription']
            starDate = serializer.validated_data['starDate']
            endDate = serializer.validated_data['endDate']
            print(company, subscription)
            save = Reservations.objects.create(company=company, subscription=subscription,starDate=starDate, endDate=endDate)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
