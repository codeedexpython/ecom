from django.shortcuts import render
from razorpay import Customer
from rest_framework.views import APIView
from rest_framework.response import Response
from customers.serializers import CustomerProfileSerializer
from rest_framework import viewsets
from .models import Product, ProductSize, RefundOrder
from .serializers import ProductSerializer, ProductSizeSerializer, RefundOrderSerializer
# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductSizeViewSet(viewsets.ModelViewSet):
    queryset = ProductSize.objects.all()
    serializer_class = ProductSizeSerializer
    
class CustomerRefundProductDetailsAPIView(APIView):
    def get(self, request, customer_id):
        refund_orders = RefundOrder.objects.filter(customer_id=customer_id)
        serialized_data = []
        for refund_order in refund_orders:
            customer_serializer=CustomerProfileSerializer(refund_order.customer)
            product_serializer = ProductSerializer(refund_order.product)
            customer_data=customer_serializer.data
            product_data = product_serializer.data
            total = refund_order.quantity * refund_order.product.sale_price
            product_data['total'] = total
            serialized_data.append({
                'order': refund_order.order,
                'customer': customer_data,
                'product': product_data,
                'quantity': refund_order.quantity
            })

        return Response(serialized_data)
    
    def post(self, request, customer_id):
        serializer = RefundOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(customer_id=customer_id)
            return Response(serializer.data)
        return Response(serializer.errors)