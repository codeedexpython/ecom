from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, ProductSize
from .serializers import ProductSerializer, ProductSizeSerializer
# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductSizeViewSet(viewsets.ModelViewSet):
    queryset = ProductSize.objects.all()
    serializer_class = ProductSizeSerializer