# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer



class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Quitte le groupe de room
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Reçoit le message du WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        auteur = text_data_json['auteur']

        # Envoie le message au groupe de la room
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'auteur': auteur,
            }
        )

    # Reçoit le message de la room
    async def chat_message(self, event):
        message = event['message']
        auteur = event['auteur']

        # Envoie un message au WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'auteur': auteur
        }))