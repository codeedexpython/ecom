from django.db import models
from order_app.models import Order

class Transaction(models.Model):
    STATUS_CHOICES = (
        ('SUCCESS', 'Success'),
        ('FAILURE', 'Failure'),
        ('PENDING', 'Pending')
    )
    payment_id = models.CharField(max_length=100,verbose_name="Payment_ID")
    order_payment = models.OneToOneField(Order,on_delete=models.CASCADE,related_name="payment",null=True)
    order_id = models.CharField(max_length=100,verbose_name="Order_ID")
    signature = models.CharField(max_length=100,verbose_name="Signature")
    amount = models.IntegerField(verbose_name="Amount")
    datetime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES,default='PENDING')

    def __str__(self):
        return str(self.payment_id)