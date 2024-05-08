# models.py
from django.db import models

class Category(models.Model):
    
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Tag(models.Model):
    
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class ProductSize(models.Model):
    
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='sizes')
    size = models.CharField(max_length=10)
    inventory = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product.name

class Product(models.Model):
    name = models.CharField(max_length=255,unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    gender = models.CharField(max_length=10, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unisex')
    ])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    color = models.CharField(max_length=50)
    fabric_type = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='products_images/',blank=True, null=True)
    def __str__(self):
        return self.name