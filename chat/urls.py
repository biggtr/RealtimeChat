from django.urls import path
from .views import ChatListView, ChatDetailView, HomePageView, CreateChatView

urlpatterns = [
    path("", HomePageView, name="home"),
    path("chats/", ChatListView, name="chat-list"),
    path("chats/<int:chat_pk>/", ChatDetailView, name="chat-detail"),
    path("chats/create", CreateChatView, name="chat-create"),
]
