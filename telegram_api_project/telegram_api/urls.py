from django.urls import path
from .views import UserProfileList, MessageList, MessageDetail

urlpatterns = [
    path('users/', UserProfileList.as_view(), name='userprofile-list'),
    path('messages/', MessageList.as_view(), name='message-list'),
    path('messages/<int:pk>/', MessageDetail.as_view(), name='message-detail'),
]