from rest_framework import serializers
from .models import Transaction
        
class CreateOrderSerializers(serializers.Serializer):
    amount = serializers.IntegerField()
    currency = serializers.CharField()

class TranscationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["payment_id","order_id","signature","amount","order_payment"]
