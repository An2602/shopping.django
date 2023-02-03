from http.client import HTTPResponse
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from django.contrib import messages
from .serializers import ProductSerializer


@api_view(['GET', 'POST'])
def products(request):
    """
    List all products or create a new product.
    """
    if request.method == 'GET': #list
        products = Product.objects.filter(archive = 'False')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': #create new
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def cartitem(request):
    """
    List all products or create a new product.
    """
    if request.method == 'GET': 
        products = Product.objects.filter(archive = 'False')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': 
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['DELETE', 'PUT', 'GET'])
# def product(request, pk):
#     if request.method == 'DELETE':
#         product = Product.objects.get(id=pk)
#         product.archive = True
#         product.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     if request.method == 'GET':
#         product = Product.objects.get(id=pk) 
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         product = Product.objects.get(id=pk)
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

