from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CartItem, Product
from .serializers import CartSerializer, ProductSerializer, CartSerializertwo
from django.contrib import messages
# from snippets.serializers import SnippetSerializer


@api_view(['GET', 'POST'])
def products(request):
    """
    List all products, or create a new product.
    """
    if request.method == 'GET': #list products
        products = Product.objects.filter(archive = "False")
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': #create new product
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#delete products
@api_view(['DELETE', 'PUT','GET'])
def product(request,pk):
    if request.method == 'GET': #list products
        products = Product.objects.get(id=pk)
        serializer = ProductSerializer(products)
        return Response(serializer.data) 

    if request.method == 'DELETE':
        prod = Product.objects.get(id=pk)
        prod.archive=True
        prod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        prod = Product.objects.get(pk=pk)
        serializer = ProductSerializer(prod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'POST'])
def cart_list(request):
    """
    List all products, or create a new product.
    """
    if request.method == 'GET': 
        cart = CartItem.objects.all()
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': 
        serializer = CartSerializertwo(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def deletetfromcart(request,pk):
    
    if request.method == 'DELETE':
        deletedprod = CartItem.objects.filter(product_id=pk)
     
        deletedprod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def updatecart(request,pk):
    print(request.data)
    try:
        prod = CartItem.objects.get(pk=pk)
        print(prod)
    except CartItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        

      
        serializer = CartSerializertwo(prod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)