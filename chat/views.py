from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import ChatRoom, Message

# Create your views here.


def HomePage(request):
    return render(request, "home.html")


def ChatList(request):
    chat_rooms = get_list_or_404(ChatRoom)

    return render(request, "chat-list.html", context={"chat_rooms": chat_rooms})


def ChatDetail(request, chat_pk):
    chat = get_object_or_404(ChatRoom, pk=chat_pk)

    return render(request, "chat-detail.html", context={"chat": chat})
