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
def get_product(request,*args,**kwargs):
    products = ProductTB.objects.all()
    search_id = request.query_params.get('id',None)
    search_name = request.query_params.get('name',None)
    search_image = request.query_params.get('image',None)
    if search_id:
        product = products.filter(id=search_id)
        prod_serializer = ProductSerializer(product,many = True)
        return Response(prod_serializer.data)
    elif search_name:
        product = products.filter(name__contains=search_name)
        prod_serializer = ProductSerializer(product,many = True)
        return Response(prod_serializer.data)
    elif search_image:
        product = products.filter(image=search_image)
        prod_serializer = ProductSerializer(product,many = True)

    prods_serializer = ProductSerializer(products,many = True)
    return Response(prods_serializer.data)



@api_view(['GET'])
def get_category(request):
    categories = CategoryTB.objects.all()
    search_id = request.query_params.get('id',None)
    search_name = request.query_params.get('name',None)
    if search_id:
        category = categories.filter(id=search_id)
        categ_serializer = CategorySerializer(category,many = True)
        return Response(categ_serializer.data)
    elif search_name:
        category = categories.filter(name__contains=search_name)
        categ_serializer = ProductSerializer(category,many = True)
        return Response(categ_serializer.data)
    categ_serializer = CategorySerializer(categories,many = True)
    return Response(categ_serializer.data)

@api_view(['POST'])
def create_category(request):
    serializer = CategorySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status = status.HTTP_201_CREATED)
    return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
