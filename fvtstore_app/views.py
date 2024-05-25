from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from .models import *
from collections import defaultdict
from .serializers import *

# Create your views here.
@api_view(['GET'])
def view_fvtstore(request):
    stores = FavoriteStore.objects.all()
    serializer = FavoriteStoreSerializer(stores, many=True)
    total_rates = defaultdict(int)
    for store in stores:
        total_rates[store.store_id] += store.rate
    for store_data in serializer.data:
        store_id = store_data['store_id']
        store_data['total_rate'] = total_rates.get(store_id, 0)
    return Response(serializer.data)

@api_view(['GET'])
def get_view_store(request,store_id):
    store=FavoriteStore.objects.get(store_id=store_id)
    serializer=FavoriteStoreSerializer(store,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def add_store(request):
    serializer=FavoriteStoreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['PUT'])
def update_store(request,store_id):
    store=FavoriteStore.objects.get(store_id=store_id)
    serializer=FavoriteStoreSerializer(instance=store ,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
@api_view(['GET'])
def delete_store(request,store_id):
    store=FavoriteStore.objects.get(store_id=store_id)
    store.delete()
    return Response("deleted successfully")
