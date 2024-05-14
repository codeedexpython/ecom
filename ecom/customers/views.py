from django.shortcuts import render
from rest_framework import viewsets
from oder.models import Order
from .models import CustomerModel
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomerRegisterSerializer
from django.db.models import Sum

# Create your views here.

class CustomerModelViewSet(viewsets.ModelViewSet):
    queryset = CustomerModel.objects.all()
    serializer_class = CustomerRegisterSerializer


class CustomersSummaryAPIView(APIView):
    def get(self, request):
        customers = CustomerModel.objects.all()
        data = []
        for customer in customers:
            profile = customer.profile
            total_spent = Order.objects.filter(customer=profile).aggregate(total_spent=Sum('total'))['total_spent'] or 0
            total_orders = Order.objects.filter(customer=profile).count()
            last_order = Order.objects.filter(customer=profile).order_by('-date').first()
            data.append({
                'first_name': customer.first_name,
                'last_name': customer.last_name,
                'email': customer.email,
                'city': profile.city,
                'profile_pic': profile.profile_pic.url if profile.profile_pic else None,
                'total_spent': total_spent,
                'total_orders': total_orders,
                'last_order': last_order,
                'last_seen': customer.last_seen
            })
        return Response(data)
