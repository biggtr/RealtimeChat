from django.urls import path
from .views import ChatListView, ChatDetailView, HomePageView, CreateChatView

urlpatterns = [
    path("", HomePageView, name="home"),
    path("chats/", ChatListView, name="chat-list"),
    path("chats/<str:room_title>/", ChatDetailView, name="chat-detail"),
    path("create/", CreateChatView, name="chat-create"),
]
