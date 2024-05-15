from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
from order_app.models import Order
from .serializers import CreateOrderSerializers, TranscationSerializer
from razorpay_backend.razorpay_conf.main import  RazorpayClient

# Create your views here.

rz_client = RazorpayClient()

class CreateOderAPIview(APIView):
    def post (self,request):
        serializer = CreateOrderSerializers(data=request.data)
        if serializer.is_valid():
            order_response = rz_client.create_order(
                amount=serializer.validated_data.get("amount"),
                currency='INR',
            )
            response ={
                "status_code":status.HTTP_201_CREATED
                ,'mwssage':"order created"
                ,"data":order_response
            }
            return Response(response,status=status.HTTP_201_CREATED)
        else:
            response ={
                "status_code":status.HTTP_400_BAD_REQUEST
                ,'mwssage':"Bad Request"
                ,"error":serializer.errors
            }
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
        
class TransactionAPIView(APIView):
    def post(self,request):
        serializer = TranscationSerializer(data=request.data)
        if serializer.is_valid():
            result = rz_client.verify_payment(razorpay_order_id=serializer.validated_data.get("order_id"),
                                     razorpay_payment_id=serializer.validated_data.get("payment_id"),
                                     razorpay_signature=serializer.validated_data.get("signature"))
            if result:
                serializer.save()
                id = request.data.get('order_payment')
                order = Order.objects.get(id=id)
                order.payment_status = 'PAID'
                order.save()
                payment_id = request.data.get('payment_id')
                payment_status = Transaction.objects.get(payment_id=payment_id)
                payment_status.status = "SUCCESS"
                payment_status.save()

                response ={
                    'message':"successfull transaction"
                    ,"data":serializer.data
                }
                return Response(response,status=status.HTTP_201_CREATED)
            else:
                payment_id = request.data.get('payment_id')
                payment_status = Transaction.objects.get(payment_id=payment_id)
                payment_status.status = "FAILURE"
                payment_status.save()
                response ={
                    'message':"Signature mismatch"
                }
                return Response(response,status=status.HTTP_400_BAD_REQUEST)
        else:
            response ={
                    'message':"Bad Request"
                    ,"error":serializer.errors
                }
            return Response(response,status=status.HTTP_400_BAD_REQUEST)