from rest_framework import serializers
from .models import Cart
from product.serializers import ProductSerializer

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Cart
        fields = '__all__'