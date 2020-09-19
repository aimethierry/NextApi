from django.shortcuts import render
from .models import Invitation
from .serializers import InvitationSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import HttpResponse
import urllib.parse as urlparse
from urllib.parse import parse_qs
# from rest_framework import viewsets
import uuid
from smtplib import SMTPException
from django.core.mail import EmailMessage
from django.core.exceptions import ValidationError
from validate_email import validate_email

# str(uuid.uuid4().fields[-1])[:5]


class InvitationView(APIView):
    '''
    this function is for creating a client 
    '''
    def get(self, request, format=None):
        
        snippets = Invitation.objects.all()
        serializer = InvitationSerializer(snippets, many=True)
        
        # uni = str(uuid.uuid4().fields[-1])[:8]
        # print("unique numbe is", uni)
        # print(user)
        # email = EmailMessage('Subject', 'http://127.0.0.1:8000/invitation/createInvitation/', to=['aime.thierry97@gmail.com'])
        # email.send()
        return Response(serializer.data)
    

    def post(self, request, format=None):
        serializer = InvitationSerializer(data=request.data)
        if serializer.is_valid():
            employeeEmail = serializer.validated_data['employeeEmail']
            email = EmailMessage('Subject', 'http://127.0.0.1:8000/invitation/createInvitation/', to=[employeeEmail])
            user = request.user
            is_valid = validate_email(employeeEmail)
            if is_valid == False:
                return Response({"response": "invalid email"})
            else:
                print("good email")
                email.send()
                save = Invitation.objects.create(employeeEmail=employeeEmail, sender_username=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)