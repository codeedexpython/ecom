# serializers.py
from rest_framework import serializers
from .models import Product, Category, Tag, ProductSize



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['id', 'size', 'inventory']

class ProductSerializer(serializers.ModelSerializer):
    sizes = ProductSizeSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"

    def create(self, validated_data):
        sizes_data = validated_data.pop('sizes')
        tags_data = validated_data.pop('tags', [])  # Get tags data if provided, or set to empty list
        product = Product.objects.create(**validated_data)
        for size_data in sizes_data:
            ProductSize.objects.create(product=product, **size_data)
        product.tags.set(tags_data)
        return product