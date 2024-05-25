from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
def view_order(request):
    order=Order.objects.all()
    serializer=OrderSerializer(order,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_view_order(request,order_id):
    order=Order.objects.get(order_id=order_id)
    serializer=OrderSerializer(order,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def add_order(request):
    serializer=OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
@api_view(['PUT'])
def update_order(request,order_id):
    order=Order.objects.get(order_id=order_id)
    serializer=OrderSerializer(instance=order ,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
def delete_order(request,order_id):
    order=Order.objects.get(order_id=order_id)
    order.delete()
    return Response("deleted successfully")

@api_view(['GET'])
def total_order(request):
    orders = Order.objects.all()
    total_orders = orders.count()
    serializer = OrderSerializer(orders, many=True)
    response_data = {
        'total_orders': total_orders,
        'orders': serializer.data
    }
    return Response(response_data)

@api_view(['GET'])
def total_pending_order(request):
    pending_orders = Order.objects.filter(payment_status='pending')
    serializer = OrderSerializer(pending_orders, many=True)
    pending_orders_count = pending_orders.count()
    return Response({
        'pending_orders_count': pending_orders_count,
        'pending_orders': serializer.data
    })

@api_view(['GET'])
def total_completed_order(request):
    completed_orders = Order.objects.filter(payment_status='completed')
    serializer = OrderSerializer(completed_orders, many=True)
    completed_orders_count = completed_orders.count()
    return Response({
        'completed_orders_count': completed_orders_count,
        'completed_orders': serializer.data
    })

@api_view(['GET'])
def total_failed_order(request):
    failed_orders = Order.objects.filter(payment_status='failed')
    serializer = OrderSerializer(failed_orders, many=True)
    failed_orders_count = failed_orders.count()
    return Response({
        'failed_orders_count': failed_orders_count,
        'failed_orders': serializer.data
    })

@api_view(['GET'])
def total_unfulfilled_order(request):
    unfulfilled_orders = Order.objects.filter(fulfilment_status='unfulfilled')
    serializer = OrderSerializer(unfulfilled_orders, many=True)
    unfulfilled_orders_count = unfulfilled_orders.count()
    return Response({
        'unfulfilled_orders_count': unfulfilled_orders_count,
        'unfulfilled_orders': serializer.data
    })


@api_view(['GET'])
def search_order(request):
    order_id = request.GET.get('order_id')
    customer = request.GET.get('customer')
    search_content = {}
    if order_id:
        search_content['order_id'] = order_id
    if customer:
        search_content['customer'] = customer
    orders = Order.objects.all()
    if order_id:
        orders = orders.filter(order_id=order_id)
    if customer:
        orders = orders.filter(customer__icontains=customer)
    serializer = OrderSerializer(orders, many=True)
    return Response({
        'search_content': search_content,
        'orders': serializer.data
    })


@api_view(['GET'])
def fetch_customer_orders(request, customer_id):
    orders = Order.objects.filter(customer_id=customer_id).select_related('product_id', 'customer_id')
    order_data = []
    for order in orders:
        product_serializer = ProductSerializer(order.product_id)
        order_data.append({
            'order_id': order.order_id,
            'product': product_serializer.data,
            'total': order.product_id.price * order.product_id.quantity
        })
    total_price_all_products = sum(order['total'] for order in order_data)
    customer = orders.first().customer_id
    customer_serializer = CustomerSerializer(customer)
    response_data = {
        'orders': order_data,
        'total_price_all_products': total_price_all_products,
        'customer': customer_serializer.data,
    }
    return Response(response_data)

