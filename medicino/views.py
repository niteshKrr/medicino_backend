from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from medicino.models import Cure
from medicino.serializers import DepartmentSerializer
from rest_framework.decorators import api_view


@csrf_exempt
def customer_list(request):
    if request.method == 'GET':
        customers = Cure.objects.all()
        customers_serializer = DepartmentSerializer(customers, many=True)
        return JsonResponse(customers_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        customer_data = JSONParser().parse(request)
        customer_serializer = DepartmentSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save() 
            return JsonResponse(customer_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt 
def customer_detail(request, pk):
    try: 
        customer = Cure.objects.get(pk=pk) 
    except Cure.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        customer_serializer = DepartmentSerializer(customer) 
        return JsonResponse(customer_serializer.data) 
 
    elif request.method == 'PUT': 
        customer_data = JSONParser().parse(request) 
        customer_serializer = DepartmentSerializer(customer, data=customer_data) 
        if customer_serializer.is_valid(): 
            customer_serializer.save() 
            return JsonResponse(customer_serializer.data) 
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        customer.delete() 
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)