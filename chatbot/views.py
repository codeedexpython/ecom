from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Message
from .serializers import MessageSerializer
from django.utils import timezone

@api_view(['POST'])
def message_view(request, user_id):
    user_message = request.data.get('user_message')
    if not user_message:
        return Response({'error': 'User message is required'}, status=status.HTTP_400_BAD_REQUEST)

    bot_response = request.data.get('bot_response', '')
    timestamp = timezone.now()
    message = Message(user_id=user_id, user_message=user_message, bot_response=bot_response, timestamp=timestamp)
    message.save()
    chat_history = Message.objects.filter(user_id=user_id).order_by('timestamp')
    serializer = MessageSerializer(chat_history, many=True)

    return Response(serializer.data, status=status.HTTP_201_CREATED)
