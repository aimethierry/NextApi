from django.shortcuts import render

from .serializers import CompanyAccountSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import HttpResponse
import urllib.parse as urlparse
from urllib.parse import parse_qs
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import CompanyAccount

class CompanyAccountView(APIView):
    '''
    this function is for creating a client 
    '''
    def get(self, request, format=None):
        
        snippets = CompanyAccount.objects.all()
        serializer = CompanyAccountSerializer(snippets, many=True)
        return Response(serializer.data)
    

    def post(self, request, format=None):
        serializer = CompanyAccountSerializer(data=request.data)
        if serializer.is_valid():
            company =  serializer.validated_data['company']
            usesrname =   serializer.validated_data['usesrname']
            email =  serializer.validated_data['email']
            passwd =  serializer.validated_data['password']
            print(company, usesrname, email, passwd)

            all_usr = User.objects.all()
            save = False

            for us in all_usr:
                if(us.username == usesrname):
                    save = True
                    
            if(save == False):
                new_user = CompanyAccount.objects.create(company=company, usesrname=usesrname,email=email,companyName="c")
                createdUser = User.objects.create_user(usesrname, email, passwd)
                save = False
                print("saved well")
                
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

