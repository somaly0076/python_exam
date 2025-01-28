from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ProductTB, CategoryTB
from .serializer import ProductSerializer, CategorySerializer
# Create your views here.

@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status = status.HTTP_201_CREATED)
    return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_product(request):
    products = ProductTB.objects.all()
    prod_serializer = ProductSerializer(products,many = True)
    return Response(prod_serializer.data)


@api_view(['GET'])
def get_category(request):
    categories = CategoryTB.objects.all()
    categ_serializer = CategorySerializer(categories,many = True)
    return Response(categ_serializer.data)

@api_view(['POST'])
def create_category(request):
    serializer = CategorySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status = status.HTTP_201_CREATED)
    return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
