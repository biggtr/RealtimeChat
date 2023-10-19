from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from .models import ChatRoom, Message
from .forms import CreateChatRoom

# Create your views here.


def HomePageView(request):
    return render(request, "home.html")


def ChatListView(request):
    chat_rooms = get_list_or_404(ChatRoom)

    return render(request, "chat-list.html", context={"chat_rooms": chat_rooms})


def ChatDetailView(request, chat_pk):
    chat = get_object_or_404(ChatRoom, pk=chat_pk)

    return render(request, "chat-detail.html", context={"chat": chat})


def CreateChatView(request):
    form = CreateChatRoom(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("chat-list")
    else:
        form = CreateChatRoom()

    return render(request, "chat-create.html", context={"form": form})
