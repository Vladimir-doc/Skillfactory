import json
from django.contrib.auth.models import AnonymousUser
from asgiref.sync import async_to_sync
from channels.exceptions import DenyConnection
from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.cache.backends.locmem import _caches as cache


class ChatConsumer(AsyncWebsocketConsumer):
    def add_cache(self):
        group = cache['us'].get(f'{self.room_name}', None)
        if group:
            group[self.channel_name] = self.user.username
        else:
            group = {self.channel_name: self.user.username}
        cache['us'][f'{self.room_name}'] = group
        return group

    def del_cache(self):
        group = cache['us'].get(f'{self.room_name}', None)
        if group:
            if self.channel_name in group:
                del group[self.channel_name]
                if group:
                    cache['us'][f'{self.room_name}'] = group
                else:
                    del cache['us'][f'{self.room_name}']
        return group

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        self.user = self.scope['user']
        if self.user == AnonymousUser():
            raise DenyConnection("Register before")

        usernames = self.add_cache()
        group_send_dict = {"type": "chat_message", "message": 'online', "username": self.user.username,
                           "usernames": usernames, 'whom': 'room'}
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        await self.channel_layer.group_send(
            self.room_group_name, group_send_dict
        )

    async def disconnect(self, close_code):

        usernames = self.del_cache()
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": 'left', "username": self.scope['user'].username,
                                   "usernames": usernames, 'whom': 'room'}
        )
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)


    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        whom = text_data_json["whom"]
        usernames = cache['us'].get(f'{self.room_name}', None)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message, "username": username,
                                   "usernames": usernames, 'whom': whom}
        )

    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        usernames = event["usernames"]
        whom = event["whom"]

        if whom == 'room':
            await self.send(text_data=json.dumps({"message": message, "username": username,
                                                 "usernames": usernames, 'from': 'room'}))
        else:
            if self.channel_name == whom:
                await self.send(text_data=json.dumps({"message": message, "username": username,
                                                      "usernames": usernames, 'from': username}))
