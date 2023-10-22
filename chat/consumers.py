import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from chat.models import ChatRoom, Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_title"]
        self.room_group_name = f"chat_{self.room_name}"
        self.user = self.scope["user"]

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.add_user(self.room_name, self.user)
        await self.accept()

    async def disconnect(self, close_code):
        await self.remove_user(self.room_name, self.user)
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = self.user
        room = self.room_name
        email = self.user.email

        await self.save_message(room, user, message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "email": email,
            },
        )

    async def chat_message(self, event):
        message = event["message"]
        email = event["email"]
        message_html = f"<div hx-swap-oob='beforeend:#messages'><p><b>{email}</b>: {message}</p></div>"
        await self.send(text_data=json.dumps({"message": message_html, "email": email}))

    @sync_to_async
    def save_message(self, room, user, message):
        room = ChatRoom.objects.get(title=room)
        Message.objects.create(chat_room=room, sender=user, text=message)

    @sync_to_async
    def add_user(self, room, user):
        room = ChatRoom.objects.get(title=room)
        if user not in room.users.all():
            room.users.add(user)
            room.save()

    @sync_to_async
    def remove_user(self, room, user):
        room = ChatRoom.objects.get(title=room)
        if user in room.users.all():
            room.users.remove(user)
            room.save()
