from rest_framework import serializers
from .models import Category, Vendor, Tag, Product, ProductSize, ProductImage,ProductID

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ProductIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductID
        fields = ['id', 'product_id_type','product_type_id']

class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['id', 'size','color', 'quantity']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id','image']

class ProductSerializer(serializers.ModelSerializer):
    product_id = ProductIDSerializer()
    product_size = ProductSizeSerializer(many=True)
    product_images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        product_id_data = validated_data.pop('product_id')
        product_size_data = validated_data.pop('product_size')
        product_images_data = validated_data.pop('product_images')
        tags_data = validated_data.pop('tags', [])
        
        product = Product.objects.create(**validated_data)
        ProductID.objects.create(product=product, **product_id_data)
        for product_size_item in product_size_data:
            ProductSize.objects.create(product=product, **product_size_item)
        for product_image_item in product_images_data:
            ProductImage.objects.create(product=product, **product_image_item)
        product.tags.set(tags_data)
        return product
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.delivery == 'selected_countries':
            representation['selected_countries'] = instance.selected_countries.split(',')
        return representation
    