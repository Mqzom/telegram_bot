from rest_framework import generics, permissions
from .models import UserProfile, Message
from .serializers import UserProfileSerializer, MessageSerializer
import requests
from django.conf import settings

class MessageList(generics.ListCreateAPIView):
    # ...
    def perform_create(self, serializer):
        user_profile = UserProfile.objects.get(user=self.request.user)
        new_message = serializer.save(user=user_profile)

        # Отправка сообщения в Telegram бот
        telegram_token = user_profile.telegram_token
        message_text = new_message.text
        chat_id = '6578675433:AAHGbxnchPZ0yCN3IiPKj5m_apgGVy66f1A'  # Получите chat_id пользователя
        telegram_url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'
        payload = {'chat_id': chat_id, 'text': message_text}
        response = requests.post(telegram_url, data=payload)
class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class MessageDetail(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
