from django.db import models

class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=1000)
    color=models.CharField(max_length=500)
    size=models.CharField(max_length=500)
    price=models.IntegerField()
    quantity=models.IntegerField()

    class Meta:
        db_table="product_table"

class Customer(models.Model):
    customer_id=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=500)
    email=models.CharField(max_length=500)
    address=models.CharField(max_length=1500)
    phone_no=models.CharField(max_length=500)

    class Meta:
        db_table="customer_table"

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    total=models.IntegerField()
    payment_status=models.CharField(max_length=500)
    fulfilment_status=models.CharField(max_length=500)
    delivery_type=models.CharField(max_length=500)
    date=models.DateTimeField(auto_now=True,null=True)

    class Meta:
        db_table="order_table"

