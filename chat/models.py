from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class ChatRoom(models.Model):
    title = models.CharField(max_length=50)
    users = models.ManyToManyField(get_user_model())

    def __str__(self) -> str:
        return self.title


class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    chat_room = models.ForeignKey(
        ChatRoom, on_delete=models.CASCADE, related_name="messages"
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text
