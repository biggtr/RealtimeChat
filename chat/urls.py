from django.urls import path
from .views import ChatList, ChatDetail, HomePage

urlpatterns = [
    path("", HomePage, name="home"),
    path("chats/", ChatList, name="chat-list"),
    path("chats/<int:chat_pk>/", ChatDetail, name="chat-detail"),
]
