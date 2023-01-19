from http.client import HTTPResponse
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart
from django.contrib import messages
from .serializers import CartSerializer


@api_view(['GET', 'POST'])
def cart(request):
    """
    List all products in cart or create a add product.
    """
    if request.method == 'GET': #list
        products_in_cart = Cart.objects.filter(incart = 'True')
        serializer = CartSerializer(products_in_cart, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': #create new
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'PUT', 'GET'])
def cartitem(request, pk):
    if request.method == 'DELETE':
        product = Cart.objects.get(id=pk)
        product.archive = True
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        product = Cart.objects.get(id=pk) 
        serializer = CartSerializer(product)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        product = Cart.objects.get(id=pk)
        serializer = CartSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

