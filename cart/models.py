from django.db import models
from product.models import Product

# Create your models here.

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
    quantity = models.SmallIntegerField(default=0)
    incart = models.BooleanField(default=False)
