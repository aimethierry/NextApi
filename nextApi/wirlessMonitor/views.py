from django.shortcuts import render
from .serializers import internetMonitorAccountSerializer, UserSerializer, api
from wirlessMonitor.serializers import internetMonitorAccountSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import HttpResponse
import urllib.parse as urlparse
from urllib.parse import parse_qs
from rest_framework import viewsets
from .models import internetMonitor, vpnApi 

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate as auth
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from user.models import CompanyAccount
from rest_framework.decorators import api_view
import requests
from user.models import CompanyAccount
from employee.models import employeeAccount
from .models import internetMonitor
from subprocess import call

# import urllib2
import urllib.request
from urllib.request import urlopen
import os
from os import path
from paramiko import SSHClient
from scp import SCPClient
import paramiko
from scp import SCPClient




@api_view(['GET'])
def currentUser(request):
    user = request.user
    return Response({'username': user.username})



class loginCompany(APIView):
    '''
    this function is for creating a client 
    '''
    def post(self, request, format=None):
        cridentials = request.data
        username = cridentials.get('username')
        psswd = cridentials.get('password')
        all_company  = CompanyAccount.objects.all()
        access = ""
        refresh = ""
        login = False
        print("cridentials", username, psswd)
        data = { "username": username, "password":psswd}
        for com in all_company:
            if(com.companyName == "c" and com.usesrname == username):
                login = True
               
        if(login == True):
            red = requests.post('http://127.0.0.1:8000/monitor/api/token/', json={"username": username, "password":psswd})
            access = (red.json()['access'])
            refresh = (red.json()['refresh'])
            login = False
            return Response({"access":access, "refresh":refresh})
        return Response({"error":"failed to login as company "})
        


class loginEmployee(APIView):
    '''
    this function is for creating a client 
    '''
    def post(self, request, format=None):
        cridentials = request.data
        username = cridentials.get('username')
        psswd = cridentials.get('password')

        all_employee  = employeeAccount.objects.all()
        access = ""
        refresh = ""
        login = False
        data = { "username": username, "password":psswd}

        for e in all_employee:
            if(e.companyNameRole == "e" and  e.username == username):
                login = True
        
        if(login == True):
            red = requests.post('http://127.0.0.1:8000/monitor/api/token/', json={"username": username, "password":psswd})
            access = (red.json()['access'])
            refresh = (red.json()['refresh'])
            login = False
            return Response({"access":access, "refresh":refresh})
        return Response({"error":"failed to login as employee"})


class fileView(APIView):
    def get(self, request, format=None):
        return Response({"file": "file"})
    
    def post(self, request, format=None):
        return Response({"file": "file"})

    
def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client


# this is the view for the vpn and authentication to the api 
# @permission_classes((IsAuthenticated,))
class openvpnView(APIView):
    '''
    this function is for creating a client 
    '''
    def get(self, request, format=None):
        return Response({"hello":"world"})
       
    def post(self, request, format=None):
        # write the text 
        data = request.data
        filename = data.get('name')
        username = data.get('username')
        password = data.get('password')
        print(filename,username,password)


        file_path = path.relpath(str("media/" + filename))
        f = open(file_path,"w+")
        f.write(username)
        f.write("\n")
        f.write(password)
        f.close()

        save = vpnApi.objects.create(name="newtiti.txt", username=username,password=password)
        print(save)

        return Response({"done":"well"})


class wifiControl(APIView):
    '''
    this function is for creating a client 
    '''
    def get(self, request, format=None):
        return Response({"hello":"world"})
       
    def post(self, request, format=None):
        status = str(False)
        model = internetMonitor.objects.all()
        wifi_ssid = request.data.get('name')

        print(wifi_ssid)

        for wifi in model:
            if (wifi.name == wifi_ssid):
                status = str(True)
        return Response({"status ":status})



  











     