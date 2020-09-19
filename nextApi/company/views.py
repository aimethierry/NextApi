from django.shortcuts import render
from .models import Company
from .serializers import companySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import HttpResponse
import urllib.parse as urlparse
from urllib.parse import parse_qs


from rest_framework import viewsets


from time import sleep
import requests
import uuid

headers = {'token': 'OINjoOhop()*42CS%EWCSf@4r54%vfds!#gd^'}  


def test(request):
    # print("i have to start making the payment in post paid ")
    # global status_check
    # my_url = 'http://akokanya.com/mtn-pay/'
    # print("total price to pay is ")
    # print("code unique code is " )
    # request_api = requests.post(url=my_url, data=({'amount':(int)(100), 'code': (int)(2018134),
    # 'phone': str("0783628174"), "company_name":"baza" }),headers=headers, verify=False)

        
    # url_transaction_id = request_api.json()['transactionid']
    # # print()
    # transaction_id = int(url_transaction_id)
    # print("start paying with transaction id ", transaction_id)

    # url = 'http://akokanya.com/api/mtn-integration/' + str(transaction_id)
    # response = requests.get(url,  headers=headers, verify=False)
    # response_status = response.json()[0]['payment_status']
    # print((response_status))
    # print("id is ", str(transaction_id))
    # # SUCCESSFUL PENDING
    # print("after the delay",(response_status))
    # if(response_status == "SUCCESSFUL"):
    #     print("am post paid paying")

    # prepaid purchase 
    company_name =  "ThiPo",
    user_name =  "POS1",
    password =  "123456",
    password_vend =  "123456",
    meter_number =  str("47500137717") 
    is_vend_by_unit =  "true",
    amount = str(5)

    my_url_device = 'https://prepayment.calinhost.com/api/POS_Purchase'
    request_api_device = requests.post(url=my_url_device, 
        data=({"company_name": company_name, 
            "user_name":user_name, 
            "password" : password, 
            "password_vend":password_vend,
            "meter_number": meter_number,
            "is_vend_by_unit": is_vend_by_unit, 
            "amount":amount}),verify=False)
        # return "device_code"
    response_status = request_api_device.json()
    print(response_status)
    return HttpResponse("dev")




class CompanyView(APIView):
    '''
    this function is for creating a client 
    '''
    def get(self, request, format=None):
        
        snippets = Company.objects.all()
        serializer = companySerializer(snippets, many=True)
        return Response(serializer.data)
    

    def post(self, request, format=None):
        serializer = companySerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            country = serializer.validated_data['country']
            city = serializer.validated_data['city']
            pbox = serializer.validated_data['pbox']
            description = serializer.validated_data['description']
            # print(name, country, city, pbox, description)
            save = Company.objects.create(name=name, country=country,city=city, pbox=pbox, description=description)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
