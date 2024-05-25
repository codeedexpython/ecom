from rest_framework import serializers
from fvtstore_app.models import *

class FavoriteStoreSerializer(serializers.ModelSerializer):
     total_rate = serializers.IntegerField(read_only=True)  # Add this field
     class Meta:
        model = FavoriteStore
        fields = ['store_id', 'store_image', 'store_name', 'rate', 'total_rate']
