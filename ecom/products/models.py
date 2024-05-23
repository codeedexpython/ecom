from django.db import models
from customers.models import CustomerProfileModel

class Category(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Product(models.Model):
    SHIPPING_CHOICES = (
        ('seller', 'Fullfilled by Seller'),
        ('ecom', 'Fullfilled by ECOM'),
    )
    DELIVERY_OPTIONS = [
        ('worldwide', 'Worldwide Delivery'),
        ('selected_countries', 'Selected Countries'),
        ('local_delivery', 'Local Delivery'),
    ]
    title = models.CharField(max_length=250,unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    collection = models.CharField(max_length=250)
    tags = models.ManyToManyField(Tag)
    regular_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping = models.CharField(max_length=100,choices=SHIPPING_CHOICES)
    delivery = models.CharField(max_length=20, choices=DELIVERY_OPTIONS)
    selected_countries = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title
    
class ProductID(models.Model):
    PRODUCT_ID_TYPES = [
        ('ISBN', 'ISBN'),
        ('UPC', 'UPC'),
        ('EAN', 'EAN'),
        ('JAN', 'JAN'),
    ]
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='product_id')
    product_id_type = models.CharField(max_length=20, choices=PRODUCT_ID_TYPES)
    product_type_id = models.IntegerField()

    def __str__(self):
        return self.product_type_id
    
class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_size')
    size = models.CharField(max_length=10)
    color=models.CharField(max_length=10)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product.title
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.CharField(max_length=250)

class RefundOrder(models.Model):
    order= models.IntegerField()
    customer= models.ForeignKey(CustomerProfileModel,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='refund_product')
    quantity = models.IntegerField()