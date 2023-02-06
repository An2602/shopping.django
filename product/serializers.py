from rest_framework import serializers
from .models import Product,CartItem
from django.db import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '_all_'


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = '_all_'

class CartSerializertwo(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '_all_'