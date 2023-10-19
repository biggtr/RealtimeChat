from django import forms
from .models import ChatRoom


class CreateChatRoom(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ["title"]
