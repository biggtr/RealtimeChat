from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [path("chats/<str:room_title>/", ChatConsumer.as_asgi())]
